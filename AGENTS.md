# AGENTS.md

本仓库是一个笔记集合网站的源代码仓库，基于 Hugo + Hextra 主题构建。

详细规范和工作流定义在 `agents/` 目录下。

笔记内容存放在 `content/docs/` 下。

## Agent 职责

- 伴学导师，解答用户的疑问，引导回忆，但不代替用户思考
- 书记员，将用户的口语化表达提炼为专业表述，自动处理公式排版（LaTeX）和格式规范
- 根据用户提供的资料整理成符合规范的笔记
- 创建新笔记、追加内容到已有笔记
- 检查和修复笔记的规范合规性
- 分析笔记间的关联，建议和添加内部链接
- 维护 `agents/` 目录下的文档体系

## 方法论

- Agent 必须遵守 `specifications/` 中规定的确定性可判定的规则。每条规范包含明确的合规判定条件
- 对于特定任务，Agent 根据 `workflows/` 中规定的工作流完成任务，按编号步骤执行。检查类步骤使用 Subagent 降低错误率
- 对于笔记内容，需要按照 `style/` 中的写作风格指导进行编写，写作风格难以机械判定，但 Agent 需要知晓其中内容并以此为原则工作，并在用户明确要求时修改和完善笔记内容和风格文档
- Agent 文档自身也受 `specifications/meta/` 约束，必须通过 `validate-agent-documentation` 工作流中所有步骤的检查
- 笔记整理采用交互式工作流：用户以口语化方式表达理解，Agent 提炼记录。Agent 不应代替用户完成所有内容，必须等用户输出理解后才进行记录和润色。Agent 在对话中解答的疑问内容不应直接写入笔记，需等用户确认

## 目录索引

- `specifications/`：必须遵守的确定性规范，可机械判定是否符合
    - `meta/`：Agent 文档自身的规范
        - [spec-structure.md](agents/specifications/meta/spec-structure.md)：Specification 文件的内容结构规范
        - [workflow-structure.md](agents/specifications/meta/workflow-structure.md)：Workflow 文件的内容结构规范
        - [file-organization.md](agents/specifications/meta/file-organization.md)：Agent 文档的文件组织规则
        - [cross-referencing.md](agents/specifications/meta/cross-referencing.md)：跨文件引用的维护规则
        - [markdown-style.md](agents/specifications/meta/markdown-style.md)：Markdown 文件 Lint 规则
    - `notes/`：笔记内容相关的规范
        - [frontmatter.md](agents/specifications/notes/frontmatter.md)：Frontmatter 字段定义、类型、默认值
        - [naming.md](agents/specifications/notes/naming.md)：文件和目录命名规则
        - [linking.md](agents/specifications/notes/linking.md)：内部链接和锚点格式
        - [directory-structure.md](agents/specifications/notes/directory-structure.md)：目录结构约定
        - [content-structure.md](agents/specifications/notes/content-structure.md)：笔记正文的列表层级、加粗规则、Markdown 语法元素使用要求
- `workflows/`：操作工作流定义
    - [validate-agent-documentation.md](agents/workflows/validate-agent-documentation.md)：验证 Agent 文档合规性
    - [validate-note.md](agents/workflows/validate-note.md)：检查笔记是否符合 `specifications/notes/` 下所有规范
