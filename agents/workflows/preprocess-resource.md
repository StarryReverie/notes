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
- 使用 `uv run` 执行脚本，输出保存为 `.resources/{basename}.raw.md`
- 对于 PDF 文件，先以默认文本模式提取，检查结果是否稀疏（大量空白、字符极少）。若稀疏则以 `--ocr` 模式重新提取并覆盖 `.raw.md`。由于 Subagent 仅负责转换，Subagent 应当尽量避免读取直接转换结果，以提高效率。
- 返回 `.raw.md` 文件路径

### 3. 整理原始纯文本

将 `.raw.md` 路径传给整理 Subagent，由其执行以下操作：

- 去噪：移除幻灯片元数据（课程名、页码、页眉页脚）、图片引用残留、重复内容
- 重连断行：将被换行打断的段落重新连接
- 重建结构：识别章节层次，使用 Markdown 标题和列表重建文档结构
- 修复公式：将退化的数学符号还原为 LaTeX 公式
- 整理表格：将破碎的表格数据重建为 Markdown 表格
- 将整理结果保存为 `.resources/{basename}.md`
- 返回 `.md` 文件路径

### 4. 完整性校验

将 `.raw.md` 和 `.md` 路径传给独立的校验 Subagent，由其执行以下操作：

- 对比两个文件，检查是否有实质性内容丢失（排除已清理的噪声）
- 检查公式和关键术语是否完整保留
- 若发现问题，返回具体的修正意见

主 Agent 收到校验结果后，若有修正意见则传回整理 Subagent 执行修正，修正后重新校验，直到校验通过或用户确认可接受。

### 5. 返回结果

返回 `.md` 文件路径给主 Agent。

## 参考规范

- `agents/scripts/convert-docx-to-md.py`
- `agents/scripts/convert-pptx-to-md.py`
- `agents/scripts/convert-pdf-to-md.py`
