---
deck_id: scroll-rail
kind: deck
native_structure_mode: structured
summary: 이어지는 서사의 라이트 페이퍼 덱 — 연혁·로드맵, 데이터 스토리, 신제품 공개, 진단 브리핑, 키노트 선언 (하단 진행 레일 + 정지점 한 곳 한 주장 + 앵커 라인 handoff)
canvas_format: ppt169
canvas_width: 1280
canvas_height: 720
canvas_viewbox: "0 0 1280 720"
source_canvas_width: 1280
source_canvas_height: 720
source_viewbox: "0 0 1280 720"
replication_mode: standard
page_count: 10
primary_color: "#FF4F2E"
keywords: [scroll-story, progress-rail, handoff, timeline, narrative]
defaults:
  mode: narrative
  visual_style: editorial
  delivery_purpose: presentation
placeholders:
  01_cover: ["{{TITLE}}", "{{SUBTITLE}}", "{{PRESENTER}}", "{{DATE}}", "{{BRAND_MARK}}", "{{STOP_LABEL}}"]
  02_overview: ["{{TITLE}}", "{{SUPPORT}}", "{{STOP_1_NO}}", "{{STOP_1_TITLE}}", "{{STOP_1_DESC}}", "{{STOP_2_NO}}", "{{STOP_2_TITLE}}", "{{STOP_2_DESC}}", "{{STOP_3_NO}}", "{{STOP_3_TITLE}}", "{{STOP_3_DESC}}", "{{STOP_4_NO}}", "{{STOP_4_TITLE}}", "{{STOP_4_DESC}}", "{{STOP_5_NO}}", "{{STOP_5_TITLE}}", "{{STOP_5_DESC}}", "{{STOP_LABEL}}", "{{BRAND_MARK}}"]
  03_era_shift: ["{{YEAR}}", "{{TITLE}}", "{{SUPPORT}}", "{{SOURCE}}", "{{STOP_LABEL}}", "{{BRAND_MARK}}"]
  04_event: ["{{WHEN}}", "{{TITLE}}", "{{DETAIL_1}}", "{{DETAIL_2}}", "{{PREV_DATE}}", "{{PREV_TITLE}}", "{{NEXT_DATE}}", "{{NEXT_TITLE}}", "{{SOURCE}}", "{{STOP_LABEL}}", "{{BRAND_MARK}}"]
  05_number_slam: ["{{NUMBER}}", "{{TITLE}}", "{{SOURCE}}", "{{STOP_LABEL}}", "{{BRAND_MARK}}"]
  06_data_carry: ["{{TITLE}}", "{{SUPPORT}}", "{{NUMBER}}", "{{CAT_1}}", "{{CAT_2}}", "{{CAT_3}}", "{{CAT_4}}", "{{CAT_5}}", "{{SOURCE}}", "{{STOP_LABEL}}", "{{BRAND_MARK}}"]
  07_annotation_pin: ["{{TITLE}}", "{{SUPPORT}}", "{{LEGEND_A}}", "{{LEGEND_B}}", "{{PIN_TITLE}}", "{{PIN_NOTE}}", "{{SOURCE}}", "{{STOP_LABEL}}", "{{BRAND_MARK}}"]
  08_zoom_dive: ["{{TITLE}}", "{{SUPPORT}}", "{{PART_NAME}}", "{{PART_VALUE}}", "{{MID_NAME}}", "{{MID_VALUE}}", "{{WHOLE_NAME}}", "{{WHOLE_VALUE}}", "{{SOURCE}}", "{{STOP_LABEL}}", "{{BRAND_MARK}}"]
  09_kinetic_line: ["{{LINE_LEAD}}", "{{WORD}}", "{{LINE_TAIL}}", "{{SUPPORT}}", "{{SOURCE}}", "{{STOP_LABEL}}", "{{BRAND_MARK}}"]
  10_closing: ["{{CLOSING_LINE}}", "{{CONTACT_LINE}}", "{{BRAND_MARK}}", "{{STOP_LABEL}}"]
---

# Scroll Rail — Design Specification

> 원저작 템플릿. 스크롤 덱 원칙(정지점·handoff·컨셉 문법)은 gongnyang/awesome-html-scrolline-deck(MIT)을 참고했으며 코드는 포함하지 않는다. 원작의 "무대 1개·연속 타임라인·컷 대신 handoff"를 정적 PPTX 문법으로 옮겼다 — 모든 페이지가 같은 하단 레일 위에 서고, 이어지는 두 페이지가 같은 대상을 다루면 그 대상은 **같은 좌표**에 놓인다. 어떤 회사의 상표·로고·독점 UI도 복제하거나 번들하지 않으며, 브랜드는 `{{BRAND_MARK}}` 텍스트로만 존재한다. 글꼴은 install-local Pretendard 락을 따른다.

---

## I. Template Overview

| Property | Description |
| --- | --- |
| **Template Name** | scroll-rail |
| **Display Name** | 스크롤 레일 |
| **Use Cases** | 연혁·로드맵 발표, 데이터 스토리, 신제품 공개, 진단(전체→원인) 브리핑, 키노트 선언 |
| **Design Tone** | 이어지는 서사 — 한 정지점에 한 주장. 넘기는 것이 아니라 레일을 따라 걷는다 |
| **Theme Mode** | Light paper (`#FAFAF7`) 단일 극성 + 먹 + 주홍 한 점 |

한눈에 알아보는 표식: **하단 진행 레일**(모든 페이지 y=628)과 그 위의 **주홍 정지 마커**, 그리고 페이지마다 바뀌어도 늘 같은 높이에 있는 **앵커 라인 A**(baseline y=352).

**Anti-mood**: "카드 그리드 대시보드", "다크 키노트 무대", "다색 카테고리 팔레트", "3D·그림자로 깊이를 연출한 슬라이드", "메타 캡션이 붙은 데모 화면".

**Litmus test**: 페이지에서 결론 한 줄만 남기고 나머지를 가렸을 때 이야기가 이어지면 통과. 그리고 앞뒤 페이지를 겹쳐 봤을 때 공유 대상(연도·숫자·프레임)이 한 자리에 포개지지 않으면 실패 — 그건 handoff가 아니라 컷이다.

---

## II. Canvas & Rail Geometry

| Property | Value |
| --- | --- |
| **Format** | Standard 16:9 (`ppt169`), 1280 × 720, viewBox `0 0 1280 720` |
| **Side margins** | 80px — 콘텐츠 폭 1120 (x: 80 → 1200) |
| **Content zone** | y 96 → 600 (레일 위) |
| **Progress rail** | Master 원자: 선 (80,628)→(1200,628) `#D5D8DE` 2px + 시작·끝 틱 (x=80 / x=1200, y 621→635) `#8A8F98` 2px |
| **Stop marker** | Slide-local `rail-marker` 그룹: 진행선 (80,628)→(xᵢ,628) `#14161A` 2px(1쪽 생략) + 헤일로 r12 주홍 16% + 점 r6 주홍 + `{{STOP_LABEL}}` (xᵢ, 658) 13px |
| **Marker x formula** | `xᵢ = 80 + 1120 × (i − 1) / (N − 1)` — i = 페이지 번호, N = 덱 총 페이지. 라벨 anchor는 첫 페이지 start, 마지막 end, 나머지 middle |
| **Footer row** | y=690 — 좌 `{{BRAND_MARK}}` 13px, 우 `{{SOURCE}}` 14px anchor end (01/10은 브랜드를 좌상단 (80,104)로 올린다) |
| **Anchor line A** | **x=80, baseline y=352** — handoff 대상이 앉는 정지선 (§VII) |
| **Title zone** | 헤드라인형 페이지(02/06/07/08) 제목 baseline 144, 보충 baseline 192 |

10쪽 기준 마커 x: 80 · 204 · 329 · 453 · 578 · 702 · 827 · 951 · 1076 · 1200. 페이지 수가 바뀌면 공식으로 다시 계산한다 — 마커를 균등 위치에 "대충" 두지 않는다. 1쪽(표지)은 레일 시작점, 마지막 쪽(클로징)은 레일 끝점에 마커가 놓이고 진행선이 레일 전체를 채운다.

---

## III. Color Scheme — LOCKED

이 8개 외의 HEX는 어떤 생성 SVG에도 나타나서는 안 된다.

| Role | HEX | Token | Purpose |
| --- | --- | --- | --- |
| Paper | `#FAFAF7` | `--paper` | 전 페이지 배경 (Master `p:bg`), 빈 정지점 원의 속 |
| Ink | `#14161A` | `--ink` | 결론 텍스트, 진행선, 여정 레일, 주 계열 라인 |
| Body | `#3C4048` | `--body` | 보충 텍스트, 상세, 맥락 값 라벨 |
| Muted | `#8A8F98` | `--muted` | 출처·축·레전드 보조, 레일 끝 틱, 중간 프레임, 지나간/다음 사건(trail) |
| Rail | `#D5D8DE` | `--rail` | 진행 레일, 표지·클로징 눈금, 맥락 막대, 사건 행 규칙선, 전체 프레임 |
| Hairline | `#E6E8EC` | `--hairline` | 차트 그리드 전용 |
| Vermilion | `#FF4F2E` | `--vermilion` | **주색** — 정지 마커 + 그 페이지의 handoff 대상 한 개 |
| Teal | `#0F9D8A` | `--teal` | 데이터 보조 계열 (07 계열 B) — 글자에는 쓰지 않는다 |

### Color Rules

- **주홍 예산 = 2 객체.** 정지 마커 1 + 그 페이지가 다음/이전 페이지와 주고받는 대상 1 (03 연도, 04 날짜, 05 숫자, 06 첫 막대, 07 핀, 08 부분 프레임, 09 단어 문). 01·02·10은 마커만
- **handoff 대상은 색을 유지한다** — 03 연도와 04 날짜가 둘 다 주홍이어야 같은 대상으로 읽힌다
- **회색은 맥락, 주홍은 지금 볼 것.** 비교 막대·이웃 사건은 `#D5D8DE` / `#8A8F98`로 물러난다
- **틸은 계열 색**이다. 두 번째 데이터 계열에만 쓰고, 강조·텍스트·장식에는 쓰지 않는다
- 반투명은 두 곳뿐: 마커·핀 헤일로(주홍 `fill-opacity 0.16`), 부분 프레임·단어 문 속(주홍 `fill-opacity 0.08`)
- **Forbidden**: 그라디언트, 그림자, 글로우, 3D, 다크 배경, 위 8색 외 유채색

---

## IV. Typography — 3단 위계

install-local Pretendard 락. 굵기는 패밀리 이름으로 고른다.

| Weight | `font-family` attribute |
| --- | --- |
| 400 | `Pretendard, 'Malgun Gothic', sans-serif` |
| 500 | `'Pretendard Medium', Pretendard, 'Malgun Gothic', sans-serif` |
| 600 | `'Pretendard SemiBold', Pretendard, 'Malgun Gothic', sans-serif` |
| 800 | `'Pretendard ExtraBold', Pretendard, 'Malgun Gothic', sans-serif` |

**글자 위계는 3단을 넘지 않는다 — 결론 · 보충 · 출처.** 거대한 연도·숫자·단어는 위계 단이 아니라 *대상*(handoff 오브젝트)이다. 다이어그램 라벨(정지점 번호, 축, 레벨 이름)은 데이터 표기로 보고 위계에 세지 않는다.

| Level | Role | Size | Weight | Color | Pages |
| --- | --- | --- | --- | --- | --- |
| 대상 | Era year | 220 | 800, ls −6 | vermilion | 03 |
| 대상 | Big number | 200 | 800, ls −6 | vermilion | 05 |
| 대상 | Kinetic word | 88 | 800 | vermilion | 09 |
| 대상 | Event date / carried number / part value | 56 / 48 / 44 | 800 | vermilion | 04 / 06 / 08 |
| 1 결론 | Cover title / closing line | 72 / 64 | 800 | ink | 01 / 10 |
| 1 결론 | Kinetic lead · tail | 64 | 600, ls −1.2 | ink | 09 |
| 1 결론 | Page headline / event title | 40 | 600, ls −0.8 | ink | 02 04 06 07 08 |
| 1 결론 | Claim under object | 36 | 600, ls −0.6 | ink | 03 05 |
| 2 보충 | Support · detail · subtitle · contact | 22–24 | 400 | body | all |
| 2 보충 | Stop title · pin title · level value | 20–30 | 600 | ink | 02 07 08 |
| 3 출처 | Source · trail · axis · names | 14–18 | 400–500 | muted | all |
| chrome | Stop label / footer brand | 13 | 600 / 500 | ink / muted | all |

본문 최소 18px(차트 축·레전드·레벨 이름 16px은 주석 단). 크롬은 13–14px. 한글 런의 음수 자간은 위 값 이하로 유지한다.

---

## V. Page Roster

Master: `scroll-rail-master` / picker "Scroll Rail" — 원자 4개(`master-bg`, `master-rail`, `master-rail-start`, `master-rail-end`)가 전 페이지 동일.

| File | Layout key / picker | Scrolline 개념·move | Purpose & slots |
| --- | --- | --- | --- |
| `01_cover.svg` | `01_cover` / Cover · Rail Start | rail — 레일의 시작 | 72px 제목이 앵커 라인 A에 앉고, 레일 눈금(layout 원자) 위 마커가 x=80. title + subtitle 슬롯, 좌상단 브랜드, 발표자·날짜 행 |
| `02_overview.svg` | `02_overview` / Overview · Journey Rail | rail — 전체 여정 | 앵커 라인 A에 여정 레일(layout 원자, 먹 2px + 끝 틱)과 정지점 5개(번호·제목·한 줄 설명). 첫 정지점만 채운 원. title + body 슬롯 |
| `03_era_shift.svg` | `03_era_shift` / Era Shift | rail: era-shift | 220px 주홍 연도 + 결론 한 줄(36) + 보충. title + body 슬롯 |
| `04_event.svg` | `04_event` / Event Entry | rail: rail-advance | 연감 행: 규칙선 두 줄(layout 원자) 사이에 날짜(좌, 앵커 A) + 제목·2줄 상세(우, x=440). 위·아래에 지나간/다음 사건이 muted로 흐른다. title + body(상세) 슬롯 |
| `05_number_slam.svg` | `05_number_slam` / Number Slam | launch: number-slam | 200px 주홍 숫자 하나 + 의미 한 줄 + 출처. title 슬롯만 |
| `06_data_carry.svg` | `chart_stage` / Chart Stage | data: mark-morph · counter-handoff | 05의 숫자가 첫 막대(최댓값, 주홍)의 라벨이 되어 같은 좌표에 남는다. 나머지 4개는 회색 맥락. title + body 슬롯, plot 기준선(layout 원자) |
| `07_annotation_pin.svg` | `chart_stage` / Chart Stage | data: annotation-pin | 06과 같은 차트 무대에서 막대→선. 주 계열 먹, 보조 계열 틸, 핀 하나(주홍 점 + 리더 + 2줄 콜아웃) |
| `08_zoom_dive.svg` | `08_zoom_dive` / Zoom Dive | zoom: zoom-dive · depth-ladder | (80,256) 꼭짓점을 공유하는 3중 프레임(전체 rail → 중간 muted → 부분 주홍, layout 원자). 라벨이 왼쪽 위→아래로 부분→전체 사다리 |
| `09_kinetic_line.svg` | `09_kinetic_line` / Kinetic Line | kinetic: word-door · phrase-fold | 문장 하나가 무대. 앞 구(64) / 단어 문 안의 단어(88, 주홍) + 뒤 구(64) / 보충. 단어 문 프레임은 layout 원자 |
| `10_closing.svg` | `10_closing` / Closing · Rail End | rail — 도착 | 64px 클로징 라인(앵커 A) + 연락처, 레일 눈금, 진행선 100%·마커 x=1200 |

`06`/`07`은 고정 Layout 원자(plot 기준선)와 슬롯 계약(title 80 96 1120 64 · body 80 164 1120 44)이 동일하므로 `chart_stage` 키를 공유한다 — 차트 무대가 페이지를 넘어 그대로 남는 것 자체가 handoff다. 나머지 키는 원자 또는 슬롯 경계가 서로 다르다. 보충·상세·연락처는 `body` 슬롯(idx 1), 커버 부제는 `subtitle` 슬롯(idx 1).

---

## VI. Signature Design Elements

1. **하단 진행 레일** — Master에 고정된 2px 레일. 페이지는 넘어가도 레일은 그대로이고, 마커만 공식대로 전진한다. 지나온 구간은 먹색 진행선으로 칠한다
2. **정지 마커** — 주홍 점 + 16% 헤일로 + `03 / 10` 라벨. 07의 데이터 핀도 같은 모양이다: "정지점"은 덱 전체에서 한 가지 기호다
3. **앵커 라인 A (80, 352)** — 표지 제목, 여정 레일, 연도, 날짜, 숫자, 첫 막대 라벨, 부분 값, 단어, 클로징 라인이 모두 이 baseline에 앉는다. 시선이 한 높이에 머물고 내용만 바뀐다 — 원작의 "무대 1개"
4. **한 정지점 한 주장** — 거대한 대상 하나 + 결론 한 줄 + 보충 + 출처. 그 이상은 다음 정지점으로 넘긴다
5. **흐르는 이웃** — 04의 지나간/다음 사건, 02의 빈 정지점처럼 맥락은 muted로 남겨 타임라인이 화면 밖으로 이어짐을 보인다
6. **표지·클로징 눈금** — 28px 간격 눈금(5칸마다 긴 눈금)이 레일을 자(ruler)로 만든다. 출발과 도착 페이지에만 있다

---

## VII. Handoff Anchors & Export

이어지는 두 페이지가 같은 대상을 다루면 **같은 좌표**에 둔다. 생성 시 아래 좌표를 바꾸지 않는다(내용이 길면 대상 크기가 아니라 결론 문장을 줄인다).

| Page pair | Shared object | Anchor (SVG px) |
| --- | --- | --- |
| 전 페이지 | 진행 레일 · 정지 마커 | 레일 y=628, x 80→1200; 마커 xᵢ 공식 (§II) |
| 01 → 02 | 레일 시작 → 여정 레일 | 01 제목 baseline (80,352) = 02 여정 레일 y=352; 01 마커 (80,628) = 02 진행선 시작 |
| 03 → 04 | 연도 → 사건 날짜 | `{{YEAR}}` 220px / `{{WHEN}}` 56px 모두 start-anchor (80, 352), 주홍 |
| 05 → 06 | 숫자 → 첫 막대 라벨 | `{{NUMBER}}` 200px / 48px 모두 (80, 352) — 같은 토큰. 06 첫 막대 rect (80, 368, 128, 200) |
| 06 → 07 | 차트 무대 | plot area 80,368 → 1200,568, 기준선 y=568 (layout 원자), title/body 슬롯 동일 |
| 08 → 09 | 부분 프레임 → 단어 문 | rect (80, 256, 400, 128) 주홍 2px + 8% — 08 `layout-frame-part` = 09 `layout-word-door`. 08 부분 값과 09 단어 baseline 모두 y=352 |
| 09 → 10 | 결론 문장 → 클로징 문장 | 09 단어·뒤 구 baseline y=352 = 10 클로징 라인 (80,352) |

**Export recommendation** — 원작의 연속 스크롤에 가장 가까운 네이티브 전환은 가로 `push`다(이 파이프라인에 morph는 없다). 같은 좌표의 대상이 밀려 들어오며 레일이 끊기지 않는다.

```bash
python3 .claude/skills/ppt-master/scripts/svg_to_pptx.py <project> -t push --transition-duration 0.6
```

요소 애니메이션은 기본(off)을 유지한다. 원작의 "한 정지점에 단계 진입"이 필요할 때만 `-a auto --animation-trigger on-click`; `rail-marker`·`page-foot`·`claim-source`는 정적으로 두도록 `animations.json`에서 `effect: none`을 준다.

---

## VIII. Chart Treatment

- **무대 공유**: 06·07은 plot area `80,368 → 1200,568`과 먹 1px 기준선을 공유한다
- **06 막대**: 폭 128, 간격 120, 5개(x 80/328/576/824/1072). 첫 막대 = 넘겨받은 숫자(최댓값, plot 상단까지, 주홍) + 48px 라벨. 나머지 `#D5D8DE`, 값 22px SemiBold body, 범주 18px (첫 범주만 SemiBold ink). 그리드 없음, 모서리 0
- **07 라인**: 6점 x = 140 + 204k. 그리드 4줄 `#E6E8EC` 1px, y 라벨 16px muted를 그리드 위 왼쪽(x=80)에. 주 계열 먹 2.5px, 보조 계열 틸 2.5px, 둘 다 점 없음. 핀은 한 개 — 주홍 점 r6 + 헤일로, 리더 1.5px가 y=276까지, 콜아웃 20px SemiBold + 18px body (x = 핀 + 16)
- **레전드**: 07만, (80,244)·(320,244) 24px 선 스와치 + 16px 라벨
- **Forbidden**: 그림자, 3D, 그라디언트, 파이, 이중 축, 핀 2개 이상, 계열 3개 이상(나누어 다음 정지점으로)

| Page | Marker |
| --- | --- |
| `06_data_carry` | `<!-- chart-plot-area: 80,368,1200,568 -->` |
| `07_annotation_pin` | `<!-- chart-plot-area: 80,368,1200,568 -->` |

---

## IX. Placeholder Vocabulary

| Token | Pages | Content |
| --- | --- | --- |
| `{{TITLE}}` | 01–08 | 결론 한 줄 — 01 표지 72px ≤ 15자 · 40px 헤드라인 ≤ 26자 · 03/05 36px ≤ 28자 · 04 사건 제목 ≤ 18자 |
| `{{SUPPORT}}` | 02 03 06 07 08 09 | 보충 한 줄 (≤ 1100px, 약 45자) |
| `{{SOURCE}}` | 03–09 | 출처 한 줄 — 실데이터면 필수 ("출처: 기관, 연도") |
| `{{STOP_LABEL}}` | 전 페이지 | 정지 마커 라벨 (`03 / 10`) |
| `{{BRAND_MARK}}` | 전 페이지 | 브랜드명 **텍스트** (01/10 좌상단, 나머지 푸터) |
| `{{SUBTITLE}}` / `{{PRESENTER}}` / `{{DATE}}` | 01 | 부제 / 발표자 / 날짜 |
| `{{STOP_n_NO}}` / `{{STOP_n_TITLE}}` / `{{STOP_n_DESC}}` | 02 | 정지점 n=1..5 (제목 ≤ 9자, 설명 ≤ 11자) |
| `{{YEAR}}` | 03 | 시대 연도 (4–5자) |
| `{{WHEN}}` / `{{DETAIL_1}}` / `{{DETAIL_2}}` | 04 | 사건 날짜 (≤ 9자) / 상세 2줄 (각 ≤ 30자) |
| `{{PREV_DATE}}` `{{PREV_TITLE}}` / `{{NEXT_DATE}}` `{{NEXT_TITLE}}` | 04 | 지나간 / 다음 사건 (muted, 제목 ≤ 34자) |
| `{{NUMBER}}` | 05, 06 | 넘겨주는 숫자 — **두 페이지에 같은 값** (≤ 5자, 단위 포함) |
| `{{CAT_1}}`…`{{CAT_5}}` | 06 | 막대 범주 (≤ 7자) |
| `{{LEGEND_A}}` / `{{LEGEND_B}}` | 07 | 계열 이름 |
| `{{PIN_TITLE}}` / `{{PIN_NOTE}}` | 07 | 핀 콜아웃 2줄 (각 ≤ 18자) |
| `{{PART_*}}` / `{{MID_*}}` / `{{WHOLE_*}}` (`NAME`, `VALUE`) | 08 | 부분(SOM) / 중간(SAM) / 전체(TAM) — 이름 ≤ 20자, PART 값 ≤ 8자(부분 프레임 안), MID·WHOLE 값 ≤ 20자 |
| `{{LINE_LEAD}}` / `{{WORD}}` / `{{LINE_TAIL}}` | 09 | 앞 구 ≤ 16자 / 단어 문 안 단어 2–4자 / 뒤 구 ≤ 10자 |
| `{{CLOSING_LINE}}` / `{{CONTACT_LINE}}` | 10 | 클로징 문장 ≤ 17자 / 연락처 |

`{{KEY_MESSAGE}}` 대신 `{{TITLE}}`, `{{LEAD}}` 대신 `{{SUPPORT}}`를 쓰는 이유: 이 덱의 텍스트 위계는 결론(`TITLE`)·보충(`SUPPORT`)·출처(`SOURCE`) 세 단이고, 토큰 이름이 그 규칙을 그대로 드러낸다. 차트 막대 값·축 숫자는 표본 데이터이며 덱 생성 시 실데이터로 다시 그린다.

---

## X. Anti-Pattern Checklist

| ✗ 금지 | 대안 |
| --- | --- |
| 메타 캡션 ("25초 데모", "녹화 화면", "스크롤하세요") | 내용만 쓴다. 진행은 레일이 말한다 |
| 글자 위계 4단 이상 (키커 + 제목 + 리드 + 본문 + 각주) | 결론 · 보충 · 출처 3단 |
| 한 정지점에 주장 두 개 | 두 번째 주장은 다음 페이지로 — 페이지를 늘리는 것이 handoff다 |
| 같은 대상을 다루는 이웃 페이지에서 좌표가 바뀜 (컷) | §VII 앵커 좌표 유지, 대상 색도 유지 |
| 마커를 공식이 아닌 임의 위치에 | `xᵢ = 80 + 1120 × (i−1)/(N−1)` |
| 주홍 3곳 이상 / 주홍 본문 | 마커 + 대상 1개. 본문은 ink/body |
| 틸로 강조·텍스트 | 틸은 보조 데이터 계열 전용 |
| 장식용 3D·그림자·그라디언트 | 평면. 깊이는 08 프레임 중첩과 회색 단계로만 |
| 카드 그리드로 여러 사실을 한 화면에 | 한 정지점씩 나눠 레일 위에 세운다 |
| 레일·마커 제거 또는 위치 이동 | 레일은 Master — 모든 페이지 y=628 |
| 로고 이미지 번들 | `{{BRAND_MARK}}` 텍스트 |
| 출처 없는 실수치 | `{{SOURCE}}` 필수, 가상 데이터면 "표본"을 출처 칸에 명시 |
