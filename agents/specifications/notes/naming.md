# 命名规范

## 文件命名

### 笔记文件（非 `_index.md`）

- 使用英文、kebab-case 格式
- 后缀为 `.md`
- 文件名应能反映笔记内容对应的英文术语
- 多词术语用 `-` 连接

示例：

- `differential-equation.md` → `微分方程`
- `linear-algebra.md` → `线性代数`
- `first-order-differential-equation.md` → `一阶微分方程`
- `os-introduction.md` → `OS 概论`

### `_index.md`

- 每个内容目录必须包含一个 `_index.md`
- `_index.md` 是 Hugo 的分支 bundle 入口
- 其 `title` 字段为该目录的中文名称

## 目录命名

- 使用英文、kebab-case 格式
- 目录名对应学科或课程的英文名称

现有学科目录：

- `mathematics`
- `computer-science`
- `physics`

现有课程目录示例：

- `calculus`（微积分）
- `linear-algebra`（线性代数）
- `operating-system`（操作系统）
- `electromagnetism`（电磁学）

## 文件名与 title 的映射

文件名是英文 kebab-case，`title` 是中文名称。两者使用不同的命名体系，不需要字面对应。

示例：

| 文件名 | title |
| ------ | ----- |
| `limit.md` | 极限 |
| `matrix.md` | 矩阵 |
| `process.md` | 进程 |
| `electrostatic-field.md` | 静电场 |
| `formula-and-inequality.md` | 常用公式与不等式 |

## 合规判定

以下情况判定为不合规：

- 文件名包含大写字母
- 文件名包含空格
- 文件名使用下划线而非连字符
- 文件名包含非 ASCII 字符
- 内容目录缺少 `_index.md`
