---
title: 质点系和质心
weight: 100
math: true
---

- **质点系**
    - 若干个质点共同组成的系统称为质点系。
    - 质点系中各质点的总体情况可能很复杂，所以研究质点系一般会选取质心。
    - 质心是各质点质量的集中，位置是各质点位置的加权平均。
- **质心位置矢量** <span id="pmrdyk"></span>
    - 离散的质点的情况：
      $$
      \boldsymbol r_C=\frac{\sum\limits_{i=1}^n m_i\boldsymbol r_i}{\sum\limits_{i=1}^n m_i}
      $$
    - 这里的质点也可以是其他物体的质心，如果物体由多个规则几何体组成，则可以先计算几何体的质心，再计算整体的质心。
    - 连续物体的情况：
      $$
      \boldsymbol r_C=\frac{\iiint_V \boldsymbol r_i\mathrm dm}{\iiint_V\mathrm dm}
      $$
- **质点系动量与质心动量**
    - $$
      \boldsymbol p=\sum_{i=1}^n \boldsymbol p_i=\sum_{i=1}^n m_i\boldsymbol v_i=m\boldsymbol v_c\ \left(m=\sum_{i=1}^n m_i\right)
      $$
- **质心运动定理**
    - 质点系所受合外力 $\boldsymbol F$ 为各质点受力之和，即
      $$
      \boldsymbol F=\sum_{i=1}^n \boldsymbol F_i
      $$
    - 质心加速度的方向与质点系所受合外力的方向相同，其大小与质点系所受合外力的大小成正比，与质点系的质量成反比，即
      $$
      \boldsymbol F=m\boldsymbol a_C\ \left(m=\sum_{i=1}^n m_i\right)
      $$
    - 展开为
      $$
      \sum_{i=1}^n \boldsymbol F_i=\sum_{i=1}^n m_i\boldsymbol a_i
      $$
    - 质心运动定理在形式上与牛顿第二定律相同，可以看作质点系的牛顿第二定律。
- **质心系** <span id="stv368"></span>
    - 质心在其中静止的坐标系，常将坐标系的点置于质心。
    - 在质心系中，系统的动量为零。
    - 尽管质心系不一定是惯性系，但一些定律在质心系是成立的。
