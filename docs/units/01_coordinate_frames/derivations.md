# 参考推导与核对步骤

本页包含参考过程。请先在[工作簿](workbook.md)的“步骤 3：练习与推导”中完成全部题目的独立尝试，再打开本页核对第一处差异。

不要用本页覆盖原始错误。可验证证据应保存在 `sessions/` 中，并同时保留：原始过程、第一处错误、修正原因和不看答案后的再次完成。

所有推导使用列向量，并约定变换下标表示源坐标系，左上标表示目标坐标系。

## D1：二维点变换

已知：

$$
{}^{A}\mathbf R_B=
\begin{bmatrix}
0&-1\\
1&0
\end{bmatrix},
\qquad
{}^{A}\mathbf t_B=
\begin{bmatrix}
3\\1
\end{bmatrix},
\qquad
{}^{B}\mathbf p=
\begin{bmatrix}
2\\1
\end{bmatrix}
$$

先计算旋转部分：

$$
{}^{A}\mathbf R_B{}^{B}\mathbf p
=
\begin{bmatrix}
0&-1\\
1&0
\end{bmatrix}
\begin{bmatrix}
2\\1
\end{bmatrix}
=
\begin{bmatrix}
-1\\2
\end{bmatrix}
$$

它表示：

$$
\overrightarrow{O_BP}
$$

在坐标系 $A$ 中的坐标表达，不是点 $P$ 在 $A$ 中的最终坐标。

再加平移：

$$
{}^{A}\mathbf p
=
\begin{bmatrix}
-1\\2
\end{bmatrix}
+
\begin{bmatrix}
3\\1
\end{bmatrix}
=
\begin{bmatrix}
2\\3
\end{bmatrix}
$$

几何关系为：

$$
\overrightarrow{O_AP}
=
\overrightarrow{O_AO_B}
+
\overrightarrow{O_BP}
$$

数值上：

$$
\begin{bmatrix}
2\\3
\end{bmatrix}
=
\begin{bmatrix}
3\\1
\end{bmatrix}
+
\begin{bmatrix}
-1\\2
\end{bmatrix}
$$

## D2：旋转矩阵与坐标轴

对于：

$$
{}^{A}\mathbf R_B=
\begin{bmatrix}
0&-1\\
1&0
\end{bmatrix}
$$

第一列为：

$$
{}^{A}\mathbf e_{x_B}
=
\begin{bmatrix}
0\\1
\end{bmatrix}
$$

表示 $B$ 的 $x_B$ 轴在 $A$ 中向上。

第二列为：

$$
{}^{A}\mathbf e_{y_B}
=
\begin{bmatrix}
-1\\0
\end{bmatrix}
$$

表示 $B$ 的 $y_B$ 轴在 $A$ 中向左。

合法旋转矩阵满足：

$$
\mathbf R^{\mathsf T}\mathbf R=\mathbf I
$$

$$
\det(\mathbf R)=1
$$

因为各列都是单位向量且互相正交，所以：

$$
\mathbf R^{-1}=\mathbf R^{\mathsf T}
$$

该性质只适用于正交矩阵，不能推广到任意可逆矩阵。

## D3：变换组合

已知：

$$
{}^{B}\mathbf p
=
{}^{B}\mathbf T_C{}^{C}\mathbf p
$$

$$
{}^{A}\mathbf p
=
{}^{A}\mathbf T_B{}^{B}\mathbf p
$$

把第一式代入第二式：

$$
{}^{A}\mathbf p
=
{}^{A}\mathbf T_B
{}^{B}\mathbf T_C
{}^{C}\mathbf p
$$

因此：

$$
\boxed{
{}^{A}\mathbf T_C
=
{}^{A}\mathbf T_B{}^{B}\mathbf T_C
}
$$

采用列向量时，最靠近点的 ${}^{B}\mathbf T_C$ 最先作用。

“相邻坐标系消去”：

$$
{}^{A}\mathbf T_{\cancel B}
{}^{\cancel B}\mathbf T_C
=
{}^{A}\mathbf T_C
$$

只是检查方法。数学来源是代入关系，以及前一段输出坐标系必须等于后一段输入坐标系。

若：

$$
{}^{A}\mathbf T_B=
\begin{bmatrix}
{}^{A}\mathbf R_B&{}^{A}\mathbf t_B\\
0&1
\end{bmatrix}
$$

$$
{}^{B}\mathbf T_C=
\begin{bmatrix}
{}^{B}\mathbf R_C&{}^{B}\mathbf t_C\\
0&1
\end{bmatrix}
$$

则：

$$
{}^{A}\mathbf R_C
=
{}^{A}\mathbf R_B{}^{B}\mathbf R_C
$$

$$
{}^{A}\mathbf t_C
=
{}^{A}\mathbf R_B{}^{B}\mathbf t_C
+{}^{A}\mathbf t_B
$$

第二式中，${}^{B}\mathbf t_C$ 必须先转成 $A$ 的表达，才能与 ${}^{A}\mathbf t_B$ 相加。

## D4：齐次刚体变换求逆

从：

$$
{}^{A}\mathbf p
=
{}^{A}\mathbf R_B{}^{B}\mathbf p
+{}^{A}\mathbf t_B
$$

开始。先移项：

$$
{}^{A}\mathbf p-{}^{A}\mathbf t_B
=
{}^{A}\mathbf R_B{}^{B}\mathbf p
$$

左乘旋转的逆：

$$
{}^{B}\mathbf p
=
\left({}^{A}\mathbf R_B\right)^{-1}
\left({}^{A}\mathbf p-{}^{A}\mathbf t_B\right)
$$

利用旋转矩阵性质：

$$
\left({}^{A}\mathbf R_B\right)^{-1}
=
\left({}^{A}\mathbf R_B\right)^{\mathsf T}
$$

得到：

$$
{}^{B}\mathbf p
=
\left({}^{A}\mathbf R_B\right)^{\mathsf T}{}^{A}\mathbf p
-
\left({}^{A}\mathbf R_B\right)^{\mathsf T}{}^{A}\mathbf t_B
$$

因此：

$$
{}^{B}\mathbf R_A
=
\left({}^{A}\mathbf R_B\right)^{\mathsf T}
$$

$$
{}^{B}\mathbf t_A
=
-
\left({}^{A}\mathbf R_B\right)^{\mathsf T}{}^{A}\mathbf t_B
$$

完整逆变换为：

$$
\boxed{
{}^{B}\mathbf T_A
=
\left({}^{A}\mathbf T_B\right)^{-1}
=
\begin{bmatrix}
\left({}^{A}\mathbf R_B\right)^{\mathsf T}
&
-\left({}^{A}\mathbf R_B\right)^{\mathsf T}{}^{A}\mathbf t_B\\
\mathbf 0^{\mathsf T}&1
\end{bmatrix}
}
$$

逆平移通常不是简单的 $-\mathbf t$，因为方向反转后，还必须把向量重新表达在反向目标坐标系中。

完整齐次变换一般不满足：

$$
\mathbf T^{-1}=\mathbf T^{\mathsf T}
$$

数值自检：

$$
\mathbf T\mathbf T^{-1}\approx\mathbf I
$$

并对任意点检查：

$$
{}^{B}\mathbf p
\xrightarrow{{}^{A}\mathbf T_B}
{}^{A}\mathbf p
\xrightarrow{{}^{B}\mathbf T_A}
{}^{B}\mathbf p
$$

## D5：根据全局位姿求相对位姿

已知：

$$
{}^{W}\mathbf T_A,
\qquad
{}^{W}\mathbf T_B
$$

目标是把点坐标从 $B$ 转到 $A$。坐标路径为：

```text
B → W → A
```

其中：

$$
{}^{A}\mathbf T_W
=
\left({}^{W}\mathbf T_A\right)^{-1}
$$

所以：

$$
\boxed{
{}^{A}\mathbf T_B
=
\left({}^{W}\mathbf T_A\right)^{-1}
{}^{W}\mathbf T_B
}
$$

检查上下标：

$$
{}^{A}\mathbf T_{\cancel W}
{}^{\cancel W}\mathbf T_B
=
{}^{A}\mathbf T_B
$$

## D6：完整定位坐标链

已知：

$$
{}^{\mathrm{map}}\mathbf T_{\mathrm{odom}},
\qquad
{}^{\mathrm{odom}}\mathbf T_{\mathrm{base}},
\qquad
{}^{\mathrm{base}}\mathbf T_{\mathrm{lidar}},
\qquad
{}^{\mathrm{lidar}}\mathbf p
$$

完整点变换为：

$$
\boxed{
{}^{\mathrm{map}}\mathbf p
=
{}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}
{}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}
{}^{\mathrm{base}}\mathbf T_{\mathrm{lidar}}
{}^{\mathrm{lidar}}\mathbf p
}
$$

执行路径为：

```text
lidar → base → odom → map
```

最终复合变换为：

$$
{}^{\mathrm{map}}\mathbf T_{\mathrm{lidar}}
=
{}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}
{}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}
{}^{\mathrm{base}}\mathbf T_{\mathrm{lidar}}
$$

TF 树按父帧到子帧常画成：

```text
map → odom → base → lidar
```

它描述父子拓扑；点坐标映射路径描述源坐标到目标坐标的计算，所以箭头看起来相反。

动态变换必须使用测量产生时刻。若点在 $t_m$ 产生，则应使用：

$$
{}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}(t_m)
$$

而不是消息处理时刻的最新变换。

## 核对完成后

1. 在工作簿中标出自己的第一处错误；
2. 合上本页重新完成对应题目；
3. 继续运行[实验 001](../../../experiments/exp_001_transform_chain/README.md)；
4. 真实、可复现的错误写入[mistakes.md](mistakes.md)。