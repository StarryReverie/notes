# 目录结构约定

## 三级层次结构

笔记内容存放在 `content/docs/` 下，采用学科 → 课程 → 知识点的三级结构：

```text
content/docs/
  _index.md                          # 文档首页
  {学科}/
    _index.md                        # 学科首页（如"数学"）
    {课程}/
      _index.md                      # 课程首页（如"微积分"）
      {知识点}.md                    # 笔记页面（如"极限"）
```

## 现有学科

| 目录名 | title |
| ------ | ----- |
| `mathematics` | 数学 |
| `computer-science` | 计算机科学 |
| `physics` | 物理 |

## 添加新学科

在 `content/docs/` 下创建新目录，包含 `_index.md`。`_index.md` 需设置 `title`（中文学科名）和 `weight`。

## 添加新课程

在目标学科目录下创建新目录，包含 `_index.md`。`_index.md` 需设置 `title`（中文课程名）和 `weight`。

## `_index.md` 规范

- 每个内容目录（学科、课程）必须包含 `_index.md`
- `_index.md` 不是笔记页面，而是目录的入口和导航
- frontmatter 至少包含 `title` 字段
- 可选 `weight` 字段控制排序

## 文件放置

- 笔记文件（`.md`）直接放在课程目录下
- 不创建更深的子目录（保持三级结构）
- 图片等资源放在 `static/images/` 或 `assets/` 下，不在内容目录中

## 合规判定

以下情况判定为不合规：

- 学科或课程目录缺少 `_index.md`
- 在课程目录下创建了子目录（违反三级结构）
- 笔记文件放在 `content/docs/` 或学科目录下（未归入课程目录）
