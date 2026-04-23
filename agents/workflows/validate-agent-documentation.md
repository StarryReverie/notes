# 工作流：验证 agent 文档合规性

## 触发条件

修改、新增、重命名或移动 `agents/` 目录下的文件后，需要验证所有 Agent 文档是否符合规范。

## 步骤

### 1. 确定变更范围

必须执行 `git diff` 获取实际变更，不得依赖缓存的变更信息。仅当用户显式指定文件列表时可跳过 `git diff`。确定变更文件列表，将变更分为两类：

- 受影响文件：本次新增、修改、重命名的文件
- 受关联文件：使用 Grep 等工具在仓库中搜索引用了受影响文件路径的文档，确保结果基于实际文件内容而非推断

未涉及的文件默认不需要重新检查。

### 2. 检查文件组织与结构

启动 Subagent，仅对受影响文件执行以下检查：

- 对照 `specifications/meta/file-organization.md` 检查文件组织
- 对照 `specifications/meta/spec-structure.md` 检查每个 Specification 文件结构
- 对照 `specifications/meta/workflow-structure.md` 检查每个 Workflow 文件结构
- 检查受影响文件是否在 `AGENTS.md` 中被索引
- 检查 `AGENTS.md` 中无指向不存在文件的索引条目

### 3. 检查交叉引用与 markdown 风格

启动 Subagent，仅对受影响文件和受关联文件执行以下检查：

- 对照 `specifications/meta/cross-referencing.md` 验证相关文件中的相对路径链接
- 对照 `specifications/meta/markdown-style.md` 检查受影响文件的 Markdown 风格

### 4. 汇总报告

合并各 Subagent 的结果，按文件分组输出合规/不合规条目。

## 参考规范

- `specifications/meta/spec-structure.md`
- `specifications/meta/workflow-structure.md`
- `specifications/meta/file-organization.md`
- `specifications/meta/cross-referencing.md`
- `specifications/meta/markdown-style.md`
