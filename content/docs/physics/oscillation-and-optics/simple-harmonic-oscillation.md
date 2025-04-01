---
tags:
  - physics
  - oscillation
---
- **定义**
    - **基本概念**
        - 合力为零的位置定义为平衡位置。
        - 振动物体偏离平衡位置时使其恢复原来位置的力定义为恢复力。
        - 表达式为
          $$
          x=A\cos(\omega t+\varphi)
          $$
          $$
          v=-A\omega\sin(\omega t+\varphi)=A\omega\cos\left(\omega t+\varphi+\frac{\pi}{2}\right)
          $$
          $$
          a=-A\omega^2\cos(\omega t+\varphi)=A\omega^2\cos\left(\omega t+\varphi+\pi\right)
          $$
    - **特征量**
        - **振幅**
            - 任意时刻：
              $$
              A=\sqrt{x^2+\left(\frac{v}{\omega}\right)^2}
              $$
        - **周期、频率、角频率**
            - 周期为 $T$，频率为 $\nu$，角频率为 $\omega$。
            - 角频率是 $2\pi$ 秒内的振动次数。
        - **相位、初相**
            - 相位 $\omega t+\varphi$ 描述了 $t$ 时刻的振动状态。
            - 初相 $\varphi$ 是 $t=0$ 的振动状态。
            - $$
              \cos\varphi=\frac{x_0}{A}
              $$
              $$
              \sin\varphi=-\frac{v_0}{A\omega}
              $$
              $$
              \varphi=\arctan\left(-\frac{x_0\omega}{v_0}\right)
              $$
        - **相位差**
            - $\Delta \varphi=\varphi_2-\varphi_1$，若 $\Delta\varphi>0$，则 2 超前 1，反之落后。
            - $\Delta\varphi$ 一般取 $[-\pi,\pi]$。
            - 时间差为 $\Delta t=\frac{\Delta\varphi}{\omega}$。
    - **表示**
        - **公式**
        - **旋转矢量**
            - 旋转矢量 $\boldsymbol A$ 长度为 $A$，不断绕原点旋转。
            - $\boldsymbol A$ 与 $x$ 轴正方向夹角为相位。
            - $\boldsymbol A$ 的终点做匀速圆周运动，其各变量在 $x$ 轴上的投影与简谐振动有关。
                - 终点的投影是简谐振动的位置。
                - 终点的速度是沿切线方向的矢量，在 $x$ 轴上的投影是简谐振动的速度。
                - 终点的向心加速度是指向圆心的矢量，在 $x$ 轴上的投影是简谐振动的加速度。
- **常见简谐振动**
    - **弹簧振子**
        - 质量为 $m$ 的物体连接在弹簧 $k$ 上。
        - $$
          \omega=\sqrt{\frac{k}{m}}\iff T=2\pi\sqrt{\frac{m}{k}}
          $$
    - **复摆**
        - $$
          \omega=\sqrt{\frac{mgh}{J}}\iff T=2\pi\sqrt{\frac{J}{mgh}}
          $$
- **简谐振动的能量**
    - **瞬时值**
        - 动能：
          $$
          E_{\mathrm k}=\frac{1}{2}m\omega^2A^2\sin^2(\omega t+\varphi)=\frac{1}{2}kA^2\sin^2(\omega t+\varphi)
          $$
        - 势能：
          $$
          E_{\mathrm p}=\frac{1}{2}m\omega^2A^2\cos^2(\omega t+\varphi)=\frac{1}{2}kA^2\cos^2(\omega t+\varphi)
          $$
        - 动能和势能的角频率是 $2\omega$。
        - 机械能：
          $$
          E=E_{\mathrm k}+E_{\mathrm p}=\frac{1}{2}kA^2
          $$
    - **平均值**
        - $$
          \bar{E}_{\mathrm k}=\frac{1}{2}E=\bar{E}_{\mathrm p}=\frac{1}{4}kA^2
          $$
        - 系统确定时（$\omega$ 一定），能量与振幅的平方成正比
          $$
          A=\sqrt{\frac{2E}{k}}
          $$
    - **能量方法推导简谐振动**
        - 对于系统的机械能满足：
          $$
          E=\frac{1}{2}mv^2+\frac{1}{2}kx^2=\mathrm{constant}
          $$
        - 对于以上方程对 $t$ 求导：
          $$
          mv\frac{\mathrm dv}{\mathrm dt}+kx\frac{\mathrm dx}{\mathrm dt}=0\iff \frac{\mathrm d^2x}{\mathrm dt^2}+\omega^2x=0
          $$
- **简谐振动的合成**
    - **同方向同频率合成**
        - 一个质点同时参与两个简谐振动 $x_1=A_1\cos(\omega t+\varphi_1),x_2=\cos(\omega t+\varphi_2)$。
        - 合成的运动仍然是简谐振动，并且有
          $$
          A=\sqrt{A_1^2+A_2^2+2A_1A_2\cos(\varphi_1-\varphi_2)}
          $$
          $$
          \varphi=\arctan\frac{A_1\sin\varphi_1+A_2\sin\varphi_2}{A_1\cos\varphi_1+A_2\cos\varphi_2}
          $$
        - 同时可以利用旋转矢量的合成来求解。一般使用这种方法。
        - 当 $\varphi_2-\varphi_1=2k\pi$ 时，振幅最大，当 $\varphi_2-\varphi_1=(2k+1)\pi$ 时，振幅最小。
    - **同方向不同频率合成**
        - 一个质点同时参与两个简谐振动 $x_1=A_1\cos(\omega_1 t+\varphi_1),x_2=\cos(\omega_2 t+\varphi_2)$。
        - 此时合运动不是简谐振动，振幅不断加强和减弱，$\omega=|\omega_1-\omega_2|$。
        - 当 $\omega_1,\omega_2$ 都很大并且很接近时，振幅的强弱变化就会缓慢，这种现象称为拍。
        - 拍频 $\nu=|\nu_1-\nu_2|$ 表示振幅的强弱变化的频率。
