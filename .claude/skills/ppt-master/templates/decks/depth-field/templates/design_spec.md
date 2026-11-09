---
deck_id: depth-field
kind: deck
native_structure_mode: structured
summary: three.js로 직접 렌더한 3D 장면을 배경에 까는 다크 테크 키노트 덱 — 기술 비전·아키텍처 발표, AI·데이터 플랫폼 소개, 해커톤 데모, 미래 전략 키노트 (reveal.js-threejs 계열의 3D 배경 슬라이드에서 착안)
canvas_format: ppt169
canvas_width: 1280
canvas_height: 720
canvas_viewbox: "0 0 1280 720"
source_canvas_width: 1280
source_canvas_height: 720
source_viewbox: "0 0 1280 720"
replication_mode: standard
page_count: 10
primary_color: "#5CE1E6"
keywords: [three-js, 3d-render, depth, perspective-grid, tech-keynote]
defaults:
  mode: showcase
  visual_style: dark-tech
  delivery_purpose: presentation
placeholders:
  01_cover: ["{{TITLE}}", "{{SUBTITLE}}", "{{KICKER}}", "{{PRESENTER}}", "{{DATE}}", "{{BRAND_MARK}}"]
  02_agenda: ["{{TITLE}}", "{{DEPTH_TAG}}", "{{KICKER}}", "{{ITEM_1_NO}}", "{{ITEM_1_TITLE}}", "{{ITEM_1_DESC}}", "{{ITEM_1_TAG}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  03_section: ["{{CHAPTER_NUM}}", "{{CHAPTER_TITLE}}", "{{CHAPTER_DESC}}", "{{DEPTH_TAG}}", "{{KICKER}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  04_hero_visual: ["{{TITLE}}", "{{BODY}}", "{{DEPTH_TAG}}", "{{KICKER}}", "{{STAT_1_VALUE}}", "{{STAT_1_LABEL}}", "{{STAT_2_VALUE}}", "{{STAT_2_LABEL}}", "{{CAPTION}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  05_depth_layers: ["{{TITLE}}", "{{DEPTH_TAG}}", "{{KICKER}}", "{{LEAD}}", "{{LAYER_1_TITLE}}", "{{LAYER_1_BODY}}", "{{LAYER_2_TITLE}}", "{{LAYER_2_BODY}}", "{{LAYER_3_TITLE}}", "{{LAYER_3_BODY}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  06_metrics: ["{{TITLE}}", "{{DEPTH_TAG}}", "{{KICKER}}", "{{LEAD}}", "{{METRIC_1_VALUE}}", "{{METRIC_1_LABEL}}", "{{METRIC_1_DELTA}}", "{{METRIC_4_VALUE}}", "{{SOURCE}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  07_chart: ["{{TITLE}}", "{{DEPTH_TAG}}", "{{KICKER}}", "{{LEGEND_SERIES_A}}", "{{LEGEND_SERIES_B}}", "{{CALLOUT}}", "{{SOURCE}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  08_perspective_arch: ["{{TITLE}}", "{{DEPTH_TAG}}", "{{KICKER}}", "{{LEAD}}", "{{NODE_1_TITLE}}", "{{NODE_1_DESC}}", "{{NODE_5_TITLE}}", "{{NODE_5_DESC}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  09_quote: ["{{QUOTE}}", "{{QUOTE_AUTHOR}}", "{{QUOTE_ROLE}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
  10_closing: ["{{CLOSING_MESSAGE}}", "{{ENDING_SUBTITLE}}", "{{DEPTH_TAG}}", "{{KICKER}}", "{{PRESENTER}}", "{{CONTACT_INFO}}", "{{BRAND_MARK}}", "{{PAGE_LABEL}}"]
---

# Depth Field — Design Specification

> 원저작 템플릿. 3D 장면은 three.js(MIT, CDN 고정 버전)로 직접 작성·렌더했으며, 슬라이드 뒤에 3D 장면을 까는 방식은 reveal.js-threejs 계열 덱에서 착안했다. 코드는 포함하지 않는다. PPTX는 WebGL을 실행할 수 없으므로 장면은 **비트맵으로 구워** 배경·히어로에만 쓰고, 모든 텍스트는 편집 가능한 SVG→PPTX 텍스트로 남긴다. 사진·로고·상표를 번들하지 않으며 비트맵은 이 템플릿이 직접 렌더한 4장뿐이다. 브랜드 표기는 `{{BRAND_MARK}}` 텍스트로만 존재한다. 글꼴은 install-local Pretendard 락을 따른다.

---

## I. Template Overview

| Property | Description |
| --- | --- |
| **Template Name** | depth-field |
| **Display Name** | Depth Field (뎁스 필드) |
| **Use Cases** | 기술 비전·아키텍처 발표, AI·데이터 플랫폼 소개, 해커톤 데모, 미래 전략 키노트 |
| **Design Tone** | 깊이감·미래지향·정돈 — 화면 안쪽으로 공간이 열린다 |
| **Theme Mode** | **Dark** — 전 페이지 `#060B1A` 딥 네이비 |

한눈에 보이는 정체성: **렌더된 3D 지평선·오브젝트가 화면 뒤에 깔리고, 콘텐츠 페이지에는 소실점으로 모이는 원근 바닥 그리드와 `Z-01` 깊이 라벨이 남는다.** 표지·섹션·히어로·클로징은 렌더 비트맵, 나머지는 평면 패널 + 얇은 선이다.

**Anti-mood**: "신스웨이브 석양(마젠타·주황)", "네온 과포화", "글래스모피즘 카드 더미", "무지개 데이터 팔레트", "렌더를 모든 페이지에 도배".

**Litmus test**: 렌더 이미지를 지워도 텍스트·위계가 그대로 읽히면 통과. 깊이는 **배경과 원근선**이 만들고, 텍스트는 평면에 선다. 한 페이지에 빛나는 것이 두 개면 하나를 끈다.

---

## II. Canvas Specification

| Property | Value |
| --- | --- |
| **Format** | Standard 16:9 (`ppt169`) |
| **Dimensions** | 1280 × 720 px |
| **viewBox** | `0 0 1280 720` |
| **Side margins** | 80px — 콘텐츠 폭 1120 (x: 80 → 1200) |
| **Header** | 키커 baseline y=96 (`{{DEPTH_TAG}} · {{KICKER}}`), 제목 baseline y=152, 리드 baseline y=196 |
| **Footer chrome** | 좌 `{{BRAND_MARK}}` x=80 / 우 `{{PAGE_LABEL}}` x=1200 anchor end, baseline y=676 |

8px 베이스 스페이싱(4/8/16/24/32/48). 패널 간격 24px.

---

## III. Color Scheme — LOCKED

이 8개 외의 HEX는 어떤 생성 SVG에도 나타나서는 안 된다(렌더 비트맵 안의 색은 이 8색의 혼합·발광으로만 만든다).

| Role | HEX | Token | Purpose |
| --- | --- | --- | --- |
| Deep navy | `#060B1A` | `--bg` | 전 페이지 배경, 스크림·페이드 색 |
| Panel | `#0E1630` | `--panel` | 패널·카드·슬랩 면 |
| Panel line | `#1E2A4A` | `--line` | 1px 경계선, 원근 그리드, 차트 그리드 |
| Text | `#EAF0FF` | `--text` | 제목·강조 텍스트 |
| Body | `#AEB9D6` | `--body` | 본문·부제·리드 |
| Muted | `#6F7BA0` | `--muted` | 키커·캡션·축 라벨·푸터 |
| Cyan | `#5CE1E6` | `--cyan` | **주색** — 깊이 라벨, 주 계열, 한 점의 글로우 |
| Violet | `#8B7CFF` | `--violet` | **보조색** — 비교 계열, 두 번째 층, 림 라이트 |

### Color Rules

- **글로우는 페이지당 최대 1개.** 필터 글로우(`feGaussianBlur` + cyan flood) 또는 radial 헤일로 중 하나만. 본문 텍스트에는 절대 글로우를 걸지 않는다
- **cyan = 가까움·주체, violet = 한 단계 뒤.** 층·계열·노드의 깊이 순서를 색으로 일관되게 유지한다 (Z-01 cyan → Z-02 violet → Z-03 muted)
- **렌더 위 텍스트는 반드시 스크림 위에.** `#060B1A` 그라디언트(stop-opacity 0.8→0)를 이미지와 텍스트 사이에 둔다
- **다크 위 본문은 `#AEB9D6` 이상 밝기.** `#6F7BA0`은 14px 이하 크롬 전용
- **Forbidden**: 흰 배경 페이지, 마젠타·주황·그린, 그림자(다크 위에서는 무의미), 다색 카테고리 팔레트

---

## IV. Typography System

install-local Pretendard 락. 디스플레이는 ExtraBold, 페이지 제목은 700, 본문은 400.

| Weight | `font-family` attribute |
| --- | --- |
| 400 | `Pretendard, 'Malgun Gothic', sans-serif` |
| 500 | `'Pretendard Medium', Pretendard, 'Malgun Gothic', sans-serif` |
| 600 | `'Pretendard SemiBold', Pretendard, 'Malgun Gothic', sans-serif` |
| 700 | `Pretendard, 'Malgun Gothic', sans-serif` + `font-weight="700"` |
| 800 | `'Pretendard ExtraBold', Pretendard, 'Malgun Gothic', sans-serif` |

| Role | Size | Weight | Letter-spacing | Use |
| --- | --- | --- | --- | --- |
| Section number | 112 | 800 | -2 | 챕터 번호 (cyan + 글로우) |
| Cover title | 64 | 800 | -1.2 | 표지 헤드라인 |
| Closing title | 56 | 800 | -1 | 클로징 문장 |
| KPI number | 52 | 700 | -1 | 지표 숫자 |
| Chapter title | 48 | 800 | -0.8 | 섹션 제목 |
| Hero headline | 44 | 700 | -0.7 | 히어로 좌측 헤드라인 (2행) |
| Page title | 40 | 700 | -0.6 | 표준 페이지 제목 |
| Quote | 36 | 600 | -0.5 | 인용문 (중앙 정렬) |
| Subtitle | 22–24 | 400 | -0.3 | 표지·클로징 부제 |
| Subheading | 24 | 600 | -0.3 | 목차 항목·층 제목 |
| Lead / Body | 18–20 | 400 | 0 | 리드·본문·노드 설명 |
| Kicker / depth label | 14 | 600 | +1.5 | `Z-01`, 키커 |
| Axis / caption | 14 | 400 | 0 | 차트 축·캡션 |
| Footer | 13 | 400–500 | 0 | 브랜드·페이지 번호 |

**본문 하한 18px**, 크롬(키커·축·푸터)만 13–14px. 한글 비중이 높은 런은 음수 자간을 표의 값보다 키우지 않는다.

---

## V. Page Roster

| File | Layout key | Surface | Purpose |
| --- | --- | --- | --- |
| `01_cover.svg` | `01_cover` | **render** `df_cover.jpg` | 표지 — 와이어프레임 지형 지평선 + 좌·하단 스크림, 하늘 영역에 제목·부제, 좌하단 발표자/날짜, 좌상단 브랜드, 우하단 `Z-00` |
| `02_agenda.svg` | `02_agenda` | flat + 원근 바닥 | 목차 — 깊이 인덱스 5행, 하단에 희미한 원근 그리드 |
| `03_section.svg` | `03_section` | **render** `df_section.jpg` | 섹션 — 토러스 매듭 + 이코사헤드론 렌더 우측, 좌측 cyan 글로우 챕터 번호 + 제목 + 설명 |
| `04_hero_visual.svg` | `04_hero_visual` | **render** `df_hero.jpg` (우 60%) | 히어로 — 우측 768×720 레이어 스택 렌더(좌측 페이드), 좌측 헤드라인·본문·미니 지표 2개 |
| `05_depth_layers.svg` | `05_depth_layers` | flat | 3층 아이소메트릭 슬랩(경험·서비스·데이터) + 깊이 레일 라벨 |
| `06_metrics.svg` | `06_metrics` | flat 패널 4 | 지표 4-up — 선두 지표만 글로우, 깊이 바가 오른쪽으로 갈수록 짧아짐 |
| `07_chart.svg` | `07_chart` | flat 패널 1 | 영역 차트 — cyan 주 계열(영역+선) + violet 점선 비교 계열 |
| `08_perspective_arch.svg` | `08_perspective_arch` | 원근 바닥 | 아키텍처 — 원근 바닥 위 5노드(코어 1·중간 2·전면 2), 바닥 위 연결선 |
| `09_quote.svg` | `09_quote` | 원근 바닥 + 지평선 글로우 | 인용 — 중앙 정렬 진술문, 낮은 지평선 헤일로 1개 |
| `10_closing.svg` | `10_closing` | **render** `df_closing.jpg` | 클로징 — 파티클 지구 + 궤도 렌더 우측, 좌측 클로징 문장·부제·연락처 |

모든 페이지는 Master `depth-master`(`Depth Field`) 하나를 공유한다. Master 원자는 배경 `#060B1A` rect 하나뿐이다. Layout 키는 10개 모두 서로 다르다 — 렌더 페이지는 이미지·스크림 원자, 콘텐츠 페이지는 원근 바닥·패널·레일 원자로 구분된다. PowerPoint picker 이름: Cover (Render) / Agenda (Depth Grid) / Section (Render) / Hero Visual (Render Right) / Depth Layers (Isometric) / Metrics (4-up) / Chart (Area Panel) / Architecture (Perspective Floor) / Quote (Horizon Glow) / Closing (Render).

---

## VI. Signature Design Elements

1. **렌더 배경 = 3D 공간** — `01`/`03`/`10`은 풀블리드, `04`는 우측 60% 렌더. 렌더는 Layout 원자(`<image>`)이며 그 위에 `#060B1A` 스크림 원자가 있어 텍스트 대비를 보장한다
2. **원근 바닥 그리드** — 소실점(x=640)으로 모이는 선 + 원근 간격 가로선. `stroke` 세로 그라디언트로 지평선 쪽이 사라진다. `02`/`08`/`09`의 Layout 원자이며 표지 폴백에도 쓰인다
3. **깊이 라벨 `Z-NN`** — 14px SemiBold +1.5 자간. 페이지 키커(`{{DEPTH_TAG}}`), 목차 인덱스, 층·지표 번호. 표지는 `Z-00` 고정
4. **깊이 = 색 순서** — Z-01 cyan → Z-02 violet → Z-03 muted. 슬랩 테두리, 지표 바, 노드 링, 차트 계열이 같은 순서를 따른다
5. **평면 패널 + 1px 선** — 콘텐츠 페이지는 `#0E1630` 면과 `#1E2A4A` 선만. 반경 6, 그림자 없음
6. **아이소메트릭 슬랩(`05`)** — SVG 원시 도형(path/polygon)으로 그린 마름모 윗면 + 두께 10px 측면 2개. `skew` 변환을 쓰지 않는다

### 렌더 폴백 계약

카드 미리보기 등에서 `../images/` 상대 경로가 풀리지 않을 수 있다. 렌더 페이지는 이미지 **아래**에 SVG 폴백 원자를 둔다 — `01`은 세로 그라디언트 + 원근 그리드 + cyan 지평선, `03`/`10`은 radial 헤일로, `04`는 `#0E1630` 면. 이미지가 없어도 표지가 성립한다.

### Assets

| File | Size | Page | Scene id | Content |
| --- | --- | --- | --- | --- |
| `images/df_cover.jpg` | 1600×900, 130 KB | `01_cover` | `cover` | 와이어프레임 지형(은선 제거), cyan 능선, violet 지평선 헤이즈, 별·파티클 |
| `images/df_section.jpg` | 1600×900, 82 KB | `03_section` | `section` | 프레넬 림 토러스 매듭 + 이코사헤드론 와이어 케이지 + 궤도 링 (우측 배치) |
| `images/df_hero.jpg` | 1152×1080, 119 KB | `04_hero_visual` | `hero` | 반투명 UI 레이어 4장 스택 + 수직 점선 커넥터 + 원근 바닥 (768×720 프레임 1.5배) |
| `images/df_closing.jpg` | 1600×900, 71 KB | `10_closing` | `closing` | 피보나치 파티클 지구(대륙 노이즈) + 네트워크 호 + 적도 궤도·위성 (우측 배치) |

JPEG quality 82, 합계 약 402 KB. 렌더 위 텍스트 영역(좌측)은 장면 구도에서 비워 두었다.

### three.js 장면 소스와 재렌더

- 소스: `templates/three/scene.html` — 장면 4개를 `?scene=cover|section|hero|closing&w=&h=`로 선택. 시드 고정 난수(mulberry32), 고정 카메라, 한 프레임 렌더, `preserveDrawingBuffer: true`, UnrealBloom 후처리. 끝나면 `window.__done = true`
- three.js는 import map으로 `https://cdn.jsdelivr.net/npm/three@0.160.0/`에 고정해 불러온다(MIT). 벤더링하지 않는다
- 팔레트는 파일 상단 `PAL` 객체 한 곳에서 바뀐다. 재렌더 절차는 `templates/three/README.md`

---

## VII. Chart Treatment

- 패널: `#0E1630` 면 + `#1E2A4A` 1px, 반경 6 (Layout 원자)
- 그리드: 가로선 5개 `#1E2A4A` 1px. 세로 그리드·축선 없음
- 축 라벨: 14px `#6F7BA0`. y축 anchor end, x축 anchor middle
- 주 계열: cyan 실선 2.5px + 영역(cyan stop-opacity 0.32→0) + 속이 빈 점(r4). **마지막 점만** 채운 cyan + 글로우(페이지의 유일한 글로우) + 수직 점선 가이드
- 비교 계열: violet 점선 2px (`6 5`), 영역·점 없음
- 레전드: 헤더 우측, 24px 선 스와치 + 14px `#AEB9D6`
- 콜아웃: 마지막 점 위 18px SemiBold `#EAF0FF` (`{{CALLOUT}}`)
- **Forbidden**: 3D 차트, 파이, 세 번째 유채색 계열(필요하면 차트를 나눈다), 계열마다 글로우

| Page | Marker |
| --- | --- |
| `07_chart` | `<!-- chart-plot-area: 170,268,1160,548 -->` |

---

## VIII. Placeholder Vocabulary

| Token | Pages | Content |
| --- | --- | --- |
| `{{TITLE}}` | 01/02/04–08 | 페이지 헤드라인 (`04`는 2행 허용) |
| `{{SUBTITLE}}` | 01 | 표지 부제 |
| `{{KICKER}}` | 01–08/10 | 키커 (영문 대문자 또는 짧은 한글) |
| `{{DEPTH_TAG}}` | 02–08/10 | 페이지 깊이 라벨 `Z-NN` |
| `{{PRESENTER}}` / `{{DATE}}` | 01, 10 / 01 | 발표자·소속 / 날짜 |
| `{{ITEM_n_NO}}` / `{{ITEM_n_TITLE}}` / `{{ITEM_n_DESC}}` / `{{ITEM_n_TAG}}` | 02 | 목차 (n=1..5, NO는 `Z-0n`, TAG는 시간·쪽수) |
| `{{CHAPTER_NUM}}` / `{{CHAPTER_TITLE}}` / `{{CHAPTER_DESC}}` | 03 | 챕터 번호 / 제목 / 설명 |
| `{{BODY}}` / `{{CAPTION}}` | 04 | 히어로 본문 / 렌더 캡션 |
| `{{STAT_n_VALUE}}` / `{{STAT_n_LABEL}}` | 04 | 미니 지표 (n=1..2) |
| `{{LEAD}}` | 05/06/08 | 페이지 리드 1행 |
| `{{LAYER_n_TITLE}}` / `{{LAYER_n_BODY}}` | 05 | 층 (n=1..3, 1=가장 위/가까움) |
| `{{METRIC_n_VALUE}}` / `{{METRIC_n_LABEL}}` / `{{METRIC_n_DELTA}}` | 06 | 지표 (n=1..4, 1=선두·글로우) |
| `{{LEGEND_SERIES_A}}` / `{{LEGEND_SERIES_B}}` / `{{CALLOUT}}` | 07 | 레전드 / 마지막 점 콜아웃 |
| `{{SOURCE}}` | 06/07 | 출처·단위 |
| `{{NODE_n_TITLE}}` / `{{NODE_n_DESC}}` | 08 | 노드 (n=1 코어, 2–3 중간, 4–5 전면) |
| `{{QUOTE}}` / `{{QUOTE_AUTHOR}}` / `{{QUOTE_ROLE}}` | 09 | 인용문 / 화자 / 직함 |
| `{{CLOSING_MESSAGE}}` / `{{ENDING_SUBTITLE}}` / `{{CONTACT_INFO}}` | 10 | 클로징 문장 / 부제 / 연락처 |
| `{{BRAND_MARK}}` | 전 페이지 | 브랜드명 **텍스트** (표지는 좌상단, 그 외 푸터) |
| `{{PAGE_LABEL}}` | 02–10 | 페이지 번호 |

`Z-01`–`Z-04`(층·지표 번호)와 `Z-00`(표지)은 구조 장식이므로 리터럴로 둔다. 차트 축 값·분기 라벨은 샘플 데이터이며 생성 시 실제 데이터로 다시 그린다.

---

## IX. Anti-Pattern Checklist

| ✗ 금지 | 대안 |
| --- | --- |
| 한 페이지에 글로우 2개 이상 | 가장 중요한 한 점만 (번호·선두 지표·피크·코어) |
| 스크림 없이 렌더 위에 텍스트 | `#060B1A` 그라디언트 스크림 원자 위에 배치 |
| 렌더를 콘텐츠 페이지에 추가 | 콘텐츠는 평면 패널 + 원근 그리드로 깊이 표현 |
| 렌더 비트맵에 텍스트·로고 굽기 | 텍스트는 모두 편집 가능한 SVG 텍스트 |
| 웹 사진·스톡 3D 이미지로 교체 | `scene.html` 수정 후 재렌더 (팔레트 8색 유지) |
| `skewX`/`skewY`로 아이소메트릭 면 | 꼭짓점을 계산한 path/polygon |
| 신스웨이브 마젠타·주황 지평선 | cyan 능선 + violet 헤이즈 |
| 다크 위 본문에 `#6F7BA0` | 본문은 `#AEB9D6`, `#6F7BA0`은 크롬 전용 |
| 로고 이미지 번들 | `{{BRAND_MARK}}` 텍스트 |
