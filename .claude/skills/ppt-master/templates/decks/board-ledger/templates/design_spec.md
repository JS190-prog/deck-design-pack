---
deck_id: board-ledger
kind: deck
native_structure_mode: structured
summary: 절제·정밀·근거 우선의 경영진 보고 덱 — 이사회·경영위원회 보고, 경영계획·투자 심의, 전략 검토, 분기 성과 리뷰 (컨설팅 보고서 관용 문법 + 오픈소스 디자인 시스템의 16열 그리드·회색 단계에서 착안)
canvas_format: ppt169
canvas_width: 1280
canvas_height: 720
canvas_viewbox: "0 0 1280 720"
source_canvas_width: 1280
source_canvas_height: 720
source_viewbox: "0 0 1280 720"
replication_mode: standard
page_count: 12
primary_color: "#1E4FD8"
keywords: [board-report, action-title, exhibit, tracker, dense]
defaults:
  mode: pyramid
  visual_style: swiss-minimal
  delivery_purpose: text
placeholders:
  01_cover: ["{{TITLE}}", "{{SUBTITLE}}", "{{BRAND_MARK}}", "{{CLASSIFICATION}}", "{{MEETING_LABEL}}", "{{DATE}}", "{{AUTHOR}}", "{{ORGANIZATION}}", "{{DISCLAIMER}}"]
  02_exec_summary: ["{{TITLE}}", "{{ANSWER}}", "{{POINT_1}}", "{{POINT_1_DETAIL}}", "{{FIG_1}}", "{{FIG_1_LABEL}}", "{{POINT_2}}", "{{POINT_2_DETAIL}}", "{{FIG_2}}", "{{FIG_2_LABEL}}", "{{POINT_3}}", "{{POINT_3_DETAIL}}", "{{FIG_3}}", "{{FIG_3_LABEL}}", "{{ASK}}", "{{TRACK_1}}", "{{TRACK_2}}", "{{TRACK_3}}", "{{TRACK_4}}", "{{TRACK_5}}", "{{CLASSIFICATION}}", "{{SOURCE}}", "{{BRAND_MARK}}", "{{PAGE_NUM}}"]
  03_agenda: ["{{TITLE}}", "{{TOC_ITEM_1_TITLE}}", "{{TOC_ITEM_1_DESC}}", "{{TOC_ITEM_1_PAGE}}", "{{TOC_ITEM_2_TITLE}}", "{{TOC_ITEM_2_DESC}}", "{{TOC_ITEM_2_PAGE}}", "{{TOC_ITEM_3_TITLE}}", "{{TOC_ITEM_3_DESC}}", "{{TOC_ITEM_3_PAGE}}", "{{TOC_ITEM_4_TITLE}}", "{{TOC_ITEM_4_DESC}}", "{{TOC_ITEM_4_PAGE}}", "{{TOC_ITEM_5_TITLE}}", "{{TOC_ITEM_5_DESC}}", "{{TOC_ITEM_5_PAGE}}", "{{TRACK_1}}", "{{TRACK_2}}", "{{TRACK_3}}", "{{TRACK_4}}", "{{TRACK_5}}", "{{CLASSIFICATION}}", "{{BRAND_MARK}}", "{{PAGE_NUM}}"]
  04_section: ["{{CHAPTER_NUM}}", "{{CHAPTER_TITLE}}", "{{CHAPTER_DESC}}", "{{TRACK_1}}", "{{TRACK_2}}", "{{TRACK_3}}", "{{TRACK_4}}", "{{TRACK_5}}", "{{CLASSIFICATION}}", "{{BRAND_MARK}}", "{{PAGE_NUM}}"]
  05_exhibit_chart: ["{{TITLE}}", "{{EXHIBIT_NO}}", "{{EXHIBIT_TITLE}}", "{{UNIT}}", "{{TAKEAWAY_1}}", "{{TAKEAWAY_2}}", "{{TAKEAWAY_3}}", "{{TRACK_1}}", "{{TRACK_2}}", "{{TRACK_3}}", "{{TRACK_4}}", "{{TRACK_5}}", "{{CLASSIFICATION}}", "{{SOURCE}}", "{{BRAND_MARK}}", "{{PAGE_NUM}}"]
  06_exhibit_table: ["{{TITLE}}", "{{EXHIBIT_NO}}", "{{EXHIBIT_TITLE}}", "{{OPTION_1}}", "{{OPTION_1_NOTE}}", "{{OPTION_2}}", "{{OPTION_2_NOTE}}", "{{OPTION_3}}", "{{OPTION_3_NOTE}}", "{{OPTION_4}}", "{{OPTION_4_NOTE}}", "{{CRITERION_1}}", "{{CRITERION_2}}", "{{CRITERION_3}}", "{{CRITERION_4}}", "{{CRITERION_5}}", "{{TRACK_1}}", "{{TRACK_2}}", "{{TRACK_3}}", "{{TRACK_4}}", "{{TRACK_5}}", "{{CLASSIFICATION}}", "{{SOURCE}}", "{{BRAND_MARK}}", "{{PAGE_NUM}}"]
  07_issue_tree: ["{{TITLE}}", "{{EXHIBIT_NO}}", "{{EXHIBIT_TITLE}}", "{{UNIT}}", "{{ROOT}}", "{{DRIVER_1}}", "{{DRIVER_2}}", "{{DRIVER_3}}", "{{LEAF_1}}", "{{LEAF_2}}", "{{LEAF_3}}", "{{LEAF_4}}", "{{LEAF_5}}", "{{LEAF_6}}", "{{KEY_DRIVER}}", "{{TRACK_1}}", "{{TRACK_2}}", "{{TRACK_3}}", "{{TRACK_4}}", "{{TRACK_5}}", "{{CLASSIFICATION}}", "{{SOURCE}}", "{{BRAND_MARK}}", "{{PAGE_NUM}}"]
  08_matrix_2x2: ["{{TITLE}}", "{{EXHIBIT_NO}}", "{{EXHIBIT_TITLE}}", "{{BUBBLE_SIZE}}", "{{AXIS_X}}", "{{AXIS_Y}}", "{{QUAD_1}}", "{{QUAD_2}}", "{{QUAD_3}}", "{{QUAD_4}}", "{{ITEM_1}}", "{{ITEM_2}}", "{{ITEM_3}}", "{{ITEM_4}}", "{{ITEM_5}}", "{{ITEM_6}}", "{{TAKEAWAY_1}}", "{{TAKEAWAY_2}}", "{{TAKEAWAY_3}}", "{{TRACK_1}}", "{{TRACK_2}}", "{{TRACK_3}}", "{{TRACK_4}}", "{{TRACK_5}}", "{{CLASSIFICATION}}", "{{SOURCE}}", "{{BRAND_MARK}}", "{{PAGE_NUM}}"]
  09_roadmap: ["{{TITLE}}", "{{EXHIBIT_NO}}", "{{EXHIBIT_TITLE}}", "{{STREAM_1}}", "{{STREAM_1_OWNER}}", "{{STREAM_2}}", "{{STREAM_2_OWNER}}", "{{STREAM_3}}", "{{STREAM_3_OWNER}}", "{{STREAM_4}}", "{{STREAM_4_OWNER}}", "{{AS_OF}}", "{{TRACK_1}}", "{{TRACK_2}}", "{{TRACK_3}}", "{{TRACK_4}}", "{{TRACK_5}}", "{{CLASSIFICATION}}", "{{SOURCE}}", "{{BRAND_MARK}}", "{{PAGE_NUM}}"]
  10_kpi_scorecard: ["{{TITLE}}", "{{EXHIBIT_NO}}", "{{EXHIBIT_TITLE}}", "{{AS_OF}}", "{{KPI_1}}", "{{KPI_2}}", "{{KPI_3}}", "{{KPI_4}}", "{{COMMENTARY}}", "{{TRACK_1}}", "{{TRACK_2}}", "{{TRACK_3}}", "{{TRACK_4}}", "{{TRACK_5}}", "{{CLASSIFICATION}}", "{{SOURCE}}", "{{BRAND_MARK}}", "{{PAGE_NUM}}"]
  11_decision: ["{{TITLE}}", "{{DECISION}}", "{{ALT_1}}", "{{ALT_1_NOTE}}", "{{ALT_2}}", "{{ALT_2_NOTE}}", "{{ALT_3}}", "{{ALT_3_NOTE}}", "{{BUDGET}}", "{{FUNDING}}", "{{TIMELINE}}", "{{OWNER}}", "{{TRACK_1}}", "{{TRACK_2}}", "{{TRACK_3}}", "{{TRACK_4}}", "{{TRACK_5}}", "{{CLASSIFICATION}}", "{{SOURCE}}", "{{BRAND_MARK}}", "{{PAGE_NUM}}"]
  12_appendix: ["{{TITLE}}", "{{TRACK_1}}", "{{TRACK_2}}", "{{TRACK_3}}", "{{TRACK_4}}", "{{TRACK_5}}", "{{CLASSIFICATION}}", "{{SOURCE}}", "{{BRAND_MARK}}", "{{PAGE_NUM}}"]
---

# Board Ledger (보드 레저) — Design Specification

> 원저작 템플릿. 전략 컨설팅 보고서에서 널리 통용되는 **비독점 관용 문법** — 문장형 액션 타이틀, 페이지 상단 진행 트래커, 제목 아래 `Exhibit n`·단위 라인, 좌하단 출처·우하단 쪽번호, 콘텐츠 페이지 3단 글자 크기 — 과 Apache-2.0 공개 디자인 시스템의 **16열 2x 그리드·회색 단계·단일 액센트** 규율을 슬라이드 문법으로 새로 설계했다. 어떤 회사의 상표·로고·서체·독점 서식도 번들하지 않으며, 브랜드 표기는 `{{BRAND_MARK}}` 텍스트로만 존재한다. 서체는 install-local Pretendard 락을 따른다.

---

## I. Template Overview

| Property | Description |
| --- | --- |
| **Template Name** | board-ledger |
| **Display Name** | Board Ledger (보드 레저) |
| **Use Cases** | 이사회·경영위원회 보고, 경영계획·투자 심의, 전략 검토 보고, 분기 성과 리뷰 |
| **Design Tone** | 절제·정밀·근거 우선 — **제목만 읽어도 결론이 이어진다** |
| **Theme Mode** | **Light** — 전 페이지 `#FFFFFF`, 패널은 별도 재질인 영역에만 |

한눈에 알아보는 표식은 세 가지다. 상단의 **5단 트래커**(현재 장만 잉크 + 128px 블루 언더라인), 고정 높이의 **2줄 액션 타이틀 존**, 그리고 모든 근거 페이지의 **`Exhibit n · 제목 ……… 단위` 라인과 잉크 1px 규칙선**. 나머지는 회색 규칙선의 위계로만 정리된다.

**Anti-mood**: "마케팅 키노트", "라운드 카드 갤러리", "그라디언트 대시보드", "아이콘 인포그래픽", "다색 카테고리 팔레트".

**Litmus test**: ① 액션 타이틀만 이어 읽어 보고서의 결론이 재구성되면 통과. ② 블루를 지워도 페이지가 성립하면 통과 — 블루는 **초점 표시**이지 장식이 아니다. ③ 숫자 옆에 단위·기준·출처가 없으면 실패.

---

## II. Canvas & Grid

| Property | Value |
| --- | --- |
| **Format** | Standard 16:9 (`ppt169`), 1280 × 720, viewBox `0 0 1280 720` |
| **Margins** | 좌우 64 — 콘텐츠 폭 1152 (x 64 → 1216) |
| **Grid** | 16열 × 72px, 열 경계 x = 64 + 72k. 영역은 열 경계에서 시작·끝난다 |
| **Corners** | 전부 0 (라운드 없음) |

콘텐츠 페이지 세로 리듬(고정):

| Zone | y | 내용 |
| --- | --- | --- |
| Tracker | baseline 52 | 5탭, 탭 폭 2열(144), 언더라인 128×3 at y 62 |
| Header rule | 64 | 마스터 원자 `#C6C6C6` |
| Action title | 84 – 160 | 28px, 기준선 110 / 148 (2줄 고정 존) |
| Exhibit line | baseline 188 | 좌 `Exhibit n · 제목`, 우 단위·범례 |
| Exhibit rule | 202 | 잉크 1px (레이아웃 원자) |
| Body | 218 – 648 | 근거 영역 |
| Footer rule | 664 | 마스터 원자 `#E0E0E0` |
| Footer | baseline 689 | 좌 `{{SOURCE}}`, 우 `{{BRAND_MARK}}`(x 1120 end) · `{{PAGE_NUM}}`(x 1216 end) |

**레일 분할**(`ledger_exhibit_rail`): Exhibit 1–10열(64 → 784) · 거터 11열 · 시사점 레일 12–16열(856 → 1216). 제목 존은 레일 여부와 무관하게 항상 전폭이다.

액션 타이틀이 1줄이어도 Exhibit 라인은 y 188에 고정한다 — 본문 시작선이 페이지마다 같아야 넘길 때 시선이 흔들리지 않는다.

---

## III. Color Scheme — LOCKED

이 12개 외의 HEX는 어떤 생성 SVG에도 나타나서는 안 된다.

| Role | HEX | Purpose |
| --- | --- | --- |
| Ink | `#161616` | 제목·핵심 수치·Exhibit 규칙선·표 머리/합계 규칙선 |
| Body | `#393939` | 본문, 보조 수치 |
| Muted | `#6F6F6F` | 라벨·단위·축·비활성 트래커·출처, 트리 연결선, 스파크라인 |
| Rule | `#C6C6C6` | 구조 규칙선, 비초점 막대·버블, 리프 테두리 |
| Hairline | `#E0E0E0` | 행 구분선, 푸터 규칙선 |
| Surface | `#F4F4F4` | **별도 재질 영역만** — 의사결정 레일, 승인란, 트리 1차 동인, 2×2 우선 사분면 |
| Canvas | `#FFFFFF` | 배경 |
| Accent | `#1E4FD8` | **유일한 액센트** — 트래커 언더라인 + 페이지당 초점 1곳 |
| Accent tint | `#E8EEFC` | 액센트 초점의 바탕(결론 박스, 권고안 열·행, 핵심 동인 리프) |
| Positive | `#1F7A3A` | 상태 셀 전용 — 계획 초과 |
| Caution | `#B7791F` | 상태 셀 전용 — 경계 |
| Negative | `#C62828` | 상태 셀 전용 — 미달 |

### Color Rules

- **액센트는 페이지당 최대 2회**: 크롬인 트래커 언더라인 1회 + 콘텐츠 초점 1곳(강조 막대 / 권고안 열 / 핵심 동인 / 핵심 경로 막대 / 권고 대안 / 결론 박스). 초점이 없는 페이지(KPI·부록)는 트래커만 쓴다
- **틴트는 액센트가 표시한 그 초점 뒤에만 깐다.** 단독 장식 배경으로 쓰지 않는다
- **상태색(긍정·경계·부정)은 상태 셀 안에서만** — KPI 차이 값과 삼각 표식, RAG 점. 막대·제목·본문에 쓰지 않는다
- **차트 래더**: 초점 `#1E4FD8` → 비초점 `#C6C6C6` → 보조선 `#6F6F6F`. 두 번째 유채 계열이 필요하면 Exhibit을 나눈다
- **Forbidden**: 그라디언트, 그림자, 글로우, 반투명 겹침, 라운드, 액센트 외 유채색 장식

---

## IV. Typography System

install-local Pretendard 락. **제목은 SemiBold, 표지·숫자만 Bold.**

| Weight | `font-family` attribute |
| --- | --- |
| 400 | `Pretendard, 'Malgun Gothic', sans-serif` |
| 500 | `'Pretendard Medium', Pretendard, 'Malgun Gothic', sans-serif` |
| 600 | `'Pretendard SemiBold', Pretendard, 'Malgun Gothic', sans-serif` |
| 700 | `Pretendard, 'Malgun Gothic', sans-serif` + `font-weight="700"` |

**콘텐츠 페이지는 3단 크기 — 제목 28 / 본문 18 / 라벨 13** (+ 크롬 12). 큰 숫자는 제목 크기(28)를 기본으로 하고, KPI 실적값(40)·트리 루트값(32)만 예외다.

| Role | Size | Weight | Letter-spacing | Use |
| --- | --- | --- | --- | --- |
| Chapter number | 104 | 700 | -3 | 간지 대형 번호 |
| Cover title | 48 | 700 | -1.0 | 표지 제목 (1줄 ≈ 21자) |
| Chapter title | 44 | 700 | -0.8 | 간지 제목 |
| KPI actual | 40 | 700 | -0.8 | 스코어카드 실적값 |
| Action title | 28 | 600 | -0.4 | 콘텐츠 제목, 2줄·행간 38 (1줄 ≈ 41자) |
| Key figure | 28 | 700 | -0.4 | 요약 핵심 수치 |
| Cover subtitle | 22 | 400 | -0.2 | 표지 부제 |
| Lead | 20 | 600 | -0.2 | 결론 문장·요약 포인트·의결 안건 (1줄 ≈ 50자) |
| Body | 18 | 400–600 | 0 | 본문·표 셀·트리 노드·시사점 (레일 1줄 ≈ 18자) |
| Appendix | 15 | 400 / 600 | 0 | 부록 노트, 행간 26 |
| Exhibit line | 14 | 600 / 500 | 0 | `Exhibit n` 잉크 + 제목 Body색 |
| Label | 13 | 400–600 | 0 | 단위·축·열 머리·범례·트래커 |
| Chrome | 12 | 400–600 | 0–0.4 | 출처·쪽번호·분류 표기 |

본문 18px 미만은 크롬(12–13)과 부록(15)뿐이다. 글이 넘치면 크기를 줄이지 말고 문장을 줄이거나 Exhibit을 나눈다.

---

## V. Page Roster

| File | Layout key | Picker name | Master | Purpose |
| --- | --- | --- | --- | --- |
| `01_cover.svg` | `ledger_cover` | Cover | `ledger_title_master` | 표지 — 백지 위 48px 제목, 48×3 블루 규칙선, 우상단 분류 스탬프, 보고일자·보고자·소관 부서 메타 |
| `02_exec_summary.svg` | `ledger_exec_summary` | Executive Summary | `ledger_content_master` | 결론 먼저 — 틴트 결론 박스, 번호 3행 근거 + 우측 핵심 수치, 하단 의사결정 요청 레일 |
| `03_agenda.svg` | `ledger_agenda` | Agenda | `ledger_content_master` | 목차 — 규칙선 5행(번호·안건·주요 내용·쪽) |
| `04_section.svg` | `ledger_section` | Section | `ledger_title_master` | 간지 — 104px 장 번호, 장 제목·설명, 하단 5단 위치 스트립 |
| `05_exhibit_chart.svg` | `ledger_exhibit_rail` | Exhibit + Takeaway Rail | `ledger_content_master` | 8개 막대(초점 1개 블루), 직접 값 라벨, CAGR 브래킷 + 시사점 레일 3항 |
| `06_exhibit_table.svg` | `ledger_exhibit_full` | Exhibit — Full Width | `ledger_content_master` | 4개 대안 × 5개 기준, 하비볼 0–4, 가중치 열, 합계 행, 권고안 열 틴트 |
| `07_issue_tree.svg` | `ledger_exhibit_full` | Exhibit — Full Width | `ledger_content_master` | MECE 트리 — 결과 1 → 1차 동인 3 → 2차 동인 6, 직각 연결선, 핵심 동인 콜아웃 |
| `08_matrix_2x2.svg` | `ledger_exhibit_rail` | Exhibit + Takeaway Rail | `ledger_content_master` | 2×2 우선순위 — 화살표 축, 사분면 라벨, 크기 버블 6개(초점 1개) + 시사점 레일 |
| `09_roadmap.svg` | `ledger_exhibit_full` | Exhibit — Full Width | `ledger_content_master` | 분기 간트 — 6분기, 4개 과제, 핵심 경로 막대, 마일스톤 다이아몬드, 기준일 점선 |
| `10_kpi_scorecard.svg` | `ledger_kpi` | KPI Scorecard | `ledger_content_master` | 지표 4개 — 실적·계획·차이(상태색)·8분기 스파크라인, 코멘트 행 |
| `11_decision.svg` | `ledger_decision` | Decision Request | `ledger_content_master` | 의결 요청(엔딩) — 의결 안건, 검토 대안 vs 권고, 소요 자원·일정·책임, 승인란 |
| `12_appendix.svg` | `ledger_appendix` | Appendix — Two Column | `ledger_content_master` | 부록 — 단일 세로 규칙선 위 2단 노트(방법론·용어·출처·유의 사항), 패널 없음 |

### Master / Layout / Slot contract

- **`ledger_content_master`** 원자: `master-bg`(#FFFFFF) · `master-header-rule`(y 64, #C6C6C6) · `master-footer-rule`(y 664, #E0E0E0).
- **`ledger_title_master`** 원자: `master-bg` · `master-footer-rule`. 헤더 규칙선이 없는 것이 표지·간지의 차이다.
- 콘텐츠 공통 슬롯: `title`(64 84 1152 76) · `footer` idx 2 = 출처(64 672 800 24) · `slide-number` idx 3(1136 672 80 24). `ledger_agenda`는 출처 슬롯이 없다.
- `ledger_exec_summary`: 레이아웃 원자 = 결론 패널·블루 바·"핵심 결론" 라벨·요청 패널·"의사결정 요청" 라벨, `body` idx 1 = 결론 문장(176 188 1016 72).
- `ledger_decision`: 레이아웃 원자 = 상단 잉크 규칙선·안건 하단 규칙선·승인 패널·"의결 안건" 라벨, `body` idx 1 = 의결 안건(208 188 1008 72).
- `ledger_exhibit_rail`: Exhibit 규칙선(64→784) + 레일 규칙선(856→1216). `ledger_exhibit_full`: 전폭 Exhibit 규칙선(64→1216). `ledger_kpi`: 타일 상단 2px 잉크 규칙선 4개 + 코멘트 규칙선. `ledger_appendix`: x 640 세로 규칙선. `ledger_agenda`: y 212 잉크 머리 규칙선.
- 표지: `title`(64 294 1024 72) + `subtitle` idx 1(64 372 1024 44). 간지: `title`(64 340 1152 64) + `body` idx 1 = 장 설명(64 412 768 68) + `slide-number` idx 3.
- `05`/`08`은 고정 원자와 슬롯 계약이 같아 `ledger_exhibit_rail`을, `06`/`07`/`09`는 `ledger_exhibit_full`을 공유한다. Exhibit 내용(막대·표·트리·사분면·간트)은 슬라이드 로컬이다.
- 트래커의 현재 탭·간지 스트립의 현재 구간은 페이지마다 다르므로 슬라이드 로컬 그룹이다.

---

## VI. Signature Design Elements

1. **5단 트래커** — 탭마다 `0n` + 장 이름(`{{TRACK_n}}`), 현재 장만 잉크 SemiBold + 블루 128×3 언더라인이 헤더 규칙선 위에 얹힌다. 요약·목차·부록은 현재 장이 없으므로 언더라인도 없다. 간지에서는 같은 5단이 하단 4px 위치 스트립으로 나타난다
2. **고정 액션 타이틀 존** — 28px SemiBold 완결 문장, 최대 2줄. 라벨형 제목("매출 현황")과 질문형 제목은 쓰지 않는다
3. **Exhibit 라인** — `Exhibit n · 제목`(좌) ↔ `단위: …` 또는 범례(우), 그 아래 잉크 1px. 모든 숫자에 단위·기준이 붙는다
4. **규칙선 위계, 패널은 예외** — 잉크 1px(Exhibit·표 머리·합계) → `#C6C6C6`(구조) → `#E0E0E0`(행). 채운 패널은 결론 박스·의사결정 레일·승인란·트리 1차 동인처럼 **재질이 다른 영역**에만
5. **원장식 숫자** — 수치는 우측 정렬 또는 고정 열 정렬, 수치 라벨은 아래 13px Muted. 감소는 `−`(U+2212)로 쓴다
6. **분류 표기** — 표지는 160×30 잉크 테두리 스탬프, 콘텐츠·간지는 우상단 12px `{{CLASSIFICATION}}`. 표지 하단에는 `{{DISCLAIMER}}`

---

## VII. Chart & Table Treatment

숫자·축 라벨·하비볼·간트 막대·트리 값·부록 노트는 **샘플 데이터**다. 생성 시 실제 값으로 다시 그리고, 구조(위치·색·규칙선 위계)는 유지한다.

- **막대(05)**: 정사각 모서리, 비초점 `#C6C6C6`, 초점 1개 `#1E4FD8`. y축·그리드 없이 막대 위 14px 직접 값 라벨(초점만 잉크 SemiBold). 기준선 잉크 1px, x축 라벨 13px. 성장률은 막대 위 `#6F6F6F` 브래킷 + 13px 라벨. 막대 폭 52 / 슬롯 90
- **표(06)**: 머리 위 잉크(Exhibit 규칙선) → 머리 아래 `#C6C6C6` → 행 `#E0E0E0` → 합계 행은 잉크 1px 두 줄 사이. 권고안 열은 틴트 + 상단 3px 블루 + 12px "권고안". 하비볼은 r 11, 잉크 1.5px 테두리, 0/¼/½/¾/1 다섯 단계 — 범례는 Exhibit 라인 우측 "낮음 ○◔◑◕● 높음". 주석 행은 13px Muted
- **트리(07)**: 결과 = 잉크 1.5px 테두리 흰 상자, 1차 동인 = Surface 상자, 2차 동인 = `#C6C6C6` 테두리 흰 상자. 연결선은 `#6F6F6F` 1px 직각. 핵심 동인 리프만 틴트 + 블루 1.5px 테두리, 블루 연결선과 2px 세로 바의 콜아웃("핵심 동인" + 18px 설명 ≤ 3줄). 열 머리 "결과 / 1차 동인 / 2차 동인" 13px. 상위 값 = 하위 값의 합
- **2×2(08)**: 축은 잉크 1px + 삼각 화살촉, 중앙선 `#C6C6C6`, 우선 사분면만 Surface. 버블 `#C6C6C6` + 흰 1.5px 테두리, 초점 1개 블루, 라벨은 버블 오른쪽 14px(우측 끝 버블은 왼쪽). y축 라벨은 -90° 회전
- **간트(09)**: 분기 열 144px, 연도 경계 `#C6C6C6`, 분기 경계 `#E0E0E0`. 막대 높이 24·정사각, 라벨은 막대 중앙 13px. 핵심 경로 1개만 블루(흰 글자). 마일스톤은 잉크 다이아몬드(흰 테두리) + 오른쪽 13px 라벨. 기준일은 잉크 `4 3` 점선 + 하단 라벨
- **KPI(10)**: 실적 40px, 계획·차이는 x0+178 정렬, 차이 값과 삼각 표식만 상태색. 스파크라인 `#6F6F6F` 1.5px + 계획 `#C6C6C6` 점선 + 마지막 점 잉크
- **Forbidden**: 3D, 파이, 그리드 상자, 범례 박스, 막대 라운드, 다색 계열

| Page | Marker |
| --- | --- |
| `05_exhibit_chart` | `<!-- chart-plot-area: 64,268,784,568 -->` (y 236–268은 브래킷·값 라벨 띠) |
| `08_matrix_2x2` | `<!-- chart-plot-area: 120,228,776,572 -->` |

---

## VIII. Placeholder Vocabulary

| Token | Pages | Content |
| --- | --- | --- |
| `{{TITLE}}` | 01–03, 05–12 | 표지 제목 / 액션 타이틀(완결 문장, ≤ 2줄) |
| `{{SUBTITLE}}` / `{{MEETING_LABEL}}` | 01 | 부제 / 회의·안건 표기("제12차 정기 이사회 · 안건 제2호") |
| `{{DATE}}` / `{{AUTHOR}}` / `{{ORGANIZATION}}` | 01 | 보고일자 / 보고자 / 소관 부서 |
| `{{DISCLAIMER}}` | 01 | 배포 제한 문구 |
| `{{CLASSIFICATION}}` | 전 페이지 | 분류 표기(≤ 12자, 예 "대외비 · 이사회 한정") |
| `{{TRACK_1}}`–`{{TRACK_5}}` | 02–12 | 장 이름(번호 제외, ≤ 7자) |
| `{{ANSWER}}` | 02 | 핵심 결론 1문장(≤ 2줄) |
| `{{POINT_n}}` / `{{POINT_n_DETAIL}}` / `{{FIG_n}}` / `{{FIG_n_LABEL}}` | 02 | 근거 헤드라인 / 보조 1줄 / 핵심 수치 / 수치 설명 (n=1..3) |
| `{{ASK}}` | 02 | 의사결정 요청 1문장 |
| `{{TOC_ITEM_n_TITLE}}` / `_DESC` / `_PAGE` | 03 | 안건 / 주요 내용(≤ 28자) / 쪽 (n=1..5) |
| `{{CHAPTER_NUM}}` / `{{CHAPTER_TITLE}}` / `{{CHAPTER_DESC}}` | 04 | 장 번호("02") / 장 제목 / 설명(≤ 2줄) |
| `{{EXHIBIT_NO}}` / `{{EXHIBIT_TITLE}}` | 05–10 | Exhibit 번호 / Exhibit 제목 |
| `{{UNIT}}` / `{{AS_OF}}` / `{{BUBBLE_SIZE}}` | 05·07 / 09·10 / 08 | 단위 / 기준 시점 / 버블 크기 기준 |
| `{{TAKEAWAY_n}}` | 05, 08 | 시사점(1줄 ≈ 18자, ≤ 3줄, n=1..3) |
| `{{OPTION_n}}` / `{{OPTION_n_NOTE}}` / `{{CRITERION_n}}` | 06 | 대안명 / 대안 설명 (n=1..4) / 평가 기준 (n=1..5) |
| `{{ROOT}}` / `{{DRIVER_n}}` / `{{LEAF_n}}` / `{{KEY_DRIVER}}` | 07 | 결과 / 1차 동인(n=1..3) / 2차 동인(n=1..6) / 콜아웃(≤ 3줄) |
| `{{AXIS_X}}` / `{{AXIS_Y}}` / `{{QUAD_n}}` / `{{ITEM_n}}` | 08 | 축 / 사분면(1=우상 우선) / 버블 라벨(≤ 8자, n=1..6) |
| `{{STREAM_n}}` / `{{STREAM_n_OWNER}}` | 09 | 추진 과제 / 책임 조직·임원 (n=1..4) |
| `{{KPI_n}}` / `{{COMMENTARY}}` | 10 | 지표명 (n=1..4) / 코멘트 1–2줄 |
| `{{DECISION}}` / `{{ALT_n}}` / `{{ALT_n_NOTE}}` | 11 | 의결 안건 / 대안 / 대안 판단 근거 (n=1..3) |
| `{{BUDGET}}` / `{{FUNDING}}` / `{{TIMELINE}}` / `{{OWNER}}` | 11 | 총 소요 예산 / 재원 / 추진 일정 / 책임 임원 |
| `{{SOURCE}}` | 02, 05–12 | "자료: …" 출처 1줄 |
| `{{BRAND_MARK}}` | 전 페이지 | 브랜드명 **텍스트** |
| `{{PAGE_NUM}}` | 02–12 | 쪽번호 |

표지 제목이 2줄이 되면 부제를 60px 내린다. 액션 타이틀이 1줄이어도 Exhibit 라인·본문 위치는 옮기지 않는다.

---

## IX. Anti-Pattern Checklist

| ✗ 금지 | 대안 |
| --- | --- |
| 라벨형·질문형 제목("시장 현황", "왜 지금인가?") | 결론을 담은 완결 문장 |
| 제목 길이에 따라 본문 시작선 이동 | 제목 존 84–160 고정, Exhibit 라인 y 188 |
| 블루를 페이지 여러 곳에 | 트래커 + 초점 1곳 |
| 상태색을 막대·제목·본문에 | 상태 셀(KPI 차이·RAG)에만 |
| 모든 블록을 카드·박스로 감싸기 | 규칙선으로 묶고, 패널은 재질이 다른 영역만 |
| 라운드·그림자·그라디언트 | 정사각, 평면, 회색 단계 |
| 단위·기준 없는 숫자 | Exhibit 라인 단위 + 수치 아래 라벨 |
| 출처 없는 근거 페이지 | `{{SOURCE}}` 좌하단 |
| 넘치는 글을 16px 이하로 축소 | 문장 축약 또는 Exhibit 분할(부록만 15px) |
| y축·그리드 상자로 막대 차트 채우기 | 직접 값 라벨 + 기준선 1개 |
| 로고 이미지 번들 | `{{BRAND_MARK}}` 텍스트 |
