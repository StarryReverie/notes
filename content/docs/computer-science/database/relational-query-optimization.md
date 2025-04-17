---
title: 关系查询优化
weight: 600
math: true
---

- **代数优化**
    - **规则**
        - **交换律**
            - $E_1 \times E_2 = E_2 \times E_1$
            - $E_1 \Join E_2 = E_2 \Join E_1$
            - $E_1 \underset{F}{\Join} E_2 = E_2 \underset{F}{\Join} E_1$
            - $\sigma_F(\Pi_{A_1, \dots, A_n}(E)) = \Pi_{A_1, \dots, A_n}(\sigma_F(E))$，其中 $F$ 只使用 $A_1, \dots, A_n$ 中的属性。
            - $\sigma_F(E_1 \times E_2) = \sigma_F(E_1) \times E_2$，其中 $F$ 只使用 $E_1$ 中的属性。
            - $\sigma_{F_1 \land F_2}(E_1 \times E_2) = \sigma_{F_1}(E_1) \times \sigma_{F_2}(E_2)$，其中 $F_1, F_2$ 只分别使用 $E_1, E_2$ 中的属性。
            - $\sigma_{F_1 \land F_2}(E_1 \times E_2) = \sigma_{F_2}(\sigma_{F_1}(E_1) \times E_2)$，其中 $F_1$ 只使用 $E_1$ 中的属性。
        - **结合律**
            - $(E_1 \times E_2) \times E_3 = E_1 \times (E_2 \times E_3)$
            - $(E_1 \Join E_2) \Join E_3 = E_1 \Join (E_2 \Join E_3)$
            - $(E_1 \underset{F_1}{\Join} E_2) \underset{F_2}{\Join} E_3 = E_1 \underset{F_1}{\Join} (E_2 \underset{F_2}{\Join} E_3)$
        - **分配律**
            - $\sigma_F(E_1 \cup E_2) = \sigma_F(E_1) \cup \sigma_F(E_2)$
            - $\sigma_F(E_1 \cap E_2) = \sigma_F(E_1) \cap \sigma_F(E_2)$
            - $\sigma_F(E_1 - E_2) = \sigma_F(E_1) - \sigma_F(E_2)$
            - $\sigma_F(E_1 \Join E_2) = \sigma_F(E_1) \Join \sigma_F(E_2)$，其中 $F$ 只使用 $E_1, E_2$ 中的公共属性。
            - $\Pi_{A_1, \dots, A_n}(E_1 \cup E_2) = \Pi_{A_1, \dots, A_n}(E_1) \cup \Pi_{A_1, \dots, A_n}(E_2)$
            - $\Pi_{A_1, \dots, A_n}(E_1 \cap E_2) = \Pi_{A_1, \dots, A_n}(E_1) \cap \Pi_{A_1, \dots, A_n}(E_2)$
            - $\Pi_{A_1, \dots, A_n}(E_1 - E_2) = \Pi_{A_1, \dots, A_n}(E_1) - \Pi_{A_1, \dots, A_n}(E_2)$
            - $\Pi_{A_1, \dots, A_n, B_1, \dots, B_m}(E_1 \times E_2) = \Pi_{A_1, \dots, A_n}(E_1) \times \Pi_{B_1, \dots, B_m}(E_2)$，其中 $A_1, \dots, A_n$ 是 $E_1$ 的属性，$B_1, \dots, B_m$ 是 $E_2$ 的属性。
        - **串接律**
            - $\Pi_{A_1, \dots, A_n}(\Pi_{B_1, \dots, B_m}(E)) = \Pi_{A_1, \dots, A_n}(E)$，其中 $\{A_1, \dots, A_n\} \subseteq \{B_1, \dots, B_m\}$。
            - $\sigma_{F_1}(\sigma_{F_2}(E)) = \sigma_{F_1 \land F_2}(E)$
    - **策略**
        - 尽量早进行选择运算：减小中间关系的大小。
        - 投影和选择同时进行：避免重复扫描。
        - 投影和双目运算结合：减少关系的大小，进而减少重复扫描。
        - 尽量把笛卡尔积转换为连接。
        - 缓存公共子表达式。
