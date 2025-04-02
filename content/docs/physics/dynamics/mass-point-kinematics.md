---
title: 质点运动学
weight: 100
math: true
---

- **运动参量**
    - **位置矢量**
        - **定义**
            - 选定坐标系后，从坐标系原点向质点的向量称为位置矢量，记作 $\boldsymbol r$，单位为 $\text m$。
            - 记 $r=|\boldsymbol r|$。
        - **表示**
            - 在空间直角坐标系中，质点在 $(x,y,z)$，则
              $$
              \boldsymbol r=x\boldsymbol i+y\boldsymbol j+z\boldsymbol k
              $$
              $$
              r=\sqrt{x^2+y^2+z^2}
              $$
            - 在极坐标系中，质点在 $(r,\theta)$，则
              $$
              \boldsymbol r=r\boldsymbol e_r
              $$
              其中 $\boldsymbol e_r$ 与极轴夹角为 $\theta$。
            - 一般还会定义 $\boldsymbol e_\theta$，其方向为 $\theta$ 增加的方向，与 $\boldsymbol e_r$ 垂直。
            - $\boldsymbol e_r,\boldsymbol e_\theta$ 会随着 $\theta$ 的变化而改变方向。
        - **位移矢量**
            - 在 $\Delta t$ 时间内，位置矢量的变化量称为位移矢量，定义为
              $$
              \Delta\boldsymbol r=\boldsymbol r(t+\Delta t)-\boldsymbol r(t)
              $$
            - 位移矢量大小为 $|\Delta\boldsymbol r|$。
            - 而这需要与位置矢量大小的变化量 $\Delta r$ 区分，即
              $$
              \Delta r=r(t+\Delta t)-r(t)=|\boldsymbol r(t+\Delta t)|-|\boldsymbol r(t)|
              $$
        - **路程**
            - 质点在空间中运动的实际路径的长度称为路程，记作 $\Delta s$。
            - 在 $\mathrm dt$ 内，$\mathrm ds=|\mathrm d\boldsymbol r|$。
    - **速度**
        - **平均速度**
            - 质点在 $\Delta t$ 内发生位移 $\Delta\boldsymbol r$，定义平均速度为
              $$
              \bar{\boldsymbol v}=\frac{\Delta\boldsymbol r}{\Delta t}
              $$
            - 平均速度单位为 $\text{m/s}$。
            - 平均速度大小为
              $$
              |\bar{\boldsymbol v}|=\frac{|\Delta\boldsymbol r|}{\Delta t}
              $$
              注意与 $\Delta r$ 区别。
            - 平均速度方向与位移相同。
        - **速度 / 瞬时速度**
            - 质点在无限小时间间隔内发生位移，平均速度则为瞬时速度，即
              $$
              \boldsymbol v=\lim_{\Delta t\to 0}\bar{\boldsymbol v}=\lim_{\Delta t\to 0}\frac{\Delta\boldsymbol r}{\Delta t}=\frac{\mathrm d\boldsymbol r}{\mathrm dt}
              $$
            - 速度单位为 $\text{m/s}$。
            - 速度大小定义为速率：
              $$
              v=|\boldsymbol v|=\left|\frac{\mathrm d\boldsymbol r}{\mathrm dt}\right|=\left|\frac{\mathrm ds}{\mathrm dt}\right|
              $$
            - 速度方向为位移矢量的轨迹的切线方向。
            - 空间直角坐标系中，速度表示为
              $$
              \boldsymbol v=v_x\boldsymbol i+v_y\boldsymbol j+v_z\boldsymbol k=\frac{\mathrm dx}{\mathrm dt}\boldsymbol i+\frac{\mathrm dy}{\mathrm dt}\boldsymbol j+\frac{\mathrm dz}{\mathrm dt}\boldsymbol k
              $$
              $$
              v=\sqrt{v_x^2+v_y^2+v_z^2}
              $$
            - 极坐标系中，速度表示为
              $$
              \boldsymbol v=\frac{\mathrm d(r\boldsymbol e_r)}{\mathrm dt}=\frac{\mathrm dr}{\mathrm dt}\boldsymbol e_r+r\frac{\mathrm d\boldsymbol e_r}{\mathrm dt}=\frac{\mathrm dr}{\mathrm dt}\boldsymbol e_r+r\frac{\mathrm d\theta}{\mathrm dt}\boldsymbol e_\theta
              $$
              $$
              v=\sqrt{\left(\frac{\mathrm dr}{\mathrm dt}\right)^2+r^2\left(\frac{\mathrm d\theta}{\mathrm dt}\right)^2}
              $$
            - 由于 $\boldsymbol e_r,\boldsymbol e_\theta$ 会改变方向，所以以上公式的最后一步需要
              $$
              \frac{\mathrm d\boldsymbol e_r}{\mathrm dt}=\frac{\mathrm d\theta}{\mathrm dt}\boldsymbol e_\theta
              $$
              $$
              \frac{\mathrm d\boldsymbol e_\theta}{\mathrm dt}=-\frac{\mathrm d\theta}{\mathrm dt}\boldsymbol e_r
              $$
    - **加速度**
        - **平均加速度**
            - 质点在 $\Delta t$ 内速度变化 $\Delta\boldsymbol v$，定义平均加速度为
              $$
              \bar{\boldsymbol a}=\frac{\Delta\boldsymbol v}{\Delta t}
              $$
            - 平均加速度单位为 $\mathrm{m/s^2}$。
        - **加速度 / 瞬时加速度**
            - 质点在无限小时间间隔内速度变化，定义加速度为
              $$
              \boldsymbol a=\frac{\mathrm d\boldsymbol v}{\mathrm dt}
              $$
            - 空间直角坐标系中，加速度表示为
              $$
              \boldsymbol a=a_x\boldsymbol i+a_y\boldsymbol j+a_z\boldsymbol k=\frac{\mathrm d^2x}{\mathrm dt^2}\boldsymbol i+\frac{\mathrm d^2y}{\mathrm dt^2}\boldsymbol j+\frac{\mathrm d^2z}{\mathrm dt^2}\boldsymbol k
              $$
            - 极坐标系中，速度表示为
              $$
              \boldsymbol a=\frac{\mathrm d\boldsymbol v}{\mathrm dt}=\frac{\mathrm d}{\mathrm dt}\left(\frac{\mathrm dr}{\mathrm dt}\boldsymbol e_r+r\frac{\mathrm d\theta}{\mathrm dt}\boldsymbol e_\theta\right)=\left[\frac{\mathrm d^2r}{\mathrm dt^2}-r\left(\frac{\mathrm d\theta}{\mathrm dt}\right)^2\right]\boldsymbol e_r+\left(r\frac{\mathrm d^2\theta}{\mathrm dt^2}+2\frac{\mathrm dr}{\mathrm dt}\frac{\mathrm d\theta}{\mathrm dt}\right)\boldsymbol e_\theta
              $$
    - **角速度** <span id="i9fcjq"></span>
        - 设某个质点沿圆心位于 $O$ 点、半径为 $R$ 的圆周做运动，定义角速度为
          $$
          \omega=\lim_{\Delta t\to 0}\frac{\Delta\theta}{\Delta t}=\frac{\mathrm d\theta}{\mathrm dt}
          $$
        - 角速度为 $\mathrm{rad/s}$ 或 $\mathrm{s^{-1}}$。
        - 一般称圆周运动中的速度 $\boldsymbol v$ 为线速度，角速度与线速度大小有如下关系：
          $$
          v=R\omega
          $$
    - **角加速度** <span id="snpyim"></span>
        - 角加速度描述角速度变化快慢，定义为
          $$
          \alpha=\lim_{\Delta t\to 0}\frac{\Delta\omega}{\Delta t}=\frac{\mathrm d\omega}{\mathrm dt}
          $$
- **相对运动**
    - 质点 $P$ 相对 $S$ 有 $\boldsymbol r_{PS},\boldsymbol v_{PS},\boldsymbol a_{PS}$，相对 $S'$ 有 $\boldsymbol r_{PS'},\boldsymbol v_{PS'},\boldsymbol a_{PS'}$，$S'$ 相对 $S$ 有 $\boldsymbol r_{S'S},\boldsymbol v_{S'S},\boldsymbol a_{S'S}$，则
      $$
      \boldsymbol r_{PS}=\boldsymbol r_{PS'}+\boldsymbol r_{S'S}
      $$
      $$
      \boldsymbol v_{PS}=\boldsymbol v_{PS'}+\boldsymbol v_{S'S}
      $$
      $$
      \boldsymbol a_{PS}=\boldsymbol a_{PS'}+\boldsymbol a_{S'S}
      $$
- **圆周运动**
    - 圆周运动的加速度一般分解为两个方向：
        - 切向加速度：
          $$
          a_{\mathrm t}=\frac{\mathrm dv}{\mathrm dt}=R\alpha
          $$
        - 法向加速度：
          $$
          a_{\mathrm n}=\frac{v^2}{R}=R\omega^2=\omega v
          $$
    - 加速度大小为
      $$
      |\boldsymbol a|=\sqrt{a_{\mathrm t}^2+a_{\mathrm n}^2}
      $$
    - 对于一般曲线运动，则把半径换为曲率半径。
