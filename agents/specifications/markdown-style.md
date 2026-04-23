# Markdownlint 规范

所有 Markdown 文件（包括笔记和 agents 目录下的文件）必须通过 markdownlint 检查。

规则定义在仓库根目录的 `.markdownlint.json` 中，以该文件为权威来源。

## 常见违规

以下规则在实践中容易违反：

### MD032/blanks-around-lists

列表前后必须有空行。引导语与列表之间必须有空行。

正确：

```markdown
示例：

- item1
- item2
```

错误：

```markdown
示例：
- item1
- item2
```

### MD040/fenced-code-language

所有围栏代码块必须指定语言标识。不允许空的 ` ``` ` ，必须写 ` ```text ` 或其他语言名。

### MD060/table-column-style

表格分隔行必须使用带空格的风格 `| --- |` 而非紧凑风格 `|---|`。

## 合规判定

以下情况判定为不合规：

- markdownlint 检查报告任何错误或警告
