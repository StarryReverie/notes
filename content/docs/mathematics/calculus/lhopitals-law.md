---
title: 洛必达法则
weight: 800
math: true
---

- **定理**
    - 设 $f(x),g(x)$ 满足以下条件，则 $\lim\limits_{x\to x_0}\frac{f(x)}{g(x)}=\lim\limits_{x\to x_0}\frac{f'(x)}{g'(x)}$：
        - $\lim\limits_{x\to x_0}f(x)=0,\lim\limits_{x\to x_0}g(x)=0$ 或 $\lim\limits_{x\to x_0}f(x)=\infty,\lim\limits_{x\to x_0}g(x)=\infty$;
        - 在 $x_0$ 的某一个去心邻域内，$f(x),g(x)$ 均[可导](/docs/mathematics/calculus/derivative#ri73aj)；
        - $\lim\limits_{x\to x_0}\frac{f'(x)}{g'(x)}$ 存在或为 $\infty$。
    - 其中的 $x\to x_0$ 可以换为其他趋向。
- **应用**
    - $\frac{0}{0},\frac{\infty}{\infty}$ **型不定式**
        - 若分式上下的[函数](/docs/mathematics/calculus/function)满足条件，直接应用洛必达法则即可。
        - 若用过一次洛必达法则后仍为不定式，则可以继续使用洛必达法则。
    - $0\cdot\infty$ **型不定式**
        - 设 $f(x),g(x)$ 满足 $\lim f(x)=0,\lim g(x)=\infty$，则 $\lim f(x)g(x)=\lim\frac{f(x)}{\frac{1}{g(x)}}=\lim\frac{g(x)}{\frac{1}{f(x)}}$。
    - $\infty-\infty$ **型不定式**
        - 设 $f(x),g(x)$ 满足 $\lim f(x)=\infty,\lim g(x)=\infty$，则 $\lim(f(x)-g(x))=\frac{\frac{1}{g(x)}-\frac{1}{f(x)}}{\frac{1}{f(x)g(x)}}$。
        - 如果已经确定 $\lim f(x)=+\infty,\lim g(x)=-\infty$ 或 $\lim f(x)=-\infty,\lim g(x)=+\infty$，则可以直接写出答案，不必使用洛必达法则。
    - $1^{\infty},0^0,\infty^0$ **型不定式**
        - 取自然对数转换为 $e$ 的指数，转化为 $0\cdot\infty$ 型不定式问题求解。
        - $\lim f(x)^{g(x)}=\lim\exp(g(x)\ln f(x))=\exp\lim(g(x)\ln f(x))$。
- **注意事项**
    - 使用洛必达法则前先检查是否是不定式。
    - $\lim\frac{f'(x)}{g'(x)}$ 如果不存在且不是 $\infty$，并不一定说明 $\lim\frac{f(x)}{g(x)}$ 也是如此。
    - 先用[等价无穷小](/docs/mathematics/calculus/infinitesimal-and-infinite#tbuz72)替换可以简化计算。
