---
tags:
  - mathematics
  - calculus
  - function
  - limits
---
- **多元函数定义**
    - 设 $D\in R^n$ 是一个点集，对于 $\forall P(x_1,x_2,\dots,x_n)\in D$。$y$ 按照一定规则 $f$ 总有唯一确定的值与 $P(x_1,x_2,\dots,x_n)$ 对于，则称 $y$ 或 $f$ 为 $x_1,x_2,\dots,x_n$ 或 $P$ 的 $n$ 元函数，记作 $y=f(x_1,x_2,\dots,x_n)$ 或 $z=f(P)$。
    - $x_1,x_2,\dots,x_n$ 为自变量，$y$ 为因变量，$D$ 为定义域。
    - 二元函数一般表示为 $z=f(x,y)$，三元函数一般表示为 $u=f(x,y,z)$。
- **多元极限**
    - **定义**
        - 设 $f(x_1,x_2,\dots,x_n)$ 在 $P_0(x_{10},x_{20},\dots,x_{n0})$ 的某去心邻域内有定义，$A$ 是一个数，如果对于 $\forall \epsilon>0$，$\exists \delta>0$，使得
          $$
          |f(x_1,x_2,\dots,x_n)-A|<\epsilon\ \left((x_1,x_2,\dots,x_n)\in \mathring U(P_0, \delta)\right)
          $$
          则当 $x_1,x_2,\dots,x_n$ 时，$f(x_1,x_2,\dots,x_n)$ 的极限为 $A$，记作
          $$
          \lim_{(x_1,x_2,\dots,x_n)\to(x_{10},x_{20},\dots,x_{n0})} f(x_1,x_2,\dots,x_n)=A
          $$
          $$
          \lim_{P\to P_0} f(P)=A
          $$
    - **注意事项**
        - 多元极限中 $P\to P_0$ 的方式是任意的，如果存在不同的方式使得 $\lim_{P\to P_0} f(P)$ 不同，则 $\lim_{P\to P_0} f(P)$ 不存在。
        - 一元[极限](/notes/docs/mathematics/calculus/limit)的方法在此时仍然适用，只需要是对一个整体应用这些方法。
- **连续性**
    - **定义**
        - 设 $f(P)$ 在 $P_0$ 的某去心邻域内有定义，若
          $$
          \lim_{P\to P_0} f(P)=f(P_0)
          $$
          则 $f(P)$ 在 $P_0$ 处连续。
    - **性质**
        - 与一元函数[连续性](/notes/docs/mathematics/calculus/function#oi6fm3)类似，有以下性质：
            - 有界性：如果函数 $f(P)$ 在有界闭区域 $D$ 上连续，则 $f(P)$ 在区域 $D$ 上有界，即存在正数 $M$，使对 $\forall P\in D$，都有
              $$
              |f(P)|\le M
              $$
            - 最值定理：如果函数 $f(P)$ 在有界闭区域 $D$ 上连续，则 $f(P)$ 在区域 $D$ 上必定取得最大值和最小值，即存在 $P_1,P_2\in D$，使得对 $\forall P\in D$，都有
              $$
              f(P_1)\le f(P)\le f(P_2)
              $$
            - 介值定理：如果函数 $f(P)$ 在有界闭区域 $D$ 上连续，$m=\min\limits_{P\in D} f(P),M=\max\limits_{P\in D} f(P)$，则 $\forall \mu\in [m,M]$，都 $\exists P_0\in D$，使得
              $$
              f(P_0)=\mu
              $$
