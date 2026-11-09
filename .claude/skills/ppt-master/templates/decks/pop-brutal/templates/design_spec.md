---
deck_id: pop-brutal
kind: deck
native_structure_mode: structured
summary: 크림 바탕 팝 네오브루탈리즘 덱 — 해커톤 피칭·데모데이, 사내 캠페인·이벤트, 워크숍 오프닝, 공모전 발표 (두꺼운 잉크 외곽선 + 블러 없는 하드 그림자 + 원색 블록 + 스티커·마퀴 띠)
canvas_format: ppt169
canvas_width: 1280
canvas_height: 720
canvas_viewbox: "0 0 1280 720"
source_canvas_width: 1280
source_canvas_height: 720
source_viewbox: "0 0 1280 720"
replication_mode: standard
page_count: 10
primary_color: "#FFD23F"
keywords: [neo-brutalism, pop, hackathon, bold, sticker]
defaults:
  mode: showcase
  visual_style: brutalist
  delivery_purpose: presentation
placeholders:
  01_cover: ["{{TITLE}}", "{{SUBTITLE}}", "{{KICKER}}", "{{PRESENTER}}", "{{DATE}}", "{{BRAND_MARK}}", "{{STICKER}}", "{{MARQUEE}}"]
  02_agenda: ["{{TITLE}}", "{{LEAD}}", "{{STICKER}}", "{{TOC_ITEM_1_TITLE}}", "{{TOC_ITEM_1_DESC}}", "{{TOC_ITEM_2_TITLE}}", "{{TOC_ITEM_2_DESC}}", "{{TOC_ITEM_3_TITLE}}", "{{TOC_ITEM_3_DESC}}", "{{TOC_ITEM_4_TITLE}}", "{{TOC_ITEM_4_DESC}}", "{{TOC_ITEM_5_TITLE}}", "{{TOC_ITEM_5_DESC}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  03_section: ["{{TITLE}}", "{{CHAPTER_DESC}}", "{{STICKER}}", "{{MARQUEE}}"]
  04_problem_solution: ["{{TITLE}}", "{{LEAD}}", "{{STICKER}}", "{{PROBLEM_TAG}}", "{{PROBLEM_TITLE}}", "{{PROBLEM_BODY}}", "{{SOLUTION_TAG}}", "{{SOLUTION_TITLE}}", "{{SOLUTION_BODY}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  05_card_trio: ["{{TITLE}}", "{{LEAD}}", "{{STICKER}}", "{{CARD_1_TITLE}}", "{{CARD_1_BODY}}", "{{CARD_2_TITLE}}", "{{CARD_2_BODY}}", "{{CARD_3_TITLE}}", "{{CARD_3_BODY}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  06_big_number: ["{{TITLE}}", "{{LEAD}}", "{{STICKER}}", "{{BIG_LABEL}}", "{{STAT_1}}", "{{STAT_1_LABEL}}", "{{STAT_2}}", "{{STAT_2_LABEL}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  07_chart: ["{{TITLE}}", "{{LEAD}}", "{{STICKER}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  08_steps: ["{{TITLE}}", "{{LEAD}}", "{{STICKER}}", "{{STEP_1_TITLE}}", "{{STEP_1_BODY}}", "{{STEP_2_TITLE}}", "{{STEP_2_BODY}}", "{{STEP_3_TITLE}}", "{{STEP_3_BODY}}", "{{STEP_4_TITLE}}", "{{STEP_4_BODY}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  09_quote: ["{{QUOTE}}", "{{QUOTE_AUTHOR}}", "{{QUOTE_ROLE}}", "{{STICKER}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  10_closing: ["{{CLOSING_LINE}}", "{{CONTACT_LINE}}", "{{BRAND_MARK}}", "{{STICKER}}", "{{MARQUEE}}"]
---

# Pop Brutal — Design Specification

> 원저작 템플릿. 웹·포스터 디자인에서 널리 쓰이는 **비독점 양식인 네오브루탈리즘** — 브루탈리즘의 날것 구조에 색과 성격을 더한 흐름: 두꺼운 검정 외곽선, 블러 없는 하드 오프셋 그림자, 평면 원색 블록, 거대한 굵은 타이포, 스티커·배지 라벨, 마퀴(티커) 띠 — 를 슬라이드 문법으로 새로 설계했다. 특정 회사의 상표·로고·마스코트·독점 UI를 복제하거나 번들하지 않으며 비트맵 자산이 없다. 브랜드 표기는 `{{BRAND_MARK}}` 텍스트로만 존재한다. 폰트는 install-local Pretendard 락을 따른다.

---

## I. Template Overview

| Property | Description |
| --- | --- |
| **Template Name** | pop-brutal |
| **Display Name** | 팝 브루탈 (Pop Brutal) |
| **Use Cases** | 해커톤 피칭·데모데이, 사내 캠페인·이벤트, 워크숍 오프닝, 공모전 발표 |
| **Design Tone** | 경쾌·대담·직설 — 한 장에 한 메시지를 크게 외친다 |
| **Theme Mode** | **Light** — 크림 `#FFF6E0` 단일 마스터. 다크 페이지 없음 (마퀴 띠만 잉크) |

한눈에 알아보는 표식: **모든 블록이 3px 잉크 외곽선 + 오른쪽 아래 8px 잉크 그림자**를 달고 크림 위에 떠 있고, 페이지마다 **기울어진 스티커 하나**가 블록 모서리에 붙어 있다. 표지·섹션·클로징은 하단 **잉크 마퀴 띠**로 닫힌다.

**Anti-mood**: "유치한 키즈 앱", "그라디언트 SaaS 랜딩", "소프트 섀도 카드", "레인보우 범벅", "손글씨 낙서".

**Litmus test**: 페이지를 흑백으로 인쇄해도 외곽선·하드 그림자·크기 대비만으로 위계가 서면 통과. 색을 다 지웠을 때 형태가 무너지면 색에 기대고 있는 것이다. 두 번째 시험 — 스티커를 하나 더 붙이고 싶어지면 이미 충분하다.

---

## II. Canvas Specification

| Property | Value |
| --- | --- |
| **Format** | Standard 16:9 (`ppt169`) |
| **Dimensions** | 1280 × 720 px |
| **viewBox** | `0 0 1280 720` |
| **Side margins** | 64px — 콘텐츠 폭 1152 (x: 64 → 1216). 블록 그림자(+8)는 여백 쪽으로 넘쳐도 된다 |
| **Content header** | 제목 baseline y=124 (52px), 리드 baseline y=174 (22px), 본문 영역 y≈208 → 600 |
| **Footer chrome** | 좌 `{{BRAND_MARK}}` x=64 / 우 `{{PAGE_LABEL}}` x=1216 anchor end, baseline y=684, 14px |
| **Marquee band** | 표지·섹션·클로징 전용. 잉크 띠 y=632 → 688, 풀블리드. 이 세 페이지는 푸터 대신 띠가 바닥을 닫는다 |

8px 베이스 그리드. 블록 사이 간격은 그림자를 포함해 최소 16px(그림자 8 + 여백 8) — 그림자가 이웃 블록 외곽선에 닿으면 안 된다.

**Master**: `pop-master` / "Pop Brutal" 1개. Master 원자는 크림 배경 `master-bg` 하나뿐이며 모든 페이지에서 동일하다.

---

## III. Color Scheme — LOCKED

이 7개 외의 HEX는 어떤 생성 SVG에도 나타나서는 안 된다. 불투명도로 만든 중간색도 쓰지 않는다.

| Role | HEX | Token | Purpose |
| --- | --- | --- | --- |
| Cream | `#FFF6E0` | `--cream` | 마스터 배경 (전 페이지) |
| Paper | `#FFFFFF` | `--paper` | 중립 블록·칩 채움, 블루 위 텍스트 |
| Ink | `#111111` | `--ink` | 외곽선·하드 그림자·본문 텍스트·마퀴 띠·번호 셀 |
| Yellow | `#FFD23F` | `--yellow` | **프라이머리** — 표지 블록, 지표 블록, 해결 블록, 차트 기본 바, 마퀴 글자 |
| Pink | `#FF5C8A` | `--pink` | 클로징 블록, 화살표, 차트 강조 바, 스티커 |
| Blue | `#3D5AFE` | `--blue` | 말풍선, 섹션 번호 블록, 스티커 |
| Mint | `#2EC4B6` | `--mint` | 칩, 스티커, 로테이션 4번째 |

### 로테이션 규칙

반복 카드·행은 **노랑 → 핑크 → 블루 → 민트** 순서로 고정 순환하고 5번째는 노랑으로 돌아간다 (`02` 아젠다 5행, `05` 카드 3장, `06` 미니 블록은 노랑 다음부터 핑크·블루, `08` 스텝 4장). 섹션 번호 블록은 **챕터 순번**으로 같은 순서를 따른다 (1장 노랑, 2장 핑크, 3장 블루 …) — 프로토타입은 3장=블루를 보여 준다.

### 대비 규칙 (WCAG, 실측)

| 채움 | 잉크 `#111111` | 화이트 `#FFFFFF` | 텍스트 색 |
| --- | --- | --- | --- |
| Cream / Paper | 17.5 / 18.9 | — | 잉크 |
| Yellow | **13.1** | 1.4 ✗ | 잉크 |
| Mint | **8.7** | 2.2 ✗ | 잉크 |
| Pink | **6.4** | 2.9 ✗ | 잉크 |
| Blue | 3.7 ✗ | **5.1** | **화이트** |
| Ink (번호 셀·마퀴·태그) | — | 18.9 | 화이트 또는 노랑(13.1). 번호 셀의 큰 숫자(34px+)만 로테이션 색 허용 (블루 3.7 ≥ 대형 텍스트 3:1) |

- **화이트 텍스트는 블루와 잉크 위에서만.** 핑크·민트·노랑 위 화이트 금지
- **한 페이지 액센트는 3색까지** (로테이션 페이지 `02`·`08`은 예외). 표지 = 노랑·핑크·블루, 클로징 = 핑크·노랑·민트
- **의미 고정색**: 문제=페이퍼, 해결=노랑, 흐름 화살표=핑크(대형)·잉크(소형), 차트 기본=노랑·강조=핑크, 인용=블루
- **Forbidden**: 그라디언트, 블러 그림자·글로우(`filter`), 팔레트 밖 HEX, 반투명 오버레이

---

## IV. Typography System

install-local Pretendard 락. 디스플레이는 별도 패밀리명 `'Pretendard ExtraBold'`(800)를 쓴다. `Pretendard Black`(900)은 이 저장소 번들(`assets/fonts/Pretendard/`)에 없어 이식성이 떨어지므로 쓰지 않는다.

| Weight | `font-family` attribute |
| --- | --- |
| 800 (display) | `'Pretendard ExtraBold', Pretendard, 'Malgun Gothic', sans-serif` |
| 600 (label) | `'Pretendard SemiBold', Pretendard, 'Malgun Gothic', sans-serif` |
| 500 (body) | `'Pretendard Medium', Pretendard, 'Malgun Gothic', sans-serif` |

**헤드라인·번호·스티커·마퀴는 800, 부제·축 라벨은 600, 본문은 500.** 400 이하는 로스터에 없다 — 두꺼운 외곽선 옆에서 얇은 글자는 묻힌다.

| Role | Size | Weight | Letter-spacing | Use |
| --- | --- | --- | --- | --- |
| Giant numeral | 280 / 220 | 800 | -8 / -6 | 섹션 번호 / 대형 지표 |
| Cover title | 112 | 800 | -3 | 표지 헤드라인 (줄간 1.0–1.05) |
| Closing line | 104 | 800 | -3 | 클로징 한 줄 |
| Section title | 88 | 800 | -2.5 | 챕터 제목 (최대 2줄) |
| Agenda title | 72 | 800 | -2 | 아젠다 좌측 제목 |
| Page title / Quote | 52 | 800 | -1 | 콘텐츠 제목, 인용문 (줄간 66) |
| Card numeral / Mini stat | 56 · 48 | 800 | -2 | 카드·스텝 번호, 미니 지표 |
| Block title | 32 · 30 · 26 | 800 | -0.5 · -0.3 | 문제/해결 · 카드 · 아젠다/스텝 제목 |
| Subtitle | 28 | 600 | -0.5 | 표지 부제 |
| Lead / Caption | 22 · 26 | 500 · 600 | 0 · -0.3 | 페이지 리드 · 지표 캡션 |
| Body | 20 | 500 | 0 | 본문 (줄간 30–32) |
| Small | 18 | 500 · 600 | 0 | 아젠다 설명, 인용 직함, 차트 축 라벨 |
| Sticker / Marquee | 18 · 22 | 800 | +0.5 · +1 | 스티커 태그·스타버스트 · 마퀴 토큰 |
| Chrome | 14 | 800 · 600 | +0.5 | 푸터 브랜드 · 페이지 번호 |

본문 최소 18px. 회전은 스티커 라벨에만 — 본문·제목은 절대 기울이지 않는다.

---

## V. Page Roster

| File | Layout key | Picker name | Layout 고정 원자 | Purpose |
| --- | --- | --- | --- | --- |
| `01_cover.svg` | `01_cover` | Cover | 마퀴 띠, 노랑 제목 블록+그림자 | 표지 — 112px 제목 블록, 핑크 스타버스트, 발표자·날짜 칩, 마퀴 |
| `02_agenda.svg` | `02_agenda` | Agenda Stack | — (좌측 제목 슬롯 경계로 구분) | 아젠다 — 좌측 72px 제목 + 우측 5단 바, 지그재그 오프셋 0/24/48/24/0 |
| `03_section.svg` | `03_section` | Section Numeral | 마퀴 띠 | 챕터 전환 — 280px 번호 블록(챕터 색), 88px 제목, 마퀴 |
| `04_problem_solution.svg` | `04_problem_solution` | Problem to Solution | 문제 블록·해결 블록·핑크 화살표 (각 그림자 포함 6개) | 문제 → 해결 대비 |
| `05_card_trio.svg` | `05_card_trio` | Card Trio | — | 3장 카드, 가운데 카드만 40px 내려 엇갈림 |
| `06_big_number.svg` | `06_big_number` | Big Number | 노랑 지표 블록+그림자 | 220px 지표 1개 + 미니 블록 2개 |
| `07_chart.svg` | `07_chart` | Chart (Bars) | 3px 잉크 베이스라인 | 외곽선 막대 차트 (샘플 데이터) |
| `08_steps.svg` | `08_steps` | Steps | 잉크 화살표 3개 | 4단계 — 24px씩 올라가는 계단 블록 |
| `09_quote.svg` | `09_quote` | Quote Bubble | 블루 말풍선+그림자 | 인용 — 꼬리 달린 말풍선, 노랑 따옴표 배지, 아바타 점 |
| `10_closing.svg` | `10_closing` | Closing | 마퀴 띠, 핑크 클로징 블록+그림자 | 클로징 — 104px 한 줄, 노랑 스타버스트, 연락처·브랜드 칩, 마퀴 |

모든 페이지가 `title` 슬롯을 가지며(`01`은 `subtitle` 슬롯 추가), 10개 Layout 키는 고정 원자 또는 슬롯 경계가 서로 달라 중복 Layout으로 컴파일되지 않는다. 색이 페이지마다 바뀌는 블록(섹션 번호 블록, 반복 카드)은 Layout 원자가 아니라 Slide-local 그룹이다.

---

## VI. Signature Design Elements

1. **외곽선 + 하드 그림자 블록** — 모든 블록은 ① 같은 크기의 잉크 사각형을 (+8, +8) 밀어 먼저 깔고 ② 그 위에 채움 + 3px 잉크 외곽선을 얹는다. `filter`를 쓰지 않으므로 PPTX에서 그대로 편집 가능한 도형 2개가 된다. 그림자 방향은 덱 전체에서 오른쪽 아래 하나뿐이다.

   ```xml
   <rect x="72" y="120" width="1000" height="264" fill="#111111"/>
   <rect x="64" y="112" width="1000" height="264" fill="#FFD23F" stroke="#111111" stroke-width="3"/>
   ```

   막대 차트는 그림자를 베이스라인에서 끊는다 (높이 `h − 8`). 말풍선처럼 경로로 된 블록은 같은 `d`에 `transform="translate(8 8)"`를 준 잉크 경로를 아래에 둔다. 원(아바타·따옴표 배지)은 중심을 (+8, +8) 옮긴 잉크 원.

2. **모서리는 0 아니면 16** — 히어로 블록·아젠다 바·섹션 번호 블록·차트 막대·마퀴 띠는 `rx=0`. 카드·스텝·문제/해결 블록·칩·스티커 태그·말풍선은 `rx=16`. 그 사이 값은 없다.

3. **스티커 1장/페이지** — 높이 48 · `rx=16` 태그(18px 800, 중앙 정렬) 또는 18각 스타버스트(외경 96·내경 80, 표지·클로징 전용). 그룹 단위 `rotate(-6…+6, cx, cy)`로만 기울인다. 붙이는 자리: 히어로 블록의 오른쪽 위 모서리에 반쯤 걸치거나(`01`·`04`·`05`·`06`·`09`·`10`), 걸칠 블록이 없으면 헤더 오른쪽(`08`)·제목 위(`02`·`03`)·강조 막대 옆(`07`). 스티커 문구는 2–8자 감탄형("1등 노린다!", "Q&A").

4. **마퀴 띠** — 잉크 풀블리드 띠(높이 56)에 `{{MARQUEE}}` 토큰 4개를 x=160/480/800/1120 중앙 정렬, 사이에 핑크 4각 반짝이 3개. 토큰 1개 폭 예산 ≈ 240px(22px 기준 영문 15자·한글 10자). 띠는 Layout 원자, 토큰·반짝이는 Slide-local 그룹.

5. **청키 화살표** — 7점 폴리곤(몸통 + 머리). 대형(`04`, 폭 136)은 핑크 채움 + 외곽선 + 하드 그림자, 소형(`08`, 폭 32)은 잉크 단색. 흐름을 표시할 때만 쓰고 장식으로 흩뿌리지 않는다.

6. **번호는 크게, 색으로** — 아젠다는 잉크 번호 셀에 로테이션 색 숫자, 카드·스텝은 블록 안 56/48px 숫자, 섹션은 280px 숫자. 번호가 아이콘을 대신한다 — 아이콘 라이브러리를 쓰지 않는다.

---

## VII. Chart Treatment

- 막대: 채움 + 3px 잉크 외곽선 + 하드 그림자, `rx=0`, 폭 120, 슬롯 184. 기본 노랑, **강조 1개만 핑크**
- 베이스라인: 3px 잉크 선 (Layout 원자, x 96 → 1216, y=568). 그리드·y축·플롯 프레임 금지 — 값은 막대 위에 직접 쓴다
- 값 라벨: 24px 800 잉크, 막대 상단 −16. x축 라벨: 18px 600 잉크, baseline y=604
- 스티커는 강조 막대 옆에 붙여 "왜 튀는지"를 한마디로 말한다
- 계열이 2개 이상이면 노랑(기본) + 블루(비교, 화이트 라벨 금지 — 라벨은 막대 밖 잉크). 3계열 이상은 차트를 나눈다
- **Forbidden**: 그라디언트 막대, 3D, 블러 그림자, 파이 차트, 4색 로테이션 막대

| Page | Marker |
| --- | --- |
| `07_chart` | `<!-- chart-plot-area: 112,232,1216,568 -->` |

---

## VIII. Placeholder Vocabulary

| Token | Pages | Content · 수용량 |
| --- | --- | --- |
| `{{TITLE}}` | 01–08 | 페이지 제목. 표지 112px 1줄 ≈ 9자(2줄이면 88px로 낮춤) · 콘텐츠 52px 1줄 ≈ 17자 |
| `{{SUBTITLE}}` | 01 | 표지 부제 1줄 ≈ 34자 |
| `{{KICKER}}` | 01 | 행사명·맥락 1줄 (노랑 블록 안, ■ 표식 뒤) |
| `{{PRESENTER}}` / `{{DATE}}` | 01 | 발표자 칩(≈12자) / 날짜 칩(블루, 화이트 글자) |
| `{{LEAD}}` | 02/04–08 | 리드 1줄 ≈ 50자 (아젠다는 좌측 칼럼 ≈ 19자) |
| `{{TOC_ITEM_n_TITLE}}` / `{{TOC_ITEM_n_DESC}}` | 02 | 아젠다 n=1..5, 제목 ≈ 18자 / 설명 ≈ 30자 |
| `{{CHAPTER_DESC}}` | 03 | 챕터 설명 2줄 × ≈ 27자 |
| `{{PROBLEM_TAG}}` / `{{SOLUTION_TAG}}` | 04 | 잉크 태그 라벨 ≈ 8자 ("지금" / "노트봇 이후") |
| `{{PROBLEM_TITLE}}` · `{{PROBLEM_BODY}}` / `{{SOLUTION_…}}` | 04 | 제목 1줄 ≈ 13자 · 본문 3–4줄 × ≈ 20자 |
| `{{CARD_n_TITLE}}` / `{{CARD_n_BODY}}` | 05 | n=1..3, 제목 ≈ 9자 / 본문 2줄 × ≈ 14자 |
| `{{BIG_LABEL}}` | 06 | 대형 지표 캡션 1–2줄 × ≈ 24자 |
| `{{STAT_n}}` / `{{STAT_n_LABEL}}` | 06 | 미니 지표 n=1..2, 값 ≈ 6자 / 라벨 ≈ 16자 |
| `{{STEP_n_TITLE}}` / `{{STEP_n_BODY}}` | 08 | n=1..4, 제목 ≈ 7자 / 본문 2–3줄 × ≈ 10자 |
| `{{QUOTE}}` | 09 | 인용문 3줄 × ≈ 18자 (52px) |
| `{{QUOTE_AUTHOR}}` / `{{QUOTE_ROLE}}` | 09 | 화자 / 소속·직함 |
| `{{CLOSING_LINE}}` / `{{CONTACT_LINE}}` | 10 | 클로징 한 줄 ≈ 8자 / 연락처 1줄 ≈ 40자 |
| `{{STICKER}}` | 전 페이지 | 스티커 문구 2–8자 |
| `{{MARQUEE}}` | 01/03/10 | 마퀴 토큰 (영문 ≤15자 · 한글 ≤10자), 4회 반복 |
| `{{BRAND_MARK}}` | 01 상단 · 02/04–09 푸터 · 10 칩 | 브랜드명 **텍스트** |
| `{{PAGE_LABEL}}` | 02/04–09 푸터 | 페이지 번호 |

**리터럴 샘플** — 거대 숫자는 토큰 문자열이 캔버스를 넘치므로 짧은 샘플 값으로 둔다: `03` 섹션 번호 "03"(= 챕터 번호), `06` 지표 "87%", `02`/`05`/`08` 순번 "01…", `07` 막대 값·월 라벨. 덱 생성 시 실제 값으로 교체한다.

여러 줄 본문은 하나의 `<text>` 안에서 부모 `x`를 반복하는 `<tspan dy>`로 쌓는다(20px 본문 dy=30–32).

---

## IX. Anti-Pattern Checklist

| ✗ 금지 | 대안 |
| --- | --- |
| 블러 그림자·글로우 (`filter`) | 잉크 사각형 (+8, +8) 하드 그림자 |
| 그림자 방향이 페이지마다 다름 | 오른쪽 아래 한 방향, 오프셋 8 고정 |
| 외곽선 없는 색 블록 | 모든 블록 3px 잉크 외곽선 |
| `rx` 4·8·24 등 중간값 | 0 또는 16 |
| 핑크·민트·노랑 위 화이트 글자 | 잉크 글자 (화이트는 블루·잉크 위만) |
| 한 페이지에 액센트 4색 | 3색까지 (로테이션 페이지 제외) |
| 스티커 2장 이상, ±6° 초과 회전 | 페이지당 1장, −6…+6° |
| 본문·제목 회전 | 회전은 스티커 라벨만 |
| 400 이하 웨이트 | 본문 500, 헤드라인 800 |
| 그라디언트·반투명 오버레이 | 평면 원색 |
| 장식용 도형 흩뿌리기(별·원·지그재그) | 스티커 1장 + 흐름 화살표만 |
| 로고·사진 비트맵 | `{{BRAND_MARK}}` 텍스트, 번호가 아이콘 대신 |
