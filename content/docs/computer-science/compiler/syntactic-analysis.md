---
title: 语法分析
weight: 200
math: true
---

- **文法**
    - **定义**
        - 文法 $G = (V_N, V_T, S, P)$，其中：
            - $V_N$：非空有限非终结符号集合。
            - $V_T$：非空有限终结符号集合。
            - $S$：开始符号。
            - $P$：有限产生式集合。
        - $V_N \cup V_T = V$，$V_N \cap V_T = \varnothing$。
        - 语言 $L(G)$：从 $G$ 的 $S$ 开始，不断用产生式替换非终结符号，得到的只有终结符号的串集合。
    - **推导和规约**
        - 直接推导：当且仅当 $A \to \gamma$ 时，$V = \alpha A \beta \to W = \alpha \gamma \beta$。$V$ 直接推导出 $W$，$W$ 直接规约到 $V$。
        - 多步推导：$V$ 经过 $\alpha_0 \Rightarrow \alpha_1, \alpha_1 \Rightarrow \alpha_2, \cdots, \alpha_{n - 1} \Rightarrow \alpha_n$，$n$ 个推导得到 $W$，则 $V \xRightarrow{*} W$。如果 $V = W$ 或 $V \xRightarrow{*} W$，则 $V \xRightarrow{*} W$。
        - 最左/右推导：从 $V$ 推导到 $W$，总是替换最左/右边的非终结符号。
        - 规范推导：最右推导又称规范推导，逆序为规范规约。
    - **句型与句子**
        - 句型：$S \xRightarrow{*} \alpha, \alpha \in (V_N \cup V_T)^*, \alpha$ 为 $G(S)$ 的句型。
        - 句子：$S \xRightarrow{*} \alpha, \alpha \in V_T^*, \alpha$ 为 $G(S)$ 的句子。
        - 规范句型/句子：仅用规范推导得到的句型/句子。
    - **递归**
        - 直接递归：$G$ 存在产生式 $A \to \alpha A \beta$ 时，$G$ 为直接递归文法。
        - 间接递归：$G$ 可以有 $A \to \gamma$ 和推导 $\gamma \xRightarrow{+} \alpha A \beta$ 时，$G$ 为间接递归文法。
        - 递归文法：直接与间接递归文法统称递归文法。
        - 左递归：$A \to \gamma$ 且 $\gamma \xRightarrow{+} A \beta$。
        - 右递归：$A \to \gamma$ 且 $\gamma \xRightarrow{+} \alpha A$。
    - **表示**
        