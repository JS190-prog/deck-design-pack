---
deck_id: motion-cue
kind: deck
native_structure_mode: structured
summary: 다크 모션그래픽 덱 — 교육·설명 발표, 제품 데모, 해커톤 피칭, 사내 교육 오프닝, 영상 녹화용 발표 (한 장면 한 초점, 페이지별 모션 맵 동봉)
canvas_format: ppt169
canvas_width: 1280
canvas_height: 720
canvas_viewbox: "0 0 1280 720"
source_canvas_width: 1280
source_canvas_height: 720
source_viewbox: "0 0 1280 720"
replication_mode: standard
page_count: 10
primary_color: "#FFE14D"
keywords: [motion, kinetic, timecode, animation-map, video-ready]
defaults:
  mode: showcase
  visual_style: dark-tech
  delivery_purpose: presentation
placeholders:
  01_cover: ["{{TIMECODE}}", "{{TITLE}}", "{{SUBTITLE}}", "{{AUTHOR}}", "{{DATE}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  02_agenda: ["{{TIMECODE}}", "{{TITLE}}", "{{TOC_ITEM_1_TC}}", "{{TOC_ITEM_1_TITLE}}", "{{TOC_ITEM_1_DESC}}", "{{TOC_ITEM_2_TC}}", "{{TOC_ITEM_2_TITLE}}", "{{TOC_ITEM_2_DESC}}", "{{TOC_ITEM_3_TC}}", "{{TOC_ITEM_3_TITLE}}", "{{TOC_ITEM_3_DESC}}", "{{TOC_ITEM_4_TC}}", "{{TOC_ITEM_4_TITLE}}", "{{TOC_ITEM_4_DESC}}", "{{TOC_ITEM_5_TC}}", "{{TOC_ITEM_5_TITLE}}", "{{TOC_ITEM_5_DESC}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  03_section: ["{{TIMECODE}}", "{{CHAPTER_NUM}}", "{{CHAPTER_TITLE}}", "{{CHAPTER_DESC}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  04_word_emphasis: ["{{TIMECODE}}", "{{STATEMENT}}", "{{EMPHASIS}}", "{{STATEMENT_NOTE}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  05_stagger_cards: ["{{TIMECODE}}", "{{TITLE}}", "{{LEAD}}", "{{CARD_1_TITLE}}", "{{CARD_1_BODY}}", "{{CARD_2_TITLE}}", "{{CARD_2_BODY}}", "{{CARD_3_TITLE}}", "{{CARD_3_BODY}}", "{{CARD_4_TITLE}}", "{{CARD_4_BODY}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  06_count_up: ["{{TIMECODE}}", "{{TITLE}}", "{{KPI_VALUE}}", "{{KPI_LABEL}}", "{{KPI_NOTE}}", "{{STAT_1_VALUE}}", "{{STAT_1_LABEL}}", "{{STAT_2_VALUE}}", "{{STAT_2_LABEL}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  07_bar_grow: ["{{TIMECODE}}", "{{TITLE}}", "{{TAKEAWAY}}", "{{TAKEAWAY_NOTE}}", "{{SOURCE}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  08_line_draw: ["{{TIMECODE}}", "{{TITLE}}", "{{LEAD}}", "{{STEP_1_TITLE}}", "{{STEP_1_DESC}}", "{{STEP_2_TITLE}}", "{{STEP_2_DESC}}", "{{STEP_3_TITLE}}", "{{STEP_3_DESC}}", "{{STEP_4_TITLE}}", "{{STEP_4_DESC}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  09_spotlight: ["{{TIMECODE}}", "{{TITLE}}", "{{ITEM_1_TITLE}}", "{{ITEM_1_BODY}}", "{{ITEM_2_TITLE}}", "{{ITEM_2_BODY}}", "{{ITEM_3_TITLE}}", "{{ITEM_3_BODY}}", "{{ITEM_4_TITLE}}", "{{ITEM_4_BODY}}", "{{FOCUS_TITLE}}", "{{FOCUS_BODY}}", "{{FOCUS_NOTE}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  10_closing: ["{{TIMECODE}}", "{{CLOSING_LINE}}", "{{CONTACT_LINE}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
---

# Motion Cue — Design Specification

> 원저작 템플릿. 영상 편집·모션그래픽 도구에서 널리 쓰이는 **비독점 화면 문법** — 크롭 마크와 세이프 영역 브래킷, 타임코드, 타임라인 눈금자, 베지어 이징 커브와 핸들 점, 스피드 라인 — 을 PPTX 슬라이드 문법으로 새로 설계했다. 모션 원칙·기법 이름은 gongnyang/awesome-ai-motion(MIT)을 참고했으며 코드·클립은 포함하지 않는다. 어떤 회사의 상표·로고·독점 UI도 복제하거나 번들하지 않으며, 브랜드 표기는 `{{BRAND_MARK}}` 텍스트로만 존재한다. 글꼴은 install-local Pretendard 락을 따른다.

---

## I. Template Overview

| Property | Description |
| --- | --- |
| **Template Name** | motion-cue |
| **Display Name** | 모션 큐 |
| **Use Cases** | 교육·설명 발표, 제품 데모, 해커톤 피칭, 사내 교육 오프닝, 영상 녹화용 발표 |
| **Design Tone** | 리듬감·명료·한 장면 한 초점 — 움직임은 읽는 순서를 만들 때만 쓴다 |
| **Theme Mode** | **Dark** 단일 — 전 페이지 `#0D0F14` |

한눈에 보이는 정체성: 검은 화면 네 모서리의 크롭 마크, 좌상단 타임코드와 눈금자, 페이지마다 **노란 큐 하나**, 그 뒤를 따르는 시안 스피드 라인. 정지 화면이 이미 "다음 동작"을 예고한다.

**Anti-mood**: "모든 요소가 날아다니는 AI 덱", "네온 그라디언트 사이버펑크", "아이콘 그리드 SaaS", "장식용 파티클".

**Litmus test**: 페이지에서 노랑을 찾았을 때 그것이 **청중이 마지막에 봐야 할 한 곳**이면 통과. 노랑이 두 곳이거나, 노란 요소가 아무 의미 없이 움직이면 실패다.

---

## II. Canvas Specification

| Property | Value |
| --- | --- |
| **Format** | Standard 16:9 (`ppt169`) |
| **Dimensions** | 1280 × 720 px |
| **viewBox** | `0 0 1280 720` |
| **Side margins** | 80px — 콘텐츠 폭 1120 (x: 80 → 1200) |
| **Kinetic indent** | 표지·섹션·KPI의 대형 타입은 x=168(또는 160)에서 시작 — 왼쪽 80–148은 스피드 라인 자리 |
| **Header** | 타임코드 x=80 baseline y=77 / 눈금자 x=240→1200, y=72 / 페이지 제목 baseline y=146 |
| **Footer chrome** | 좌 `{{BRAND_MARK}}` x=80 / 우 `{{PAGE_LABEL}}` x=1200 anchor end, baseline y=680 |
| **Frame guides** | 크롭 마크 인셋 28px(마스터), 세이프 브래킷 64/48 → 1216/644(표지·섹션·클로징 레이아웃) |

---

## III. Color Scheme — LOCKED

이 8개 외의 HEX는 어떤 생성 SVG에도 나타나서는 안 된다.

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | `#0D0F14` | 전 페이지 배경(마스터), 노란 띠 위 글자색, 핸들 점 내부 |
| Panel | `#151923` | 카드·타일 서피스 |
| Guide | `#2A2F3A` | 세이프 브래킷, 눈금자, 헤어라인, 그리드, 비활성 카드 상단 바, 장식 대형 순번 |
| Text | `#F5F7FA` | 제목·대형 타입·카드 제목 |
| Body | `#A8AEBD` | 본문·리드·부제·타임코드 |
| Muted | `#6B7280` | 크롬 전용(푸터, 축 눈금, 12–14px 라벨), 크롭 마크, 비강조 막대 |
| Cue yellow | `#FFE14D` | **페이지당 단 하나의 초점** — 움직임이 도착하는 곳 |
| Cyan | `#4DD8FF` | 보조 동작 — 스피드 라인, 이징 커브, 보조 지표 바, STEP 라벨 |

### Color Rules

- **노랑은 페이지당 정확히 한 요소(군)**: 표지 밑줄, 섹션 숫자, 강조 띠, 마지막 카드 상단 바, KPI 숫자, 피크 막대, 그려지는 트랙, 포커스 브래킷, 클로징 밑줄, 아젠다 플레이헤드
- **노랑 = 주 동작의 대상.** 노란 요소가 정지해 있는 장식이면 안 된다 — 모션 맵(§VII)에서 노란 그룹은 항상 주 동작 또는 그 도착점이다
- **시안은 노랑을 돕는다.** 스피드 라인은 노란·흰 초점 뒤(왼쪽)에만 2–3줄, 불투명도 1 → 0.6 → 0.3
- **다크 위 본문(≥18px)은 `#A8AEBD` 이상 밝기.** `#6B7280`은 12–14px 크롬과 비데이터 장식에만
- 노란 띠 위 글자는 `#0D0F14` — 흰 글자를 노랑 위에 올리지 않는다
- **Forbidden**: 그라디언트, 그림자, 글로우, 8색 외 유채색

---

## IV. Typography System

install-local Pretendard 락. 대형 키네틱 타입은 ExtraBold, 제목은 700, 라벨은 SemiBold.

| Weight | `font-family` attribute |
| --- | --- |
| 400 | `Pretendard, 'Malgun Gothic', sans-serif` |
| 500 | `'Pretendard Medium', Pretendard, 'Malgun Gothic', sans-serif` |
| 600 | `'Pretendard SemiBold', Pretendard, 'Malgun Gothic', sans-serif` |
| 700 | `Pretendard, 'Malgun Gothic', sans-serif` + `font-weight="700"` |
| 800 | `'Pretendard ExtraBold', Pretendard, 'Malgun Gothic', sans-serif` |

| Role | Size | Weight | Color | Use |
| --- | --- | --- | --- | --- |
| Section number | 260 | 800 | yellow | `03` 거대 숫자 |
| KPI value | 200 | 800 | yellow | `06` 카운트업 숫자 |
| Kinetic title | 72 | 800 | text | `01` 표지 제목 |
| Emphasis word | 68 | 800 | bg on yellow | `04` 강조 띠 |
| Closing line | 64 | 800 | text | `10` 클로징 |
| Statement / Chapter title | 52 | 700 | text | `04` 진술문, `03` 장 제목 |
| Stat value | 48 | 700 | text | `06` 보조 지표 |
| Page title | 40 | 700 | text | 콘텐츠 페이지 제목 |
| Card / step title | 24–26 | 600 | text | 카드·단계·목차 제목 |
| Subtitle / lead | 22–26 | 400 | body | 부제·리드·노트 |
| Body | 18–20 | 400 | body | 본문·설명 |
| Timecode | 14 | 600, +1.5 | body | 타임코드 키커 |
| Chrome label | 12–14 | 500/600 | muted | 푸터, 축 눈금, `PRESENTER`/`DATE` 라벨 |

**자간**: 한글 비중 높은 대형 타입은 -0.5 ~ -1, 숫자 전용 대형 타입은 -5 ~ -6. 본문은 0 근처.
**본문 하한 18px**, 크롬은 12–14px. 그 사이(15–17px)는 쓰지 않는다.

---

## V. Page Roster

| File | Layout key | Picker name | 고정 Layout 원자 | 슬롯 | Purpose |
| --- | --- | --- | --- | --- | --- |
| `01_cover.svg` | `01_cover` | Cover (Kinetic Title) | 세이프 브래킷, 이징 그리드·축·라벨 | slide-number | 표지 — 키네틱 제목 + 이징 커브 + 노란 밑줄 큐 |
| `02_agenda.svg` | `02_agenda` | Agenda (Timecoded) | 눈금자, 목차 레일 | title, slide-number | 타임코드 목차 5행 + 노란 플레이헤드 |
| `03_section.svg` | `03_section` | Section (Push-in Number) | 세이프 브래킷, 세로 구분선 | title, slide-number | 장 전환 — 거대 노란 숫자 + 스피드 라인 + ease-in-out 모션 패스 |
| `04_word_emphasis.svg` | `04_word_emphasis` | Word Emphasis (Highlight Sweep) | 눈금자 | title(진술문), slide-number | 진술문 + 노란 하이라이트 띠 위 강조어 |
| `05_stagger_cards.svg` | `05_stagger_cards` | Stagger Cards (4-up) | 눈금자, 스태거 틱 라인 | title, body(리드), slide-number | 4카드 순차 등장, 마지막 카드만 노란 바 |
| `06_count_up.svg` | `06_count_up` | Count-up KPI | 눈금자, KPI 구분선 | title, slide-number | 거대 KPI 1 + 보조 지표 2 |
| `07_bar_grow.svg` | `07_bar_grow` | Bar Grow Chart | 눈금자, 테이크어웨이 구분선 | title, slide-number | 6막대 + 노란 피크 + 테이크어웨이 |
| `08_line_draw.svg` | `08_line_draw` | Line Draw Process | 눈금자, 트랙 가이드 | title, body(리드), slide-number | 노란 트랙이 그려지는 4단계 프로세스 |
| `09_spotlight.svg` | `09_spotlight` | Spotlight (Focus + Context) | 눈금자 | title, slide-number | 흐린 맥락 4 + 노란 포커스 브래킷 1 |
| `10_closing.svg` | `10_closing` | Closing (End Card) | 세이프 브래킷, 중앙 마크 | slide-number | 중앙 정렬 엔드 카드 + 노란 밑줄 큐 |

- Master `motion-master` / "Motion Cue": 배경 `#0D0F14` + 네 모서리 크롭 마크. 10페이지 모두 동일하다.
- 모든 Layout 키는 고정 원자 또는 슬롯 계약이 서로 다르다(위 표). 같은 계약을 공유하는 페이지는 없다.
- **`01`·`10`은 제목 슬롯이 없는 고정 구성이다.** 제목 자체가 주 동작이라 애니메이션 가능한 Slide-local 그룹(`cover-title`, `closing-title`)에 둔다 — 슬롯은 내보내기에서 애니메이션 대상이 될 수 없다(§VII).
- 타임코드(`timecode-header`)와 브랜드 푸터(`page-footer`)는 `data-pptx-role="header|footer"` 정적 그룹, 페이지 번호는 `slide-number` 슬롯 — 셋 다 애니메이션에서 자동 제외된다.

---

## VI. Signature Design Elements

1. **비디오 프레임 가이드** — 마스터의 크롭 마크(`#6B7280`, 인셋 28)와 앵커 페이지의 세이프 브래킷(`#2A2F3A`, 64/48). 클로징은 프레임 중앙 마크를 더한다
2. **타임코드 키커 + 눈금자** — 모든 페이지에 `{{TIMECODE}}`(예: `00:12`, `01:30`). 콘텐츠 페이지는 눈금자(40px 간격, 160px마다 긴 눈금)가 헤더를 이룬다. 타임코드는 발표 흐름상 위치이며, 녹화용이면 실제 영상 시점과 맞춘다
3. **이징 커브 오너먼트** — 표지는 그래프 에디터형 ease-out 커브(`0.16, 0.84, 0.44, 1`)와 핸들 점, 섹션은 키프레임 다이아몬드가 달린 ease-in-out 모션 패스. 커브 수치를 바꾸면 라벨도 함께 바꾼다
4. **스피드 라인** — 초점 요소 왼쪽 2–3줄 시안 라인(길이 68/48/28, 우측 정렬, 불투명도 1/0.6/0.3). 표지 제목·섹션 숫자·KPI에만 쓴다
5. **하이라이트 스윕 띠** — `04`의 노란 띠. 띠 폭 = 강조어 폭 + 좌우 24px, 높이 96(68px 글자 기준)
6. **키네틱 대형 타입** — 72–260px ExtraBold. 페이지당 대형 타입은 하나

---

## VII. 모션 맵 — awesome-ai-motion 기법 → PowerPoint 효과

공통 규칙(출처 원칙): **한 장면 한 초점, 주 동작 1 + 보조 1–2, 카드 기본값에서 시작, 완성 상태를 읽을 만큼 홀드.** PPTX에서는 이를 다음처럼 옮긴다.

- 페이지 제목·리드 슬롯은 **슬라이드 전환과 함께 정지 상태로 먼저 보인다**(문장을 먼저 보여 주고 초점을 움직이는 순서). 움직이는 것은 Slide-local 그룹뿐이다
- 트리거는 기본 `after-previous`(녹화·키오스크). 라이브 발표에서 화자가 박자를 쥐려면 슬라이드 `animation.trigger`만 `on-click`으로 바꾼다
- 효과 방향은 파이프라인 튜플로 고정된다: `fly` = 아래에서(`slide(fromBottom)`), `wipe` = 가로(`wipe(left)`). 막대 성장은 그래서 `fly`로 옮긴다
- 같은 슬라이드 안에서 그룹마다 트리거를 달리할 수 없다. 보조 동작은 주 동작 **뒤에** 짧게 이어지거나, 같은 그룹 안에 묶여 함께 들어온다(스피드 라인은 초점 그룹 안)

| Page | 주 동작 (그룹 → 효과 / 지속) | 보조 동작 | 정지 그룹 | awesome-ai-motion 기법 | 전환 | 애니메이션 합계 | 홀드 | 녹화용 `auto_advance` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `01_cover` | `cover-title` → fade 0.7 | ① `cue-track` → wipe 0.45 (+0.3) ② `easing-track` → wipe 0.8 (+0.2) | `cover-meta` | mask-reveal · motion-hierarchy → underline-draw · easing-curves (레시피 title-opener) | fade 0.6 | 2.45s | 2.0s | 4.5 |
| `02_agenda` | `item-1..5` → fly 0.25 ×5 (+0.05) | `callout-playhead` → zoom 0.35 (+0.2) | `title-slot` | stagger → focus-handoff | fade 0.4 | 2.0s | 3.0s | 5.0 |
| `03_section` | `chapter-number` → zoom 0.8 | ① `chapter-desc` → fade 0.4 (+0.2) ② `easing-track` → wipe 0.7 (+0.2) | `title-slot` | push-in → motion-hierarchy (레시피 chapter-transition) | **wipe 0.5** | 2.3s | 1.5s | 4.0 |
| `04_word_emphasis` | `highlight-track` → wipe 0.9 (지연 0.3) | `statement-note` → fade 0.4 (+0.2) | `title-slot` | highlight-sweep · word-emphasis (레시피 quote-card) | fade 0.4 | 1.8s | 2.5s | 4.5 |
| `05_stagger_cards` | `card-1..4` → fly 0.35 ×4 (+0.06) | — (마지막 카드의 노란 바가 도착점) | `title-slot`, `lead-slot` | stagger | fade 0.4 | 1.58s | 3.0s | 5.0 |
| `06_count_up` | `kpi` → zoom 0.6 | ① `value-note` → fade 0.3 (+0.25) ② `callout-stats` → fade 0.4 (+0.3) | `title-slot` | count-up (레시피 data-story 첫 박자) | fade 0.4 | 1.85s | 2.0s | 4.0 |
| `07_bar_grow` | `chart-bars` → fly 0.9 | ① `chart-values` → fade 0.3 (+0.2) ② `takeaway` → fade 0.5 (+0.3) | `title-slot`, `chart-axis`, `source` | bar-grow → annotation-callout | fade 0.4 | 2.2s | 3.0s | 5.5 |
| `08_line_draw` | `timeline-track` → wipe 1.2 | `step-1..4` → fly 0.3 ×4 (+0.06) | `title-slot`, `lead-slot` | line-draw → stagger | fade 0.4 | 2.64s | 3.0s | 6.0 |
| `09_spotlight` | `hero-focus` → circle 0.65 | `focus-note` → fade 0.4 (+0.5) | `title-slot`, `context-items` | spotlight (레시피 concept-explainer 끝 박자) | fade 0.4 | 1.55s | 2.5s | 4.0 |
| `10_closing` | `closing-title` → fade 0.8 | ① `cue-track` → wipe 0.45 (+0.3) ② `contact-note` → fade 0.5 (+0.3) | — | motion-hierarchy → underline-draw | fade 0.8 | 2.35s | 3.0s | 5.5 |

`(+n)`은 앞 그룹이 끝난 뒤의 간격(초)이다. 카드 기본값(예: stagger 0.06s, bar-grow 1.05s, line-draw 1.85s, spotlight 0.65s, highlight-sweep 1.35s)을 PowerPoint 효과 길이에 맞게 줄였고, 큰 목록의 총 등장 시간은 1.5–2초 안에 둔다. 홀드는 최종 상태를 읽는 시간(카드 권장 ≥0.5s + 읽기)이며, 라이브 발표에서는 화자가 말하는 시간이 곧 홀드다.

### 그룹 id와 `-a auto` 매핑

| id 규칙 | auto 결과 | 쓰는 곳 |
| --- | --- | --- |
| `*-title`, `chapter-*`, `cover-*` | fade | `cover-title`, `closing-title`, `chapter-number`, `chapter-desc`, `cover-meta` |
| `*track*`, `chart-*`, `timeline*` | wipe | `cue-track`, `easing-track`, `highlight-track`, `timeline-track`, `chart-*` |
| `item-*`, `card-*`, `step-*` | fly | 목차 행, 카드, 단계 |
| `*callout*`, `*note*`, `takeaway`, `source` | fade | `callout-playhead`, `callout-stats`, `value-note`, `statement-note`, `focus-note`, `contact-note` |
| `kpi`, `hero-*` | 이미지 풀 순환(zoom/dissolve/circle/box/diamond/wheel) | `kpi`, `hero-focus` |

> **슬롯과 `-a auto`**: 사이드카 없이 `-a auto`만 주면 `title`/`body` 슬롯도 함께 움직인다(내보내기는 정상). 이 덱은 "한 장면 한 초점"을 지키려고 아래 사이드카처럼 **슬라이드 기본값은 `effect: "auto"`, 모든 `title-slot`·`lead-slot`은 `"none"`으로 고정**한다 — 제목은 처음부터 서 있고 노란 초점만 움직인다. 타임코드·푸터(role 그룹)와 `slide-number` 슬롯은 자동 제외라 적지 않는다.

### 예시 `animations.json` (전 페이지, 그대로 복사)

프로젝트 SVG 파일명이 템플릿과 다르면 `slides` 키를 실제 SVG stem으로 바꾼다. 녹화용이면 각 슬라이드 `transition`에 위 표의 `"auto_advance"`를 더한다(클릭 진행은 계속 가능하므로 라이브 발표에는 넣지 않는다).

```json
{
  "version": 1,
  "defaults": {
    "transition": { "effect": "fade", "duration": 0.4 },
    "animation": { "effect": "auto", "duration": 0.4, "stagger": 0.2, "trigger": "after-previous" }
  },
  "slides": {
    "01_cover": {
      "transition": { "effect": "fade", "duration": 0.6 },
      "animation": { "effect": "auto", "duration": 0.5, "stagger": 0.3, "trigger": "after-previous" },
      "groups": {
        "cover-meta": { "effect": "none" },
        "cover-title": { "effect": "fade", "duration": 0.7 },
        "cue-track": { "effect": "wipe", "duration": 0.45 },
        "easing-track": { "effect": "wipe", "duration": 0.8, "delay": 0.2 }
      }
    },
    "02_agenda": {
      "transition": { "effect": "fade", "duration": 0.4 },
      "animation": { "effect": "auto", "duration": 0.25, "stagger": 0.05, "trigger": "after-previous" },
      "groups": {
        "title-slot": { "effect": "none" },
        "callout-playhead": { "effect": "zoom", "duration": 0.35, "delay": 0.2 }
      }
    },
    "03_section": {
      "transition": { "effect": "wipe", "duration": 0.5 },
      "animation": { "effect": "auto", "duration": 0.4, "stagger": 0.2, "trigger": "after-previous" },
      "groups": {
        "title-slot": { "effect": "none" },
        "chapter-number": { "effect": "zoom", "duration": 0.8 },
        "easing-track": { "effect": "wipe", "duration": 0.7 }
      }
    },
    "04_word_emphasis": {
      "transition": { "effect": "fade", "duration": 0.4 },
      "animation": { "effect": "auto", "duration": 0.4, "stagger": 0.2, "trigger": "after-previous" },
      "groups": {
        "title-slot": { "effect": "none" },
        "highlight-track": { "effect": "wipe", "duration": 0.9, "delay": 0.3 }
      }
    },
    "05_stagger_cards": {
      "transition": { "effect": "fade", "duration": 0.4 },
      "animation": { "effect": "auto", "duration": 0.35, "stagger": 0.06, "trigger": "after-previous" },
      "groups": {
        "title-slot": { "effect": "none" },
        "lead-slot": { "effect": "none" }
      }
    },
    "06_count_up": {
      "transition": { "effect": "fade", "duration": 0.4 },
      "animation": { "effect": "auto", "duration": 0.4, "stagger": 0.3, "trigger": "after-previous" },
      "groups": {
        "title-slot": { "effect": "none" },
        "kpi": { "effect": "zoom", "duration": 0.6 },
        "value-note": { "effect": "fade", "duration": 0.3, "delay": 0.25 }
      }
    },
    "07_bar_grow": {
      "transition": { "effect": "fade", "duration": 0.4 },
      "animation": { "effect": "auto", "duration": 0.4, "stagger": 0.2, "trigger": "after-previous" },
      "groups": {
        "title-slot": { "effect": "none" },
        "chart-axis": { "effect": "none" },
        "chart-bars": { "effect": "fly", "duration": 0.9 },
        "chart-values": { "effect": "fade", "duration": 0.3 },
        "takeaway": { "effect": "fade", "duration": 0.5, "delay": 0.3 },
        "source": { "effect": "none" }
      }
    },
    "08_line_draw": {
      "transition": { "effect": "fade", "duration": 0.4 },
      "animation": { "effect": "auto", "duration": 0.3, "stagger": 0.06, "trigger": "after-previous" },
      "groups": {
        "title-slot": { "effect": "none" },
        "lead-slot": { "effect": "none" },
        "timeline-track": { "effect": "wipe", "duration": 1.2 }
      }
    },
    "09_spotlight": {
      "transition": { "effect": "fade", "duration": 0.4 },
      "animation": { "effect": "auto", "duration": 0.4, "stagger": 0.2, "trigger": "after-previous" },
      "groups": {
        "title-slot": { "effect": "none" },
        "context-items": { "effect": "none" },
        "hero-focus": { "effect": "circle", "duration": 0.65 },
        "focus-note": { "effect": "fade", "duration": 0.4, "delay": 0.5 }
      }
    },
    "10_closing": {
      "transition": { "effect": "fade", "duration": 0.8 },
      "animation": { "effect": "auto", "duration": 0.5, "stagger": 0.3, "trigger": "after-previous" },
      "groups": {
        "closing-title": { "effect": "fade", "duration": 0.8 },
        "cue-track": { "effect": "wipe", "duration": 0.45 }
      }
    }
  }
}
```

검증: 이 블록은 템플릿 SVG 10장을 그대로 넣은 프로브 프로젝트에서 `animation_config.py validate` 통과, `svg_to_pptx.py` 내보내기·애니메이션 리드백 통과(슬라이드별 진입 행: 3/6/3/2/4/3/3/5/2/3).

**페이지를 반복할 때**: 같은 템플릿 페이지를 여러 장 쓰면 각 SVG stem마다 블록을 복사한다. 카드·단계·목차 행 수를 줄이면 남는 id를 지우고, 늘리면 같은 접두사(`card-5`, `step-5`)를 이어 쓴다 — 접두사가 auto 매핑을 유지한다.

---

## VIII. Chart Treatment (`07_bar_grow`)

- 플롯: `<!-- chart-plot-area: 136,232,800,552 -->`, 6칸 균등 분할, 막대 폭 64, 라운드 2
- 그리드: 가로 4줄 `#2A2F3A` 1px + 기준선 `#6B7280` 1.5px. 세로 그리드·프레임 금지
- 축: y 눈금 14px `#6B7280` anchor end(x=120), x 범주 18px `#A8AEBD` anchor middle(y=586)
- 막대: 비강조 `#6B7280`, **피크 하나만 `#FFE14D`** — 피크가 곧 페이지 초점
- 값 라벨: 18px `#A8AEBD`, 피크만 20px 700 `#F5F7FA`, 막대 위 14px
- 차트는 세 그룹으로 나눈다: `chart-axis`(정지) → `chart-bars`(주 동작) → `chart-values`(보조). 막대와 값을 한 그룹에 넣지 않는다
- 테이크어웨이는 구분선(x=840) 오른쪽 x=896, 시안 바와 함께. 출처는 `{{SOURCE}}` 13px
- **Forbidden**: 다색 계열, 범례 남발, 그림자, 3D, 파이

---

## IX. Placeholder Vocabulary

| Token | Pages | Content |
| --- | --- | --- |
| `{{TIMECODE}}` | 전 페이지 | 타임코드 키커 `mm:ss` (예: `00:12`) |
| `{{TITLE}}` / `{{SUBTITLE}}` | 01 / 02·05–09 | 표지 제목·부제 / 페이지 제목 |
| `{{AUTHOR}}` / `{{DATE}}` | 01 | 슬레이트형 발표자·날짜 |
| `{{TOC_ITEM_n_TC}}` / `{{TOC_ITEM_n_TITLE}}` / `{{TOC_ITEM_n_DESC}}` | 02 | 목차 시작 시점·제목·설명 (n=1..5) |
| `{{CHAPTER_NUM}}` / `{{CHAPTER_TITLE}}` / `{{CHAPTER_DESC}}` | 03 | 2자리 장 번호·장 제목·한 줄 설명 |
| `{{STATEMENT}}` / `{{EMPHASIS}}` / `{{STATEMENT_NOTE}}` | 04 | 진술문 앞부분 / 노란 띠 강조어(2–8자) / 보조 문장 |
| `{{LEAD}}` | 05·08 | 리드 한 줄 |
| `{{CARD_n_TITLE}}` / `{{CARD_n_BODY}}` | 05 | 카드 (n=1..4) |
| `{{KPI_VALUE}}` / `{{KPI_LABEL}}` / `{{KPI_NOTE}}` | 06 | 대형 지표(4자 이내, 단위 포함 가능) / 라벨 / 근거 |
| `{{STAT_n_VALUE}}` / `{{STAT_n_LABEL}}` | 06 | 보조 지표 (n=1..2) |
| `{{TAKEAWAY}}` / `{{TAKEAWAY_NOTE}}` / `{{SOURCE}}` | 07 | 결론 / 보조 설명 / 출처 |
| `{{STEP_n_TITLE}}` / `{{STEP_n_DESC}}` | 08 | 단계 (n=1..4) |
| `{{ITEM_n_TITLE}}` / `{{ITEM_n_BODY}}` | 09 | 흐린 맥락 항목 (n=1..4; 열 1·2·4·5) |
| `{{FOCUS_TITLE}}` / `{{FOCUS_BODY}}` / `{{FOCUS_NOTE}}` | 09 | 포커스 항목 / 왜 이것인가 |
| `{{CLOSING_LINE}}` / `{{CONTACT_LINE}}` | 10 | 클로징 문장 / 연락처 |
| `{{BRAND_MARK}}` | 전 페이지 푸터 | 브랜드명 **텍스트** |
| `{{PAGE_LABEL}}` | 전 페이지 푸터 | 페이지 번호 (`slide-number` 슬롯) |

`CARD_n_BODY`·`STEP_n_DESC`·`ITEM_n_BODY`는 열 폭 안에서 2–3줄로 줄바꿈한다(18px 기준 카드 11자, 단계 13자, 타일 8자 내외/줄).

---

## X. Anti-Pattern Checklist

| ✗ 금지 | 대안 |
| --- | --- |
| 모든 그룹이 움직임 | 주 동작 1 + 보조 1–2, 나머지는 `"none"`(제목·축·맥락·출처) |
| 의미 없는 장식 모션(커브·라인이 그냥 날아다님) | 움직임은 읽는 순서나 초점 이동을 설명할 때만 |
| 홀드 없이 다음 장으로 | 완성 상태 홀드(§VII 표), 녹화용은 `auto_advance` = 합계 + 홀드 |
| 노랑 2곳 이상 / 노란 요소가 정지 장식 | 노랑 = 그 페이지 주 동작의 도착점 하나 |
| 큰 목록을 0.4초 이상씩 기다리게 함 | 행당 0.25–0.35s, 총 1.5–2s |
| 슬롯 그룹에 애니메이션 지정 | 슬롯은 `"none"`, 움직일 내용은 Slide-local 그룹으로 |
| `-a auto`만 주고 사이드카 없이 내보내기(제목까지 움직여 초점이 흩어짐) | §VII 사이드카 사용(슬롯 `"none"` 고정) |
| 스피드 라인을 초점 앞이나 본문 옆에 | 초점 왼쪽 2–3줄, 표지·섹션·KPI만 |
| 노란 띠 위 흰 글자, 띠가 글자를 덮음 | 띠 뒤에 `#0D0F14` 글자, 띠 폭 = 글자 폭 + 48 |
| 다크 위 18px 이상 본문에 `#6B7280` | `#A8AEBD` 이상 밝기 |
| 그라디언트 / 그림자 / 글로우 | 평면 + 가이드 선으로 깊이 |
| 로고 이미지 번들 | `{{BRAND_MARK}}` 텍스트 |
