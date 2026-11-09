# NOTICE — deck-voice

## gongnyang/gn-voice — https://github.com/gongnyang/gn-voice

gn-voice는 분할 라이선스다. 파이프라인과 스킬 정의(LICENSE Section A)는 MIT이고, 저자의 글과 거기서 만든
데이터(Section B)는 권리가 유보되어 있다. deck-voice는 **Section A에서만** 가져왔다.

가져온 것 (MIT):

- `references/presentation.md` — gn-voice `references/profiles/presentation.md`를 옮겼다. 원저자 개인 문체
  지시('공냥 터치')는 사용자 문체 가이드를 적용하는 규칙으로 바꾸고, ppt-master `design_spec.md` 대응과
  규칙 우선순위를 더했다.
- 방식 — 서식을 걷어낸 본문 → 문체 지표 → 분위수 허용 범위 → 스크립트 검사, 범위 이탈 2개까지 허용,
  음슴체 종성 판정과 명사 오탐 목록(`scripts/verify_style.py`), 숫자·영문 이름 대조(`scripts/gate_fidelity.py`) —
  를 `scripts/deck_voice.py`에 다시 구현했다. 장표 역할(제목·본문·노트) 분리와 PPTX 읽기는 새로 썼다.

가져오지 않은 것 (Section B, 권리 유보 — 이 저장소에 없다):

- `corpus/`, `analysis/`, `examples/`
- 개인 장르 팩 9종: chat, reply, lecture-tip, promo, lecture, biz-s, biz-l, essay, column
- 저자 코퍼스에서 뽑은 수치: `fingerprint-slim.json` 밴드, `ai-tells.json` 목록. 일반 AI 상투구 목록은 직접 적었고,
  밴드는 사용자 견본으로 `build`가 새로 만든다.

```
MIT License (gn-voice LICENSE Section A)

Copyright (c) 2026 gn-voice authors

Permission is hereby granted, free of charge, to any person obtaining a copy
of the software and associated documentation files enumerated above (the
"Software"), to deal in the Software without restriction, including without
limitation the rights to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software, and to permit persons to whom
the Software is furnished to do so, subject to the following conditions:

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

## kosoe-office `tools/voice/voice_tool.py` (MIT, Copyright (c) 2026 kosoe-office contributors)

5줄 묶음 표본, 분위수 밴드와 여유값, 한 건 빼고 검증과 라벨(시험용·소표본·표본·미검증), `~ 필요`를 존댓말로
세지 않는 끝맺음 분류, 날짜·연도 정규화를 포함한 숫자 대조는 이 도구에서 가져왔다(MIT 고지는 위와 같은 문구).
