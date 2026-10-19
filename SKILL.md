---
name: music-prompt
description: 配乐与背景音乐提示词方法论。当用户要给视频配乐、写 BGM/音乐生成提示词（Suno、豆包等 AI 音乐工具）、选择音乐情绪方向时使用。Music prompting methodology for videos — emotion switches (mode/BPM/register/articulation/instruments/chords & drone), an eight-section prompt formula, dual-box prompts for international tools (English Style tags + structure metatags) vs natural-language prompts for domestic tools, eight genre recipes, mixing red lines, and reference-track workflow. Use when writing BGM prompts or choosing music direction.
---

# Music prompting — scoring direction & BGM briefs

Read this when: the user wants music for a video, asks you to write a
background-music prompt, or needs a BGM direction chosen. Not for: a finished
track that only needs beat-cut editing (timing anchors are a different,
editing-side concern), or sound effects only — those are different requests.

This page is a methodology for **writing music-generation prompts** for AI
music tools (Suno, 豆包, 海绵音乐, etc.). It produces text, not audio:
AI can generate the track, but *which emotion to ask for* is a decision the
user (with you) makes first. Everything below feeds the eight-section formula
at the end — fill it in and hand it to the music tool.

## When the request is thin — default, then disclose

Users often open with almost nothing: 「给这个视频配个乐」. Don't reply with a
questionnaire. Name the video type, let the type set the defaults, and move:

1. **Name the video type** — vlog? promo? talking-head? That one fact implies
   most of the switches below.
2. **Fill type-appropriate defaults and proceed**: 露营 vlog → 大调、
   90–110 BPM、木吉他；宣传片 → 小调起步、渐紧、亮相打开（见速查表）。
3. **Deliver, then disclose the guesses** — one line after the prompt:
   「我按露营 vlog 补了这些假设（大调 / 100 BPM / 木吉他），哪条不合适
   直接说，我改」。

Only two gaps genuinely change the deliverable; mention them in passing
instead of blocking: 有没有解说人声（决定下面的混音红线），用哪个工具生成
（决定国际版还是国内版）。No answer? Take conservative defaults — assume
narration, and ship both versions.

## The emotion switches, in order of impact

Controlled experiments that vary one music element at a time rank the levers
by how strongly they move emotion. Work down the list — the top switches
decide most of the feel; instrumentation is the *last* thing to pick.

1. **Mode: major vs minor.** The single biggest lever. Major = bright/open;
   minor = sad or tense. The same melody flips to minor by changing three
   notes — the mood flips instantly. (Which letter the key is named by does
   not matter — C major and A minor are both white keys.) Undecided? Default
   to **C major** (bright, happy) or **A minor** (sad, tense).
2. **Tempo (BPM).** Remember four ranges:
   - 60–80 — quiet, heart-to-heart
   - 90–110 — natural, conversational
   - 120–140 — energetic
   - 150+ — tense, high-burn
3. **Register & dynamics.** High notes played softly = bright and tender;
   low notes played heavily = gloomy.
4. **Articulation.** Short detached notes (staccato) = playful; notes joined
   smoothly (legato) = calm.
5. **Instruments** — last. Marimba = positive/upbeat; piano + strings = warm.

### Deeper lever: chords & drone

When the switches above are set, chord color refines the mood:

- major triad — brighter; minor triad — darker;
- suspended chord (sus) — like a sentence left unfinished, keeps hanging;
- diminished chord — extremely unstable, tense/thriller;
- **drone (持续低音)** — the suspense recipe: the lowest note never moves
  while the chords above change; the longer you listen the more uneasy it
  gets. In a prompt, write it literally: 「低音持续一个音」.

## Eight-section formula (fill in and send)

The prompt template that carries all decisions above. Write each section
explicitly; write the duration as a **number**:

1. **用途和画面** — what the video is and what's on screen
2. **时长** — seconds, as a number
3. **情绪** — the target feeling
4. **调性** — major/minor (and key if chosen)
5. **速度和拍子** — BPM from the ranges above
6. **乐器** — chosen last, per switch 5
7. **结构和时间点** — the shape over time, e.g. 「第 22 秒一个重音」
8. **负面清单** — what to avoid: 不要人声 / 不要突然的鼓点 / …

## Eight video genres — quick recipes

| Genre | Recipe |
|---|---|
| 宣传片 promo | minor-key start, growing tension, accent/turn-on the second the product appears |
| 悬疑 suspense | slow tempo, drone (bass doesn't move), a few scattered dissonant notes on top |
| 旅行 vlog | major key, 118 BPM, ukulele + light percussion |
| 带货 selling | 128 BPM, instrumental ensemble, clear rhythm |
| 治愈 healing | slower, piano + light percussion + a touch of chords |
| 古风 | pentatonic scale, guzheng |
| 搞笑 comedy | bounce feel, xylophone, bassoon |
| 知识口播 talking-head | marimba, steady tempo, no prominent melody, the smaller the dynamics swing the better |

## Three mixing red lines

1. Music **below the voice** — keep BGM roughly **20 dB** under the
   narration/dialogue.
2. Under talking-head narration, the music must have **no prominent melody**.
3. When something else cuts in mid-video (insert, announcement), the music
   **steps aside first**.

## Music vs picture first — pick one workflow

- **Music first**: generate the track, then cut the picture to its drum hits
  (beat-cut / 卡点 videos).
- **Picture first**: cut the edit, note the transition time points, then write
  them into the prompt (「第 22 秒一个重音」) — durations as plain numbers.
- **Long videos** with big arcs: generate in several segments and join them in
  the edit — far easier to control than one long generation.
- **Endings**: stop cleanly, or resolve on a chord — don't let it trail off
  and ring out; a clean tail is easy to cut.

## Reference tracks & copyright

When the user likes an existing track, it cannot be used directly. Feed it to
an AI music tool as a reference and ask for: **an original piece with the same
instrumentation, groove and mood — do not copy the melody.** Copyright terms
follow the platform's user agreement; treat large commercial projects with
extra care and let the user decide.
