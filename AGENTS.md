# AGENTS.md

本仓库是一个笔记集合网站的源代码仓库，基于 Hugo + Hextra 主题构建。

详细规范和工作流定义在 `agents/` 目录下。

- `specifications/`：必须遵守的确定性规范，可机械判定是否符合
    - `meta/`：agents 文档自身的规范
        - [spec-structure.md](agents/specifications/meta/spec-structure.md)：Specification 文件的内容结构规范
        - [workflow-structure.md](agents/specifications/meta/workflow-structure.md)：Workflow 文件的内容结构规范
        - [file-organization.md](agents/specifications/meta/file-organization.md)：agents 文档的文件组织规则
        - [cross-referencing.md](agents/specifications/meta/cross-referencing.md)：跨文件引用的维护规则
        - [markdown-style.md](agents/specifications/meta/markdown-style.md)：Markdown 文件 lint 规则
    - `notes/`：笔记内容相关的规范
        - [frontmatter.md](agents/specifications/notes/frontmatter.md)：Frontmatter 字段定义、类型、默认值
        - [naming.md](agents/specifications/notes/naming.md)：文件和目录命名规则
        - [linking.md](agents/specifications/notes/linking.md)：内部链接和锚点格式
        - [directory-structure.md](agents/specifications/notes/directory-structure.md)：目录结构约定
        - [content-structure.md](agents/specifications/notes/content-structure.md)：笔记内容的确定性结构规则
