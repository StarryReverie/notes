# 工作流：预处理课程资料

## 触发条件

用户提供课程资料文件（docx、pptx、pdf），需要提取和整理其中的文本内容，用于后续交互式笔记整理。

## 步骤

### 1. 初始化

检查 `.resources/` 目录是否存在，不存在则创建。检查 `.resources/.gitignore` 是否存在且内容为忽略所有文件（`*`），不存在则创建。

### 2. 转换资源为原始纯文本

将资源文件路径传给转换 Subagent，由其执行以下操作：

- 根据文件扩展名选择转换脚本：
    - `.docx` → `agents/scripts/convert-docx-to-md.py`
    - `.pptx` → `agents/scripts/convert-pptx-to-md.py`
    - `.pdf` → `agents/scripts/convert-pdf-to-md.py`
- 使用 Python 执行脚本（优先直接使用 `python`，其次尝试 `uv run`），输出保存为 `.resources/{basename}.raw.md`
- 对于 PDF 文件，先以默认文本模式提取，检查结果是否稀疏（大量空白、字符极少）。若稀疏则以 `--ocr` 模式重新提取并覆盖 `.raw.md`。由于 Subagent 仅负责转换，Subagent 应当尽量避免读取直接转换结果，以提高效率。
- 返回 `.raw.md` 文件路径

### 3. 分段整理原始纯文本

整理 Subagent 必须遵守以下约束：

- **禁止编写或运行任何脚本**，必须直接读取原始文本、在脑中分析整理、用 Write 工具写出结果
- **严格只读取被分配的行范围**，使用 Read 工具的 `offset` 和 `limit` 参数精确限定读取区域，绝不允许跨区域读取

#### 3.1 分段

根据 `.raw.md` 文件大小决定是否分段：

- 文件 ≤ 1500 行：不分段，单次处理
- 文件 > 1500 行：扫描内容寻找自然章节边界（如重复出现的目录页、主题切换点），按章节分为若干段，每段不超过 1500 行。在 `.resources/.parts/` 目录下创建 `part1.md`、`part2.md`、... 分别存放各段整理结果

#### 3.2 整理操作

每个整理 Subagent 仅被传入其负责的行范围，执行以下操作：

- 去噪：移除幻灯片元数据（课程名、页码、页眉页脚）、图片引用残留、重复内容
- 重连断行：将被换行打断的段落重新连接
- 重建结构：识别章节层次，使用 Markdown 标题和列表重建文档结构
- 修复公式：将退化的数学符号还原为 LaTeX 公式
- 整理表格：将破碎的表格数据重建为 Markdown 表格

#### 3.3 并行执行

若分为多段，各段整理 Subagent 可并行启动。全部完成后，主 Agent 将各段按顺序拼接为 `.resources/{basename}.md`。

### 4. 返回结果

返回 `.md` 文件路径给主 Agent。

## 参考规范

- `agents/scripts/convert-docx-to-md.py`
- `agents/scripts/convert-pptx-to-md.py`
- `agents/scripts/convert-pdf-to-md.py`
