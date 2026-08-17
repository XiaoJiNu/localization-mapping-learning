# 关键推导

所有推导使用列向量和 `{}^{A}T_B` 将 B 中坐标映射到 A 的约定。

## 1. 变换复合

已知：

$$
{}^{A}p = {}^{A}T_B{}^{B}p,
\qquad
{}^{B}p = {}^{B}T_C{}^{C}p
$$

代入得到：

$$
{}^{A}p
= {}^{A}T_B{}^{B}T_C{}^{C}p
= {}^{A}T_C{}^{C}p
$$

因此：

$$
\boxed{{}^{A}T_C = {}^{A}T_B{}^{B}T_C}
$$

检查点：乘号两侧相邻的 B 正好消去。

## 2. 齐次变换求逆

设：

$$
{}^{A}T_B =
\begin{bmatrix}R&t\\0&1\end{bmatrix}
$$

由 `{}^{A}p=R{}^{B}p+t` 得：

$$
{}^{B}p=R^{\mathsf T}{}^{A}p-R^{\mathsf T}t
$$

所以：

$$
\boxed{({}^{A}T_B)^{-1}={}^{B}T_A=
\begin{bmatrix}
R^{\mathsf T}&-R^{\mathsf T}t\\
0&1
\end{bmatrix}}
$$

容易犯的错误是写成 `-t`。只有在两个坐标系方向完全相同时，这个简化才成立。

## 3. 点与方向向量

齐次点和方向分别写成：

$$
\bar p=\begin{bmatrix}p\\1\end{bmatrix},
\qquad
\bar v=\begin{bmatrix}v\\0\end{bmatrix}
$$

因此：

$$
T\bar p=\begin{bmatrix}Rp+t\\1\end{bmatrix},
\qquad
T\bar v=\begin{bmatrix}Rv\\0\end{bmatrix}
$$

这说明平移改变点的位置，但不改变速度方向、法向量等纯方向量。

## 4. `map→odom` 的计算

若全局定位给出 `{}^{map}T_{base}`，局部里程计给出 `{}^{odom}T_{base}`，由

$$
{}^{map}T_{base}={}^{map}T_{odom}{}^{odom}T_{base}
$$

右乘 `({}^{odom}T_{base})^{-1}`：

$$
\boxed{{}^{map}T_{odom}
={}^{map}T_{base}({}^{odom}T_{base})^{-1}}
$$

全局修正更新左侧这项，就能保留局部里程计的连续输出。

## 自主练习

不要直接看代码，先完成以下操作：

1. 设 B 相对 A 绕 `+z` 旋转 90°，且 B 原点在 A 中为 `[1,2,0]^T`，写出 `{}^{A}T_B`。
2. 将 `{}^{B}p=[1,0,0]^T` 映射到 A。
3. 手算逆变换，再把结果映射回 B。
4. 用数值程序验证两个方向的误差小于 `1e-9`。
