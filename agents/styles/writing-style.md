# 笔记写作风格

本文件定义笔记内容的写作风格。风格难以机械判定，但 Agent 应以此为原则编写和润色笔记内容。

本文件是一份持续迭代的"菜谱"，每次发现新的风格偏好时应更新。

## 角色与读者

- 角色：笔记作者的知识整理，面向未来的自己
- 读者：具有相关学科背景的人（包括未来的作者本人）
- 语气：教科书式的精炼陈述，不带个人情感、口语化修饰或感叹

## 风格要点

### 精炼陈述

- 用最少的文字传达完整信息，不加多余的修饰语
- 不写引导性文字（如"首先我们来看"、"接下来"）
- 不写总结性文字（如"综上所述"、"总之"）
- 不写强调性冗余（如"值得注意的是"、"需要特别指出的是"）
- 一行一个要点，不在同一个列表项中用句号分隔多个独立要点

### 定义句式

- "……称为……"：`X` 称为 `Y`
- "……记作……"：`X` 记作 `Y`
- "……定义为……"：`X` 定义为 `Y`
- "如果……则……"：条件→结论
- "设……，则……"：引入假设→推导结果
- "已知……，则……"：引入前提→给出结论（如判别法的表述）

### 数学与文字的关系

- 数学公式是陈述的一部分，不是独立展示块
- 先中文描述，紧跟公式。公式和中文是同一个句子的组成部分
- 短公式用行内 `$...$`，只有需要多行环境（如 `\begin{cases}`、积分号等长表达式）时才用 `$$...$$`
- 符号首次出现时用中文注明含义
- 单位紧跟数值，用 `\mathrm{}` 排版（如 `$8.31\ \mathrm{J\cdot mol^{-1}\cdot K^{-1}}$`）
- 同一主题下的多个相关公式用逗号或句号分隔，不拆成独立列表项

### 连接词

- 极简：能用"同理"、"类似"、"推广到"四个字说清的，不用更多
- 常用连接词：同理、类似、推广到、反之、特别地、注意、即、则
- "函数的情况同理"：用简短语句表示类比结论，不重复完整论述
- 不使用：然而、此外、与此同时、不仅如此、显而易见

### 推导和证明风格

- 不写完整证明过程，只记录关键步骤和结论
- 推论直接陈述结论，必要时在括号中注明推导来源
- 计算方法只记录核心步骤和关键公式，省略中间代数运算

### 术语处理

- 英文术语首次出现时可附英文原文（如"电路交换即 Circuit Switching"），后续不再重复
- 外国人名不翻译，直接使用原文（如"莱布尼茨判别法"）
- 特定领域的惯例缩写直接使用，不每次展开（如 PCB、FCFS、SJF）

## 禁止清单

- 废话开场白："本文将介绍"、"首先来看"
- 总结结尾："综上所述"、"总而言之"
- 强调拐棍："值得注意的是"、"需要特别指出的是"、"显而易见"
- 口语化表述：任何感叹号、反问句
- 重复陈述：定义已经说过的内容不换种说法再说一遍
- 军事化/商业用语：深耕、赋能、闭环、抓手
- 三段式套话："首先……其次……最后……"作为文章结构

## 参考资料

本风格提炼自以下笔记（写作范文）：

- `content/docs/mathematics/calculus/limit.md`
- `content/docs/mathematics/calculus/series.md`
- `content/docs/mathematics/linear-algebra/matrix.md`
- `content/docs/mathematics/discrete-mathematics/graph-basis.md`
- `content/docs/mathematics/probability-theory/random-variable.md`
- `content/docs/computer-science/operating-system/process.md`
- `content/docs/computer-science/network/introduction.md`
- `content/docs/computer-science/digital-logic/digital-system.md`
- `content/docs/physics/electromagnetism/electrostatic-field.md`
- `content/docs/physics/electromagnetism/electromagnetic-induction.md`
- `content/docs/physics/thermodynamics/ideal-gas.md`
