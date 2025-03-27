---
tags:
  - mathematics
  - calculus
  - function
  - integral
---
- **第一类曲线积分**
	- **定义**
		- 设 $L$ 是平面 $xOy$ 上的光滑曲线弧，$f(x,y)$ 在 $L$ 上有界。
		- 将 $L$ 分为 $\Delta s_1,\Delta s_2,\dots,\Delta s_n$，对于第 $i$ 段任取 $(\xi_i,\eta_i)$，设 $\lambda=\max\limits_{i=1}^n\{\Delta s_i\}$。
		- 如果以下极限存在且为一个数，则将其称为 $f(x,y)$ 在 $L$ 上的第一类曲线积分：
		  $$
		  \lim_{\lambda\to+\infty}\sum_{i=1}^n f(\xi_i,\eta_i)\Delta s_i
		  $$
		- 记作
		  $$
		  \int_L f(x,y)\mathrm ds
		  $$
		- 如果 $L$ 是一条闭合曲线，则记作
		  $$
		  \oint_L f(x,y)\mathrm ds
		  $$
	- **性质**
		- 类比[重积分的性质](/pages/mathematics/calculus/multiple-integral.md#c6nt3c)。
	- **计算**
		- 若 $f(x,y)$ 在 $L$ 上连续，$L:\left\{\begin{matrix}x=\varphi(t)\\ y=\psi(t)\end{matrix}\right.\ (a\le t\le b)$，$\varphi(t),\psi(t)$ 在 $[a,b]$ 上可导，则
		  $$
		  \int_L f(x,y)\mathrm ds=\int_a^b f(\varphi(t),\psi(t))\sqrt{(\varphi'(t))^2+(\psi'(t))^2}\mathrm dt
		  $$
		- $y=y(x)$ 的特殊情况：
		  $$
		  \int_L f(x,y)\mathrm ds=\int_a^b f(x,y(x))\sqrt{1+(y'(x))^2}\mathrm dx
		  $$
		- $x=x(y)$ 的特殊情况：
		  $$
		  \int_L f(x,y)\mathrm ds=\int_a^b f(x(y),y)\sqrt{1+(x'(y))^2}\mathrm dy
		  $$
- **第二类曲线积分**
	- **定义**
		- 设 $L$ 是平面 $xOy$ 上的有向光滑曲线弧，$\boldsymbol F(x,y)=X(x,y)\boldsymbol i+Y(x,y)\boldsymbol j$ 在 $L$ 上有界。
		- 将 $L$ 分为 $\Delta \boldsymbol s_1,\Delta\boldsymbol s_2,\dots,\Delta\boldsymbol s_n$，$\Delta x_i,\Delta y_i$ 是每一段弧的坐标的增量，对于第 $i$ 段任取 $(\xi_i,\eta_i)$，设 $\lambda=\max\limits_{i=1}^n\{\Delta s_i\}$。
		- 如果以下极限存在且为一个数，则将其称为 $X(x,y)$ 在 $L$ 上对 $x$ 的曲线积分：
		  $$
		  \int_L X(x,y)\mathrm dx := \lim_{\lambda\to+\infty}\sum_{i=1}^n X(\xi_i,\eta_i)\Delta x_i
		  $$
		- 如果以下极限存在且为一个数，则将其称为 $Y(x,y)$ 在 $L$ 上对 $y$ 的曲线积分：
		  $$
		  \int_L Y(x,y)\mathrm dy:=\lim_{\lambda\to+\infty}\sum_{i=1}^n Y(\xi_i,\eta_i)\Delta y_i
		  $$
		- 合并后：
		  $$
		  \int_L X(x,y)\mathrm dx+\int_L Y(x,y)\mathrm dy=\int_L X(x,y)\mathrm dx+Y(x,y)\mathrm dy=\int_L\boldsymbol F(x,y)\cdot\mathrm d\boldsymbol s
		  $$
		- 对于闭合曲线 $L$，规定 $L^+$ 表示逆时针，$L^-$ 表示顺时针。
	- **性质**
		- **方向性**
			- 第二类曲线积分与积分路径的方向有关（$L_1$ 与 $L_2$ 方向相反）：
			  $$
			  \int_{L_1}\boldsymbol F(x,y)\cdot\mathrm d\boldsymbol s=-\int_{L_2}\boldsymbol F(x,y)\cdot\mathrm d\boldsymbol s
			  $$
		- **与第一类曲线积分的关系**
			- 设 $(\cos\alpha,\cos\beta)$ 为 $L$ 在 $(x,y)$ 处的方向余弦，则
			  $$
			  \int_L X(x,y)\mathrm dx+\int_L Y(x,y)\mathrm dy=\int_L (X(x,y)\cos\alpha+Y(x,y)\cos\beta)\mathrm ds
			  $$
		- **其他性质**
			- 参考第一类曲线积分的性质。
	- **计算**
		- 设 $L:\left\{\begin{matrix}x=\varphi(t)\\ y=\psi(t)\end{matrix}\right.\ (a\le t\le b)$，$t$ 从 $a$ 到 $b$ 中 $\varphi(t),\psi(t)$ 可导，且 $(\varphi'(t))^2+(\psi'(t))^2\ne 0$。
		- 若 $\boldsymbol F(x,y)=X(x,y)\boldsymbol i+Y(x,y)\boldsymbol j$ 在 $L$ 上连续，$\varphi(t),\psi(t)$ 在 $[a,b]$ 上可导，则
		  $$
		  \int_L \boldsymbol F(x,y)\cdot\mathrm d\boldsymbol s=\int_L \left(X(\varphi(t),\psi(t))\varphi'(t)+Y(\varphi(t),\psi(t))\psi'(t)\right)\mathrm dt
		  $$
		- $L\parallel x$ 轴的特殊情况：
		  $$
		  \int_L Y(x,y)\mathrm dy=0
		  $$
		- $L\parallel y$ 轴的特殊情况：
		  $$
		  \int_L X(x,y)\mathrm dx=0
		  $$
- **格林公式**
	- 设闭区域 $D$ 由光滑或分段光滑的曲线 $L$ 围成，$L$ 取正向（沿正向时，区域总在曲线左边）。
	- $X(x,y),Y(x,y)$ 在 $D$ 上有一阶连续偏导数，则
	  $$
	  \oint_L X\mathrm dx+Y\mathrm dy=\iint_D\left(\frac{\partial Y}{\partial x}-\frac{\partial X}{\partial y}\right)\mathrm dx\mathrm dy
	  $$
- **路径无关**
	- **定义**
		- 设 $D$ 是一个区域，$A,B$ 是 $D$ 内任意两点，$L_1,L_2$ 是在 $D$ 内 $A,B$ 之间任意两条路径。
		- 若 $\int_{L_1}X\mathrm dx+Y\mathrm dy=\int_{L_2}X\mathrm dx+Y\mathrm dy$ 总成立，则 $\int_{L}X\mathrm dx+Y\mathrm dy$ 在 $D$ 内与路径无关。
		- 若积分与路径无关，则引入新记号：
		  $$
		  \int_{L}X\mathrm dx+Y\mathrm dy=\int_A^BX\mathrm dx+Y\mathrm dy=\int_{(x_1,y_1)}^{(x_2,y_2)}X\mathrm dx+Y\mathrm dy
		  $$
	- **等价关系**
		- $\int_{L}X\mathrm dx+Y\mathrm dy$ 在 $D$ 内与路径无关。
		- $C$ 是 $D$ 内任意闭合曲线，总满足 $\int_{C}X\mathrm dx+Y\mathrm dy=0$ 。
		- $X(x,y),Y(x,y)$ 在 $D$ 内有一阶连续偏导数，总满足 $\frac{\partial Y}{\partial x}=\frac{\partial X}{\partial y}$ 。
		- $X\mathrm dx+Y\mathrm dy$ 是 $D$ 内某个二元函数的全微分。
- **全微分**
	- 如果存在二元函数 $u=u(x,y)$，其全微分为 $\mathrm du=X\mathrm dx+Y\mathrm dy$，则 $u$ 是 $X\mathrm dx+Y\mathrm dy$ 的原函数。
	- 路径无关等价于 $X\mathrm dx+Y\mathrm dy$ 有原函数，是某函数的全微分。
	- 如果 $X\mathrm dx+Y\mathrm dy$ 有原函数 $u(x,y)$，则
	  $$
	  u(x,y)=\int_{(x_0,y_0)}^{(x,y)} X\mathrm dx+Y\mathrm dy+C
	  $$
