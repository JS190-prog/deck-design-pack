# Third-party notices

This repository bundles software and fonts written by other people. Their licences are
reproduced or pointed to below, and their copyright notices are preserved as those licences
require. The pack's own material — the fourteen deck templates, the seven brand presets, the
contact sheets, the three.js renders in `depth-field/images/`, and `install.py` — is
[MIT © 2026 humanist96](LICENSE).

---

## PPT Master workflow — `.claude/`, `.codex/`, `AGENTS.md`, `CLAUDE.md`, `docs/`, `requirements.txt`, `projects/`

The whole SVG-authoring → native-PPTX pipeline vendored into this repository comes from
**[byungjunjang/slide-master](https://github.com/byungjunjang/slide-master)**, itself a Korean-workflow
customisation of **[hugohe3/ppt-master](https://github.com/hugohe3/ppt-master)**. Both are MIT.

Vendored at slide-master `main`, 2026-08-04. Files are byte-identical to upstream except where
this repository's own README, docs index, and template library extend them; upstream's own README
is kept verbatim at [`docs/slide-master-README.md`](docs/slide-master-README.md).

```
MIT License

Copyright (c) 2025-2026 Hugo He

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

Two skills vendored under `.claude/skills/` carry their own `LICENSE` file alongside their
`SKILL.md` — `codex-image` and `diagram-design`. Those files are unmodified; read them there.

---

## gn-voice method and presentation profile — `.claude/skills/deck-voice/`

`deck-voice` adapts the measured-style method and the `presentation` profile of
**[gongnyang/gn-voice](https://github.com/gongnyang/gn-voice)** — its LICENSE Section A, MIT © 2026 gn-voice
authors. gn-voice's Section B material (the author's corpus, the analysis data derived from it, the nine
personal genre packs, and the examples) is reserved and is **not** included. Scope, changes, and the MIT text:
[`.claude/skills/deck-voice/NOTICE.md`](.claude/skills/deck-voice/NOTICE.md).

---

## Motion and scroll-deck principles — `decks/motion-cue/`, `decks/scroll-rail/`

`motion-cue` reflects the motion principles and technique vocabulary of
**[gongnyang/awesome-ai-motion](https://github.com/gongnyang/awesome-ai-motion)** (one focus per scene, one main
action with one or two supporting actions, hold the completed state), mapped onto PowerPoint's native
entrance effects. `scroll-rail` reflects the stop / handoff / concept-grammar principles of
**[gongnyang/awesome-html-scrolline-deck](https://github.com/gongnyang/awesome-html-scrolline-deck)**, mapped onto a
persistent progress rail and the `push` page transition. Both repositories are MIT © 2026 gongnyang. No code,
CSS, clips, or other files from either repository are included — the SVG pages and specs are original work.

---

## three.js — `decks/depth-field/templates/three/scene.html`

The scene source that produced the four bitmaps in `decks/depth-field/images/` imports
**[three.js](https://github.com/mrdoob/three.js)** `0.160.0` (and its UnrealBloom example add-on) from the jsDelivr
CDN by exact version. three.js is MIT © 2010-2026 three.js authors; it is **not** vendored in this repository.
The rendered images are original work of this pack. Placing a 3D scene behind slides follows the idiom of
reveal.js + three.js decks such as `dimroc/reveal.js-threejs` (MIT); no code from those decks is included.

---

## Bundled template libraries

`.claude/skills/ppt-master/templates/` ships upstream's deck and brand templates
(`apple`, `jangpm`, `mckinsey`, `naver_ir`; `anthropic`, `apple`, `google`, `jangpm`,
`mckinsey`, `naver`) plus upstream's icon and chart libraries. They arrive under the MIT
licence above. Where a template names a company it identifies a design *idiom* as a reference
point — descriptive comparison, not a claim of endorsement or affiliation. See
[`TRADEMARKS.md`](TRADEMARKS.md).

---

## Fonts

**Pretendard** — `.claude/skills/ppt-master/assets/fonts/Pretendard/`

> Copyright (c) 2021, Kil Hyung-jin (https://github.com/orioncactus/pretendard),
> with Reserved Font Name Pretendard.

SIL Open Font License 1.1. Full text:
[`assets/fonts/Pretendard/LICENSE.txt`](.claude/skills/ppt-master/assets/fonts/Pretendard/LICENSE.txt).

**KoPub돋움체 (KoPub Dotum)** — `.claude/skills/ppt-master/templates/decks/koscom-chevron/fonts/`

Published by the Korea Publishers Association, free to use and redistribute unmodified.
Details and the family/weight mapping:
[`fonts/FONTS.md`](.claude/skills/ppt-master/templates/decks/koscom-chevron/fonts/FONTS.md).

Neither font is embedded in an exported `.pptx` — PowerPoint does not embed fonts through this
pipeline. Install them wherever a deck is opened.
