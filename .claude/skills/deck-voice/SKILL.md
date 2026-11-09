---
name: deck-voice
description: >-
  Analyze the writing style of the user's own decks and documents, then write slide copy (titles, body,
  speaker notes) in that style and check it with a script — the gn-voice method (measured style bands +
  deterministic gate) adapted to slides. Reads .pptx directly and measures titles, body, and notes
  separately. Use for "write the deck in my voice", "analyze my slide writing style", "match our team's
  deck style", and Korean requests such as "내 문체로 PPT", "우리 팀 발표자료 문체로", "이 덱들 문체 분석해서",
  "문체 분석", "예전 발표자료처럼 써줘", "장표 문구 내 말투로", "장표 텍스트로", "슬라이드 글로".
  Deck generation itself stays with the ppt-master pipeline; this skill runs before it (style analysis)
  and overlays its Step 4 copywriting and Step 7 check. Prose rewriting that is not slide copy belongs to gn-voice.
---

# deck-voice — 장표 문체 분석·적용·검사

ROOT = 이 SKILL.md가 있는 폴더. 명령은 저장소 루트에서 실행한다(`python3`가 없으면 `python`). 표준 라이브러리만 쓴다.

```
내 덱·글 ──(deck_voice.py build)──> voices/<이름>/  style-guide.md + 검사 밴드
                                        │ 복사
ppt-master 프로젝트 ── <project>/voice/ ─┬─ Step 4: style-guide 대로 §IX 작성 -> gate(design_spec.md)
                                        └─ Step 7: 내보낸 PPTX -> gate (문체 + 상투구 + 숫자)
```

## A. 문체 분석 (build)

1. **견본**: 사용자가 **직접 쓴** 덱·글 2~5건. 같은 용도(보고 덱끼리, 강의 덱끼리)를 모을수록 정밀하다.
   - AI 도움을 받은 글은 넣지 않는다(기준이 오염된다). 사용자가 "내가 쓴 자료"라고 했으면 `--human`을 붙이고, 불분명하면 한 번 묻는다.
   - 남의 저작물(책·기사·타사 덱)을 넣어 그 사람의 문체를 복제하지 않는다. 팀 문체는 팀이 쓴 자료로 만든다.
2. **형식**: `.pptx`는 그대로 넣는다(제목 개체나 가장 큰 글자로 제목을, 노트 페이지로 노트를 읽고, 숨긴 장은 뺀다). `.md`/`.txt`도 그대로. `.docx`/`.pdf`는 `python3 .claude/skills/ppt-master/scripts/source_to_md.py <파일>`로 만든 `.md`를 넣는다. 한글 문서는 `.md`나 `.txt`로 저장해 넣는다.
   - `.md` 읽기: `#` 제목 → 제목, `- `·`1. ` 목록 → 본문, 일반 문단 → 노트(말하듯 쓴 문장). 그래서 글만 줘도 제목·노트 문체는 잡히지만, 장표 본문 문체는 덱 견본이 있어야 정확하다.
   - `.txt`는 한글 개조식으로도 읽는다: `□`(기호 글꼴 포함)·짧은 `1. 제목` 줄 → 제목(`:` 뒤는 본문), `ㅇ ○ - · * ※ 가.` 항목 → 본문, 기호 없는 문장 → 노트, `- 아래 -`·`(단위: …)` 줄은 뺀다. 한글 보고서·기안문은 본문을 `.txt`로 뽑아 넣는다(예: `koscom-hwp-report`의 `voice_tool.read_text`).
3. **실행**:
   ```bash
   python3 .claude/skills/deck-voice/scripts/deck_voice.py build <견본1.pptx> <견본2.pptx> [<글.md> ...] --out voices/<이름> --name "<이름>" --human
   ```
4. **알리기**: 출력 JSON의 `label`·`leave_one_out`·`rules`를 요약해 알린다.
   - `문체 시험용(1건)`: 견본 1건. 검사는 참고만 된다. `문체 소표본`(2~3건)·`문체 표본`(4건+): 한 건 빼고 검증을 통과했다.
   - `문체 미검증`: 견본끼리 문체 차이가 크다. 용도가 같은 견본만 다시 고르게 안내한다.
5. **만들어지는 것**: `style-guide.md`(역할별 작성 규칙, 끝맺음 비율, 길이·장표당 어절, 숫자·날짜 표기, 자주 쓴 표현, 원문 예문, 검사 기준), `fingerprint-slim.json`(역할별 허용 범위), `ai-tells.json`(금지 상투구 — 견본에 실제로 쓴 표현은 자동으로 빠짐), `manifest.jsonl`, `corpus/`(서식을 걷어낸 견본). `voices/`는 git에서 빠진다. 견본 문장이 그대로 들어 있으니 공유 전에 개인정보·대외비를 확인하라고 알린다.
6. **분석만** 원하면 `style-guide.md`의 "1. 이렇게 쓴다"를 요약해 보여 주고 파일 경로를 알린 뒤 끝낸다.

## B. 덱에 입히기 (ppt-master)

1. ppt-master Step 2에서 프로젝트를 만든 뒤 문체 폴더를 `<project>/voice/`로 복사한다(`cp -r voices/<이름> <project>/voice`, PowerShell은 `Copy-Item -Recurse`). 견본을 이번에 처음 받았으면 `build --out <project>/voice`로 바로 만든다.
2. 나머지는 ppt-master가 한다: Step 4의 **Voice overlay**가 `voice/style-guide.md`와 [`references/presentation.md`](references/presentation.md)를 읽고 §IX를 그 문체로 쓴 뒤 `design_spec.md`를 검사하고, Step 7이 내보낸 PPTX를 다시 검사한다. 확인 단계(Confirm UI)는 늘지 않는다.
3. 규칙이 부딪히면: 장표 구조(한 장표 한 메시지, 제목만 읽어도 이야기가 흐름, 불릿 병렬, 장표와 대본 분리)는 `presentation.md`, 표면(끝맺음·길이·밀도·숫자 표기·표현)은 `style-guide.md`가 이긴다. 폰트·레이아웃·text-fit 등 ppt-master 규칙은 건드리지 않는다.

## C. 덱 없이 장표 문구만 (gn-voice "장표 텍스트로")

PPTX 없이 "이 글을 장표 문구로/슬라이드 글로"만 원하면:
1. `presentation.md`의 로직과 출력 포맷(`## S1 — 헤드라인` / `- 불릿` / `(노트: …)`)으로 `<작업폴더>/deck_outline.md`를 쓴다. 문체 폴더가 있으면 `style-guide.md`를 덧입힌다.
2. `deck_voice.py gate --voice <문체 폴더> --facts <원문 파일> <작업폴더>/deck_outline.md`로 검사하고 D의 순서로 고친다.
3. 결과 개요를 보여 준다. 문체 폴더가 없으면 gate 없이 `presentation.md`의 자기검증만 한다.

## D. 검사(gate)와 고치기

```bash
python3 .claude/skills/deck-voice/scripts/deck_voice.py gate --voice <project>/voice --facts <project>/sources <대상>
```

- **대상**: `design_spec.md`(§IX의 Title·Subtitle·Core message·Content만 읽는다), 개요 `.md`, 내보낸 `.pptx`.
- **`--facts`**: 근거 파일이나 폴더. 폴더면 `.md .txt .csv .tsv .json .jsonl .yaml`을 읽고(JSON은 값만), 변환 기록 `*.conversion_profile.json`은 뺀다. 사용자가 대화로 준 수치·날짜·작성자 정보는 `<project>/sources/request_facts.md`에 적어 두고 함께 넘긴다.
- **exit 0** = 합격. **exit 3**이면 `rework` 항목만 고친다.
  - `[금지]`: 그 표현을 뺀다.
  - `[제목]`·`[본문]`·`[노트] … 높습니다/낮습니다`: 그 역할의 줄을 `style-guide.md` 규칙 쪽으로 고친다(예: 본문 `~요/~니다` 높음 → 명사형으로, 장표당 어절 수 높음 → 줄이거나 장표를 나눈다).
  - `[숫자] 근거에 없는 값`: 근거대로 고치거나 `[확인 필요]`로 표시한다. 계산한 값(합계·비율)은 계산 근거를 `request_facts.md`에 적는다.
  - 고친 뒤 다시 gate. **최대 2번**. 그래도 문체가 불합격이면 남은 항목을 그대로 보고하고 진행한다. **숫자 불합격은 고치기 전에는 진행하지 않는다.**
- **`titles`**: 제목만 이어 읽어 이야기가 흐르는지 직접 확인한다(타이틀만 읽기 테스트).
- **`skipped_roles`**: 3줄 미만이라 검사하지 않은 역할. **`reference_only: true`**(견본 1건)면 문체 결과는 참고만 한다.

## 한계

- 형태소 분석기 없이 정규식으로 끝맺음을 센다(gn-voice 런타임 검사와 같은 근사). '점검'처럼 ㅁ 받침 명사를 `~음`으로 세는 오분류가 조금 있다.
- 제목 개체가 없는 덱은 글자가 가장 큰 짧은 글을 제목으로 본다. 표·차트 안 글은 문체 측정에서 빼고, 표 글자만 숫자 대조에 넣는다.
- 도식 글자(줄인 연도 날짜 `’25.3`, 영문 대문자 장 라벨, 한 장에 3번 이상 똑같이 나오는 간트 막대·범례 글)도 문체 측정에서 빼고 숫자 대조에만 넣는다.
- 숫자 안의 점(`12.34`)과 천 단위 쉼표(`1,300`)는 문장부호로 세지 않는다.
- 덱 절반 이상의 장에 똑같이 반복되는 본문 줄(회사명·푸터·대외비 표기)은 틀로 보고 뺀다. 대문자 장 라벨(`SUMMARY` 등) 줄의 영문은 숫자 대조의 영문 이름에서 뺀다.
- 스크립트 판정은 문체의 통계적 근사다. 올리기 전 마지막 판단은 사람이 읽고 한다.

## 출처

gn-voice(MIT 부분)에서 가져온 것과 가져오지 않은 것은 [`NOTICE.md`](NOTICE.md)에 적었다. 자체검사: `python3 .claude/skills/deck-voice/scripts/selftest.py`(고쳤으면 실행).
