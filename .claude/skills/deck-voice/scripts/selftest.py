#!/usr/bin/env python3
"""deck_voice 자체검사.  실행: python3 .claude/skills/deck-voice/scripts/selftest.py   (python-pptx 필요)
견본은 이 파일이 만드는 합성 덱 3건이다 (토픽형 제목, 명사형 불릿, 존댓말 노트. 회사·수치는 모두 가상).
  1. 3건 build -> 문체 소표본, 한 건 빼고 검증 통과, 역할 3개 밴드, style-guide 가 잰 값과 원문 예문을 담는다
  2. 견본 문체로 쓴 개요는 합격, 근거와 숫자도 맞는다
  3. AI투 개요(존댓말 문장 제목·불릿)는 금지어가 없어도 문체 불합격, 금지어가 있으면 즉시 불합격
  4. 근거에 없는 숫자를 넣으면 fidelity 가 잡는다
  5. 1건만 넣으면 시험용 라벨, --human 없이는 거부하고 아무것도 쓰지 않는다
  6. design_spec.md 는 §IX 의 Title / Subtitle / Core message / Content 만 읽는다
  7. 제목 개체가 없는 자유 배치 덱: 글자가 가장 큰 짧은 글이 제목, 쪽 번호·단독 수치·숨긴 장은 빠지고 표는 숫자 대조에만
  8. corpus/ 를 다시 읽으면 같은 역할 줄이 나온다
  9. 견본에 실제로 쓴 상투구는 금지 목록에서 빠진다
 10. 근거 폴더: JSON 은 값으로 읽고 변환 기록(*.conversion_profile.json)은 뺀다. 장마다 반복되는 푸터와
     대문자 장 라벨은 '근거에 없는 영문 이름'으로 잡지 않는다 (ppt-master 실제 내보내기에서 찾은 오탐)
"""
import contextlib
import io
import json
import sys
import tempfile
from pathlib import Path

from pptx import Presentation
from pptx.util import Pt, Inches

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import deck_voice as dv  # noqa: E402

DECKS = {
    "3분기_실적": [
        ("3분기 실적 요약", ["매출 1,240억원, 전년 대비 12% 증가", "영업이익 186억원으로 분기 최대", "신규 고객 320개사 확보"],
         "3분기 매출은 1,240억원으로 작년보다 12% 늘었습니다. 영업이익도 분기 기준으로 가장 높았습니다."),
        ("매출 구성 변화", ["플랫폼 매출 비중 41%로 확대", "라이선스 매출은 정체 수준", "해외 매출 3분기 연속 성장"],
         "플랫폼 매출이 처음으로 40%를 넘었습니다. 라이선스는 당분간 비슷한 수준으로 봅니다."),
        ("비용 구조 점검", ["인건비 비중 38%로 2%p 감소", "클라우드 비용 월 4.2억원 수준 유지", "외주 용역비 절감 효과 확인"],
         "인건비 비중이 줄어든 것은 외주 정리 덕분입니다. 클라우드 비용은 예산 안에서 관리하고 있습니다."),
        ("부문별 성과", ["금융 부문 수주 1위 유지", "공공 부문 신규 계약 7건", "제조 부문 이탈 고객 관리 필요"],
         "금융 부문은 이번에도 수주 1위를 지켰습니다. 제조 부문은 이탈 고객이 있어 따로 챙기겠습니다."),
        ("4분기 추진 과제", ["연말 정산 시즌 대비 인프라 증설", "주요 고객 재계약 조기 추진", "신규 상품 출시 일정 확정"],
         "연말에는 트래픽이 몰려서 미리 증설합니다. 재계약은 11월 안에 마무리하려고 합니다."),
        ("건의 사항", ["클라우드 예산 15% 증액 요청", "해외 영업 인력 2명 충원 검토", "분기별 실적 공유회 정례화"],
         "예산 증액은 증설 계획과 함께 검토 부탁드립니다. 인력 충원은 다음 회의에서 다시 말씀드리겠습니다."),
    ],
    "신규_서비스": [
        ("서비스 개요", ["중소 운용사용 리스크 대시보드", "월 구독형, 고객사당 월 90만원", "2027년 1분기 출시 목표"],
         "이번 서비스는 중소 운용사를 위한 대시보드입니다. 가격은 고객사당 월 90만원으로 잡았습니다."),
        ("시장 현황", ["국내 중소 운용사 약 280곳", "리스크 관리 전담 인력 부족", "기존 솔루션 도입 비용 부담"],
         "국내에 중소 운용사가 280곳 정도 있습니다. 대부분 리스크 담당자가 한두 명뿐입니다."),
        ("핵심 기능", ["포트폴리오 위험 지표 자동 산출", "규제 한도 초과 사전 알림", "일간 리포트 메일 발송"],
         "위험 지표는 매일 아침 자동으로 계산됩니다. 한도를 넘기 전에 미리 알려 주는 게 핵심입니다."),
        ("경쟁사 비교", ["글로벌 솔루션 대비 가격 1/3 수준", "국내 규제 항목 기본 탑재", "도입 기간 2주 이내"],
         "글로벌 제품보다 가격이 3분의 1 수준입니다. 국내 규제 항목을 처음부터 넣은 점이 다릅니다."),
        ("추진 일정", ["11월 요구사항 확정", "12월 시범 고객 3곳 적용", "2027년 1월 정식 출시"],
         "요구사항은 이번 달 안에 확정하겠습니다. 시범 고객 세 곳과는 이미 이야기를 나눴습니다."),
        ("필요 자원", ["개발 인력 4명, 6개월 투입", "클라우드 비용 월 800만원 예상", "영업 지원 1명 겸임"],
         "개발은 네 명이 6개월 정도 걸릴 것으로 봅니다. 영업은 당분간 기존 인력이 겸임합니다."),
    ],
    "인프라_개선": [
        ("개선 배경", ["장애 건수 상반기 14건 발생", "노후 서버 비중 35% 수준", "백업 복구 시간 목표 미달"],
         "상반기에만 장애가 14건 있었습니다. 노후 서버가 전체의 3분의 1이 넘습니다."),
        ("현황 진단", ["데이터센터 랙 사용률 92%", "네트워크 장비 교체 주기 초과", "모니터링 도구 3종 중복 운영"],
         "랙 사용률이 92%라 여유가 거의 없습니다. 모니터링 도구도 세 가지가 따로 돌고 있습니다."),
        ("개선 방향", ["노후 서버 단계적 클라우드 이전", "모니터링 도구 단일화", "백업 체계 이중화"],
         "노후 서버부터 차례로 클라우드로 옮기겠습니다. 모니터링은 하나로 합쳐서 운영 부담을 줄입니다."),
        ("단계별 계획", ["1단계 개발계 서버 이전", "2단계 운영계 이중화 구축", "3단계 구형 장비 폐기"],
         "1단계는 위험이 낮은 개발계부터 시작합니다. 운영계는 이중화를 먼저 갖춘 뒤에 옮깁니다."),
        ("기대 효과", ["장애 건수 연 10건 이하 목표", "운영 비용 연 3억원 절감", "복구 시간 4시간 이내 단축"],
         "장애는 연 10건 아래로 줄이는 것이 목표입니다. 비용은 1년에 3억원 정도 아낄 수 있습니다."),
        ("요청 사항", ["이전 예산 12억원 승인", "운영팀 야간 작업 협조", "보안 점검 일정 사전 조율"],
         "이전 예산 12억원 승인을 요청드립니다. 야간 작업은 운영팀과 일정을 맞추겠습니다."),
    ],
}

GOOD = """# 4분기 사업 계획
## S1 — 4분기 사업 목표
- 매출 1,300억원 달성
- 신규 고객 150개사 확보
- 플랫폼 매출 비중 45%로 확대
(노트: 4분기 매출 목표는 1,300억원입니다. 플랫폼 비중은 45%까지 올리려고 합니다.)
## S2 — 시장 환경 변화
- 금융권 클라우드 전환 가속
- 경쟁사 신규 서비스 출시 증가
- 규제 대응 수요 확대
(노트: 금융권이 클라우드로 빠르게 옮겨 가고 있습니다. 경쟁사도 새 서비스를 잇달아 내고 있습니다.)
## S3 — 중점 추진 과제
- 주요 고객 재계약 조기 추진
- 리스크 대시보드 시범 적용
- 인프라 이중화 1단계 착수
(노트: 재계약은 11월 안에 끝내겠습니다. 대시보드는 시범 고객 세 곳에 먼저 적용합니다.)
## S4 — 조직 운영 계획
- 해외 영업 인력 2명 충원
- 분기별 실적 공유회 정례화
- 야간 작업 운영 기준 정비
(노트: 해외 영업은 두 명을 더 뽑겠습니다. 실적 공유회는 분기마다 열겠습니다.)
## S5 — 예산 요청
- 클라우드 예산 15% 증액
- 이전 예산 12억원 승인
- 영업 지원 예산 별도 편성
(노트: 클라우드 예산은 15% 늘려 주셨으면 합니다. 이전 예산 12억원도 함께 승인 부탁드립니다.)
"""
FACTS = ("4분기 목표: 매출 1,300억원, 신규 고객 150개사, 플랫폼 비중 45%. 재계약 11월. 인프라 이중화 1단계.\n"
         "해외 영업 2명 충원. 클라우드 예산 15% 증액. 이전 예산 12억원.\n")
AI = """# 4분기 사업 계획
## S1 — 4분기에는 전사적인 디지털 전환을 가속화하여 성장을 이루겠습니다
- 4분기에는 디지털 전환을 가속화하여 매출 성장을 도모하고자 합니다.
- 이를 위해 다양한 전략적 이니셔티브를 체계적으로 추진할 계획입니다.
- 고객 가치를 극대화하는 것을 목표로 하고 있습니다.
(노트: 오늘은 4분기 사업 계획에 대해 말씀드리겠습니다. 우리는 반드시 성장할 것입니다.)
## S2 — 시장 환경은 빠르게 변화하고 있으며 이에 대한 대응이 필요합니다
- 금융 시장의 디지털화가 빠르게 진행되고 있는 상황입니다.
- 경쟁사들도 적극적으로 신규 서비스를 출시하고 있습니다.
- 따라서 우리도 선제적인 대응 전략을 마련해야 합니다.
(노트: 시장은 정말 빠르게 바뀌고 있습니다. 우리도 서둘러야 합니다.)
## S3 — 우리는 핵심 과제를 중심으로 역량을 집중해야 합니다
- 주요 고객과의 관계를 더욱 강화해 나가야 합니다.
- 새로운 서비스를 시장에 성공적으로 안착시켜야 합니다.
- 인프라의 안정성을 획기적으로 높여야 합니다.
(노트: 이 세 가지가 가장 중요합니다. 하나씩 설명드리겠습니다.)
## S4 — 조직 역량을 강화하여 실행력을 높이겠습니다
- 우수한 인재를 적극적으로 확보해 나갈 예정입니다.
- 부서 간 협업 체계를 더욱 공고히 하겠습니다.
- 성과 중심의 조직 문화를 정착시키겠습니다.
(노트: 사람이 가장 중요한 자산입니다. 함께 노력하겠습니다.)
"""
SPEC = """# Design Spec
## I. Project Information
| Canvas | 1280x720 |
## IX. Content Outline
### Part 1: 실적
#### Slide 01 - Cover
- **Cover impact**: hero number 1,240억원
- **Layout**: full-bleed 60/40
- **Title**: 3분기 실적 요약
- **Subtitle**: 매출 1,240억원, 전년 대비 12% 증가
- **Info**: 경영기획팀 / 2026. 11. 9
#### Slide 02 - 매출
- **Layout**: two-column
- **Title**: 매출 구성 변화
- **Core message**: 플랫폼 매출 비중 41%로 확대
- **Visualization**: bar_chart
- **Content**:
  - 라이선스 매출은 정체 수준
  - 해외 매출 3분기 연속 성장
## X. Speaker Notes Requirements
None requested
"""


def make_deck(path, slides):
    prs = Presentation()
    for title, bullets, notes in slides:
        s = prs.slides.add_slide(prs.slide_layouts[1])
        s.shapes.title.text = title
        tf = s.placeholders[1].text_frame
        tf.text = bullets[0]
        for b in bullets[1:]:
            tf.add_paragraph().text = b
        s.notes_slide.notes_text_frame.text = notes
    prs.save(path)


def make_free_deck(path):
    """제목 개체 없이 글상자만 있는 장표 (ppt-master 자유 배치 내보내기와 같은 모양)."""
    prs = Presentation()
    s = prs.slides.add_slide(prs.slide_layouts[6])
    for text, size, top in (("매출 성장률", 14, 0.3), ("플랫폼이 이끈 3분기 성장", 40, 0.8), ("18%", 96, 2.0),
                            ("플랫폼 매출 비중 41%로 확대", 20, 4.0), ("3", 10, 7.0)):
        tf = s.shapes.add_textbox(Inches(0.5), Inches(top), Inches(8), Inches(1)).text_frame
        tf.text = text
        tf.paragraphs[0].runs[0].font.size = Pt(size)
    tbl = s.shapes.add_table(2, 2, Inches(5), Inches(5), Inches(4), Inches(1)).table
    for (r, c), v in {(0, 0): "구분", (0, 1): "매출", (1, 0): "플랫폼", (1, 1): "1,300"}.items():
        tbl.cell(r, c).text = v
    hidden = prs.slides.add_slide(prs.slide_layouts[1])
    hidden.shapes.title.text = "백업: 지난 분기 초안"
    hidden._element.set("show", "0")
    prs.save(path)


def run(fn, argv):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        try:
            code = fn(argv)
        except SystemExit as e:
            return e.code, None
    return code, json.loads(buf.getvalue())


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    with tempfile.TemporaryDirectory() as td:
        t = Path(td)
        decks = []
        for name, slides in DECKS.items():
            decks.append(t / f"{name}.pptx")
            make_deck(decks[-1], slides)
        voice = t / "voice"

        # 1. build
        code, b = run(dv.main, ["build", *map(str, decks), "--out", str(voice), "--name", "기획팀 보고체", "--human"])
        assert code == 0 and b["label"] == "문체 소표본" and b["status"] == "verified", b
        assert b["roles"] == ["title", "body", "notes"] and all(r["pass"] for r in b["leave_one_out"]), b
        guide = (voice / "style-guide.md").read_text(encoding="utf-8")
        assert "토픽형" in b["rules"]["title"][0], b["rules"]["title"]
        assert "명사형" in b["rules"]["body"][0] and "존댓말" in b["rules"]["notes"][0], b["rules"]
        assert "제목 끝에 마침표를 찍지 않는다" in b["rules"]["title"], b["rules"]["title"]
        examples = [x for x in guide.splitlines() if x.startswith("- 본문 예문: ")][0][len("- 본문 예문: "):].split(" / ")
        human = {x for slides in DECKS.values() for _, bl, _ in slides for x in bl}
        assert examples and all(x in human for x in examples), examples   # 예문은 견본 원문 그대로
        print("1. build: 소표본, 한 건 빼고 검증 통과, 규칙·예문 확인")

        # 2. 견본 문체 개요 합격 + 숫자 일치
        (t / "good.md").write_text(GOOD, encoding="utf-8")
        (t / "facts.txt").write_text(FACTS, encoding="utf-8")
        code, g = run(dv.main, ["gate", "--voice", str(voice), "--facts", str(t / "facts.txt"), str(t / "good.md")])
        assert code == 0 and g["pass"] and not g["rework"], g
        assert g["titles"][:2] == ["4분기 사업 계획", "4분기 사업 목표"], g["titles"]
        print("2. 견본 문체 개요: 합격")

        # 3. AI투: 금지어 없이도 문체 불합격, 금지어가 있으면 즉시 불합격
        (t / "ai.md").write_text(AI, encoding="utf-8")
        code, a = run(dv.main, ["gate", "--voice", str(voice), str(t / "ai.md")])
        assert code == 3 and not a["style_pass"] and not any(x.startswith("[금지]") for x in a["rework"]), a
        assert any(x.startswith("[제목] ~요/~니다") for x in a["rework"]) and any(x.startswith("[본문]") for x in a["rework"]), a["rework"]
        (t / "tell.md").write_text(GOOD.replace("- 규제 대응 수요 확대", "- 규제 대응 수요를 살펴보겠습니다"), encoding="utf-8")
        code, h = run(dv.main, ["gate", "--voice", str(voice), str(t / "tell.md")])
        assert code == 3 and "[금지] 살펴보겠습니다: 이 표현을 빼고 다시 쓰세요" in h["rework"], h
        print("3. AI투 개요: 문체 불합격, 금지어 즉시 불합격")

        # 4. 근거에 없는 숫자
        (t / "bad_num.md").write_text(GOOD.replace("12억원", "13억원"), encoding="utf-8")
        code, f = run(dv.main, ["gate", "--voice", str(voice), "--facts", str(t / "facts.txt"), str(t / "bad_num.md")])
        assert code == 3 and f["style_pass"] and f["fidelity_pass"] is False, f
        assert any("'13'" in x for x in f["rework"]) and "12" in f["unused_facts"]["first"], f
        print("4. 숫자 대조: 근거에 없는 13 을 잡음")

        # 5. 1건 = 시험용, --human 없으면 거부
        code, one = run(dv.main, ["build", str(decks[0]), "--out", str(t / "v1"), "--human"])
        assert code == 0 and one["label"] == "문체 시험용(1건)" and one["leave_one_out"] == [], one
        code, _ = run(dv.main, ["build", str(decks[0]), "--out", str(t / "v2")])
        assert code and not (t / "v2").exists()
        print("5. 1건 시험용 라벨, --human 없이는 거부")

        # 6. design_spec §IX
        (t / "design_spec.md").write_text(SPEC, encoding="utf-8")
        d = dv.load(t / "design_spec.md")
        assert d["titles"] == ["3분기 실적 요약", "매출 구성 변화"], d["titles"]
        body = [x for s in d["slides"] for x in s["body"]]
        assert body == ["매출 1,240억원, 전년 대비 12% 증가", "플랫폼 매출 비중 41%로 확대",
                        "라이선스 매출은 정체 수준", "해외 매출 3분기 연속 성장"], body
        assert "60" not in dv.assets(d["text"])[0] and "경영기획팀" not in d["text"], d["text"]
        print("6. design_spec §IX: 문구 칸만 읽음")

        # 7. 자유 배치 덱
        make_free_deck(t / "free.pptx")
        fs = dv.read_pptx(t / "free.pptx")
        s = fs[0]
        assert len(fs) == 1, fs   # 숨긴 슬라이드는 읽지 않는다
        assert s["title"] == ["플랫폼이 이끈 3분기 성장"] and s["body"] == ["매출 성장률", "플랫폼 매출 비중 41%로 확대"], s
        assert s["extra"] == ["구분 | 매출", "플랫폼 | 1,300"] and "1300" in dv.assets(dv.load(t / "free.pptx")["text"])[0], s
        print("7. 자유 배치 덱: 가장 큰 글이 제목, 쪽 번호·단독 수치·숨긴 장 제외, 표는 숫자 대조에만")

        # 8. corpus 다시 읽기
        for i, p in enumerate(decks, 1):
            orig, again = dv.load(p), dv.load(voice / "corpus" / f"D-{i:03d}.md")
            assert orig["lines"] == again["lines"] and orig["wps"] == again["wps"], p.name
        print("8. corpus 다시 읽기: 역할 줄 동일")

        # 9. 견본에 쓴 상투구는 허용
        extra = t / "메모.md"
        extra.write_text("# 운영 메모\n\n이번 달 장애 원인을 하나씩 살펴보겠습니다. 원인은 대부분 설정 누락이었습니다.\n"
                         "재발 방지책은 다음 주에 정리합니다. 점검 일정은 운영팀과 맞추겠습니다.\n", encoding="utf-8")
        code, c = run(dv.main, ["build", *map(str, decks), str(extra), "--out", str(t / "v3"), "--human"])
        tells = json.loads((t / "v3" / "ai-tells.json").read_text(encoding="utf-8"))
        assert code == 0 and "살펴보겠습니다" not in tells["hard"] and tells["from_corpus"] == ["살펴보겠습니다"], tells
        print("9. 견본에 쓴 상투구는 금지 목록에서 뺌")

        # 10. 근거 폴더(JSON·변환 기록) + 반복 푸터 + 대문자 라벨
        src = t / "sources"
        src.mkdir()
        (src / "source.json").write_text(json.dumps({"budget": {"total": 12.34, "unit": "억원"}, "floors": [4, 5, 6, 7]},
                                                    ensure_ascii=False), encoding="utf-8")
        (src / "memo.conversion_profile.json").write_text(json.dumps({"pages": 777}), encoding="utf-8")
        prs = Presentation()
        for i in range(4):
            s = prs.slides.add_slide(prs.slide_layouts[1])
            s.shapes.title.text = f"슬라이드 {i + 4}층 계획"
            tf = s.placeholders[1].text_frame
            tf.text = ["SUMMARY", "총 12.34억원 투입", "층별 배관 교체", "층별 가구 교체"][i]
            tf.add_paragraph().text = "koscom"
            tf.add_paragraph().text = "변환 쪽수 777" if i == 3 else f"{i + 4}층 일정 확정"
        prs.save(t / "chrome.pptx")
        d = dv.load(t / "chrome.pptx")
        assert all("koscom" not in s["body"] for s in d["slides"]), d["slides"]
        f = dv.fidelity_of(dv.facts_text([src]), d["text"])
        assert f["invented"] == ["777"], f   # 12.34·4·5·6·7 은 source.json 값, 777 은 변환 기록에만 있다
        print("10. 근거 JSON 읽기, 변환 기록 제외, 반복 푸터·대문자 라벨 오탐 없음")

        # 11. 한글 개조식 .txt (합성 예문): □·기호 글꼴 대제목 -> 제목, ㅇ·-·가. 항목 -> 본문, 결재 문장 -> 노트
        (t / "보고.txt").write_text(
            " 개 요 : 본관 승강기 제어반 노후로 교체 필요\n"
            "  ㅇ (현황) 제어반 설치 후 25년 경과로 고장 빈발\n"
            "    - 부품 단종으로 수리 기간 지연\n"
            "□ 추진 계획   (단위: 백만원)\n"
            "  ㅇ 2개 호기 순차 교체\n"
            "- 아    래 -\n"
            "1. 관련근거 : 시설2025-0101(2025. 3. 2.)\n"
            "  가. 정밀점검 결과 보고\n"
            "위 근거에 의거 승강기 교체를 추진하고자 하오니 결재하여 주시기 바랍니다.\n", encoding="utf-8")
        k = dv.load(t / "보고.txt")
        assert k["titles"] == ["개 요", "추진 계획", "관련근거"], k["titles"]
        assert [x for s in k["slides"] for x in s["body"]] == [
            "본관 승강기 제어반 노후로 교체 필요", "(현황) 제어반 설치 후 25년 경과로 고장 빈발", "부품 단종으로 수리 기간 지연",
            "2개 호기 순차 교체", "시설2025-0101(2025. 3. 2.)", "정밀점검 결과 보고"], k["slides"]
        assert k["lines"]["notes"] == ["위 근거에 의거 승강기 교체를 추진하고자 하오니 결재하여 주시기 바랍니다."], k["lines"]
        print("11. 개조식 .txt: 대제목·항목·결재 문장을 역할별로 읽음")
    print("selftest OK")


if __name__ == "__main__":
    main()
