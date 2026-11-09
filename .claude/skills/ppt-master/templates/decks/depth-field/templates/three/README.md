# depth-field 3D 장면 소스

`scene.html` 한 파일이 덱의 렌더 비트맵 4장을 만든다. 장면은 URL 쿼리로 고른다.

| scene | 크기 | 출력 | 쓰는 페이지 |
| --- | --- | --- | --- |
| `cover` | 1600×900 | `images/df_cover.jpg` | `01_cover` |
| `section` | 1600×900 | `images/df_section.jpg` | `03_section` |
| `hero` | 1152×1080 | `images/df_hero.jpg` | `04_hero_visual` (768×720 프레임의 1.5배) |
| `closing` | 1600×900 | `images/df_closing.jpg` | `10_closing` |

예: `scene.html?scene=cover&w=1600&h=900`. 렌더가 끝나면 `window.__done === true`이고 캔버스에 한 프레임이 남는다(`preserveDrawingBuffer: true`).

## 다시 렌더하기

1. 헤드리스 Edge/Chrome(playwright-core 등)으로 위 URL을 연다. GPU가 없는 환경이면 `--use-angle=swiftshader --enable-unsafe-swiftshader`를 붙인다.
2. `window.__done === true`를 기다린 뒤 `document.querySelector('canvas').toDataURL('image/png')`로 PNG를 받는다.
3. PNG를 JPEG(quality 82)로 바꿔 `images/df_<scene>.jpg`로 저장한다. 한 장 350 KB 이하, 합계 1.5 MB 이하를 지킨다.

장면은 결정적이다(시드 고정 난수 `mulberry32(20260709)`, 고정 카메라, 한 프레임). 같은 파일로 다시 렌더하면 같은 그림이 나온다.

## 색 바꾸기

파일 상단 `PAL` 객체 한 곳만 고친다. `design_spec.md` §III의 8색과 같아야 한다.

```js
const PAL = { bg: 0x060B1A, panel: 0x0E1630, line: 0x1E2A4A,
  text: 0xEAF0FF, body: 0xAEB9D6, muted: 0x6F7BA0, cyan: 0x5CE1E6, violet: 0x8B7CFF };
```

빛 번짐 세기는 각 `build*()` 끝의 `bloom = { strength, radius, threshold }`로 조절한다. 텍스트가 놓이는 왼쪽(커버는 왼쪽 위 하늘) 구도는 비워 둔다.

## 라이선스

three.js(MIT)는 import map으로 `https://cdn.jsdelivr.net/npm/three@0.160.0/`에 고정해 불러오며 이 저장소에 포함하지 않는다. 장면 코드는 이 템플릿을 위해 새로 작성했다.
