# 参考推导与核对步骤

本页包含工作簿 D1～D6 的参考过程。请先在[工作簿](workbook.md)的“步骤 3：练习与推导”中完成全部题目的独立尝试，再打开本页核对第一处差异。

不要用本页覆盖原始错误。可验证证据应保存在 `sessions/` 中，并同时保留：原始过程、第一处错误、修正原因和不看答案后的再次完成。

本页统一使用列向量。变换右下标表示源坐标系，左上标表示目标坐标系。

## D1：二维点变换

已知：

$$
{}^{A}\mathbf R_B =
\begin{bmatrix}
0 & -1\\
1 & 0
\end{bmatrix}
$$

$$
{}^{A}\mathbf t_B =
\begin{bmatrix}
3\\
1
\end{bmatrix},
\qquad
{}^{B}\mathbf p =
\begin{bmatrix}
2\\
1
\end{bmatrix}
$$

先计算从 $O_B$ 指向 $P$ 的向量在坐标系 $A$ 中的表达：

$$
{}^{A}\mathbf R_B{}^{B}\mathbf p =
\begin{bmatrix}
0 & -1\\
1 & 0
\end{bmatrix}
\begin{bmatrix}
2\\
1
\end{bmatrix}
=
\begin{bmatrix}
-1\\
2
\end{bmatrix}
$$

这个结果不是点 $P$ 在坐标系 $A$ 中的最终坐标。它表示同一个几何向量：

$$
\overrightarrow{O_BP}
$$

在坐标系 $A$ 中的坐标表达。

再加入从 $O_A$ 指向 $O_B$ 的平移：

$$
{}^{A}\mathbf p =
\begin{bmatrix}
-1\\
2
\end{bmatrix}
+
\begin{bmatrix}
3\\
1
\end{bmatrix}
=
\begin{bmatrix}
2\\
3
\end{bmatrix}
$$

纯几何关系为：

$$
\overrightarrow{O_AP} =
\overrightarrow{O_AO_B} +
\overrightarrow{O_BP}
$$

数值关系为：

$$
\begin{bmatrix}
2\\
3
\end{bmatrix}
=
\begin{bmatrix}
3\\
1
\end{bmatrix}
+
\begin{bmatrix}
-1\\
2
\end{bmatrix}
$$

几何检查：从 $O_A$ 向右 3、向上 1 到达 $O_B$，再向左 1、向上 2 到达 $P$，最终为向右 2、向上 3。

## D2：旋转矩阵与坐标轴

对于旋转矩阵：

$$
{}^{A}\mathbf R_B =
\begin{bmatrix}
0 & -1\\
1 & 0
\end{bmatrix}
$$

第一列为：

$$
{}^{A}\mathbf e_{x_B} =
\begin{bmatrix}
0\\
1
\end{bmatrix}
$$

它表示 $B$ 的 $x_B$ 轴在坐标系 $A$ 中向上。

第二列为：

$$
{}^{A}\mathbf e_{y_B} =
\begin{bmatrix}
-1\\
0
\end{bmatrix}
$$

它表示 $B$ 的 $y_B$ 轴在坐标系 $A$ 中向左。

合法旋转矩阵的列向量长度为 1，而且不同列互相垂直。因此：

$$
\mathbf R^{\mathsf T}\mathbf R = \mathbf I
$$

纯旋转还要求：

$$
\det(\mathbf R) = 1
$$

由正交性可得：

$$
\mathbf R^{-1} = \mathbf R^{\mathsf T}
$$

这个性质适用于正交旋转矩阵，不能推广到任意可逆矩阵。

## D3：变换组合

已知点先从坐标系 $C$ 转到 $B$：

$$
{}^{B}\mathbf p =
{}^{B}\mathbf T_C{}^{C}\mathbf p
$$

再从坐标系 $B$ 转到 $A$：

$$
{}^{A}\mathbf p =
{}^{A}\mathbf T_B{}^{B}\mathbf p
$$

把第一式代入第二式：

$$
{}^{A}\mathbf p =
{}^{A}\mathbf T_B
{}^{B}\mathbf T_C
{}^{C}\mathbf p
$$

因此复合变换为：

$$
{}^{A}\mathbf T_C =
{}^{A}\mathbf T_B{}^{B}\mathbf T_C
$$

采用列向量时，最靠近点的矩阵最先作用。实际顺序为：

```text
C → B → A
```

“中间坐标系消去”是快速检查方法：左边矩阵的源坐标系应与右边矩阵的目标坐标系一致。真正的数学来源是前面两式的代入。

若两段变换分别写成：

$$
{}^{A}\mathbf T_B =
\begin{bmatrix}
{}^{A}\mathbf R_B & {}^{A}\mathbf t_B\\
\mathbf 0^{\mathsf T} & 1
\end{bmatrix}
$$

$$
{}^{B}\mathbf T_C =
\begin{bmatrix}
{}^{B}\mathbf R_C & {}^{B}\mathbf t_C\\
\mathbf 0^{\mathsf T} & 1
\end{bmatrix}
$$

矩阵相乘后，旋转部分为：

$$
{}^{A}\mathbf R_C =
{}^{A}\mathbf R_B{}^{B}\mathbf R_C
$$

平移部分为：

$$
{}^{A}\mathbf t_C =
{}^{A}\mathbf R_B{}^{B}\mathbf t_C +
{}^{A}\mathbf t_B
$$

第二式再次出现“旋转后加平移”，因为 $C$ 原点相对 $B$ 原点的位置最初用坐标系 $B$ 表达，必须先改用坐标系 $A$ 表达，才能与另一段平移相加。

## D4：齐次刚体变换求逆

正向点变换为：

$$
{}^{A}\mathbf p =
{}^{A}\mathbf R_B{}^{B}\mathbf p +
{}^{A}\mathbf t_B
$$

先把平移移到左边：

$$
{}^{A}\mathbf p - {}^{A}\mathbf t_B =
{}^{A}\mathbf R_B{}^{B}\mathbf p
$$

左乘旋转矩阵的逆：

$$
{}^{B}\mathbf p =
\left({}^{A}\mathbf R_B\right)^{-1}
\left({}^{A}\mathbf p - {}^{A}\mathbf t_B\right)
$$

旋转矩阵的逆等于转置，所以：

$$
{}^{B}\mathbf p =
\left({}^{A}\mathbf R_B\right)^{\mathsf T}
{}^{A}\mathbf p
-
\left({}^{A}\mathbf R_B\right)^{\mathsf T}
{}^{A}\mathbf t_B
$$

由此读出逆旋转：

$$
{}^{B}\mathbf R_A =
\left({}^{A}\mathbf R_B\right)^{\mathsf T}
$$

以及逆平移：

$$
{}^{B}\mathbf t_A =
-
\left({}^{A}\mathbf R_B\right)^{\mathsf T}
{}^{A}\mathbf t_B
$$

完整逆变换为：

$$
{}^{B}\mathbf T_A =
\left({}^{A}\mathbf T_B\right)^{-1}
=
\begin{bmatrix}
\left({}^{A}\mathbf R_B\right)^{\mathsf T} &
-\left({}^{A}\mathbf R_B\right)^{\mathsf T}{}^{A}\mathbf t_B\\
\mathbf 0^{\mathsf T} & 1
\end{bmatrix}
$$

逆平移通常不是简单的负平移。原因是：改变箭头方向以后，还必须把平移向量重新表达在逆变换的目标坐标系中。

完整齐次变换一般不满足“逆等于转置”。可以用双向单位矩阵检查：

$$
\mathbf T\mathbf T^{-1} \approx \mathbf I
$$

$$
\mathbf T^{-1}\mathbf T \approx \mathbf I
$$

也可以选择任意点，执行正向变换后再执行逆变换，检查是否回到原坐标。

## D5：根据两个全局位姿求相对位姿

已知坐标系 $A$ 和 $B$ 在世界坐标系 $W$ 中的位姿。目标是把一个用坐标系 $B$ 表达的点转换到坐标系 $A$。

坐标路径为：

```text
B → W → A
```

从 $B$ 转到 $W$ 使用：

$$
{}^{W}\mathbf T_B
$$

从 $W$ 转到 $A$ 使用：

$$
{}^{A}\mathbf T_W =
\left({}^{W}\mathbf T_A\right)^{-1}
$$

所以相对位姿为：

$$
{}^{A}\mathbf T_B =
\left({}^{W}\mathbf T_A\right)^{-1}
{}^{W}\mathbf T_B
$$

不要背“谁减谁”。先画坐标路径，再按输入和输出写矩阵。

## D6：完整定位坐标链

已知地图、里程计、车体和激光雷达之间的三段变换，以及一个激光点。完整点坐标映射为：

$$
{}^{\mathrm{map}}\mathbf p =
{}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}
{}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}
{}^{\mathrm{base}}\mathbf T_{\mathrm{lidar}}
{}^{\mathrm{lidar}}\mathbf p
$$

从右向左执行：

```text
lidar → base → odom → map
```

最终复合变换为：

$$
{}^{\mathrm{map}}\mathbf T_{\mathrm{lidar}} =
{}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}
{}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}
{}^{\mathrm{base}}\mathbf T_{\mathrm{lidar}}
$$

TF 树常按照父帧到子帧画成：

```text
map → odom → base → lidar
```

它描述的是坐标系父子拓扑。点坐标映射则从点当前所属的源坐标系走向目标坐标系，所以两组箭头看起来相反。

动态变换必须使用测量产生时刻。若激光点在时刻 $t_m$ 产生，则应使用：

$$
{}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}(t_m)
$$

不能因为消息在稍后才被处理，就直接使用处理时刻的最新变换。

## 核对完成后

1. 在工作簿中标出自己的第一处错误；
2. 合上本页，重新完成对应题目；
3. 继续运行[实验 001](../../../experiments/exp_001_transform_chain/README.md)；
4. 将真实、可复现的错误写入[mistakes.md](mistakes.md)。
