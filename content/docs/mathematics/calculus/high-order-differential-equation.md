---
title: 高阶微分方程
weight: 1400
math: true
---

- **可降阶高阶微分方程**
    - $y^{(n)}=f(x)$
        - 两边同时加积分号，求不定积分，左边的阶数降低。
        - 两边连续求不定积分 $n$ 次即可得到通解。
    - $y^{(n)}=f\left(x,y^{(n-1)}\right)$
        - 因为 $y^{(n)}=\frac{\mathrm d}{\mathrm dx}y^{(n-1)}$，所以可以把 $y^{(n-1)}$ 看成一个新的函数。
        - 令 $p(x)=y^{(n-1)}$，则 $\frac{\mathrm dp}{\mathrm dx}=f(x,p)$。
    - $y''=f(y,y')$
        - 该方程中没有出现 $x$，则可以把 $y$ 看成自变量，则 $y'$ 和 $y''$ 与 $y$ 之间也存在函数关系。
        - 令 $p(y)=y'$，则 $y''=p\frac{\mathrm dp}{\mathrm dy}$
- **线性微分方程**
    - 部分高阶的线性微分方程也可以求解，详见[线性微分方程](/docs/mathematics/calculus/linear-differential-equation)。
