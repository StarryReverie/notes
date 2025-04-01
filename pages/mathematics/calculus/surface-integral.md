---
tags:
  - mathematics
  - calculus
  - function
  - integral
---
- **第一类曲面积分**
    - **定义**
        - 设 $S$ 是的光滑曲面， $f(x,y,z)$ 在 $S$ 上有界。
        - 将 $S$ 分为 $\Delta \sigma_1,\Delta \sigma_2,\dots,\Delta \sigma_n$ ，对于第 $i$ 段任取 $(\xi_i,\eta_i,\zeta_i)$ ，设 $\lambda=\max\limits_{i=1}^n\{d(\Delta \sigma_i)\}$ 。
        - 如果以下极限存在且为一个数，则将其称为 $f(x,y,z)$ 在 $s$ 上的第一类曲面积分：
          $$
          \iint_Sf(x,y,z)\mathrm d\sigma:=\lim_{\lambda\to+\infty}\sum_{i=1}^n f(\xi_i,\eta_i)\Delta s_i
          $$
        - 如果 $L$ 是一条闭合曲线，则记作
          $$
          \oiint_L f(x,y,z)\mathrm d\sigma
          $$
- **第二类曲面积分**
    - **定义**
        - 设 $S$ 是有向光滑曲面， $\boldsymbol F(x,y)=X(x,y,z)\boldsymbol i+Y(x,y,z)+Z(x,y,z)\boldsymbol j$ 在 $L$ 上有界。
        - 将 $S$ 分为 $\Delta s_1,\Delta s_2,\dots,\Delta s_n$ ， $\Delta x_i,\Delta y_i$ 是每一曲面的面积，$(\Delta s_i)_{xy}$ 表示 $\Delta s_i$ 在 $xOy$ 平面的有向投影。
        - 对于第 $i$ 段任取 $(\xi_i,\eta_i,\zeta_i)$ ，设 $\lambda=\max\limits_{i=1}^n\{\Delta s_i\}$ 。
        - 如果以下极限存在且为一个数，则将其称为 $Z(x,y,z)$ 在 $S$ 上对 $z$ 的曲面积分：
          $$
          \iint_S Z(x,y,z)\mathrm dx\mathrm dy := \lim_{\lambda\to+\infty}\sum_{i=1}^n Z(\xi_i,\eta_i,\zeta_i)(\Delta s_i)_{xy}
          $$
        - 同样可以定义对 $x,y$ 的曲面积分。合并后
          $$
          \iint_S X(x,y,z)\mathrm dy\mathrm dz+Y(x,y,z)\mathrm dz\mathrm dx+Z(x,y,z)\mathrm dx\mathrm dy=\iint_S \boldsymbol F(x,y,z)\cdot \mathrm d\boldsymbol s
          $$
        - 第二类曲面积分需要指定是对于曲面的哪一侧积分。
        - 对于闭合曲面，默认在外侧。
    - **计算**
        - **分别计算法**
            - $$
              \iint_S X(x,y,z)\mathrm dy\mathrm dz=\pm\iint_{D_{yz}} X(x(y,z),y,z)\mathrm dy\mathrm dz 
              $$
            - 当 $S$ 取前侧时，取正号，否则取负号。投影到其他平面时，如果侧面是指向轴的正方向，则取正号。
        - **统一计算法**
            - 对于曲面 $S:f(x,y,z)=0$：
              $$
              \iint_S X\mathrm dy\mathrm dz+Y\mathrm dz\mathrm dx+Z\mathrm dx\mathrm dy=\iint_S \left[X\left(-\frac{\partial z}{\partial x}\right)+Y\left(-\frac{\partial z}{\partial y}\right)+Z\right]\mathrm dx\mathrm dy
              $$
    - **两类曲面积分的关系**
        - $$
          \iint_S X\mathrm dy\mathrm dz+Y\mathrm dz\mathrm dx+Z\mathrm dx\mathrm dy=\iint_S (X\cos\alpha+Y\cos\beta+Z\cos\gamma)\mathrm dS
          $$
- **高斯公式**
    - 设空间闭区域 $\Omega$ 由分片光滑的闭曲面 $S$ 围成，$X,Y,Z$ 在 $\Omega$ 上有一阶连续[偏导数](/pages/mathematics/calculus/partial-derivative.md)，则：
      $$
      \oiint_{S^+} X\mathrm dy\mathrm dz+Y\mathrm dz\mathrm dx+Z\mathrm dx\mathrm dy=\iiint_\Omega\left(\frac{\partial X}{\partial x}+\frac{\partial Y}{\partial y}+\frac{\partial Z}{\partial z}\right)\mathrm dx\mathrm dy\mathrm dz
      $$
    - $S$ 取外侧。
    - 使用时注意被积分的三项的顺序。
- **曲面积分与曲面无关的条件**
    - $\Omega$ 是空间单连通区域，$X,Y,Z$ 在 $\Omega$ 上有一阶连续偏导数，则当 $\frac{\partial X}{\partial x}+\frac{\partial Y}{\partial y}+\frac{\partial Z}{\partial z}=0$ 时，曲面积分与曲面无关，封闭曲面的积分等于 $0$。
- **通量和散度**
    - **通量**
        - 设向量场 $\boldsymbol A=(X,Y,Z)$，$S$ 为向量场中的曲面，则通过 $S$ 的一侧通量为
          $$
          \Phi:=\iint_S \boldsymbol A\cdot\mathrm d\boldsymbol S=\iint_S \boldsymbol A\cdot\boldsymbol n\mathrm dS=\iint_S X\mathrm dy\mathrm dz+Y\mathrm dz\mathrm dx+Z\mathrm dx\mathrm dy
          $$
        - 对于封闭曲面 $S$，穿过 $S$ 的外侧的通量为
          $$
          \Phi:=\oiint_{S^+} \boldsymbol A\cdot\mathrm d\boldsymbol S
          $$
        - 如果 $\Phi>0$，则 $S$ 内有源，如果 $\Phi<0$，则 $S$ 内有汇，如果 $S=0$，则 $S$ 内无源也无汇。
    - **散度**
        - 设向量场 $\boldsymbol A=(X,Y,Z)$，则定义散度为
          $$
          \operatorname{div}\boldsymbol A:=\frac{\partial X}{\partial x}+\frac{\partial Y}{\partial y}+\frac{\partial Z}{\partial z}=\nabla\cdot\boldsymbol A
          $$
        - 散度表示 $\boldsymbol A$ 在场内某点的发散程度。
        - 高斯公式也可以表示为
          $$
          \oiint_{S^+}\boldsymbol A\cdot\mathrm d\boldsymbol S=\iiint_V\operatorname{div}\boldsymbol A\mathrm dx\mathrm dy\mathrm dz
          $$
- **斯托克斯公式**
    - 设 $L$ 为分片光滑的空间有向闭曲线，$S$ 是以 $L$ 为边界的分片光滑的有向曲面，$L$ 的正向与 $S$ 的侧符合右手螺旋定则。
        - 设 $X,Y,Z$ 在包含 $S$ 内的空间区域内有一阶连续[偏导数](/pages/mathematics/calculus/partial-derivative.md)，则
          $$
          \oint_L X\mathrm dx+Y\mathrm dy+Z\mathrm dz=
          \iint_S\begin{vmatrix}
          \mathrm dy\mathrm dz & \mathrm dz\mathrm dx & \mathrm dx\mathrm dy \\
          \dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\
          X & Y & Z \\
          \end{vmatrix}
          =\iint_S\begin{vmatrix}
          \cos\alpha & \cos\beta & \cos\gamma \\
          \dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\
          X & Y & Z \\
          \end{vmatrix}\mathrm dS
          $$
- **环流量和旋度**
    - **环流量**
- **空间曲线积分与路径无关条件**
    - 空间曲线积分 $\oint_L X\mathrm dx+Y\mathrm dy+Z\mathrm dz$ 在与路径无关的充要条件是
      $$
      \frac{\partial Z}{\partial y}=\frac{\partial Y}{\partial z},\frac{\partial X}{\partial z}=\frac{\partial Z}{\partial x},\frac{\partial Y}{\partial x}=\frac{\partial X}{\partial y}
      $$
