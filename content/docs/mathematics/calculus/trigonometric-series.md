---
title: 三角级数
weight: 2600
math: true
---

- **三角级数**
    - 三角级数定义为以下的函数项[级数](/notes/docs/mathematics/calculus/series)：
      $$
      \frac{a_0}{2}+\sum_{n=1}^{+\infty}(a_n\cos nx+b_n\sin nx)
      $$
- **三角函数系正交性**
    - 三角函数系是 $1,\cos x,\sin x,\cos 2x,\sin 2x,\dots,\cos nx,\sin nx,\dots$。
    - 定义两个[函数](/notes/docs/mathematics/calculus/function) $f(x),g(x)$ 的内积为
      $$
      \langle f(x),g(x)\rangle := \int_{-\pi}^{\pi}f(x)g(x)\mathrm dx
      $$
    - 如果 $\langle f(x),g(x)\rangle=0$，则 $f(x),g(x)$ 正交。
    - 三角函数系中的任意两个函数正交。
- **傅里叶级数**
    - **傅里叶系数**
        - 假设 $f(x)$ 可以展开为三角级数，则考虑求其系数。
        - 可以利用级数与系数对应的函数做内积，其他项等于 $0$。
        - 由此得到傅里叶系数：
            - $$
              a_n=\frac{1}{\pi}\int_{-\pi}^\pi f(x)\cos nx\mathrm dx, n\in \mathrm N
              $$
            - $$
              b_n=\frac{1}{\pi}\int_{-\pi}^\pi f(x)\sin nx\mathrm dx, n\in \mathrm N^*
              $$
    - **定义**
        - 定义满足系数是傅里叶系数的三角级数是傅里叶级数。
        - 当 $f(x)$ 满足狄利克雷条件时，傅里叶级数收敛到 $f(x)$：
            - 函数在一个周期内连续或只有有限个间断点；
            - 在一个周期内只有有限个极值点。
        - 满足狄利克雷条件时，傅里叶级数收敛情况：
            - 当 $x$ 处连续时，级数收敛到 $f(x)$；
            - 当 $x$ 处间断时，级数收敛到 $\dfrac{f(x^-)+f(x^+)}{2}$。
