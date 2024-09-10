---
tags:
  - physics
  - oscillation
---
- **波动**
	- **定义**
		- 一个物理量的扰动或振动在空间中的传播称为波动，简称波。
		- 波传播的只是振动状态，每个振动的质元不会向前移动。
	- **分类**
		- 横波：振动方向垂直传播方向，只能在固体介质中传播。
		- 纵波：振动方向平行传播方向，能在各种介质中传播。
	- **特征量**
		- **波长**
			- 相邻的相位差为 $2\pi$ 的两点间距离定义为波长 $\lambda$。
			- 定义波数 $\sigma=\frac{1}{\lambda}$，表示单位长度中波长的个数。
			- 定义角波数 $k=2\pi\sigma=\frac{2\pi}{\lambda}$，表示单位长度产生的相位差。
		- **周期、频率、角频率**
			- 周期既是波传播一个波长的时间，也是波上一个点的振动周期。
			- 周期、频率、角频率仅有波源决定，与介质无关。
		- **波速**
			- 单位时间振动状态传播的距离定义为波速 $u$。
			- 波速与波长、周期、频率的关系：
			  $$
			  u=\frac{\lambda}{T}=\lambda\nu
			  $$
			- 波速不是点的振动速度。
			- 波速由介质的性质决定。
				- 横波：$u_T=\sqrt{\frac{G}{\rho}}$，其中 $G$ 为剪切模量。
				- 纵波：$u_L=\sqrt{\frac{E}{\rho}}$，其中 $G$ 为杨氏模量。
	- **性质**
		- **反射**
			- 反射定律：
			  $$
			  i'=i
			  $$
		- **折射**
			- 折射定律：
			  $$
			  \frac{\sin i}{\sin r}=\frac{u_1}{u_2}=n_{21}=\frac{n_2}{n_1}
			  $$
- **简谐波**
	- **波函数**
		- 设原点的振动函数为 $y_0=A\cos(\omega t+\varphi_0)$，则平面简谐波的波函数为：
		  $$
		  y=A\cos\left(\omega\left(t\pm\frac{x}{u}\right)+\varphi_0\right)
		  $$
		- 正负号的选择：
			- 正号：沿 $+x$ 方向传播，$x$ 点的振动状态在时间上落后原点 $\frac{x}{u}$，相位上落后 $\frac{\omega x}{u}$。
			- 负号：沿 $-x$ 方向传播，$x$ 点的振动状态在时间上超前原点 $\frac{x}{u}$，相位上超前 $\frac{\omega x}{u}$。
		- 另外一种形式：
		  $$
		  y=A\cos(\omega t-\frac{2\pi x}{\lambda}+\varphi_0)=A\cos(\omega t-kx+\varphi_0)
		  $$
		- 如果已知波源位于 $x_0$，则波函数为
		  $$
		  y=A\cos\left(\omega\left(t-\frac{|x-x_0|}{u}\right)+\varphi\right)
		  $$
	- **能量**
		- 对于密度为 $\rho$ 的介质中的一个质点 $\mathrm dV$，其动能和势能为
		  $$
		  \mathrm dE_{\mathrm k}=\mathrm dE_{\mathrm p}=\frac{1}{2}\rho\mathrm dV\omega^2A^2\sin^2\omega\left(t-\frac{x}{u}\right)
		  $$
		- 总能量为
		  $$
		  \mathrm dE=\mathrm dE_{\mathrm k}+\mathrm dE_{\mathrm p}=\rho\mathrm dV\omega^2A^2\sin^2\omega\left(t-\frac{x}{u}\right)
		  $$
		- 定义能量密度为
		  $$
		  w:=\frac{\mathrm dE}{\mathrm dV}=\rho\omega^2A^2\sin^2\omega\left(t-\frac{x}{u}\right)
		  $$
		- 定义平均能量密度为一个周期内能量密度对时间的平均值：
		  $$
		  \bar{\omega}:=\frac{1}{T}\int_0^T\omega\mathrm dt=\frac{1}{2}\rho\omega^2A^2
		  $$
	- **能流**
		- 定义能流为波在单位时间内传递过介质一个垂直传播方向的截面 $S$ 的能量：
		  $$
		  P:=uSw
		  $$
		- 定义平均能流或平均功率：
		  $$
		  \bar P:=uS\bar w=\frac{1}{2}\rho Su\omega^2A^2
		  $$
		- 能流和平均能流的单位为 $\mathrm W$。
		- 定义平均能流密度 / 强度：
		  $$
		  I:=\frac{\bar P}{S}=u\bar w=\frac{1}{2}\rho u\omega^2A^2
		  $$
		- 平均能流密度的单位为 $\mathrm{W/m^2}$。
- **波的叠加**
	- **叠加原理**
		- 同一介质中，不同波源产生的波无论是否相遇，都会保持原有的振幅、频率、波长等性质传播，互不影响。
		- 波的叠加原理适用于机械波、电磁波、概率波，不适用于强度太大的波。
	- **干涉**
		- **定义**
			- 两个或几个波满足频率相同、相位差恒定、振动方向相同时，称为相干波。
			- 相干波可以发生干涉。
			- 设有两个波源 $S_1,S_2$，振动表达式为 $y_{10}=A_1\cos(\omega t+\varphi_{10}),y_{20}=A_2\cos(\omega t+\varphi_{20})$。
			- 设空间中一点 $P$，到 $S_1,S_2$ 距离为 $r_1,r_2$，两个波在 $P$ 的分振动为 $y_1=A_1\cos(\omega t-2\pi\frac{r_1}{\lambda}+\varphi_{10}),y_2=A_2\cos(\omega t-2\pi\frac{r_2}{\lambda}+\varphi_{20})$。
			- 则叠加后的强度为
			  $$
			  I=I_1+I_2+2\sqrt{I_1I_2}\cos\Delta\varphi
			  $$
			  $$
			  \Delta\varphi=\varphi_{20}-\varphi_{10}-2\pi\frac{r_2-r_1}{\lambda}
			  $$
		- **特殊情况**
			- 振动加强：
				- 当 $\Delta\varphi=2k\pi$ 时，$I=I_1+I_2+2\sqrt{I_1I_2}$。
				- 如果 $\varphi_{10}=\varphi_{20}$，则条件简化为 $\delta=r_2-r_1=k\lambda$。
			- 振动减弱：
				- 当 $\Delta\varphi=(2k+1)\pi$ 时， $I=I_1+I_2-2\sqrt{I_1I_2}$ 。
				- 如果 $\varphi_{10}=\varphi_{20}$ ，则条件简化为 $\delta=r_2-r_1=\frac{2k+1}{2}\lambda$ 。
	- **驻波**
		- **定义**
			- 波源发出的波向正方向传递，经过反射产生负方向传递的波，一定条件下，两者叠加形成驻波。
			- 设入射波的函数为 $y_1=A\cos(\omega t-2\pi\frac{x}{\lambda}),y_2=A\cos(\omega t+2\pi\frac{x}{\lambda})$，则叠加后为
			  $$
			  y=2A\cos 2\pi\frac{x}{\lambda}\cos\omega t
			  $$
		- **性质**
			- 驻波中，每一质点的振幅与 $x$ 相关，为 $2A\cos 2\pi\frac{x}{\lambda}$，振幅最大处为波腹，为零处为波节。
			- 每一段中的振动相位相同，相邻段反相。
			- 如果 $2A\cos 2\pi\frac{x}{\lambda}>0$，则这一段的相位为 $\omega t$，否则为 $\omega t+\pi$。
			- 相邻的波腹或波节距离为 $\frac{\lambda}{2}$。
			- 当各质点位移最大时，动能为零，势能最大，其中在波节附近。当各质点位移为零时，势能为零，动能最大，其中在波腹附近。
- **半波损失**
	- 对于机械波，两种介质中，特性阻抗 $Z=\rho u$ 较大的为波密介质，较小的波疏介质。
	- 波由波疏介质入射到波密介质上发生反射时，反射波相位会变化 $\pi$，即变化了半个波长。
	- 由波密介质入射到波疏介质上不发生半波损失。
	- 若形成驻波，则发生半波损失时反射处为波节，不发生时为波腹。
	- 对于电磁波，也存在半波损失。发生条件类似，折射率大的为光密介质，小的为光疏介质。