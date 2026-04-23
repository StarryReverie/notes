# 工作流：验证笔记合规性

## 触发条件

修改、新增、重命名或移动 `content/docs/` 下的笔记文件后，需要验证相关笔记是否符合规范。

## 步骤

### 1. 确定变更范围

必须执行 `git diff` 获取实际变更，不得依赖缓存的变更信息。仅当用户显式指定文件列表时可跳过 `git diff`。确定 `content/docs/` 下的变更文件列表，将变更分为两类：

- 受影响文件：本次新增、修改、重命名的笔记文件及 `_index.md`
- 受关联文件：使用 Grep 等工具在仓库中搜索引用了受影响文件路径的笔记，确保结果基于实际文件内容而非推断

未涉及的文件默认不需要重新检查。

### 2. 检查文件名与目录结构

启动 Subagent，仅对受影响文件执行以下检查：

- 对照 `specifications/notes/naming.md` 检查文件名和目录名格式
- 对照 `specifications/notes/directory-structure.md` 检查三级层次结构、`_index.md` 存在性

### 3. 检查 Frontmatter 与内容结构

启动 Subagent，仅对受影响文件执行以下检查：

- 对照 `specifications/notes/frontmatter.md` 检查必选字段、类型、顺序、无未定义字段
- 对照 `specifications/notes/content-structure.md` 检查缩进、列表标记、无标题标记、锚点放置

### 4. 检查链接与锚点

启动 Subagent，仅对受影响文件和受关联文件执行以下检查：

- 对照 `specifications/notes/linking.md` 检查内部链接格式、目标文件存在性
- 检查锚点 ID 格式（6 字符小写字母）和仓库内唯一性

### 5. 汇总报告

合并各 Subagent 的结果，按文件分组输出合规/不合规条目。

## 参考规范

- `specifications/notes/naming.md`
- `specifications/notes/directory-structure.md`
- `specifications/notes/frontmatter.md`
- `specifications/notes/content-structure.md`
- `specifications/notes/linking.md`
