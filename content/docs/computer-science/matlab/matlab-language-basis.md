---
tags:
  - programming
  - matlab
---

- **常用基础函数**
    - `whos`：列出工作空间中的变量名及其具体信息
    - `who`：列出工作空间中的变量名
    - `clear`：清除工作区变量，可在后面加上变量名以清除指定变量
    - `clc`：清除 REPL 内容
    - `quit` / `exit`：关闭 MATALB
    - `help`：显示指定函数的简短使用说明
    - `quit`：以网页形式显示指定函数的帮助页
- **常用符号**
    - `%`：注释
    - `;`：放在最后，将表达式变为语句，不在 REPL 中输出结果
    - `:`：生成数组，有以下若干种形式：
        - `start:end`：生成从 `start` 到 `end` 中的所有整数组成的数组
        - `start:step:end`：以 `step` 为间隔，从 `start` 到 `end` 取出整数组成的数组，如果 `end` 不是 `start` 加上若干个 `step`，则数组不包含 `end`
            - `start:` / `:end` / `:`：用于下标处，由解释器自动推导缺失部分
        - `{}`：用于元胞数组定义，其中元素可以是任意类型。也用于元胞数组的下标访问
        - `@`：用于已定义函数的名称前，表示获取函数句柄。也可以用于定义匿名函数
- **数据类型**
    - **整数**
        - `int8`，`int16`，`int32`，`int64`，`uint8`，`uint16`，`uint32`，`uint64`
    - **浮点数**
        - `single`，`double`
        - 默认所有数字的字面量都是 `double` 类型。
    - **复数**
        - 字面量可以把 `i` 或 `j` 加到数字后面表示虚部。
        - 可以使用 `complex(a, b)` 创建 $a+bi$。
    - **布尔 / 逻辑**
        - 在 MATLAB 中类型名为 `logical`，但用 `boolean` 函数转型。
    - **数组**
        - 用 `[]` 定义，可以定义一维或二维数组，无法定义更高维。
        - 一维数组有行列之分，若元素按列排布，则数组为向量。
        - 二维数组为矩阵。
        - `[]` 中用逗号或空格分隔的元素按行排列，用分号分隔的元素按列排列。
        - 数组中的子数组若用逗号或空格分隔，则子数组会合并，如 `[[1 2] [3 4]] => [1 2 3 4]`，该行为与分块矩阵类似。
    - **字符数组**
        - 用 `'` 包住的字符组成字符数组。
        - 单个字符是长度为 1 的字符数组。
        - 字符数组中的元素也是整数，其值是字符的 ASCII 值。
        - 假设 `a` 和 `b` 是字符数组，它们的拼接可以使用 `[a b]` 或 `strcat(a, b)`，但不可以使用 `a + b`，这会导致 `a` 和 `b` 中的数组元素逐个相加。
    - **字符串**
        - 用 `"` 包住的字符组成字符串。
        - 字符串拼接可以使用 `+`，也可以用 `strcat` 函数。
        - 字符串是一个整体的变量，不是数组，也不能按下标访问。
- **控制流**
    - **`if` 条件控制**
        - ```
          if expression
              statements
          elseif expression
              statements
          else
              statements
          end
          ```
    - **`switch` 条件控制**
        - ```
          switch switch_expression
             case case_expression
                statements
             case case_expression
                statements
             ...
             otherwise
                statements
          end
          ```
    - **`for`  循环控制**
        - ```
          for index = values
              statements
          end
          ```
        - 这里的 `values` 是任意可迭代的值，包括 `begin:step:end`、数组等。
        - 每次循环 `index` 会是数组的每一列的值。对于一个 $m\times n$ 矩阵，会循环 $n$ 次，每次获得一个 $m$ 元列向量。
        - 循环中可以使用 `break` 和 `continue` 语句退出循环或跳过当前循环。
    - **`while` 循环控制**
        - ```
          while expression
              statements
          end
          ```
