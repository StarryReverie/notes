---
tags:
  - programming
  - matlab
---

- **符号运算**
    - **定义**
        - ```matlab
          sym_x = sym('x'); % 定义一个符号变量，用 sym_x 在代码中引用，显示为 x
          syms a b; % 同时定义两个符号变量 a 和 b
          ```
    - **使用**
        - 符号变量使用与普通变量没有区别。
        - 包含符号变量的表达式赋值给其他变量，这个变量也会变成符号变量。
    - **数值代入**
        - 符号变量的表达式无法直接代入数值，需要使用 `matlabFunction` 函数转换。
        - ```matlab
          syms x y;
          z = x^2 + y^2;
          func_z = matlabFunction(z);
          % func_z = @(x,y)x.^2+y.^2
          ```
        - `matlabFunction` 函数自动识别表达式中的符号，创建对应参数的匿名函数。
        - 入参可以是数组。
- **代数运算**
    - **因式分解**
        - ```matlab
          syms x;
          f = factor(x^3 - 1);
          % f = [x - 1, x^2 + x + 1]
          ```
          ```matlab
          syms a b c d;
          % 指定对含 b 或 c 的项进行因式分解，其他项因式分解的结果放在最前面
          y = -a*b^5*c*d*(a^2 - 1)*(a*d - b*c);
          f = factor(y, [b, c]);
          % f = [-a*d*(a - 1)*(a + 1), b, b, b, b, b, c, a*d - b*c]
          ```
    - **展开**
        - ```matlab
          syms x y
          f = expand((x + y)^3);
          % f = x^3 + 3*x^2*y + 3*x*y^2 + y^3
          ```
    - **合并同类项**
        - ```matlab
          syms x y;
          f = x^2*y - x*y^2 - x*y + y^2;
          f_x = collect(f); % 默认对 x 合并
          % f_x = y*x^2 + (- y^2 - y)*x + y^2
          f_y = collect(f, y); % 指定对 y 合并
          % f_y = (1 - x)*y^2 + (x^2 - x)*y
          ```
    - **分式通分**
        - ```matlab
          syms x y;
          f = 1/x - 1/y;
          num = numden(f); % 返回分子
          % num = y - x
          [num, den] = numden(f); % 返回分子、分母
          % num = y - x, den = xy
          ```
- **线性代数**
    - **构造**
        - 单位矩阵：`A = eye(n)`，返回 $n$ 阶单位矩阵。
        - 零矩阵：`A = zeros(n)`，返回 $n$ 阶零矩阵。
        - 对角矩阵：`A = diag([a1, a2, a3])`，返回以 `a1, a2, a3` 为对角元的对角矩阵。
        - 浮点数随机矩阵：`A = rand(n)`，返回 $n$ 阶矩阵，元素为 $[0,1]$ 内的随机浮点数。
        - 整数随机矩阵：`A = magic(n)`，返回 $n$ 阶矩阵，元素为 $[1,n^2]$ 中的整数的乱序排列。
    - **运算**
        - 加法：`A + B`
        - 乘法：`A*B`
        - 乘幂：`A^n`
        - 点乘：`A.*B`，矩阵元素对应相乘。其他运算也有类似的点运算。
        - 转置：`A_transpose = A'`
        - 求逆：`A_inverse = inv(A)`
        - 行列式：`d = det(A)`
        - 特征值
            - `e = eig(A)`：返回矩阵特征值，以列向量给出。
            - `[V, D] = eig(A)`：返回矩阵单位特征向量以及相似的对角矩阵。
        - LU 分解：`[L, U] = lu(A)`
        - 单位化：`B = normalize(A)`，将矩阵的列单位化。
- **多项式**
    - **表示**
        - MATLAB 中多项式用行[向量](/pages/mathematics/linear-algrbra/vector.md)表示。
        - 对于多项式 $a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0$，行向量则是多项式的系数 $\begin{bmatrix}a_n & a_{n-1} & \cdots & a_1 & a_0\end{bmatrix}$。
    - **运算**
        - **求值**
            - ```matlab
              p = [1 -3 2]; % p(x) = x^2 - 3*x + 2
              v = polyval(p, 3) % 求 p(3)
              % v = 
              ```
        - **特征多项式**
            - ```matlab
              A = [[16, 2, 3, 13]; [5, 11, 10, 8]; [9, 7, 6, 12]; [4, 14, 15, 1]]
              p = poly(A); % 求方阵 A 的特征多项式系数向量
              % p = 1.0e+03 * [0.0010, -0.0340, -0.0800, 2.7200, 0.0000]
              ```
            - ```matlab
              lambda = [1, 2, -2, 0];
              p = poly(lambda); % 求特征值对应的特征多项式
              % p = [1, -1, -4, 4, 0]
              ```
        - **乘法**
            - ```matlab
              p = [1, -3, 2]; % p(x) = x^2 - 3*x + 2
              q = [2, -1]; % q(x) = 2*x - 1
              pq = conv(p, q); % 系数向量的卷积就是多项式乘积的系数, p(x)*q(x) = 2*x^3 - 7*x^2 + 7*x - 2
              % pq = [2 -7 7 -2]
              ```
        - **除法**
            - ```matlab
              p = [1, -3, 2]; % p(x) = x^2 - 3*x + 2
              q = [2, -1]; % q(x) = 2*x - 1
              [d, r] = deconv(p, q); % 多项式除法，p(x) = d(x)*q(x) + r(x)
              % d = [0.5000, -1.2500], r = [0, 0, 0.7500]
              ```
        - **求根**
            - ```matlab
              f = [1, -3, 2]; % f(x) = x^2 - 3*x + 2
              r = roots(f); % 求 f(x) = 0 的根
              % r = [2; 1]
              % 根以列向量形式给出
              ```
        - **求导**
            - ```matlab
              f = [1, 2, -1, 4, 1]; % f(x) = x^4 + 2*x^3 - x^2 + 4*x + 1
              der_f = polyder(f); % 对 f(x) 求导
              % der_f = [4, 6, -2, 4]
              ```
        - **拟合**
            - ```matlab
              x = [1, 3.51, 6.4, 9.92, 8.76];
              y = [0.48, 1.03, 2.31, 6.48, 4.49];
              p = polyfit(x, y, 2); % 用二次多项式拟合
              % p = [0.0865, -0.3067, 0.8058]
              ```
- **微积分**
    - **极限**
        - ```matlab
          syms x;
          f = sin(x)/x;
          l = limit(f) % 默认求自变量为 x 时 f(x) 在 x = 0 的极限
          % l = 1
          l = limit(f, x, pi/2) % 求 f(x) 在 x = 1 的极限
          % l = 2/pi
          ```
        - ```matlab
          syms x;
          f = abs(x)/x;
          l = limit(f, x, 0, 'Left'); % 求左极限
          % l = -1
          l = limit(f, x, 0, 'Right'); % 求右极限
          % l = 1
          ```
    - **求导**
        - ```matlab
          syms x;
          f = sin(x);
          d1 = diff(f); % 默认以 x 为自变量求 f'
          % d1 = 2*x*cos(x^2)
          d2 = diff(f, x, 2); % 求 f''(x)
          d2 = 2*cos(x^2) - 4*x^2*sin(x^2)
          ```
    - **积分**
        - ```matlab
          syms x;
          f = f = x^(1/2)/(1 + x^(1/3));
          intf = int(f) % 求 f(x) 的不定积分
          % intf = 6*atan(x^(1/6)) + 2*x^(1/2) - 6*x^(1/6) - (6*x^(5/6))/5 + (6*x^(7/6))/7
          intf = int(f, 0, 1) % 求 f(x) 在 [0, 1] 上的定积分
          % intf = (3*pi)/2 - 152/35
          ```
