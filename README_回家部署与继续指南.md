# 《剑烛大荒·幻梦》v8 终极提示词 & 五大通用 AI 影视技能 回家交接包指南

---

## 一、 交接包目录结构一览

```text
幻梦_v8与五大AI制片技能_回家交接包/
├── install_skills_at_home.ps1                # 【一键脚本】回家后右键用 PowerShell 运行，自动安装五大全局 Skill
├── README_回家部署与继续指南.md               # 本说明文档
│
├── 01_五大通用AI影视全局技能 (skills)/         # 100% 通用、模块化解耦的五大专业 Skill
│   ├── ai-cinematography-shot-design/        # 模块一：2D 科班镜头设计、景别漏斗、前景纵深与八大无缝转场
│   │   └── SKILL.md
│   ├── ai-video-audio-montage/               # 模块二：全链路音频工程、干声多状态矩阵、禁BGM与J/L-Cut声画蒙太奇
│   │   └── SKILL.md
│   ├── seedance-video-director/              # 模块三：2D 母脸原位衍生、单首帧85%防叠化、动词链与局部涂抹精修
│   │   └── SKILL.md
│   ├── blender-white-model-controller/       # 模块四（按需）：Blender 3D 白模防木头人三档法则、三帧验视与三层提示词
│   │   └── SKILL.md
│   └── google-flow-veo-director/             # 模块五（按需）：Google Flow Veo 3.1 权重前置五段式与光学脱敏词表
│       └── SKILL.md
│
├── 02_核心投产提示词与方法论文档/
│   ├── 幻梦_v8_终极投产提示词全集.md          # ★【核心主文件】全片35镜终极首帧+视频词+第二幕打包测试词+转场精修定稿
│   ├── 幻梦_完整剧情与分镜_v7.md              # 分镜文学与视听剧本定稿
│   ├── AI_FILM_MASTER_METHODOLOGY.md         # 通用 AI 影视工业化制片总方法论（五大模块全景速查）
│   ├── BLENDER_SEEDANCE_WHITE_MODEL_GUIDE.md # Blender + Seedance 2.0/2.5 白模全流程通用实战手册
│   ├── JIMENG_BLENDER_PLUGIN_SOP.md          # 即梦 Blender 预览上传插件安装与实操 SOP
│   ├── 丁轻烟_季寒衣_人物全景传记.md          # 人物深度小传与心理弧光档案
│   └── 剑烛大荒_第一卷_人物全景与场景美学档案.md
│
└── 03_已锁定角色视觉资产库 (assets_characters)/
    ├── CHAR-01_JiHanyi_DingQingyan.jpg       # 季寒衣 / 丁轻烟 基准设定图
    ├── CHAR-01_JiHanyi_3Expressions_Sheet.jpg# 三表情神态基准卡（俏皮 / 戏谑 / 镜中真笑）
    ├── CHAR-01_FaceA_DingQingyan_Playful.jpg # 裁切单图 A：丁轻烟灵动俏皮态（遵循“拆单图上传”原则）
    ├── CHAR-01_FaceB_JiHanyi_Teasing.jpg     # 裁切单图 B：季寒衣妖女戏谑态
    ├── CHAR-01_FaceC_Mirror_TrueSmile.jpg    # 裁切单图 C：终幕银镜干净真笑态
    ├── CHAR-03_LiuYuzao_QiXiaoxiang.jpg      # 刘玉藻 / 齐潇湘 角色设定图
    ├── CHAR-07_QiuChen_DingShengyi.jpg       # 邱辰 / 假爹丁胜意 角色设定图
    └── turnaround_candidates/                # 季寒衣多视图衍生候选图集
```

---

## 二、 回家后 1 分钟快速恢复环境步骤

### 第 1 步：一键安装五大全局 Skill 到家里电脑
1. 解压本压缩包到任意工作目录（例如 `D:\AImovie\qingyan`）。
2. 双击或使用 PowerShell 运行根目录下的 **`install_skills_at_home.ps1`**，或者手动将 `01_五大通用AI影视全局技能 (skills)` 文件夹下的 **5 个子文件夹** 复制到家里电脑的以下路径：
   ```text
   C:\Users\<你家电脑的用户名>\.gemini\config\skills\
   ```
3. 复制完成后，家里电脑的 Antigravity Agent 就会自动拥有这 5 个全局技能！

### 第 2 步：（可选）如果家里电脑装了 Blender，一键装上即梦上传插件
* 原工作区目录下的 `jimeng_blender_uploader-windows-cn-2.0.0.zip`（约 50MB）可在 Blender 的 `编辑 -> 偏好设置 -> 插件 -> 从磁盘安装` 中直接选中 ZIP 安装并勾选启用，详细操作见 `02_核心投产提示词与方法论文档/JIMENG_BLENDER_PLUGIN_SOP.md`。

### 第 3 步：直接打开 `幻梦_v8_终极投产提示词全集.md` 开工投产
* **优先测试**：打开 `幻梦_v8_终极投产提示词全集.md` 的 **「第二幕｜歧路」** 章节，复制里面的 **【合并测试方案一：12s+15s 双人交叉快切包】** 或 **【合并测试方案二：15s+13s 单角色五连镜包】**，挂载 `03_已锁定角色视觉资产库` 中的单人高清图，在即梦 `Seedance 2.5 -> 全能参考` 中直接测试多镜合一效果！
* **第一幕投产**：按 `Shot 01 -> Shot 02 -> Shot 03 -> Shot 04` 顺序生成首帧与视频（注意 `Shot 03` 空饭桌首帧直接拿 `Shot 02` 结尾的全家围坐尾帧做原位改图，实现 100% 零帧差原机位瞬间消失重击）。
