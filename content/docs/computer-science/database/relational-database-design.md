---
title: 关系数据库设计
weight: 1100
math: true
---

- **函数依赖**
    - **定义**
        - 已知元组 $U$ 和[关系](/docs/computer-science/database/relational-database#fjalge) $R(U)$，$X, Y \subseteq U$。
        - 若对任意 $t_1, t_2 \in R(U)$，$t_1[X] = t_2[X]$ 时 $t_1[Y] = t_2[Y]$，则 $X$ 函数决定 $Y$，$Y$ 函数依赖于 $X$，记作 $\mathrm{FD}\ X \to Y$。
    - **分类**
        - **平凡和非平凡**
            - 已知 $\mathrm{FD}\ X \to Y$，如果 $Y \not\subseteq X$，则其为非平凡函数依赖，否则为平凡函数依赖。
            - 平凡函数依赖中 $Y$ 是 $X$ 分量中的一部分，函数由整体得到部分。
            - 平凡函数依赖一定成立。
        - **完全和部分**
            - 已知 $\mathrm{FD}\ X \to Y$，如果任意 $X' \subset X$ 都没有 $\mathrm{FD}\ X' \to Y$，则其为完全函数依赖，否则为部分函数依赖。
            - 完全函数依赖 $X$ 的每一部分都是必要的，部分函数依赖只要一部分 $X$ 就可以决定 $Y$。
        - **传递和直接**
            - 已知 $\mathrm{FD}\ X \to Y$，$\mathrm{FD}\ Y \to Z$，则 $\mathrm{FD}\ X \to X$。
            - 如果 $Y \not\to X$，则 $\mathrm\ X \to Z$ 为传递函数依赖，否则为直接函数依赖。
            - 直接函数依赖中 $X, Y$ 一一对应，$X, Z$ 之间的依赖关系可以与 $Y$ 无关。
- **范式**
    - **1NF**
        - 若关系模式 $R$ 的每一个属性对应的值域都不可再分，则 $R$ 满足 1NF，记作 $R \in \mathrm{1NF}$。
        - 1NF 是最低级别的，所有关系都是 1NF。
    - **2NF**
        - 已知 $R \in \mathrm{1NF}$，若 $R$ 中所有非主属性都完全依赖于每个候选键，则 $R \in \mathrm{2NF}$。
        - 如果候选键有多个属性，则其部分可能重复，非主属性如果依赖部分，则会产生重复。
        - 如果 $R \notin \mathrm{2NF}$，则可以把 $R$ 以及其候选键拆分，直到子关系满足 2NF。
    - **3NF**
        - 已知 $R \in \mathrm{1NF}$，若 $R$ 中所有非主属性都直接依赖于每个候选键，则 $R \in \mathrm{3NF}$。
        - 如果 $R \in \mathrm{3NF}$ 则 $R \in \mathrm{2NF}$，$\mathrm{3NF} \subset {2NF}$。
