#!/usr/bin/env python3
"""deck-voice: 내 덱과 글의 문체를 재서, 장표 문구를 그 문체로 쓰고 검사하는 도구 (표준 라이브러리만, 결정론).

gongnyang/gn-voice 의 방식(서식을 걷어낸 본문 -> 문체 지표 -> 밴드 -> 스크립트 검사)을 장표에 맞게 옮겼다.
장표 글은 산문이 아니다(gn-voice presentation 프로파일도 장표에 산문 지표를 쓰지 않는다). 그래서 역할을 셋으로 나눠 잰다.
  title  장표 제목(헤드라인)   body  본문(불릿, 짧은 문장)   notes  발표자 노트(말하듯 쓴 문장)
5줄 묶음 밴드와 한 건 빼고 검증은 kosoe-office / koscom-hwp-report 의 voice_tool.py 에서 가져왔다.
gn-voice 저자의 코퍼스, 지문, 개인 장르 팩 데이터는 쓰지 않는다.

  build    내 덱(.pptx)과 글(.md/.txt) -> 문체 폴더 (style-guide.md, fingerprint-slim.json, ai-tells.json, manifest.jsonl, corpus/)
  check    문체 폴더 + 검사할 덱/개요 -> 합격/불합격 JSON
  fidelity 근거 vs 결과: 숫자와 영문 이름이 사라지거나 생겼는지
  gate     check + fidelity 를 함께 하고 고칠 항목을 알려준다 (스킬이 쓰는 명령)

읽는 형식: .pptx (제목, 본문, 노트를 나눠 읽음), .md/.markdown/.txt
  .md 는 '#' 제목 -> title, '- ' 목록 -> body, 문단 -> notes 로 읽는다.
  ppt-master design_spec.md 는 '## IX. Content Outline' 의 Title / Subtitle / Core message / Content 만 읽는다.
  gn-voice presentation 개요(## S1 — 헤드라인 / - 불릿 / (노트: ...))도 그대로 읽는다.
  .docx/.pdf/.hwp 는 먼저 Markdown 으로 바꿔 넣는다 (ppt-master scripts/source_to_md.py).
"""
import argparse
import hashlib
import json
import posixpath
import re
import statistics
import sys
import zipfile
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

WINDOW = 5            # 표본 단위: 5줄 묶음 (voice_tool.py 와 같다)
ALLOW = 2             # 역할마다 밴드를 벗어난 지표가 이 개수까지는 합격 (gn-voice 와 같은 규칙)
LOO_WIDEN = 1.5       # 한 건 빼고 검증이 실패하면 여유를 한 번 넓힌다
KST = timezone(timedelta(hours=9))

ROLES = ("title", "body", "notes")
ROLE_KO = {"title": "제목", "body": "본문", "notes": "노트"}
MIN_LEN = {"title": 2, "body": 4, "notes": 8}   # 이보다 짧은 줄은 문구로 보지 않는다

RATIO = ("end_m", "end_da", "end_polite", "end_other")
KEYS = RATIO + ("line_len", "period_per1k", "comma_per1k", "paren_per1k", "line_len_cv")
MIN_SLACK = {**{k: 0.10 for k in RATIO}, "line_len_cv": 0.10, "line_len": 3.0,
             "period_per1k": 3.0, "comma_per1k": 3.0, "paren_per1k": 3.0, "words_per_slide": 3.0}

# 일반 AI 상투구 (voice_tool.py 와 같은 목록 + 발표 도입부). hard=즉시 불합격, capped=한 문서 상한.
# 견본(사람이 쓴 글)에 실제로 나온 표현은 build 가 이 목록에서 뺀다: 그 사람의 문체이기 때문이다.
AI_TELLS = {
    "hard": ["알아보겠습니다", "살펴보겠습니다", "궁극적으로", "도움이 되셨다면", "놓치지 마세요"],
    "capped": {"결론적으로": 1, "요약하자면": 1, "다음과 같습니다": 2, "시사합니다": 1, "이번 글에서는": 1,
               "이번 발표에서는": 1},
}
EMOJI_RE = re.compile("[\U0001F300-\U0001FAFF✨✅]")
KH_RE = re.compile(r"[ㅋㅎ]{2,}")

# 음슴체(~음/~함/~임) 근사: 끝 어절의 마지막 글자가 ㅁ 받침. 명사 오탐은 막는다. (gn-voice verify_style.py)
_STRIP = re.compile(r"[)\"'”….?!\s~;ㄱ-ㅎㅏ-ㅣ]+$")
_TAIL = re.compile(r"[)\"'”….?!\s]+$")
_BLOCK = ("처음", "다음", "마음", "걸음", "얼음", "죽음", "사람", "이름", "아침", "점심",
          "기쁨", "슬픔", "게임", "시스템", "프로그램", "아이템")
_YO_NOUN = ("필요", "중요", "개요", "주요", "수요", "소요", "강요", "동요")   # '~ 필요'를 존댓말로 세지 않는다


def _m_end(word):
    w = _STRIP.sub("", word)
    if not w or any(w.endswith(b) for b in _BLOCK):
        return False
    o = ord(w[-1])
    return 0xAC00 <= o <= 0xD7A3 and (o - 0xAC00) % 28 == 16


def end_type(line):
    """줄 끝맺음 한 가지: 존댓말 > ~함/~임 > ~다 > 명사형·기타."""
    e = _TAIL.sub("", line)
    if re.search(r"(요|죠|니다)$", e) and not e.endswith(_YO_NOUN):
        return "end_polite"
    if _m_end(e):
        return "end_m"
    if re.search(r"(다|까|랴|자|네|지)$", e):
        return "end_da"
    return "end_other"


# ---------------------------------------------------------------- 읽기 (문서 = 장표 목록, 장표 = 역할별 줄)
A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
P = "{http://schemas.openxmlformats.org/presentationml/2006/main}"
# 쪽 번호, 축 눈금, 단독 수치 라벨: 문구가 아니라서 문체와 숫자 대조에서 뺀다
NUMERIC_ONLY = re.compile(r"^[\d.,%\s/+\-~]{1,10}$")


def _slide():
    """역할별 줄. extra 는 표 글자: 문체 측정에서는 빠지고 숫자 대조에는 들어간다."""
    return {"title": [], "body": [], "notes": [], "extra": []}


def _paras(sp):
    """도형 하나의 문단들: [(글, 가장 큰 글자 크기)]. 줄바꿈(a:br)은 띄어쓰기로 둔다."""
    out = []
    for p in sp.iter(A + "p"):
        parts, sz = [], 0
        for e in p.iter():
            if e.tag == A + "t":
                parts.append(e.text or "")
            elif e.tag == A + "br":
                parts.append(" ")
            elif e.tag in (A + "rPr", A + "endParaRPr") and (e.get("sz") or "").isdigit():
                sz = max(sz, int(e.get("sz")))
        t = re.sub(r"\s+", " ", "".join(parts)).strip()
        if t and not NUMERIC_ONLY.match(t):
            out.append((t, sz))
    return out


def _ph(sp):
    ph = sp.find(f"{P}nvSpPr/{P}nvPr/{P}ph")
    return None if ph is None else ph.get("type", "body")


def read_pptx(path):
    slides = []
    with zipfile.ZipFile(path) as z:
        names = set(z.namelist())
        order = sorted((n for n in names if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)),
                       key=lambda n: int(re.findall(r"\d+", n)[-1]))
        for n in order:
            root = ET.fromstring(z.read(n))
            if root.get("show") == "0":   # 숨긴 슬라이드(초안·백업 장)는 문체에 넣지 않는다
                continue
            s, shapes = _slide(), []
            s["extra"] = [" | ".join("".join(t.text or "" for t in tc.iter(A + "t")) for tc in tr.iter(A + "tc"))
                          for tr in root.iter(A + "tr")]
            for sp in root.iter(P + "sp"):
                typ = _ph(sp)
                if typ in ("dt", "ftr", "sldNum", "hdr"):
                    continue
                ps = _paras(sp)
                if ps:
                    shapes.append((typ, ps))
            ti = [i for i, (t, _) in enumerate(shapes) if t in ("title", "ctrTitle")]
            if not ti:   # 제목 개체가 없는 자유 배치 덱(ppt-master 내보내기 등): 글자가 가장 큰 짧은 글을 제목으로 본다
                cand = [(max(z_ for _, z_ in ps), -i) for i, (_, ps) in enumerate(shapes)
                        if sum(len(t) for t, _ in ps) <= 80 and re.search(r"[가-힣A-Za-z]{2,}", " ".join(t for t, _ in ps))]
                if cand and max(cand)[0] > 0:
                    ti = [-max(cand)[1]]
            for i, (_, ps) in enumerate(shapes):
                if i in ti:
                    s["title"].append(" ".join(t for t, _ in ps))
                else:
                    s["body"] += [t for t, _ in ps]
            rel = f"ppt/slides/_rels/{n.rsplit('/', 1)[1]}.rels"
            if rel in names:
                for r in ET.fromstring(z.read(rel)):
                    if not r.get("Type", "").endswith("/notesSlide"):
                        continue
                    nn = posixpath.normpath(posixpath.join("ppt/slides", r.get("Target", "")))
                    if nn in names:
                        for sp in ET.fromstring(z.read(nn)).iter(P + "sp"):
                            if _ph(sp) == "body":
                                s["notes"] += [t for t, _ in _paras(sp)]
            slides.append(s)
    return slides


_IX = re.compile(r"(?m)^##\s+IX\b.*$")
_HEADING = re.compile(r"^#{1,6}\s+(.*)$")
_FIELD = re.compile(r"^[-*+]\s+\*\*([^*]+?)\*\*\s*[:：]\s*(.*)$")
# design_spec.md §IX 에서 장표에 실제로 찍히는 문구 칸. 나머지(Layout, Visualization, Cover impact, Info ...)는 지시문이라 뺀다
COPY_FIELDS = {"title": "title", "subtitle": "body", "core message": "body", "content": "body",
               "제목": "title", "부제": "body", "핵심 메시지": "body", "내용": "body"}
_SLIDE_NO = re.compile(r"^(?:S|Slide|슬라이드|장표)\s*0*\d+\s*(?:[—–:|.\-]\s*)?", re.I)
_NOTE_HEAD = re.compile(r"^(?:speaker notes|notes|노트|발표자 노트|스피커 노트|발표 노트)$", re.I)
_NOTE_LINE = re.compile(r"^\(?\s*(?:노트|발표자 노트|note|notes)\s*[:：]\s*(.*?)\)?$", re.I)
_LIST = re.compile(r"^(?:[-*+•]|\d{1,2}[.)])\s+")


def read_md(text):
    spec = bool(_IX.search(text))
    if spec:   # design_spec.md: §IX 만, 다음 '## ' 절 앞까지
        text = re.split(r"(?m)^##\s", _IX.split(text, maxsplit=1)[1], maxsplit=1)[0]
    slides = [_slide()]
    in_notes = in_code = False
    f_role, f_indent = None, -1
    for raw in text.splitlines():
        s = raw.strip()
        if s.startswith("```"):
            in_code = not in_code
            continue
        if s.startswith("|") and not in_code:
            if re.search(r"[^|\s:\-]", s):   # 구분 줄(|---|)이 아닌 표 줄
                slides[-1]["extra"].append(s)
            continue
        if in_code or not s or s.startswith(("![", ">", "<!--", "---", "[시각", "[visual")):
            continue
        indent = len(raw) - len(raw.lstrip())
        h = _HEADING.match(s)
        if h:   # 제목 줄마다 새 장표
            f_role, f_indent = None, -1
            in_notes = bool(_NOTE_HEAD.match(h.group(1).strip()))
            if in_notes:
                continue
            slides.append(_slide())
            t = _SLIDE_NO.sub("", h.group(1).strip()).strip()
            if t and not spec:   # design_spec 의 '#### Slide 02 - 이름'은 내부 이름이지 장표 문구가 아니다
                slides[-1]["title"].append(t)
            continue
        cur = slides[-1]
        f = _FIELD.match(s)
        if f:
            f_role, f_indent = COPY_FIELDS.get(f.group(1).strip().lower()), indent
            if f_role and f.group(2).strip():
                cur[f_role].append(f.group(2).strip())
            continue
        if f_indent >= 0 and indent > f_indent:   # 칸 아래 들여쓴 줄 (Content 의 하위 목록)
            if f_role:
                cur[f_role].append(_LIST.sub("", s))
            continue
        f_role, f_indent = None, -1
        n = _NOTE_LINE.match(s)
        if n or in_notes:
            cur["notes"].append(n.group(1) if n else s)
        elif _LIST.match(s) or spec:
            cur["body"].append(_LIST.sub("", s))
        else:
            cur["notes"].append(s)   # 일반 글의 문단은 말하듯 쓴 문장으로 보고 노트 기준에 넣는다
    return [x for x in slides if any(x.values())]


def read_doc(path):
    p = Path(path)
    ext = p.suffix.lower()
    if ext == ".pptx":
        return read_pptx(p)
    if ext in (".md", ".markdown", ".txt"):
        return read_md(p.read_text(encoding="utf-8-sig"))
    sys.exit(f"{p.name}: 읽을 수 없는 형식입니다(.pptx, .md, .txt). .docx/.pdf 는 "
             "`python3 .claude/skills/ppt-master/scripts/source_to_md.py <파일>` 로 Markdown 을 만든 뒤 넣으세요")


# 줄 머리 기호와 번호: □ ㅇ - · * ※ ① ▶ ✓, '1.' '가.' 'I.'(뒤에 띄어쓰기가 있을 때만), '[1]'
_HEAD = re.compile(r"^(?:[□■○◦●ㅇ\-\*※•▪·∙▶►▷➤→✓✔◆◇★☆①-⑳\s]|\[\d{1,2}\]"
                   r"|(?:\d{1,2}|[가나다라마바사아자차카타파하]|[IVX]{1,4})[.)](?=\s))+")
_MD = ((re.compile(r"\*\*|__|`"), ""), (re.compile(r"\[([^\]]+)\]\([^)]*\)"), r"\1"))


def clean(role, lines):
    """서식(마크다운 강조, 링크, 머리 기호)을 걷어내고 문구 줄만 남긴다. 노트는 문장 단위로 나눈다."""
    out = []
    for raw in lines:
        s = raw.strip()
        for rx, rep in _MD:
            s = rx.sub(rep, s)
        s = _HEAD.sub("", s).strip()
        for x in (re.split(r"(?<=[.!?])\s+", s) if role == "notes" else [s]):
            x = x.strip()
            if len(x) >= MIN_LEN[role] and not NUMERIC_ONLY.match(x):
                out.append(x)
    return out


def load(path):
    """문서 하나 -> {'slides', 'lines'(역할별 정리된 줄), 'wps'(장표별 본문 어절 수), 'text'(문구 전체)}."""
    slides = read_doc(path)
    lines = {r: [x for s in slides for x in clean(r, s[r])] for r in ROLES}
    wps = [n for n in (sum(len(x.split()) for x in clean("body", s["body"])) for s in slides) if n]
    return {"slides": slides, "lines": lines, "wps": wps,
            "titles": [" ".join(s["title"]) for s in slides if s["title"]],
            "text": "\n".join(x for s in slides for r in ROLES + ("extra",) for x in s[r])}


def windows(lines, w=WINDOW):
    ws = [lines[i:i + w] for i in range(0, len(lines), w)]
    return [x for x in ws if len(x) >= max(3, w // 2)]


# ---------------------------------------------------------------- 지표와 밴드
def metrics(lines):
    text = "\n".join(lines)
    n, chars = max(len(lines), 1), max(len(text), 1)
    c = Counter(end_type(x) for x in lines)
    lens = [len(x) for x in lines]
    return {
        **{k: c[k] / n for k in RATIO},
        "line_len": sum(lens) / n,
        "line_len_cv": statistics.pstdev(lens) / statistics.mean(lens) if len(lens) > 2 else 0.0,
        "period_per1k": text.count(".") / chars * 1000,
        "comma_per1k": text.count(",") / chars * 1000,
        "paren_per1k": text.count("(") / chars * 1000,
    }


def pct(vals, p):
    s = sorted(vals)
    k = (len(s) - 1) * p / 100.0
    f, c = int(k), min(int(k) + 1, len(s) - 1)
    return s[f] + (s[c] - s[f]) * (k - f)


def make_band(points, mult=1.0):
    """points: [{지표: 값}]. 점 5개 미만이면 최솟값~최댓값, 이상이면 5~95% 분위수. 여유(slack)를 덧붙인다."""
    band = {}
    for k in points[0]:
        v = [p[k] for p in points]
        lo, hi = (min(v), max(v)) if len(v) < 5 else (pct(v, 5), pct(v, 95))
        slack = max((hi - lo) * 0.15, MIN_SLACK[k]) * mult
        band[k] = {"lo": round(max(lo - slack, 0.0), 4), "hi": round(hi + slack, 4), "raw_lo": round(lo, 4), "raw_hi": round(hi, 4)}
    return band


def bands_of(docs, mult=1.0):
    """역할마다 5줄 묶음 점으로 밴드를 만든다. 본문에는 장표당 어절 수(장표가 점)를 더한다. 점이 없는 역할은 뺀다."""
    out = {}
    for r in ROLES:
        pts = [metrics(w) for d in docs for w in windows(d["lines"][r])]
        if pts:
            out[r] = make_band(pts, mult)
    wps = [n for d in docs for n in d["wps"]]
    if "body" in out and len(wps) >= 3:
        out["body"].update(make_band([{"words_per_slide": n} for n in wps], mult))
    return out


def doc_metrics(lines):
    """검사할 문서: 줄 묶음마다 재서 지표별 중앙값을 쓴다(밴드를 만든 방식과 같은 단위)."""
    ms = [metrics(w) for w in (windows(lines) or [lines])]
    return {k: statistics.median(m[k] for m in ms) for k in KEYS}, len(ms)


def tier(n_docs):
    return "trial" if n_docs <= 1 else ("small" if n_docs <= 3 else "normal")


# ---------------------------------------------------------------- 검사
def hard_hits(text, tells):
    v = []
    if not tells.get("emoji_ok") and EMOJI_RE.search(text):
        v.append("이모지")
    if not tells.get("kh_ok") and KH_RE.search(text):
        v.append("ㅋㅋ/ㅎㅎ")
    v += [p for p in tells.get("hard", []) if p in text]
    v += [f"{p} x{text.count(p)}(상한 {cap})" for p, cap in tells.get("capped", {}).items() if text.count(p) > cap]
    return v


def judge(doc, band, tells, allow=ALLOW):
    roles = {}
    for r in ROLES:
        if r not in band or not windows(doc["lines"][r]):
            roles[r] = None   # 견본이나 검사 대상에 이 역할 줄이 3줄 미만: 검사하지 않는다
            continue
        m, nw = doc_metrics(doc["lines"][r])
        if "words_per_slide" in band[r] and doc["wps"]:
            m["words_per_slide"] = statistics.median(doc["wps"])
        oob = [{"metric": k, "value": round(m[k], 3), "expected": [b["lo"], b["hi"]]}
               for k, b in band[r].items() if k in m and not b["lo"] <= m[k] <= b["hi"]]
        roles[r] = {"pass": len(oob) <= allow, "out_of_band": oob, "n_windows": nw,
                    "metrics": {k: round(x, 3) for k, x in m.items()}}
    hard = hard_hits(doc["text"], tells)
    judged = [x for x in roles.values() if x]
    return {"pass": not hard and bool(judged) and all(x["pass"] for x in judged), "hard": hard, "roles": roles}


# ---------------------------------------------------------------- 문체 분석 (style-guide.md)
END_NAME = {"end_other": "명사형(~ 현황, ~ 12% 증가)", "end_m": "~함·~임·~음",
            "end_da": "~다", "end_polite": "존댓말(~습니다·~요)"}
DATES = [("2026. 4. 23", r"\d{4}\. \d{1,2}\. \d{1,2}"), ("2026.4.23", r"\d{4}\.\d{1,2}\.\d{1,2}"),
         ("2026-04-23", r"\d{4}-\d{1,2}-\d{1,2}"), ("2026년 4월 23일", r"\d{4}년 ?\d{1,2}월 ?\d{1,2}일"),
         ("'26. 4.", r"['’]\d{2}\.\s?\d{1,2}"), ("’26년", r"['’]\d{2}년")]
QUARTERS = [("3분기", r"[1-4]분기"), ("3Q", r"\b[1-4]Q\b"), ("’26.3Q", r"['’]\d{2}\.?\s?[1-4]Q")]
_MONEY = re.compile(r"\d[\d,.]*(\s?)(조|억|천만|백만|만|천)?(\s?)원")
SIGNS = [("%p", r"%p"), ("%", r"%(?!p)"), ("↑", "↑"), ("↓", "↓"), ("△", "△"), ("→", "→"),
         ("전년 대비", r"전년\s?대비"), ("YoY", r"\bYoY\b")]
_TOK = re.compile(r"^[\"'“‘(\[<]+|[\"'”’)\]>,.·:;!?]+$")
_LABEL = re.compile(r"^[^:：]{1,15}[:：]\s*\S")


def _words(line):
    return [w for w in (_TOK.sub("", x) for x in _TAIL.sub("", line).split()) if w]


def _ending(line):
    ws = _words(line)
    return "" if not ws or re.search(r"\d", ws[-1]) else ws[-1]


def _share(lines, pred):
    return round(sum(1 for x in lines if pred(x)) / max(len(lines), 1), 3)


def analyze_role(docs, r):
    lines = [x for d in docs for x in d["lines"][r]]
    if not lines:
        return None
    n = len(lines)
    ends = Counter(end_type(x) for x in lines)
    lens = [len(x) for x in lines]
    a = {"n": n, "endings": {k: round(ends[k] / n, 3) for k in RATIO},
         "top_endings": [(w, c) for w, c in Counter(filter(None, map(_ending, lines))).most_common(10) if c >= 2],
         "len": {"mean": round(statistics.mean(lens), 1), "p25": round(pct(lens, 25)), "p75": round(pct(lens, 75)),
                 "min": min(lens), "max": max(lens)},
         "period_end": _share(lines, lambda x: x.rstrip().endswith(".")),
         "question": _share(lines, lambda x: x.rstrip().endswith("?")),
         "digits": _share(lines, lambda x: re.search(r"\d", x)),
         "label": _share(lines, lambda x: _LABEL.match(x)),
         "comma_per_line": round(sum(x.count(",") for x in lines) / n, 2)}
    a["dominant"] = max(RATIO, key=lambda k: a["endings"][k])
    lo, hi = pct(lens, 25), pct(lens, 75)   # 예문: 주된 끝맺음이고 길이가 중간인 줄을 문서마다 고르게 (원문 그대로)
    per = -(-5 // len(docs))
    ex = []
    for d in docs:
        pool = [x for x in d["lines"][r] if end_type(x) == a["dominant"] and lo <= len(x) <= hi]
        ex += pool[::max(len(pool) // per, 1)][:per]
    a["examples"] = ex[:5]
    return a


def analyze(docs):
    text = "\n".join(d["text"] for d in docs)
    nd = len(docs)
    df, tf = Counter(), Counter()   # 두 어절 표현: 문서 수와 횟수
    for d in docs:
        seen = set()
        for x in (x for r in ROLES for x in d["lines"][r]):
            ws = _words(x)
            for a, b in zip(ws, ws[1:]):
                bg = f"{a} {b}"
                if re.search(r"[가-힣]", bg) and not re.search(r"\d", bg) and len(a) > 1 and len(b) > 1:
                    tf[bg] += 1
                    seen.add(bg)
        df.update(seen)
    money = Counter((m.group(2) or "") + (" " if m.group(3) else "") + "원" for m in _MONEY.finditer(text))
    wps = [n for d in docs for n in d["wps"]]
    return {
        "roles": {r: analyze_role(docs, r) for r in ROLES},
        "n_docs": nd, "n_slides": sum(len(d["slides"]) for d in docs),
        "wps": {"median": statistics.median(wps), "p25": round(pct(wps, 25)), "p75": round(pct(wps, 75)),
                "max": max(wps)} if wps else None,
        "phrases": [(bg, c) for bg, c in tf.most_common() if c >= 2 and df[bg] >= min(2, nd)][:12],
        "dates": [(k, c) for k, c in ((k, len(re.findall(p, text))) for k, p in DATES) if c],
        "quarters": [(k, c) for k, c in ((k, len(re.findall(p, text))) for k, p in QUARTERS) if c],
        "money": money.most_common(5),
        "signs": [(k, c) for k, c in ((k, len(re.findall(p, text))) for k, p in SIGNS) if c],
    }


def _pc(x):
    return f"{round(x * 100)}%"


def _end_rule(a, lead):
    e = a["endings"]
    o = sorted(RATIO, key=lambda k: e[k], reverse=True)
    s = f"{lead} 주로 '{END_NAME[o[0]]}' 끝맺음 ({_pc(e[o[0]])})"
    return s + (f", '{END_NAME[o[1]]}' 끝맺음도 섞는다 ({_pc(e[o[1]])})" if e[o[1]] >= 0.15 else "")


def _period_rule(a, what):
    p = a["period_end"]
    return (f"{what} 끝에 마침표를 찍지 않는다" if p < 0.1 else
            f"{what} 끝에 마침표를 찍는다({_pc(p)})" if p > 0.6 else f"{what} 끝 마침표는 섞어 쓴다({_pc(p)})")


def rules_of(a, tells):
    """분석값 -> 역할별 작성 규칙. 숫자가 기준을 넘을 때만 규칙을 만든다."""
    R = {"title": [], "body": [], "notes": [], "common": []}
    t, b, n = (a["roles"][r] for r in ROLES)
    if t:
        if t["endings"]["end_other"] >= 0.5:
            R["title"].append(f"제목은 명사로 끝내는 토픽형으로 쓴다 (예: '시장 현황', {_pc(t['endings']['end_other'])}). "
                              "장표의 주장은 제목이 아니라 Core message 한 줄로 쓴다")
        else:
            R["title"].append(_end_rule(t, "제목은 문장(주장)으로 쓴다:"))
        R["title"].append(f"제목 길이는 평균 {t['len']['mean']}자, 보통 {t['len']['p25']}~{t['len']['p75']}자")
        if t["question"] >= 0.15:
            R["title"].append(f"제목 일부를 질문으로 던진다({_pc(t['question'])})")
        elif t["question"] < 0.05:
            R["title"].append("제목을 질문형으로 쓰지 않는다")
        if t["digits"] >= 0.3:
            R["title"].append(f"제목에 숫자를 넣는다({_pc(t['digits'])})")
        if t["label"] >= 0.2:
            R["title"].append(f"'구분: 내용' 꼴 제목을 쓴다({_pc(t['label'])})")
        R["title"].append(_period_rule(t, "제목"))
    else:
        R["title"].append("제목 견본이 없다: 제목은 ppt-master 기본 규칙과 references/presentation.md 를 따른다")
    if b:
        R["body"].append(_end_rule(b, "본문 항목은"))
        if b["top_endings"]:
            R["body"].append("자주 쓴 끝말을 우선 쓴다: " + ", ".join(w for w, _ in b["top_endings"][:8]))
        R["body"].append(f"항목 한 줄은 평균 {b['len']['mean']}자, 보통 {b['len']['p25']}~{b['len']['p75']}자")
        R["body"].append(_period_rule(b, "본문 항목"))
        if b["label"] >= 0.2:
            R["body"].append(f"항목을 '라벨: 내용' 꼴로 쓴다({_pc(b['label'])})")
        if a["wps"]:
            R["body"].append(f"장표 하나의 본문은 보통 {a['wps']['p25']}~{a['wps']['p75']}어절(중앙값 {a['wps']['median']})."
                             " 넘치면 장표를 나눈다")
    if n:
        R["notes"].append(_end_rule(n, "노트는 말하듯 쓴다:"))
        R["notes"].append(f"노트 한 문장은 평균 {n['len']['mean']}자, 보통 {n['len']['p25']}~{n['len']['p75']}자")
    else:
        R["notes"].append("노트 견본이 없다: 노트를 쓰면 ppt-master references/speaker-notes.md 규칙을 따르고 노트 검사는 생략된다")
    if a["dates"]:
        R["common"].append(f"날짜는 '{max(a['dates'], key=lambda x: x[1])[0]}' 꼴로 쓴다")
    if a["quarters"]:
        R["common"].append(f"분기는 '{max(a['quarters'], key=lambda x: x[1])[0]}' 꼴로 쓴다")
    if a["money"]:
        R["common"].append("금액 단위는 " + ", ".join(f"'{u}'" for u, _ in a["money"][:3]) + " 꼴을 쓴다. 근거 금액을 다른 단위로 바꾸지 않는다")
    signs = [k for k, _ in a["signs"] if k != "%"]
    if signs:
        R["common"].append("증감 표기는 " + ", ".join(f"'{s}'" for s in signs) + "를 쓴다")
    if a["phrases"]:
        R["common"].append("자주 쓴 표현을 살려 쓴다: " + ", ".join(bg for bg, _ in a["phrases"][:8]))
    if tells["from_corpus"]:
        R["common"].append("견본에 실제로 쓴 표현이라 금지하지 않는다: " + ", ".join(tells["from_corpus"]))
    return R


def _fmt(pairs):
    return " · ".join(f"{w}({c})" for w, c in pairs) or "(없음)"


HINT = {"end_m": "~함/~임으로 끝나는 줄", "end_da": "~다로 끝나는 줄", "end_polite": "~요/~니다로 끝나는 줄",
        "end_other": "명사 등으로 끝나는 줄", "line_len": "줄 평균 길이", "line_len_cv": "줄 길이의 들쭉날쭉함",
        "period_per1k": "마침표 밀도", "comma_per1k": "쉼표 밀도", "paren_per1k": "괄호 밀도",
        "words_per_slide": "장표당 본문 어절 수"}


def guide_md(name, meta, rows, a, rules, band):
    loo = ", ".join(f"{x['held_out']} {'통과' if x['pass'] else '불합격' if x['pass'] is False else '비교 불가'}"
                    for x in meta["leave_one_out"]) or "1건이라 하지 않음"
    L = [f"# 문체 가이드: {name} ({meta['label']})", "",
         f"- 근거: 견본 {a['n_docs']}건, 장표(절) {a['n_slides']}개 · "
         + " · ".join(f"{ROLE_KO[r]} {a['roles'][r]['n'] if a['roles'][r] else 0}줄" for r in ROLES),
         *[f"  - {r['id']} {r['source_file']} ({', '.join(f'{ROLE_KO[k]} {v}' for k, v in r['lines'].items())})" for r in rows],
         f"- 한 건 빼고 검증: {loo}" + (" (여유를 한 번 넓힘)" if meta["widened_after_loo"] else ""),
         f"- 만든 때: {meta['built']} · `deck_voice.py build`", "",
         "> 장표 구조 규칙(한 장표 한 메시지, 제목만 읽어도 이야기가 이어짐, 불릿 병렬, 노트와 장표 분리)은",
         "> references/presentation.md 를 따르고, 끝맺음·길이·밀도·표기·표현은 이 가이드를 따른다. 숫자는 모두 견본에서 잰 값이다.", "",
         "## 1. 이렇게 쓴다", ""]
    for k, head in (("title", "제목 (design_spec §IX Title)"), ("body", "본문 (Subtitle · Core message · Content)"),
                    ("notes", "발표자 노트"), ("common", "공통")):
        L += [f"### {head}", "", *[f"- {x}" for x in rules[k]], ""]
    L += ["## 2. 역할별 끝맺음", "", "| 유형 | " + " | ".join(ROLE_KO[r] for r in ROLES) + " |", "|---|---|---|---|"]
    for k in RATIO:
        L.append(f"| {END_NAME[k]} | " + " | ".join(_pc(a["roles"][r]["endings"][k]) if a["roles"][r] else "-" for r in ROLES) + " |")
    L += ["", "## 3. 길이와 밀도", ""]
    for r in ROLES:
        x = a["roles"][r]
        if x:
            L.append(f"- {ROLE_KO[r]}: 평균 {x['len']['mean']}자 (25~75% {x['len']['p25']}~{x['len']['p75']}, 최소 {x['len']['min']} · "
                     f"최대 {x['len']['max']}) · 끝 마침표 {_pc(x['period_end'])} · 질문 {_pc(x['question'])} · "
                     f"숫자 포함 {_pc(x['digits'])} · 줄당 쉼표 {x['comma_per_line']}개 · 자주 쓴 끝말 {_fmt(x['top_endings'][:6])}")
    if a["wps"]:
        L.append(f"- 장표당 본문 어절 수: 중앙값 {a['wps']['median']}, 25~75% {a['wps']['p25']}~{a['wps']['p75']}, 최대 {a['wps']['max']}")
    L += ["", "## 4. 숫자·날짜 표기", "", f"- 날짜: {_fmt(a['dates'])}", f"- 분기: {_fmt(a['quarters'])}",
          f"- 금액 단위: {_fmt(a['money'])}",
          f"- 비율·증감: {_fmt(a['signs'])}", "",
          "## 5. 자주 쓴 표현 (두 어절, 여러 견본에 나온 것)", "", f"- {_fmt(a['phrases'])}", "",
          "## 6. 예문 (견본에서 그대로)", ""]
    for r in ROLES:
        if a["roles"][r] and a["roles"][r]["examples"]:
            L += [f"- {ROLE_KO[r]} 예문: " + " / ".join(a["roles"][r]["examples"])]
    L += ["", "## 7. 검사 기준 (`deck_voice.py gate`)", "",
          f"- 역할마다 허용 범위를 벗어난 지표가 {ALLOW}개 이하이면 합격. 금지 상투구(ai-tells.json)는 즉시 불합격.",
          "- 견본이나 검사 대상에 3줄 미만인 역할은 검사하지 않는다. 숫자·영문 이름은 근거(`--facts`)와 대조한다.", ""]
    for r, b in band.items():
        L += [f"### {ROLE_KO[r]}", "", "| 지표 | 견본 범위 | 허용 범위 |", "|---|---|---|",
              *[f"| {HINT[k]} | {v['raw_lo']} ~ {v['raw_hi']} | {v['lo']} ~ {v['hi']} |" for k, v in b.items()], ""]
    L += ["이 파일과 corpus/ 에는 견본 문장이 그대로 들어 있다. 개인정보와 대외비가 없는지 확인한 뒤 공유한다.", ""]
    return "\n".join(L)


# ---------------------------------------------------------------- build
def tells_for(texts):
    """일반 상투구 목록에서, 사람이 쓴 견본에 실제로 나온 표현은 뺀다(상한은 견본 최댓값까지 올린다)."""
    hard = [p for p in AI_TELLS["hard"] if not any(p in t for t in texts)]
    return {"hard": hard,
            "capped": {p: max([c] + [t.count(p) for t in texts]) for p, c in AI_TELLS["capped"].items()},
            "emoji_ok": any(EMOJI_RE.search(t) for t in texts), "kh_ok": any(KH_RE.search(t) for t in texts),
            "from_corpus": [p for p in AI_TELLS["hard"] if p not in hard],
            "rule": "hard=즉시 불합격 / capped=문서당 상한 초과 시 불합격 / 이모지·ㅋㅋ는 견본에 없으면 금지"}


def corpus_md(did, d):
    """서식을 걷어낸 견본을 개요 꼴로 남긴다 (read_md 로 다시 읽으면 같은 역할로 읽힌다)."""
    L = [f"<!-- {did} -->", ""]
    for i, s in enumerate(d["slides"], 1):
        t = clean("title", s["title"])
        L.append(f"## S{i}" + (f" — {' '.join(t)}" if t else ""))
        L += [f"- {x}" for x in clean("body", s["body"])]
        L += [f"(노트: {x})" for x in clean("notes", s["notes"])]
        L.append("")
    return "\n".join(L)


def build(args):
    if not args.human:
        sys.exit("사람이 직접 쓴 견본만 쓸 수 있습니다(--human). AI 도움을 받은 글은 기준을 오염시킵니다")
    docs, rows = [], []
    for i, f in enumerate(map(Path, args.files), 1):
        d = load(f)
        if not any(windows(d["lines"][r]) for r in ROLES):
            sys.exit(f"{f.name}: 문구 줄이 너무 적어 표본을 만들 수 없습니다(역할마다 최소 3줄: "
                     + ", ".join(f"{ROLE_KO[r]} {len(d['lines'][r])}" for r in ROLES) + ")")
        d["id"] = f"D-{i:03d}"
        docs.append(d)
        rows.append({"id": d["id"], "source_file": f.name, "sha256": hashlib.sha256(f.read_bytes()).hexdigest(),
                     "slides": len(d["slides"]), "lines": {r: len(d["lines"][r]) for r in ROLES},
                     "human_written": True, "note": "서식 제거 문구(corpus/)만 보관. 개인정보 점검 후 사용"})
    out = Path(args.out)
    (out / "corpus").mkdir(parents=True, exist_ok=True)
    for d in docs:
        (out / "corpus" / f"{d['id']}.md").write_text(corpus_md(d["id"], d), encoding="utf-8")
    (out / "manifest.jsonl").write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n", encoding="utf-8")

    n = len(docs)
    tells = tells_for([d["text"] for d in docs])

    def run_loo(mu):
        res = []
        for i in range(n if n >= 2 else 0):
            j = judge(docs[i], bands_of([d for k, d in enumerate(docs) if k != i], mu), tells)
            judged = {r: x for r, x in j["roles"].items() if x}
            res.append({"held_out": docs[i]["id"], "pass": (not j["hard"] and all(x["pass"] for x in judged.values())) if judged else None,
                        "out_of_band": [f"{ROLE_KO[r]}:{o['metric']}" for r, x in judged.items() for o in x["out_of_band"]]})
        return res

    mult, widened = 1.0, False
    loo = run_loo(mult)
    if any(r["pass"] is False for r in loo):   # 한 건 빼고 검증이 실패하면 여유를 한 번 넓힌다
        mult, widened = LOO_WIDEN, True
        loo = run_loo(mult)
    ok = [r["pass"] for r in loo if r["pass"] is not None]
    status = "trial" if n < 2 else ("verified" if ok and all(ok) else "unverified")
    label = "문체 미검증" if status == "unverified" else {"trial": "문체 시험용(1건)", "small": "문체 소표본", "normal": "문체 표본"}[tier(n)]
    band = bands_of(docs, mult)
    meta = {"generator": "deck-voice/scripts/deck_voice.py", "built": datetime.now(KST).replace(microsecond=0).isoformat(),
            "name": args.name, "n_docs": n, "unit": f"{WINDOW}줄 묶음(역할별)", "tier": tier(n), "status": status,
            "label": label, "slack_mult": mult, "widened_after_loo": widened, "allow_out_of_band": ALLOW,
            "roles": list(band), "leave_one_out": loo,
            "note": "점 5개 미만이면 min~max, 이상이면 5~95% 분위수 + 여유. 견본이 늘면 build 를 다시 돌린다."}
    (out / "fingerprint-slim.json").write_text(json.dumps({"meta": meta, "band": band}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (out / "ai-tells.json").write_text(json.dumps(tells, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    a = analyze(docs)
    rules = rules_of(a, tells)
    (out / "style-guide.md").write_text(guide_md(args.name, meta, rows, a, rules, band), encoding="utf-8")
    print(json.dumps({"out": str(out), "guide": str(out / "style-guide.md"), "n_docs": n, "tier": tier(n),
                      "status": status, "label": label, "roles": list(band), "widened": widened,
                      "leave_one_out": loo, "rules": rules}, ensure_ascii=False))
    return 0


# ---------------------------------------------------------------- check / fidelity / gate
def _load_voice(voice):
    v = Path(voice)
    return (json.loads((v / "fingerprint-slim.json").read_text(encoding="utf-8")),
            json.loads((v / "ai-tells.json").read_text(encoding="utf-8")))


def check(args):
    slim, tells = _load_voice(args.voice)
    res = judge(load(args.file), slim["band"], tells)
    res.update({"label": slim["meta"]["label"], "reference_only": slim["meta"]["tier"] == "trial"})
    print(json.dumps(res, ensure_ascii=False))
    return 0 if res["pass"] else 3


NUM_RE = re.compile(r"\d[\d,.]*\s?[%가-힣a-zA-Z]{0,3}")
LATIN_RE = re.compile(r"[A-Za-z][A-Za-z0-9_.-]{1,}")
_LIST_NO = re.compile(r"(?m)^[ \t□■○◦●ㅇ\-\*※•▪·∙]*\d{1,2}\.(?=\s)")    # 줄 머리 번호 '1. '만 뺀다
_YMD = re.compile(r"\b((?:19|20)\d{2})\.\s?(\d{1,2})(?:\.\s?(\d{1,2}))?(?!\d)")   # '2026.3'은 연·월로 나눈다
_YY = re.compile(r"['’‘](\d{2})(?=\s?년|\.)")                                      # '’26년'은 2026


def assets(text):
    text = _YY.sub(r"20\1", _LIST_NO.sub("", text))
    text = _YMD.sub(lambda m: " ".join(g for g in m.groups() if g), text)
    nums = {re.sub(r"[^\d.]", "", m.group()).strip(".") for m in NUM_RE.finditer(text)}
    nums = {x.lstrip("0") if re.fullmatch(r"0\d+", x) else x for x in nums}
    return {x for x in nums if x}, {m.group().lower() for m in LATIN_RE.finditer(text)}


def fidelity_of(src, out):
    sn, sl = assets(src)
    on, ol = assets(out)
    return {"pass": not (sn - on) and not (on - sn) and not (sl - ol) and not (ol - sl),
            "missing": sorted(sn - on) + sorted(sl - ol), "invented": sorted(on - sn) + sorted(ol - sl)}


FACT_EXT = (".md", ".markdown", ".txt", ".csv", ".tsv")


def facts_text(paths):
    """근거: 파일 또는 폴더(ppt-master 프로젝트의 sources/ 등; .md .txt .csv .tsv 만, 변환 기록 .json 은 읽지 않는다)."""
    out = []
    for p in map(Path, paths):
        files = sorted(x for x in p.iterdir() if x.suffix.lower() in FACT_EXT) if p.is_dir() else [p]
        for f in files:
            out.append(load(f)["text"] if f.suffix.lower() == ".pptx" else f.read_text(encoding="utf-8-sig"))
    return "\n".join(out)


def fidelity(args):
    res = fidelity_of(facts_text([args.src]), load(args.out)["text"])
    print(json.dumps(res, ensure_ascii=False))
    return 0 if res["pass"] else 1


def gate(args):
    """덱(.pptx)이나 개요(design_spec.md, 개요 .md) 하나에 문체 검사와 숫자 대조를 함께 하고 고칠 항목을 알려준다.
    mode=create: 새로 쓴 덱. 근거에 없는 숫자·영문 이름이 생기면 불합격, 안 쓴 근거는 참고만.
    mode=rewrite: 원래 문구를 고쳐 쓴 덱. 사라진 것도 불합격."""
    slim, tells = _load_voice(args.voice)
    doc = load(args.file)
    if not doc["text"].strip():
        sys.exit("검사할 문구가 없습니다")
    style = judge(doc, slim["band"], tells)
    fid = fidelity_of(facts_text(args.facts), doc["text"]) if args.facts else None
    fid_pass = fid is None or (not fid["invented"] and (args.mode == "create" or not fid["missing"]))
    todo = [f"[금지] {h}: 이 표현을 빼고 다시 쓰세요" for h in style["hard"]]
    if not any(style["roles"].values()):
        todo.append("[검사 불가] 견본에도 있는 역할(제목·본문·노트)이 이 문서에 3줄 이상 있어야 문체를 잽니다")
    skipped = []
    for r, x in style["roles"].items():
        if x is None:
            skipped.append(ROLE_KO[r])
            continue
        for o in x["out_of_band"]:
            lo, hi = o["expected"]
            way = "높습니다 -> 줄이세요" if o["value"] > hi else "낮습니다 -> 늘리세요"
            todo.append(f"[{ROLE_KO[r]}] {HINT.get(o['metric'], o['metric'])}: {o['value']} (허용 {lo}~{hi}) {way}")
    if fid is not None:
        todo += [f"[숫자] 근거에 없는 값 '{x}': 근거대로 고치거나 [확인 필요]로 표시하세요" for x in fid["invented"]]
        if args.mode == "rewrite":
            todo += [f"[숫자] 원래 있던 '{x}'가 사라졌습니다: 되살리세요" for x in fid["missing"]]
    unused = (fid or {}).get("missing", []) if args.mode == "create" else []
    res = {"pass": style["pass"] and fid_pass, "style_pass": style["pass"],
           "fidelity_pass": fid_pass if fid is not None else None, "label": slim["meta"]["label"],
           "reference_only": slim["meta"]["tier"] == "trial", "rework": todo,
           "skipped_roles": skipped, "titles": doc["titles"],
           "unused_facts": {"count": len(unused), "first": unused[:20]},
           "roles": {r: (x and {"pass": x["pass"], "out_of_band": x["out_of_band"]}) for r, x in style["roles"].items()}}
    print(json.dumps(res, ensure_ascii=False))
    return 0 if res["pass"] else 3


def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    b = sp.add_parser("build")
    b.add_argument("files", nargs="+")
    b.add_argument("--out", required=True)
    b.add_argument("--name", default="내 문체")
    b.add_argument("--human", action="store_true", help="사람이 직접 쓴 견본임을 확인")
    b.set_defaults(fn=build)
    c = sp.add_parser("check")
    c.add_argument("--voice", required=True)
    c.add_argument("file")
    c.set_defaults(fn=check)
    g = sp.add_parser("gate")
    g.add_argument("--voice", required=True)
    g.add_argument("--facts", action="append", default=[], help="근거 파일이나 폴더(여러 개면 --facts 를 반복)")
    g.add_argument("--mode", choices=["create", "rewrite"], default="create")
    g.add_argument("file")
    g.set_defaults(fn=gate)
    f = sp.add_parser("fidelity")
    f.add_argument("src")
    f.add_argument("out")
    f.set_defaults(fn=fidelity)
    a = ap.parse_args(argv)
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
