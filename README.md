# music-prompt-skill

给 AI agent 用的**视频配乐提示词方法论** skill：教你的 Claude Code / OpenCode
在用户说「给这个视频配个乐」时，按音乐心理学的情绪开关顺序做出专业决策，
并产出结构化的音乐生成提示词（适用于 Suno、豆包、海绵音乐等 AI 音乐工具）。

## 安装

```bash
# Claude Code / OpenCode 通用（用户级）
mkdir -p ~/.claude/skills
git clone https://github.com/youyouhe/music-prompt-skill.git ~/.claude/skills/music-prompt
```

重启会话后即生效。触发词：配乐 / 背景音乐 / BGM / 写个音乐提示词 / music direction。

## 内容一览

- **情绪开关（按影响排序）**：调式（大调/小调）→ BPM（四区间）→ 音区与力度 →
  演奏方式（断奏/连奏）→ 乐器音色；深层杠杆：大三/小三/挂留/减和弦 + 持续低音（悬疑配方）。
- **八段公式**：用途画面 / 时长 / 情绪 / 调性 / 速度拍子 / 乐器 / 结构和时间点 / 负面清单。
- **双框写法（国际工具）**：Style 框英文 tag（流派/情绪/调性/BPM/乐器/制作感）+
  结构框元标签（[Intro: Ambient Pad] / [Buildup] / [Beat Drop] / [Outro: Sudden Cut]）；
  时间点落在结构框，Style 框不写时间戳。
- **双版本输出**：同一套八段决策，产出国际版（英文 Style 串 + 元标签 + 负面清单）
  与国内版（中文自然长段）；附智能手表发布会完整示例。
- **输入很少时**：按视频类型补缺省（露营 vlog → 大调 / 90–110 BPM / 木吉他），
  输出后附一句「我补了这些假设，可改」。
- **八大类视频速查表**：宣传片、悬疑、旅行 vlog、带货、治愈、古风、搞笑、知识口播。
- **进阶（未实测）**：调性写到具体 key、能量曲线四型（线性攀升/反转高潮/平稳底色/
  三幕推进）——Gemini 建议，未逐一实测。
- **混音红线**：生成源头写 voiceover-friendly / sparse arrangement / no lead melody，
  给解说镂空中频；后期 BGM 压到人声下约 20dB；口播下无强主旋律；插播时 ducking
  让位（社区常见值 -18~-22dB / release 200–300ms）。
- **工作流**：音乐先行（按鼓点卡点）vs 画面先行（转场时间点写进提示词——国内
  自然语言工具；国际工具改写为结构框元标签）；长视频分段生成；结尾干脆收住。
- **参考生成**：喜欢的曲子拖给音乐工具，要求「同乐器/律动/情绪的原创，不照搬旋律」。

## 一分钟示例（八段公式 · 国内版格式）

> ① 科技产品宣传片，产品特写镜头 ② 60 秒 ③ 前段克制渐紧，亮相一秒明亮打开
> ④ A 小调起步，亮相转 C 大调 ⑤ 96 BPM ⑥ 合成器 pad + 少量钢琴
> ⑦ 第 22 秒一个重音，随后进入主段落 ⑧ 不要人声，不要突然的鼓点

## Examples

6 个场景(悬疑 / 治愈 / 旅行 vlog / 古风 / 带货 / 科技宣传片)的示例音频,现状三分支:

**① MiniMax API(暂不可用,已存档)**:2026-10-19 真实调用时,MiniMax 音乐生成付费接口
已按其 [服务调整通知](https://platform.minimax.cn/docs/guides/music-generation)
自 2026-08-20 起停止面向新账号服务(HTTP 410 / status_code 2153),故暂无 API 音频成品。
调用脚本([generate.py](examples/minimax/generate.py),目标模型 MiniMax music-3.0,
`is_instrumental` 纯音乐)与双版本提示词已存档于
[`examples/minimax/`](examples/minimax/PROMPTS.md),未来账号可用或改用开源
MiniMax-Music3 时可直接复用。

**② Suno 实例 ×6(用户实测,可点开试听)**:示例音频由用户 2026-10-19 在 Suno 用本仓
**国际版提示词**生成;在线试听开放,mp3 下载需 Suno 订阅,故仓库内以链接形式提供:

- 01 悬疑:https://suno.com/s/05x9AkMJ9Krw93im
- 02 治愈:https://suno.com/s/76DnjBrQWeTLCpAp
- 03 旅行 vlog:https://suno.com/s/pINxP6ETpYrRcBWf
- 04 古风:https://suno.com/s/jPH4B3LJF4oMlgHZ
- 05 带货:https://suno.com/s/Ud8WU5QS1GwzQOjq
- 06 科技宣传片:https://suno.com/s/GmKbmIXJO9lxKrax

**③ 本地生成**:任选一个 AI 音乐工具(Suno / 豆包 / 海绵音乐等),配合仓内提示词自行
生成。6 个场景的**三写法提示词**——八段公式逐项填写 + 国际版英文 Style 串 +
国内版中文自然段——见 [`examples/minimax/PROMPTS.md`](examples/minimax/PROMPTS.md)。

## 来源与致谢

- 方法论提炼自一位内容创作者的公开视频教程（微信视频号）：
  [原视频](https://channels.weixin.qq.com/finder-preview/pages/sph?id=AUXFh7vKWT)。
  本仓库的结构与措辞已重构，情绪开关排序、BPM 区间、八大类配方等**核心口径归功于原作者**——
  如果你觉得这个 skill 有用，请先给原作者点赞关注。
- 本次迭代（双框解耦、双版本输出、源头中频镂空、自适应缺省、进阶能量曲线）
  采纳了 Gemini 的优化建议，经人工审核后落地。

## 声明

- 音乐心理学排序与参数为该教程口径，**未经我们实验室复核**——最终以听感为准。
- 进阶小节为 Gemini 提出的优化建议，未逐一实测；双框/元标签、ducking 参数等为
  社区常见工程口径——同样以实际听感为准。
- 版权：AI 生成音乐的商用条款请阅读所用平台的用户协议；参考生成只借鉴风格，不照搬旋律。
- License: MIT
