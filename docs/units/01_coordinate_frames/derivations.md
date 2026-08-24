# 参考推导与核对步骤

本页包含参考推导。请先在[无答案工作簿](workbook.md#阶段-3闭卷推导)中完成完整尝试，再打开本页核对第一处错误。

参考答案存在不代表学习者已经完成推导。可验证证据应保存在 `sessions/` 中，并同时保留原始错误、修正过程和不看答案后的再次推导。

所有推导使用列向量，并约定变换的下标表示源坐标系，左上标表示目标坐标系。

## 1. 变换复合

已知：

$$
{}^{A}\mathbf p = {}^{A}\mathbf T_B{}^{B}\mathbf p,
\qquad
{}^{B}\mathbf p = {}^{B}\mathbf T_C{}^{C}\mathbf p
$$

代入得到：

$$
{}^{A}\mathbf p
= {}^{A}\mathbf T_B{}^{B}\mathbf T_C{}^{C}\mathbf p
= {}^{A}\mathbf T_C{}^{C}\mathbf p
$$

因此：

$$
\boxed{{}^{A}\mathbf T_C = {}^{A}\mathbf T_B{}^{B}\mathbf T_C}
$$

检查点：乘号两侧相邻的 $B$ 正好消去。

## 2. 齐次变换求逆

设：

$$
{}^{A}\mathbf T_B =
\begin{bmatrix}\mathbf R&\mathbf t\\\mathbf 0^{\mathsf T}&1\end{bmatrix}
$$

从点变换的旋转和平移形式开始：

$$
{}^{A}\mathbf p=\mathbf R{}^{B}\mathbf p+\mathbf t
$$

移项得到：

$$
{}^{B}\mathbf p=\mathbf R^{\mathsf T}{}^{A}\mathbf p-\mathbf R^{\mathsf T}\mathbf t
$$

所以：

$$
\boxed{\left({}^{A}\mathbf T_B\right)^{-1}={}^{B}\mathbf T_A=
\begin{bmatrix}
\mathbf R^{\mathsf T}&-\mathbf R^{\mathsf T}\mathbf t\\
\mathbf 0^{\mathsf T}&1
\end{bmatrix}}
$$

容易犯的错误是把逆变换的平移直接写成 $-\mathbf t$。对给定的
$\mathbf t$，只有在 $\mathbf R^{\mathsf T}\mathbf t=\mathbf t$ 时，两者才相同；
若要求对任意平移都能这样简化，则必须有 $\mathbf R=\mathbf I$。

## 3. 点与方向向量

齐次点和方向分别写成：

$$
\bar{\mathbf p}=\begin{bmatrix}\mathbf p\\1\end{bmatrix},
\qquad
\bar{\mathbf v}=\begin{bmatrix}\mathbf v\\0\end{bmatrix}
$$

因此：

$$
\mathbf T\bar{\mathbf p}=\begin{bmatrix}\mathbf R\mathbf p+\mathbf t\\1\end{bmatrix},
\qquad
\mathbf T\bar{\mathbf v}=\begin{bmatrix}\mathbf R\mathbf v\\0\end{bmatrix}
$$

这说明平移改变点的位置，但不改变速度方向、法向量等纯方向量。

## 4. `odom` 到 `map` 变换的计算

若全局定位给出车体在地图坐标系中的位姿，局部里程计给出车体在里程计坐标系中的位姿，则有：

$$
{}^{\mathrm{map}}\mathbf T_{\mathrm{base}}
={}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}{}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}
$$

在等式两边右乘局部里程计变换的逆：

$$
\boxed{{}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}
={}^{\mathrm{map}}\mathbf T_{\mathrm{base}}
\left({}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}\right)^{-1}}
$$

全局修正更新左侧这项，就能保留局部里程计的连续输出。

## 数值练习

不要直接看代码，先完成以下操作：

1. 设坐标系 $B$ 相对坐标系 $A$ 绕 $+z$ 旋转 $90^\circ$，且 $B$ 的原点在 $A$ 中为 $[1,2,0]^{\mathsf T}$，写出从坐标系 $B$ 映射到坐标系 $A$ 的齐次变换。
2. 将点在坐标系 $B$ 中的坐标 $[1,0,0]^{\mathsf T}$ 映射到坐标系 $A$。
3. 手算逆变换，再把结果映射回坐标系 $B$。
4. 用数值程序验证两个方向的误差小于 $10^{-9}$。

该练习与工作簿 D1 对应。完成手算后，可以用前文公式核对结构，再通过[实验 001](../../../experiments/exp_001_transform_chain/README.md)形成本人运行的数值证据。
