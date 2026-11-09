---
deck_id: bento-aurora
kind: deck
native_structure_mode: structured
summary: 벤토 그리드 + 오로라 글로우 다크 키노트 덱 — 제품·서비스 런칭, 해커톤 데모데이, 연간 성과 하이라이트, 비전 키노트 (2026 벤토 UI·초대형 타이포·다크 글로우 트렌드에서 착안)
canvas_format: ppt169
canvas_width: 1280
canvas_height: 720
canvas_viewbox: "0 0 1280 720"
source_canvas_width: 1280
source_canvas_height: 720
source_viewbox: "0 0 1280 720"
replication_mode: standard
page_count: 10
primary_color: "#7C5CFF"
keywords: [bento, aurora, dark, keynote, launch]
defaults:
  mode: showcase
  visual_style: glassmorphism
  delivery_purpose: presentation
placeholders:
  01_cover: ["{{KICKER}}", "{{TITLE}}", "{{SUBTITLE}}", "{{DATE}}", "{{PRESENTER}}", "{{BRAND_MARK}}"]
  02_agenda: ["{{KICKER}}", "{{TITLE}}", "{{LEAD}}", "{{TOC_ITEM_1_TITLE}}", "{{TOC_ITEM_1_DESC}}", "{{TOC_ITEM_2_TITLE}}", "{{TOC_ITEM_2_DESC}}", "{{TOC_ITEM_3_TITLE}}", "{{TOC_ITEM_3_DESC}}", "{{TOC_ITEM_4_TITLE}}", "{{TOC_ITEM_4_DESC}}", "{{TOC_ITEM_5_TITLE}}", "{{TOC_ITEM_5_DESC}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  03_section: ["{{CHAPTER_NUM}}", "{{KICKER}}", "{{CHAPTER_TITLE}}", "{{CHAPTER_DESC}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  04_bento_overview: ["{{KICKER}}", "{{TITLE}}", "{{HERO_TAG}}", "{{HERO_TITLE}}", "{{HERO_BODY}}", "{{METRIC_LABEL}}", "{{METRIC_VALUE}}", "{{FEATURE_TITLE}}", "{{FEATURE_BODY}}", "{{QUOTE}}", "{{QUOTE_AUTHOR}}", "{{LIST_TITLE}}", "{{LIST_ITEM_1}}", "{{LIST_ITEM_2}}", "{{LIST_ITEM_3}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  05_hero_metric: ["{{KICKER}}", "{{TITLE}}", "{{METRIC_LABEL}}", "{{METRIC_VALUE}}", "{{METRIC_DELTA}}", "{{METRIC_NOTE}}", "{{STAT_1_VALUE}}", "{{STAT_1_LABEL}}", "{{STAT_2_VALUE}}", "{{STAT_2_LABEL}}", "{{STAT_3_VALUE}}", "{{STAT_3_LABEL}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  06_feature_grid: ["{{KICKER}}", "{{TITLE}}", "{{FEATURE_1_TITLE}}", "{{FEATURE_1_BODY}}", "{{FEATURE_2_TITLE}}", "{{FEATURE_2_BODY}}", "{{FEATURE_3_TITLE}}", "{{FEATURE_3_BODY}}", "{{FEATURE_4_TITLE}}", "{{FEATURE_4_BODY}}", "{{FEATURE_5_TITLE}}", "{{FEATURE_5_BODY}}", "{{FEATURE_6_TITLE}}", "{{FEATURE_6_BODY}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  07_chart: ["{{KICKER}}", "{{TITLE}}", "{{CHART_TITLE}}", "{{LEGEND_SERIES_A}}", "{{LEGEND_SERIES_B}}", "{{INSIGHT_TITLE}}", "{{INSIGHT_BODY}}", "{{STAT_1_VALUE}}", "{{STAT_1_LABEL}}", "{{STAT_2_VALUE}}", "{{STAT_2_LABEL}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  08_roadmap: ["{{KICKER}}", "{{TITLE}}", "{{PHASE_1_TIME}}", "{{PHASE_1_TITLE}}", "{{PHASE_1_ITEM_1}}", "{{PHASE_1_ITEM_2}}", "{{PHASE_1_ITEM_3}}", "{{PHASE_1_GOAL}}", "{{PHASE_2_TIME}}", "{{PHASE_2_TITLE}}", "{{PHASE_2_ITEM_1}}", "{{PHASE_2_ITEM_2}}", "{{PHASE_2_ITEM_3}}", "{{PHASE_2_GOAL}}", "{{PHASE_3_TIME}}", "{{PHASE_3_TITLE}}", "{{PHASE_3_ITEM_1}}", "{{PHASE_3_ITEM_2}}", "{{PHASE_3_ITEM_3}}", "{{PHASE_3_GOAL}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  09_statement: ["{{KICKER}}", "{{STATEMENT}}", "{{STATEMENT_EMPHASIS}}", "{{STATEMENT_NOTE}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  10_closing: ["{{KICKER}}", "{{CLOSING_LINE}}", "{{CONTACT_LINE}}", "{{BRAND_MARK}}"]
---

# Bento Aurora — Design Specification

> 원저작 템플릿. 2026년 프레젠테이션·UI 트렌드에서 널리 통용되는 **비독점 디자인 원칙** — 모듈형 벤토 그리드(크고 밝은 타일 하나가 우선순위를 말한다), 소프트 코너 타일, 초대형 타이포, 다크 모드, 글로우 깊이 — 를 슬라이드 문법으로 새로 설계했다. 특정 제품의 UI·상표·로고·워드마크를 복제하거나 번들하지 않는다. 비트맵·사진·아이콘 라이브러리 없이 기본 도형과 그라디언트만으로 작도했다. 브랜드 표기는 `{{BRAND_MARK}}` 텍스트로만 존재한다. 서체는 install-local Pretendard 락을 따른다.

---

## I. Template Overview

| Property | Description |
| --- | --- |
| **Template Name** | bento-aurora |
| **Display Name** | 벤토 오로라 (Bento Aurora) |
| **Use Cases** | 제품·서비스 런칭, 해커톤 데모데이, 연간 성과 하이라이트, 비전 키노트 |
| **Design Tone** | 몰입·프리미엄·에너지 — 어두운 무대 위에서 한 칸만 빛난다 |
| **Theme Mode** | Dark only — `#07080F` 캔버스 고정 |

한눈에 알아보는 표식: 니어블랙 캔버스 위 12열 벤토 타일(rx 24), 그중 **딱 한 칸**이 보라·시안·핑크 오로라 리본과 그라디언트 테두리로 빛난다. 나머지 타일은 무채색이고, 숫자는 120–180px ExtraBold로 크게 선다.

**Anti-mood**: "라이트 글래스 메시", "니어블랙 절제형 리니어 UI(오로라 없음)", "네온 사이버펑크 그리드", "무지개 카드 그리드", "스톡 사진 히어로".

**Litmus test**: 히어로 타일 하나만 남기고 나머지 타일의 오로라 흔적(작은 점·글리프)을 지웠을 때 페이지의 우선순위가 그대로 읽히면 통과. 오로라는 **우선순위 신호**다 — 두 칸이 동시에 빛나면 신호가 사라진다.

**자매 템플릿과의 구분**: `gradient-mesh`는 라이트 캔버스 상단의 메시 분위기, `midnight-panel`은 글로우·그라디언트를 금지한 절제형 다크 패널이다. 이 템플릿은 **벤토 타일 위계 + 히어로 한 칸의 오로라**가 정체성이다.

---

## II. Canvas Specification

| Property | Value |
| --- | --- |
| **Format** | Standard 16:9 (`ppt169`) |
| **Dimensions** | 1280 × 720 px |
| **viewBox** | `0 0 1280 720` |
| **Margin** | 48px — 콘텐츠 폭 1184 (x: 48 → 1232) |
| **Grid** | **12열**, 열 폭 84 / 간격 16. 열 *i*(0–11)의 시작 x = `48 + 100i`, n열 스팬 폭 = `100n − 16` (2열 184 · 3열 284 · 4열 384 · 5열 484 · 6열 584 · 8열 784 · 12열 1184) |
| **Header (콘텐츠 페이지)** | 키커 칩 y 40–68, 페이지 제목 베이스라인 y=120 |
| **Tile zone** | 헤더 페이지 y 144 → 656 (높이 512: 2행 248 / 3행 160 / 4행 116, 간격 16). 헤더 없는 페이지(02·03)는 y 48 → 656 |
| **Footer chrome** | 좌 `{{BRAND_MARK}}` x=48 / 우 `{{PAGE_LABEL}}` x=1232 anchor end, 베이스라인 y=692 (표지·클로징은 생략) |

타일 내부 패딩 32px(짧은 타일 28px). 타일 간격은 항상 16px — 간격이 벤토의 리듬이다.

---

## III. Color Scheme — LOCKED

이 10개 외의 HEX는 어떤 생성 SVG에도 나타나서는 안 된다. 투명도는 `stop-opacity`·`fill-opacity`로만 만든다(별도 HEX를 만들지 않는다).

| Role | HEX | Token | Purpose |
| --- | --- | --- | --- |
| Background | `#07080F` | `--bg` | 전 페이지 캔버스 (Master 배경) |
| Tile | `#10121C` | `--tile` | 일반 타일 서피스 |
| Tile raised | `#161A29` | `--tile-raised` | 히어로 타일 바탕, 칩 바탕 |
| Hairline | `#262B40` | `--hairline` | 1px 타일 경계, 차트 그리드, 비활성 진행 바 |
| Text | `#F4F6FF` | `--text` | 헤드라인, 숫자, 히어로 타일 위 모든 텍스트 |
| Body | `#B3B8D4` | `--body` | 본문·리드·설명 (다크 배경 본문의 **하한 밝기**) |
| Muted | `#7A80A3` | `--muted` | 인덱스 번호, 라벨, 축, 푸터 — 본문에 쓰지 않는다 |
| Aurora violet | `#7C5CFF` | `--violet` | **주색** — 오로라 중심, 차트 주 계열, 키커 점 |
| Aurora cyan | `#22D3EE` | `--cyan` | 오로라 2색, 차트 피크·라인 끝 |
| Aurora pink | `#F472B6` | `--pink` | 오로라 3색, 인용 글리프 |

### Color Rules

- **오로라 필드는 페이지당 1곳.** 히어로 타일 하나(01·02·04–08) 또는 풀블리드 배경 필드(03·09·10의 배경 블롭)에만 보라·시안·핑크 블롭이 겹친다. 01은 배경 필드 + 메타 히어로 타일, 03은 배경 필드 + 숫자 히어로 타일 — 표지·챕터만 두 겹을 허용한다. 10의 브랜드 타일은 오로라 테두리만 두르고 내부 블롭은 두지 않는다
- **일반 타일은 무채색.** `#10121C` + `#262B40` 헤어라인. 오로라 색은 타일당 **10px 이하 점 1개 또는 56px 글리프 1개**로만 들어간다
- **히어로 타일 위 텍스트는 전부 `#F4F6FF`.** 오로라 위에 `#B3B8D4`를 두지 않는다(대비 붕괴). 오로라가 닿지 않는 히어로 하단에서만 리드에 `#B3B8D4` 허용
- **본문 하한은 `#B3B8D4`.** `#7A80A3`은 12–16px 크롬(라벨·축·푸터·인덱스 숫자) 전용
- **그라디언트 텍스트는 강조 구절 하나.** `09`의 `{{STATEMENT_EMPHASIS}}`만 시안→보라→핑크 그라디언트 필. 본문·제목에 그라디언트 금지
- **글로우 필터는 페이지당 최대 1개, 짧은 디스플레이 요소에만** — `03` 챕터 숫자, `05` 거대 지표, `07` 차트 피크 점. 본문·타일·그룹에 필터 금지

---

## IV. Typography System

install-local Pretendard 락. **ExtraBold 디스플레이 + Regular 본문**의 극단 대비가 성격이다.

| Weight | `font-family` attribute |
| --- | --- |
| 400 | `Pretendard, 'Malgun Gothic', sans-serif` |
| 500 | `'Pretendard Medium', Pretendard, 'Malgun Gothic', sans-serif` |
| 600 | `'Pretendard SemiBold', Pretendard, 'Malgun Gothic', sans-serif` |
| 700 | `Pretendard, 'Malgun Gothic', sans-serif` + `font-weight="700"` (페이지 제목 전용) |
| 800 | `'Pretendard ExtraBold', Pretendard, 'Malgun Gothic', sans-serif` (디스플레이·숫자) |

### 🔒 본문 baseline 락 — `delivery_purpose` 기본값보다 우선

**본문 baseline은 `20`, 타일 안 본문 하한은 `18`이다.** 기본값이 `presentation`이지만 그 목적의 일반 본문값 32를 적용하지 않는다. 근거: 벤토는 284–384px 폭 타일 안에서 문장을 다루므로 32px 본문은 타일당 8–11자에서 끊겨 그리드가 무너진다. 원거리 가독성은 88px 표지 제목과 176–180px 거대 숫자가 맡는다. 본문을 키워야 하면 최대 22까지, 대신 타일 수를 줄인다(6칸 → 4칸).

| Role | Size | Weight | Letter-spacing | Use |
| --- | --- | --- | --- | --- |
| Giant numeral | 176–180 | 800 | -6 | `03` 챕터 숫자, `05` 거대 지표 |
| Cover title | 88 | 800 | -1.8 | 표지 헤드라인 (한글 13자 이내) |
| Closing line | 76 | 800 | -1.6 | 클로징 카피 (가운데 정렬) |
| Tile metric | 72 | 800 | -2 | `04` 지표 타일 |
| Statement | 66 | 800 | -1.4 | `09` 진술문 2행 |
| Section title | 54 | 800 | -1.2 | 챕터 제목 |
| Hero heading | 48 / 36 / 30 / 28 | 800 | -1 → -0.5 | 히어로·단계·인사이트 타일 제목 |
| Stat value | 48 / 40 | 800 | -1.2 / -1 | 보조 지표 타일 |
| Page title | 40 | 700 | -0.8 | 콘텐츠 페이지 제목 |
| Index number | 56 / 44 | 800 | -1.2 / -1 | 아젠다 인덱스 (`#7A80A3`) |
| Subtitle | 26 | 400 | -0.3 | 표지 서브카피 |
| Tile title | 24–26 | 600 | -0.3 | 카드·아젠다 항목 제목 |
| Lead | 22 | 400 | -0.2 | 진술 보조, 연락처 |
| Body | 18–20 | 400 | -0.1 | 타일 본문·리스트 |
| Axis / caption | 14 | 400–500 | 0 | 차트 축·레전드, 인용 출처, 단계 기간 |
| Kicker chip | 13 | 600 | +1.2 | 필 칩 키커 |
| Label | 12 | 600 | +1.6 | `DATE` `GOAL` `KEY INSIGHT` `NOW/NEXT/LATER` 대문자 라벨 |
| Footer | 13 | 500 / 400 | 0 | 브랜드·페이지 번호 |

**자간 규칙**: 표의 음수 자간은 한글 비중 런 기준 값이다(라틴 전용 런은 ×1.5까지 죄어도 된다). 양수 자간(칩·라벨)은 언어 무관하게 유지한다.

**카피 예산**: 표지 제목 88px 한글 13자 · 챕터 제목 54px 11자 · 진술문 66px 1행 16자 · 384px 타일 본문 18px 17자 · 284px 타일 본문 12자. 넘치면 줄이지 말고 페이지를 바꾼다.

---

## V. Page Roster

모든 페이지는 Master `bento-aurora-master` ("Bento Aurora", `#07080F` 배경 rect 1개)를 공유하고, 타일·오로라 블롭·레일은 Layout 원자로, 텍스트와 페이지별 글리프는 슬롯·Slide-local 그룹으로 둔다. 10개 Layout 키는 타일 토폴로지가 모두 달라 서로 공유하지 않는다.

| File | Layout key | Layout name | Purpose |
| --- | --- | --- | --- |
| `01_cover.svg` | `01_cover` | Cover (Aurora Field) | 표지 — 우상단 오로라 필드 + 88px 제목 + 하단 3칸 메타 벤토(날짜·발표자·브랜드 히어로) |
| `02_agenda.svg` | `02_agenda` | Agenda (Bento) | 목차 — 좌측 세로 히어로(제목) + 크기가 다른 5개 항목 타일(01–05) |
| `03_section.svg` | `03_section` | Section (Aurora Numeral) | 챕터 — 배경 필드 + 히어로 타일 속 180px 글로우 숫자 + 우측 제목 타일과 진행 바 |
| `04_bento_overview.svg` | `04_bento_overview` | Bento Overview | **시그니처** — 세로 히어로 + 지표·글리프·인용·리스트 4칸 핀휠 |
| `05_hero_metric.svg` | `05_hero_metric` | Hero Metric | 8열 히어로 속 176px 거대 지표 + 델타 칩 + 우측 3단 보조 지표 |
| `06_feature_grid.svg` | `06_feature_grid` | Feature Grid (3x2) | 3×2 기능 타일, 첫 칸이 히어로. 기본 도형 글리프 + 제목 + 1행 설명 |
| `07_chart.svg` | `07_chart` | Chart + Insight | 8열 영역형 라인 차트 타일 + 인사이트 히어로 + 보조 지표 2칸 |
| `08_roadmap.svg` | `08_roadmap` | Roadmap (Now Next Later) | 오로라 레일 + 마일스톤 점 + 폭이 줄어드는 NOW(5열)·NEXT(4열)·LATER(3열) 타일 |
| `09_statement.svg` | `09_statement` | Statement (Aurora) | 풀블리드 오로라 필드 + 전폭 헤어라인 프레임 + 2행 진술문(2행째 그라디언트 강조) |
| `10_closing.svg` | `10_closing` | Closing (Aurora Horizon) | 하단에서 떠오르는 오로라 수평선 + 가운데 클로징 카피 + 브랜드 히어로 타일 |

---

## VI. Signature Design Elements

1. **히어로 타일 1칸** — `#161A29` 바탕 → 보라 워시(대각선 linear, 0.3 → 0) → 회전된 보라·핑크·시안 radial 타원 3개(중심 0.66–0.8 → 45% 0.34–0.46 → 0) → 보라→시안→핑크 그라디언트 테두리 1.5px. 타원은 타일 경계 안에 들어가도록 배치하고(클립 없음), 같은 각도(-12° ~ -30°)로 기울여 리본처럼 겹친다. **크고 밝은 칸 = 이 페이지에서 가장 중요한 말**
2. **12열 벤토 리듬** — 스팬이 서로 다른 타일(3·4·5·8열 / 116·160·248·512 높이)을 16px 간격으로 맞물린다. 같은 크기 타일만 반복하지 않는다(06의 3×2만 예외, 대신 히어로 1칸으로 깬다)
3. **스퀴클 코너 rx 24** — 모든 타일은 24, 칩은 h/2(28→14, 32→16), 진행 바·스와치는 높이/2
4. **초대형 숫자** — 176–180px ExtraBold, 자간 -6, 히어로 위 `#F4F6FF` + 보라 글로우(stdDeviation 8, 0.5)
5. **필 칩 키커** — `#161A29` 필 + 헤어라인 + 보라 4px 점 + 13px SemiBold. 히어로 위 칩은 흰색 0.1 필 + 0.3 테두리
6. **배경 오로라 필드** — 01·03·09·10만. 화면 가장자리에서 번지는 대형 radial 타원(중심 0.4–0.75 → 0), 그 위 타일은 `fill-opacity 0.78`로 살짝 비친다(유리 질감, 블러 없음)
7. **오로라 레일** — `08`의 4px 그라디언트 코어 + 16px 0.2 헤일로(필터 없이 겹친 rect). 미래로 갈수록 투명해진다

---

## VII. Chart Treatment

- 차트는 **일반 타일 안**에 그린다. 히어로 오로라는 옆의 인사이트 타일이 맡는다
- 그리드: 가로 헤어라인 5개 `#262B40` 1px. 세로 그리드·플롯 프레임 금지
- 축 라벨: 14px `#7A80A3`. y축 anchor end, x축 anchor middle
- 주 계열: 3px 라인, 보라→시안 linear 스트로크, 아래 영역은 보라 0.5 → 0 수직 그라디언트 필(영역 먼저, 라인 위)
- 비교 계열: 2px `#7A80A3` 점선 `6 6`
- 피크/최신 점: r7 `#F4F6FF` + 시안 3px 테두리 + 시안 글로우 — 페이지 유일한 필터
- 값 라벨: 피크만 16px SemiBold `#F4F6FF`
- 레전드: 차트 제목 아래 좌측, 24×4 바 스와치 / 24px 점선
- 막대형으로 바꿀 때: rx = 막대폭/2 상한 8, 피크 막대만 보라→시안 그라디언트, 나머지 `#262B40`
- **Forbidden**: 3D, 파이, 다색 카테고리 팔레트, 그림자, 계열 3개 이상(나눠서 그린다)

| Page | Marker |
| --- | --- |
| `07_chart` | `<!-- chart-plot-area: 128,264,792,576 -->` |

---

## VIII. Placeholder Vocabulary

| Token | Pages | Content |
| --- | --- | --- |
| `{{KICKER}}` | 01–10 (칩) | 키커 — 영문 대문자 또는 짧은 한글, 칩 폭 176 안 |
| `{{TITLE}}` | 01/02/04–08 | 표지·목차·콘텐츠 페이지 제목 (title 슬롯) |
| `{{SUBTITLE}}` | 01 | 표지 서브카피 (subtitle 슬롯) |
| `{{DATE}}` / `{{PRESENTER}}` | 01 | 메타 타일 |
| `{{LEAD}}` | 02 | 목차 히어로 리드 1행 |
| `{{TOC_ITEM_n_TITLE}}` / `{{TOC_ITEM_n_DESC}}` | 02 | 아젠다 (n=1..5, 번호 01–05는 고정 텍스트) |
| `{{CHAPTER_NUM}}` / `{{CHAPTER_TITLE}}` / `{{CHAPTER_DESC}}` | 03 | 챕터 숫자 / 제목(title 슬롯) / 설명 |
| `{{HERO_TAG}}` / `{{HERO_TITLE}}` / `{{HERO_BODY}}` | 04 | 히어로 타일 |
| `{{METRIC_LABEL}}` / `{{METRIC_VALUE}}` | 04/05 | 지표 라벨 / 값 |
| `{{METRIC_DELTA}}` / `{{METRIC_NOTE}}` | 05 | 델타 칩 / 기준 주석 |
| `{{FEATURE_TITLE}}` / `{{FEATURE_BODY}}` | 04 | 글리프 타일 |
| `{{QUOTE}}` / `{{QUOTE_AUTHOR}}` | 04 | 인용 1행(14자) / 출처 |
| `{{LIST_TITLE}}` / `{{LIST_ITEM_n}}` | 04 | 리스트 타일 (n=1..3) |
| `{{STAT_n_VALUE}}` / `{{STAT_n_LABEL}}` | 05 (n=1..3) / 07 (n=1..2) | 보조 지표 |
| `{{FEATURE_n_TITLE}}` / `{{FEATURE_n_BODY}}` | 06 | 기능 타일 (n=1..6) |
| `{{CHART_TITLE}}` / `{{LEGEND_SERIES_A}}` / `{{LEGEND_SERIES_B}}` | 07 | 차트 제목 / 레전드 |
| `{{INSIGHT_TITLE}}` / `{{INSIGHT_BODY}}` | 07 | 인사이트 히어로 |
| `{{PHASE_n_TIME}}` / `{{PHASE_n_TITLE}}` / `{{PHASE_n_ITEM_m}}` / `{{PHASE_n_GOAL}}` | 08 | 단계 (n=1..3 → NOW/NEXT/LATER, m=1..3) |
| `{{STATEMENT}}` / `{{STATEMENT_EMPHASIS}}` / `{{STATEMENT_NOTE}}` | 09 | 진술문(title 슬롯) / 그라디언트 강조 구절 / 보조 |
| `{{CLOSING_LINE}}` / `{{CONTACT_LINE}}` | 10 | 클로징 카피(title 슬롯) / 연락처 |
| `{{BRAND_MARK}}` | 02–09 푸터, 01·10 히어로 타일 | 브랜드명 **텍스트** — 로고 이미지가 아니다 |
| `{{PAGE_LABEL}}` | 02–09 푸터 | 페이지 번호 |

`{{TITLE}}` 대신 03은 `{{CHAPTER_TITLE}}`, 09는 `{{STATEMENT}}`, 10은 `{{CLOSING_LINE}}`이 title 슬롯을 맡는다. 키노트 성격상 진술·클로징 카피가 페이지 제목이기 때문이다.

---

## IX. Anti-Pattern Checklist

| ✗ 금지 | 대안 |
| --- | --- |
| 오로라 히어로 2칸 이상 | 페이지당 1칸 — 나머지는 무채색 타일 |
| 오로라 위 `#B3B8D4`·`#7A80A3` 텍스트 | 히어로 위 텍스트는 `#F4F6FF` |
| 본문 `#7A80A3` 또는 18px 미만 | 본문 `#B3B8D4` 18px 이상, `#7A80A3`은 크롬 전용 |
| 타일 rx 8·12 혼용, 직각 타일 | 타일 24, 칩 h/2 |
| 간격 16 이외의 타일 간격, 그리드 밖 폭 | `100n − 16` 스팬, 간격 16 |
| 같은 크기 타일만 반복 | 스팬·높이를 섞은 벤토, 히어로 1칸으로 위계 |
| 그룹·타일·본문에 글로우 필터 | 짧은 디스플레이 요소 1개(숫자·피크 점)에만 |
| `<image>`·사진·로고·아이콘 라이브러리 | 원·사각형·다각형 기본 도형 글리프 |
| 블러·마스크·블렌드 모드로 오로라 표현 | radial `stop-opacity` 페이드 타원 + linear 워시 |
| 타원이 타일 밖으로 삐져나옴 | 회전 후 외접 박스가 타일 안(여백 4px)에 들어오게 배치 |
| 로고 이미지 번들 | `{{BRAND_MARK}}` 텍스트 |
| `presentation` 목적이라고 본문 32 | §IV 락 — 본문 20, 타일 본문 18 |
