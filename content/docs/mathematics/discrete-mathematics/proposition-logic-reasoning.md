---
title: 命题逻辑推理
weight: 300
math: true
---

- **推理**
    - 设 $A_1,A_2,\dots,A_n,B$ 为命题公式，则 $A_1 \land A_2 \land \cdots \land A_n \to B$ 或 $\{A_1,A_2,\dots,A_n\} \vdash B$ 是一个推理。
    - 若 $A_1 \land A_2 \land \cdots \land A_n \to B$ 永真，则推理是有效的，记作 $A_1 \land A_2 \land \cdots \land A_n \Rightarrow B$ 或 $\{A_1,A_2,\dots,A_n\} \models B$，$B$ 为有效结论。
- **推理定律** <span id="mi4ocz"></span>
    - 通过[命题逻辑等值演算](/notes/docs/mathematics/discrete-mathematics/proposition-logic-calculation)得到。
    - 附加律：$A \Rightarrow A \lor B$
    - 化简律：$A \land B \Rightarrow A$
    - 假言推理：$A \land (A \to B) \Rightarrow B$
    - 拒取式：$\neg B \land (A \to B) \Rightarrow \neg A$
    - 析取三段论：$(A \lor B) \land \neg B \Rightarrow A$
    - 假言三段论：$(A \to B) \land (B \to C) \Rightarrow A \to C$
    - 等价三段论：$(A \leftrightarrow B) \land (B \leftrightarrow C) \Rightarrow A \leftrightarrow C$
    - 构造性二难：$(A \to B) \land (C \to D) \land (A \lor C) \Rightarrow B \lor D$，$(A \to B) \land (\neg A \to B) \Rightarrow B$
    - 破坏性二难：$(A \to B) \land (C \to D) \land (\neg B \lor \neg D) \Rightarrow \neg A \lor \neg C$
- **自然推理系统**
    - **定义**
        - 自然推理系统组成：
            - 字母：命题变项、联结词、括号、逗号。
            - 合式公式
            - 推理规则
    - **证明**
        - 设前提 $A_1,A_2,\dots,A_k$，结论 $B$，公式序列 $C_1,C_2,\dots,C_l = B$。若 $C_i$ 是某个 $A_j$ 或其前面的 $C$ 的结论，则序列是一个证明。
    - **证明方法**
        - **直接法**
            - 安装证明定义。
        - **附加前提法**
            - 要证 $A_1 \land A_2 \land \cdots \land A_k \Rightarrow B \to C$，等价证明 $A_1 \land A_2 \land \cdots \land A_k \land B \Rightarrow C$。
        - **反证法**
            - 要证 $A_1 \land A_2 \land \cdots \land A_k \Rightarrow B$，等价证明 $A_1 \land A_2 \land \cdots \land A_k \land \neg B \Rightarrow 0$。
