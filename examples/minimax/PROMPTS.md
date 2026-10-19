# MiniMax music-3.0 示例 —— 提示词存档与调用记录

6 段场景示例,全部按本仓 [SKILL.md](../../SKILL.md) 方法论编写:每段给出
**八段公式**(方法论模板逐项填写)、**国际版**(英文 Style 串,适配 Suno 类
工具)与**国内版**(中文自然段,适配 MiniMax 等官方示例口径)三种写法。

> **Suno 实例(2026-10-19,用户实测)**:下方 01~06 每段末尾附一条 Suno 在线试听链接。
> 示例音频由用户在 Suno 用本仓**国际版**提示词生成;在线试听开放、mp3 下载需 Suno 订阅,
> 故仓库内以链接形式提供,不附带音频文件。

> **调用结果(2026-10-19,如实记录):首次真实调用即被拒**
> - 端点:`POST https://api.minimax.cn/v1/music_generation`,`model:"music-3.0"`,`is_instrumental:true`
> - 返回:**HTTP 410**,`status_code: 2153`,「This Music API is no longer available to new users. Existing paying customers can continue to use the service.」
> - 即官方文档「服务调整通知」所述:自 2026-08-20 起,音乐生成付费接口不再面向新账号提供服务。
> - 处置:按预案**立即停止,未重试、未换参数绕过**。以下 6 段提示词保留存档
>   (方法论示范 + 未来可用的账号/开源模型口径),**实际时长均为空,0 段音频产出**。
> - 替代路径(官方指引):MiniMax Audio 网页版,或 Hugging Face / ModelScope 上的
>   开源 MiniMax-Music3 模型;提示词可直接复用下方国内版自然段。

完整 API 请求/响应字段见 [manifest.json](manifest.json)。生成脚本:
[generate.py](generate.py)(key 仅从环境变量 `MINIMAX_TOKEN` 读取,不落盘)。

---

## 01 悬疑 suspense

- **八大类配方**:悬疑 —— 慢速 + 持续低音(drone)+ 少量散落的不协和音
- **八段公式**
  1. 用途和画面:悬疑短片/调查段落 BGM,画面是昏暗走廊、翻找线索的特写
  2. 时长:15
  3. 情绪:不安、压抑、越听越紧
  4. 调性:A 小调
  5. 速度和拍子:60 BPM,4/4
  6. 乐器:低音提琴长音 + 细碎弦乐高音点缀
  7. 结构和时间点:低音一个音从头到尾不动,上方和弦变化;第 8 秒出现一次不协和高音
  8. 负面清单:不要人声、不要鼓点、不要明亮大调和声、结尾干净收住不拖尾
- **国际版**:`15-second suspense film underscore. A minor, 60 BPM, slow and heavy. A single low drone bass note holds from start to end while the chords above it change; sparse high strings play a few scattered dissonant notes, one around the 8th second. Dark, uneasy, quietly tense. No vocals, no drums, no bright major harmony. Clean abrupt ending, no tail ring-out.`
- **国内版(实际调用 prompt)**:`一首 15 秒的悬疑短片配乐,A 小调,60 BPM 慢速。最低音是一个持续低音,从头到尾保持同一个音不动,上方和弦在其上缓慢变化;细碎的弦乐高音散落几个不协和音,第 8 秒出现一次刺耳的不协和高音。整体昏暗、压抑,越听越不安。不要人声,不要鼓点,不要明亮的大调和声,结尾干净地收住,不要拖尾。`
- **实际时长**:无(HTTP 410 拦截,未生成)
- **Suno 实例(用户实测)**:https://suno.com/s/05x9AkMJ9Krw93im

## 02 治愈 healing

- **八大类配方**:治愈 —— 慢速,毛毡钢琴 + 轻打击乐 + 一点和弦铺垫
- **八段公式**
  1. 用途和画面:治愈系短片/日常记录 BGM,画面是清晨阳光、慢镜头生活片段
  2. 时长:15
  3. 情绪:温暖、柔软、安心
  4. 调性:C 大调
  5. 速度和拍子:72 BPM,4/4
  6. 乐器:毛毡钢琴为主,轻打击乐(指镲/沙锤)点缀,弦乐长音轻铺
  7. 结构和时间点:钢琴柔和分解和弦进入,第 6 秒轻打击乐加入,结尾渐弱收住
  8. 负面清单:不要人声、不要鼓组、不要快节奏、不要戏剧化起伏、结尾干净
- **国际版**:`15-second healing BGM. C major, 72 BPM, slow. Soft felt piano playing gentle broken chords, light percussion (shaker, soft cymbal tick) joining around the 6th second, warm string pads underneath. Tender, cozy, reassuring; high notes played softly. No vocals, no drum kit, no dramatic builds. Ends with a gentle fade to a clean stop.`
- **国内版(实际调用 prompt)**:`一首 15 秒的治愈系背景音乐,C 大调,72 BPM 慢速。毛毡钢琴弹柔和的分解和弦,第 6 秒加入轻打击乐(沙锤和很轻的镲),底下铺一层温暖的弦乐长音。整体柔软、安心,高音轻奏。不要人声,不要鼓组,不要戏剧化的情绪起伏,结尾轻轻渐弱、干净收住。`
- **实际时长**:无(未调用,见顶部调用记录)
- **Suno 实例(用户实测)**:https://suno.com/s/76DnjBrQWeTLCpAp

## 03 旅行 vlog

- **八大类配方**:旅行 vlog —— 大调 + 118 BPM + 尤克里里 + 轻打击乐
- **八段公式**
  1. 用途和画面:旅行 vlog BGM,画面是海边公路、日出、徒步镜头快剪
  2. 时长:15
  3. 情绪:轻快、阳光、自由
  4. 调性:C 大调
  5. 速度和拍子:118 BPM,4/4
  6. 乐器:尤克里里扫弦为主,轻打击乐(拍手/沙锤)+ 木吉他
  7. 结构和时间点:尤克里里扫弦直接进入,节奏从头到尾保持轻快,结尾干净收在一拍上
  8. 负面清单:不要人声、不要电吉他失真、不要沉重低音、不要慢速段落
- **国际版**:`15-second travel vlog BGM. C major, 118 BPM, bouncy and sunny. Ukulele strumming carries the groove from the very first beat, light handclaps and shaker, acoustic guitar accents. Bright, free, feel-good. No vocals, no distorted electric guitar, no heavy bass, no slow section. Clean ending on the beat.`
- **国内版(实际调用 prompt)**:`一首 15 秒的旅行 vlog 背景音乐,C 大调,118 BPM。尤克里里扫弦从第一拍就直接进入并贯穿全曲,配上轻轻的拍手和沙锤,木吉他在空隙点缀。整体阳光、轻快、自由。不要人声,不要失真电吉他,不要沉重的低音,不要慢下来的段落,结尾在一拍上干净收住。`
- **实际时长**:无(未调用,见顶部调用记录)
- **Suno 实例(用户实测)**:https://suno.com/s/pINxP6ETpYrRcBWf

## 04 古风

- **八大类配方**:古风 —— 五声音阶 + 古筝
- **八段公式**
  1. 用途和画面:古风短视频 BGM,画面是山水庭院、汉服人像慢镜
  2. 时长:15
  3. 情绪:雅致、婉转、意境悠远
  4. 调性:D 宫五声音阶(宫商角徵羽)
  5. 速度和拍子:76 BPM,4/4,中慢速
  6. 乐器:古筝主奏(带滑音),竹笛轻和,少量弦乐铺底
  7. 结构和时间点:古筝分解引入,第 7 秒竹笛进入一句,结尾古筝刮奏后干净收住
  8. 负面清单:不要人声、不要西洋流行鼓组、不要电子音色、不要强拍重音
- **国际版**:`15-second Chinese traditional (guofeng) BGM. D pentatonic scale (gong mode), 76 BPM, moderate-slow. Guzheng leads with ornaments and gentle slides (glissando), bamboo flute (dizi) enters softly around the 7th second for one phrase, soft string pad underneath. Elegant, flowing, poetic. No vocals, no western pop drum kit, no electronic timbres, no heavy accents. Ends after a short guzheng sweep with a clean stop.`
- **国内版(实际调用 prompt)**:`一首 15 秒的古风背景音乐,D 宫五声音阶,76 BPM 中慢速。古筝主奏,带装饰音和轻柔的滑音,第 7 秒竹笛轻轻进入吹一句,底下铺少量弦乐长音。整体雅致、婉转、意境悠远。不要人声,不要西洋流行鼓组,不要电子音色,不要强拍重音,结尾古筝一小段刮奏后干净收住。`
- **实际时长**:无(未调用,见顶部调用记录)
- **Suno 实例(用户实测)**:https://suno.com/s/jPH4B3LJF4oMlgHZ

## 05 带货 selling

- **八大类配方**:带货 —— 128 BPM + 器乐合奏 + 节奏清晰
- **八段公式**
  1. 用途和画面:电商带货短视频 BGM,画面是产品特写、卖点字幕快切
  2. 时长:15
  3. 情绪:明快、有推进感、节奏抓耳
  4. 调性:C 大调
  5. 速度和拍子:128 BPM,4/4
  6. 乐器:器乐合奏:明亮电钢琴 + 贝斯 + 紧凑鼓组 + 拍手,清晰的四踩点节奏
  7. 结构和时间点:节奏组一进来就满律动,全程保持能量不掉,结尾干净收在重拍
  8. 负面清单:不要人声、不要慢速段落、不要模糊松散的节奏、不要长前奏
- **国际版**:`15-second e-commerce selling BGM. C major, 128 BPM, energetic and driving. Bright electric piano, punchy bass, tight drum groove with clear four-on-the-floor beat and handclaps, small instrumental ensemble. Full energy from the first beat, no intro build-up. No vocals, no slow section, no loose rhythm. Clean stop on a downbeat.`
- **国内版(实际调用 prompt)**:`一首 15 秒的电商带货短视频背景音乐,C 大调,128 BPM。器乐合奏:明亮的电钢琴、有弹性的贝斯、紧凑的鼓组和拍手声,四踩点节奏清晰抓耳。节奏组从第一拍进来就是满律动,全程能量不掉,不要前奏铺垫。不要人声,不要慢速段落,不要松散模糊的节奏,结尾在重拍上干净收住。`
- **实际时长**:无(未调用,见顶部调用记录)
- **Suno 实例(用户实测)**:https://suno.com/s/Ud8WU5QS1GwzQOjq

## 06 科技宣传片 tech promo

- **八大类配方**:宣传片 —— 小调起步、张力渐强、产品出现瞬间转亮(重音/转调)
- **八段公式**
  1. 用途和画面:科技产品宣传片 BGM,画面是暗色产品特写,后半产品点亮、LOGO 出现
  2. 时长:15
  3. 情绪:前段冷静有张力,后段明亮有力量
  4. 调性:A 小调起步,第 8 秒转 A 大调亮色
  5. 速度和拍子:112 BPM,4/4
  6. 乐器:合成器为主:低音脉冲 + 弦乐式合成 pad,后段加明亮合成 lead
  7. 结构和时间点:A 小调低音脉冲起,张力渐强;第 8 秒一个重音同时转大调,亮度打开,结尾干净收住
  8. 负面清单:不要人声、不要松弛懒散的律动、不要爵士和声、结尾不拖尾
- **国际版**:`15-second tech product promo BGM. Starts in A minor, 112 BPM: pulsing synth bass and tense string-style pads, tension building. Right on the 8th second, one accented hit and the harmony turns to A major — the sound opens up bright and powerful, bright synth lead joins. No vocals, no loose laid-back groove, no jazz harmony. Clean ending, no tail.`
- **国内版(实际调用 prompt)**:`一首 15 秒的科技产品宣传片配乐,112 BPM。A 小调起步:合成器低音脉冲加有张力的弦乐式 pad,情绪逐渐推强;正好在第 8 秒一个重音落下,和声转到 A 大调,声音瞬间打开变亮变有力,明亮的合成 lead 进入。前段冷静克制,后段明亮昂扬。不要人声,不要松弛懒散的律动,不要爵士和声,结尾干净收住不拖尾。`
- **实际时长**:无(未调用,见顶部调用记录)
- **Suno 实例(用户实测)**:https://suno.com/s/GmKbmIXJO9lxKrax

---

## 口径自检

各段调式/BPM/乐器与 SKILL.md 八大类配方逐条对齐:悬疑(小调慢速+drone)、
治愈(慢速钢琴+轻打击乐)、旅行(大调 118 尤克里里)、古风(五声音阶古筝)、
带货(128 器乐合奏)、宣传片(小调起步转亮+重音节点)。每段均含负面清单、
时长为数字、结尾干净收住,符合八段公式与「结尾不要拖尾」规范。
