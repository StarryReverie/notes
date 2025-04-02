---
title: 动量和角动量
weight: 300
math: true
---

- **动量**
    - **动量定理**
        - 质点 / 质点系在一段时间间隔内动量的增量等于合外力在这段时间间隔内的冲量，即
          $$
          \boldsymbol I=\int_{t_1}^{t_2}\boldsymbol F\mathrm dt=\boldsymbol p_2-\boldsymbol p_1
          $$
    - **动量守恒**
        - 若质点系所受合外力为零，则质点系的动量守恒。
        - 动量守恒适用于惯性系和[质心系](/notes/docs/physics/dynamics/mass-point-system-and-centor-of-mass#stv368)。
- **力矩**
    - 作用于质点上的力相对于某个固定点的力矩 $\boldsymbol M$ 定义为
      $$
      \boldsymbol M=\boldsymbol r\times\boldsymbol F
      $$
- **角动量** <span id="ngvw7q"></span>
    - **定义**
        - 质点相对于某个固定点的角动量 $\boldsymbol L$ 定义为
          $$
          \boldsymbol L=\boldsymbol r\times\boldsymbol p
          $$
        - 质点的角动量不仅于参考系有关，还要指出是相对于哪个固定点。
    - **角动量定理**
        - 质点 / 质点系所受合力矩等于角动量对时间的变化率，即
          $$
          \boldsymbol M=\frac{\mathrm d\boldsymbol L}{\mathrm dt}
          $$
        - 积分形式为
          $$
          \int_{t_1}^{t_2}\boldsymbol M\mathrm dt=\boldsymbol L_1-\boldsymbol L_2
          $$
        - 角动量定理的形式与[牛顿第二定律](/notes/docs/physics/dynamics/newtons-law-of-motion#t9cc9r)和动量定理很相似，一个处理转动，一个处理平动。
    - **角动量守恒**
        - 与动量守恒类似，当系统的合力矩为零时，系统的角动量守恒。
