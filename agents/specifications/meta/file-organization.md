# agents 文档文件组织规范

本文件定义 `agents/specifications/` 目录的文件组织规则。

## 目录结构

```text
agents/
  README.md
  specifications/
    meta/            # agents 文档自身的规范
    notes/           # 笔记内容的规范
  workflows/
```

## 规则

- `specifications/` 按领域分子目录组织，每个子目录对应一个领域
- 每个文件只关注一个维度，不将多个不相关的规范合并在同一文件中
- 文件名使用 kebab-case 格式
- 文件移动、重命名或新增时，必须同步更新 `agents/README.md` 中的索引

## 合规判定

以下情况判定为不合规：

- `specifications/` 根目录下存在不属于任何子目录的规范文件
- 同一文件涵盖多个不相关的规范维度
- 文件名不符合 kebab-case
- `agents/README.md` 中的索引与实际文件不一致
