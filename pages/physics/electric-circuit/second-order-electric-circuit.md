---
tags:
  - physics
  - electric-circuits
  - dynamic-electric-circuits
---
- **定义**
	- 如果一个电路包含两个个动态元件（电容和电感），则这个电路就是二阶电路。
	- 在分析方法上，二阶电路与一阶电路相似，都对动态元件外的部分进行等效，使用微分方程表示电路。
	- 二阶电路使用二阶常系数线性微分方程表示。
- **RLC 串联电路**
	- **定义**
		- 电路中含有电阻 $R$、电感 $L$、电阻 $C$ 和直流电压源 $u_{\mathrm{OC}}$，四个元件串联。
		- 电路对应微分方程为
		  $$
		  LC\frac{\mathrm d^2u_C(t)}{\mathrm dt^2}+RC\frac{\mathrm du_C(t)}{\mathrm dt}+u_C(t)=u_{\mathrm{OC}}
		  $$
		- RLC 串联电路一般先求解 $u_C(t)$ 较为方便。
	- **求解**
		- 根据[二阶常系数线性微分方程](/pages/mathematics/calculus/linear-differential-equation.md#xp7c9l)的求解方法，将 $u_C(t)$ 的求解分为齐次通解 $u_{C\mathrm h}(t)$ 和特解 $u_{C\mathrm p}(t)$，最后代入初值条件。
		- 齐次通解实为电路的零输入响应。
		- 根据特征方程 $LCs^2+RCs+1=0$，写出 $u_{C\mathrm h}(t)$ 的形式。
		- $u_{\mathrm{OC}}$ 是常数，则 $u_{C\mathrm p}(t)=u_{\mathrm{OC}}$。
		- 使用 $u_C(0)$ 和 $i_L(0)$ 解出方程，注意 $i_L(0)$ 不是 $u_C(t)$ 在 $t=0$ 的导数。
- **GCL 并联电路**
	- **定义**
		- 电路中含有电导 $G$、电感 $L$、电阻 $C$ 和直流电流源 $i_{\mathrm{SC}}$，四个元件并联。
		- 电路对应微分方程为
		  $$
		  LC\frac{\mathrm d^2i_L(t)}{\mathrm dt^2}+GL\frac{\mathrm di_L(t)}{\mathrm dt}+i_L(t)=i_{\mathrm{SC}}
		  $$
	- **求解**
		- 与 RLC 串联电路类似。
