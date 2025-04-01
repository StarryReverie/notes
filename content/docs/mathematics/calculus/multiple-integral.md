---
title: 重积分
weight: 2100
math: true
---

- **二重积分**
    - **定义**
        - 设[多元函数](/notes/docs/mathematics/calculus/multivariate-function) $f(x,y)$ 在平面有界区域 $D$ 上有定义，将 $D$ 划分为 $\Delta \sigma_i$，设 $\lambda$ 为 $\Delta\sigma_i$ 的直径的最大值，任取 $(\xi_i,\eta_i)\in \Delta\sigma_i$。
        - 如果无论 $D$ 如何划分，以及 $(\xi_i,\eta_i)$ 如何选取，以下极限均存在，则 $f(x,y)$ 在 $D$ 上可积。
          $$
          \lim_{\lambda\to 0} \sum_{\Delta\sigma_i\in D} f(\xi_i,\eta_i)\Delta\sigma_i
          $$
        - 此时把以上极限记作 $f(x,y)$ 在 $D$ 上的二重积分，即
          $$
          \iint_D f(x,y)\mathrm d\sigma
          $$
    - **存在性**
        - 如果 $f(x,y)$ 在平面有界区域 $D$ 上连续，则 $f(x,y)$ 在 $D$ 上可积。
        - 如果 $f(x,y)$ 在平面有界区域 $D$ 上的有限个分片内分别连续，则 $f(x,y)$ 在 $D$ 上可积。
    - **几何意义**
        - $f(x,y)$ 在 $D$ 上的重积分等于 $D$ 为底，$z=f(x,y)$ 为顶的曲顶柱体的体积。如果曲面在 $D$ 下，则记负数。
    - **性质** <span id="c6nt3c"></span>
        - 线性性质：
          $$
          \iint_D \left(C_1f_1(x,y)+C_2f_2(x,y)\right)\mathrm d\sigma=C_1\iint_D f_1(x,y)\mathrm d\sigma+C_2\iint_D f_2(x,y)\mathrm d\sigma
          $$
        - 积分区域可加：
          $$
          \iint_{D_1\cup D_2}f(x,y)\mathrm d\sigma=\iint_{D_1}f(x,y)\mathrm d\sigma+\iint_{D_2}f(x,y)\mathrm d\sigma\ (D_1\cap D_2=\varnothing)
          $$
        - 比较性质：
          $$
          \iint_D f(x,y)\mathrm d\sigma\ge \iint_D g(x,y)\mathrm d\sigma\ (f(x,y)\ge g(x,y))
          $$
        - 绝对值性质：
          $$
          \left|\iint_D f(x,y)\mathrm d\sigma\right| \le \iint_D \left|f(x,y)\right|\mathrm d\sigma
          $$
        - 估值定理：
          $$
          \iint_D f(x,y)\mathrm d\sigma\in\left[A\min_D\{f(x,y)\},A\max_D\{f(x,y)\}\right]
          $$
        - 中值定理：
          $$
          \iint_D f(x,y)\mathrm d\sigma=f(\xi,\eta)A\ ((\xi,\eta)\in D)
          $$
        - 对称性质：区域对称时，如果关于某自变量为奇函数，则重积分为 $0$，如果为偶函数，则重积分为一半区域的两倍重积分。
- **计算**
    - **X 型**
        - 已知 $D: a\le x\le b,\varphi_1(x)\le y\le\varphi_2(x)$，则
        - $$
          \iint_D f(x,y)\mathrm d\sigma=\int_a^b\mathrm dx\int_{\varphi_1(x)}^{\varphi_2(x)} f(x,y)\mathrm dy
          $$
    - **Y 型**
        - 已知 $D: a\le y\le b,\varphi_1(y)\le x\le\varphi_2(y)$，则
        - $$
          \iint_D f(x,y)\mathrm d\sigma=\int_a^b\mathrm dy\int_{\varphi_1(y)}^{\varphi_2(y)} f(x,y)\mathrm dx
          $$
    - **极坐标系**
        - 已知 $D: a\le\theta\le b,\varphi_1(\theta)\le\rho\le\varphi_2(\theta)$，则有以下对应关系：
          $$
          x=\rho\cos\theta,y=\rho\sin\theta,\mathrm dx\mathrm dy=\rho\mathrm d\rho\mathrm d\theta
          $$
        - $$
          \iint_D f(x,y)\mathrm d\sigma=\int_a^b\mathrm d\theta\int_{\varphi_1(\theta)}^{\varphi_2(\theta)} f(\rho\cos\theta,\rho\sin\theta)\rho\mathrm d\rho
          $$
- **三重积分**
    - **定义**
        - 设[多元函数](/notes/docs/mathematics/calculus/multivariate-function) $f(x,y,z)$ 在空间有界区域 $\Omega$ 上有定义，将 $\Omega$ 划分为 $\Delta v_i$，设 $\lambda$ 为 $\Delta v_i$ 的直径的最大值，任取 $(\xi_i,\eta_i)\in \Delta v_i$。
        - 如果无论 $\Omega$ 如何划分，以及 $(\xi_i,\eta_i,\zeta_i)$ 如何选取，以下极限均存在，则 $f(x,y)$ 在 $\Omega$ 上可积。
          $$
          \lim_{\lambda\to 0} \sum_{\Delta v_i\in \Omega} f(\xi_i,\eta_i,\zeta_i)\Delta v_i
          $$
        - 此时把以上极限记作 $f(x,y,z)$ 在 $\Omega$ 上的三重积分，即
          $$
          \iiint_\Omega f(x,y,z)\mathrm dv
          $$
    - **意义**
        - $f(x,y,z)$ 在 $\Omega$ 上的重积分等于空间立体 $\Omega$ 以 $f(x,y,z)$ 为密度函数的质量。
        - $\iiint_\Omega\mathrm dv$ 表示 $\Omega$ 的体积。
    - **计算**
        - **投影法**
            - 下边界曲面为 $S_1:z=z_1(x,y)$，上边界曲面为 $S_2:z=z_2(x,y)$，将 $\Omega$ 投影到 $xOy$ 平面上的闭区域 $D$。
            - $$
              \iiint_\Omega f(x,y,z)\mathrm dv=\iint_D \mathrm d\sigma\int_{z_1(x,y)}^{z_2(x,y)} f(x,y,z)\mathrm dz
              $$
        - **平行截面法**
            - 设 $\Omega$ 中 $z\in [a,b]$，$D_z$ 为 $\Omega$ 在 $z$ 处的截平面。
            - $$
              \iiint_\Omega f(x,y,z)\mathrm dv=\int_a^b \mathrm dz\int_{D_z} f(x,y,z)\mathrm d\sigma
              $$
        - **柱坐标系**
            - 令 $x=\rho\cos\theta,y=\rho\sin\theta\ (\theta\in[0,2\pi])$，则
              $$
              \iiint_\Omega f(x,y,z)\mathrm dv=\int_\alpha^\beta\mathrm d\theta\int_{\rho_1(\theta)}^{\rho_2(\theta)}\rho\mathrm d\rho\int_{z_1(\rho,\theta)}^{z_2(\rho,\theta)}f(\rho\cos\theta,\rho\sin\theta,z)\mathrm dz
              $$
            - 其中体积元素 $\mathrm dv=\rho\mathrm d\rho\mathrm d\theta\mathrm dz$。
        - **球坐标系**
            - 令 $x=r\sin\varphi\cos\theta,y=r\sin\varphi\sin\theta,z=r\cos\varphi\ (\varphi\in[0,\pi],\varphi\in[0,2\pi])$，则
              $$
              \iiint_\Omega f(x,y,z)\mathrm dv=\int_\alpha^\beta\mathrm d\theta\int_{\varphi_1(\theta)}^{\varphi_2(\theta)}\sin\varphi\mathrm d\varphi\int_{r_1(\theta,\varphi)}^{r_2(\theta,\varphi)}f(r\sin\varphi\cos\theta,r\sin\varphi\sin\theta,r\cos\varphi)r^2\mathrm dr
              $$
            - 其中体积元素 $\mathrm dv=r^2\sin\varphi\mathrm dr\mathrm d\varphi\mathrm d\theta$。
            - 对于类似椭球面 $\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}=1$ 围成的区域，可以利用广义球坐标系：
              $$
              \left\{\begin{matrix} x=  ar\sin\varphi\cos\theta\\ y=  br\sin\varphi\sin\theta\\ z=  cr\cos\varphi\\\end{matrix}\right. \implies \mathrm dv=abcr^2\sin\varphi\mathrm dr\mathrm d\varphi\mathrm d\theta
              $$
    - **应用**
        - **空间曲面的面积**
            - 设曲面 $S$ 的方程为 $z=f(x,y)$，在 $xOy$ 平面上的投影为 $D_{xy}$。
            - 设 $\mathrm dS$ 是 $S$ 上的面积微元，$\mathrm d\sigma$ 是 $\mathrm dS$ 在 $xOy$ 平面上的投影，$\gamma$ 为两者夹角，则
              $$
              \mathrm dS=\frac{\mathrm d\sigma}{\cos\gamma}=\sqrt{1+\left(\frac{\partial z}{\partial x}\right)^2+\left(\frac{\partial z}{\partial y}\right)^2}\mathrm d\sigma
              $$
            - $S$ 的面积为
              $$
              S=\iint_{D_{xy}} \sqrt{1+\left(\frac{\partial z}{\partial x}\right)^2+\left(\frac{\partial z}{\partial y}\right)^2}\mathrm dx\mathrm dy
              $$
            - 同理可以对其他平面投影计算，结果不变。
        - **质心**
            - 参考[质心](/notes/docs/physics/dynamics/mass-point-system-and-centor-of-mass#pmrdyk)。
        - **转动惯量**
            - 参考[转动惯量](/notes/docs/physics/dynamics/rigid-body-fixed-axis-rotation#essly2)。
        - **引力**
            - 设空间立体 $V$ 和 $V$ 外的一个在 $(a,b,c)$ 的质点 $m$，$V$ 的密度为 $\rho(x,y,z)$。
            - 设
              $$
              \boldsymbol r(x,y,z)=(x-a,y-b,z-c)
              $$
            - 则 $V$ 和 $m$ 之间的引力为
              $$
              \boldsymbol F=Gm\iiint_V \frac{\boldsymbol r(x,y,z)\rho(x,y,z)}{\|\boldsymbol r(x,y,z)\|^3}\mathrm dv
              $$
- **换元法**
    - 设 $f(x,y)$ 在 $xOy$ 上的闭区域 $D$ 连续，$x=x(u,v),y=y(u,v)$，$D$ 对应 $uOv$ 上的闭区域 $D'$。
    - 若 $x(u,v),y(u,v)$ 在 $D'$ 上有一阶连续[偏导数](/notes/docs/mathematics/calculus/partial-derivative)，在 $D'$ 上雅可比行列式 $\frac{\partial(x,y)}{\partial(u,v)}\ne 0$，$D$ 与 $D'$上的点一一对应，则
      $$
      \iint_D f(x,y)\mathrm dx\mathrm dy=\iint_{D'} f(x(u,v),y(u,v))\left|\frac{\partial(x,y)}{\partial(u,v)}\right|\mathrm du\mathrm dv
      $$
- **含参变量积分**
    - **定义**
    - **性质**
        - 连续性：如果 $f(x,y)$ 在 $[a,b]\times[c,d]$ 上连续，则 $F(y)=\int_a^b f(x,y)\mathrm dx$ 在 $[c,d]$ 上连续。
        - 上下限含参的连续性：如果 $f(x,y),f'_y(x,y)$ 在 $[a,b]\times[c,d]$ 上连续，此区域内 $\varphi_1(y),\varphi_2(y)\in[a,b]$，则 $F(y)=\int_{\varphi_1(y)}^{\varphi_2(y)} f(x,y)\mathrm dx$ 在 $[c,d]$ 上连续。
        - 积分次序交换性：如果 $f(x,y)$ 在 $[a,b]\times[c,d]$ 上连续，则
          $$
          \int_a^b\mathrm dx \int_c^d f(x,y)\mathrm dy=\int_c^d\mathrm dy \int_a^b f(x,y)\mathrm dx
          $$
        - 导数：如果 $f(x,y),f_y'(x,y)$ 在 $[a,b]\times[c,d]$ 上连续，则 $F(y)$ 在 $[c,d]$ 上有连续导数，且
          $$
          F'(y)=\frac{\mathrm d}{\mathrm dy}\int_a^b f(x,y)\mathrm dx=\int_a^b f'_y(x,y)\mathrm dx
          $$
        - 上下限含参的导数：如果 $f(x,y),f'_y(x,y)$ 在 $[a,b]\times[c,d]$ 上连续，此区域内 $\varphi_1(y),\varphi_2(y)\in[a,b]$，则 $F(y)$ 在 $[c,d]$ 上有连续导数：
          $$
          F'(y)=\frac{\mathrm d}{\mathrm dy}\int_{\varphi_1(y)}^{\varphi_2(y)} f(x,y)\mathrm dx=\int_{\varphi_1(y)}^{\varphi_2(y)} f'_y(x,y)\mathrm dx+f(\varphi_2(y),y)\varphi'_2(y)-f(\varphi_1(y),y)\varphi'_1(y)
          $$
