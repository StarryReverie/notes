# 链接规范

## 内部链接格式

站内笔记之间的链接使用 Hugo 的路径引用格式：

```text
[显示文本](/docs/学科/课程/文件名)
```

示例：

- `[函数](/docs/mathematics/calculus/function)`
- `[矩阵相似](/docs/mathematics/linear-algebra/similar-matrix)`
- `[线程](/docs/computer-science/operating-system/thread)`

### 规则

- 路径以 `/docs/` 开头
- 路径中不包含文件扩展名 `.md`
- 路径中使用 kebab-case（与目录和文件命名一致）
- 显示文本为中文

## 锚点链接

### 创建锚点

使用 `<span id="..."></span>` 在需要被链接的条目行末创建锚点：

```markdown
- **电场强度** <span id="dkqgis"></span>
```

锚点 ID 规则：

- 6 个字符的随机字母组合
- 仅使用小写字母 `[a-z]`
- 全仓库内唯一

### 引用锚点

```text
[显示文本](/docs/学科/课程/文件名#锚点ID)
```

示例：

- `[等价关系](/docs/mathematics/discrete-mathematics/binary-relationship#zwakul)`

## 链接完整性

- 所有内部链接的目标文件必须存在
- 所有锚点链接的锚点 ID 必须在目标文件中存在
- 不允许指向不存在路径的死链

## 禁止事项

- 不使用裸 URL 链接到站内内容（应使用上述路径引用格式）
- 不使用相对路径引用（应使用以 `/docs/` 开头的绝对路径）
- 外部链接（指向本站之外）使用完整 URL

## 合规判定

以下情况判定为不合规：

- 内部链接目标文件不存在
- 锚点 ID 在目标文件中不存在
- 内部链接使用了 `.md` 扩展名
- 内部链接使用了相对路径
- 锚点 ID 不是 6 字符小写字母
- 锚点 ID 在仓库内重复
