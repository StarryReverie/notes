# 工作流：复习与记录

## 触发条件

用户提供课程资料（通常在 `.resources/` 目录下），要求复习特定主题并记录笔记。

## 步骤

### 1. 确定主题与资料

在 `.resources/` 目录下找到对应的课程资料文件。确认用户要复习的章节范围和目标笔记文件（已有文件则追加，不存在则新建）。

### 2. 知识框架梳理

根据资料列出该章节的知识框架（主题列表），让用户选择：

- 按顺序逐个推进
- 挑选薄弱环节优先复习

### 3. 对话式复习

按主题逐个进行交互式复习：

- 让用户用自己的话表达对当前主题的理解
- Agent 纠正错误、补充遗漏、追问不清晰的部分
- 每个主题完成后，询问用户是否可以写入笔记
- Agent 不主动将对话中的解答写入笔记，需等用户确认

要求：对话简短、反馈快，避免长篇大论。

### 4. 整理写入笔记

用户确认后，Agent 将复习内容按以下规范整理写入笔记文件：

- `agents/specifications/notes/` 下的内容结构规范
- `agents/styles/writing-style.md` 中的写作风格

写入后展示给用户确认。

### 5. 用户修正

用户可能直接修改文件内容。Agent 读取 `git diff`，总结用户修改了什么、与 Agent 生成的版本有什么不同。

### 6. 风格归纳

根据用户的修改差异，触发 `update-writing-style` 工作流，将新的风格偏好归纳到 `agents/styles/writing-style.md`。

### 7. 合规验证

触发 `validate-note` 工作流，检查修改后的笔记是否符合规范。

### 8. 提交

用户确认内容无误后提交。提交信息使用单行描述性格式，不包含 body。

## 参考规范

- `agents/specifications/notes/content-structure.md`
- `agents/specifications/notes/frontmatter.md`
- `agents/specifications/notes/naming.md`
- `agents/styles/writing-style.md`
- `agents/workflows/update-writing-style.md`
- `agents/workflows/validate-note.md`
