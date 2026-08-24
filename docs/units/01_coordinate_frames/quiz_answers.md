# 单元 01 终测参考答案

停止：只有在已经提交 [quiz.md](quiz.md) 的全部闭卷答案后，才阅读本页。

本页用于评分和定位第一处错误。参考答案存在、阅读答案或当场看懂答案，都不能作为学习者证据；原始作答和延迟复测应保存在 `sessions/` 中。

## Q1：读取变换记号（1 分）

输入是点在坐标系 $B$ 中的坐标，输出是同一点在坐标系 $A$ 中的坐标。变换的源坐标系是 $B$，目标坐标系是 $A$。

只说“从 A 到 B”或“B 相对 A”而没有明确输入输出，不给满分。

## Q2：完整传感器变换链（2 分）

完整表达式为：

$$
{}^{\mathrm{map}}\mathbf p=
{}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}
{}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}
{}^{\mathrm{base}}\mathbf T_{\mathrm{lidar}}
{}^{\mathrm{lidar}}\mathbf p
$$

采用列向量时，最右侧变换先作用。每一段的输出坐标系必须与下一段的输入坐标系一致：`lidar → base → odom → map`。

最终复合变换为：

$$
{}^{\mathrm{map}}\mathbf T_{\mathrm{lidar}}=
{}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}
{}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}
{}^{\mathrm{base}}\mathbf T_{\mathrm{lidar}}
$$

它的源坐标系是 `lidar`，目标坐标系是 `map`。“中间上下标消去”只能作为检查，不能代替输入输出衔接的解释。

## Q3：二维数值变换（2 分）

二维齐次变换为：

$$
{}^{A}\mathbf T_B=
\begin{bmatrix}
0&-1&1\\
1&0&2\\
0&0&1
\end{bmatrix}
$$

点变换为：

$$
{}^{A}\bar{\mathbf p}=
\begin{bmatrix}
0&-1&1\\
1&0&2\\
0&0&1
\end{bmatrix}
\begin{bmatrix}
1\\
0\\
1
\end{bmatrix}=
\begin{bmatrix}
1\\
3\\
1
\end{bmatrix}
$$

几何检查：先从 $A$ 的原点走到 $B$ 的原点 $[1,2]^{\mathsf T}$，再沿 $B$ 的正 $x$ 轴走 1 米。该方向在 $A$ 中等于正 $y$，终点因此为 $[1,3]^{\mathsf T}$。

## Q4：齐次刚体变换求逆（2 分）

若：

$$
\mathbf T=
\begin{bmatrix}
\mathbf R&\mathbf t\\
\mathbf 0^{\mathsf T}&1
\end{bmatrix}
$$

则：

$$
\mathbf T^{-1}=
\begin{bmatrix}
\mathbf R^{\mathsf T}&-\mathbf R^{\mathsf T}\mathbf t\\
\mathbf 0^{\mathsf T}&1
\end{bmatrix}
$$

原平移向量表达在正向变换的目标坐标系中。反向映射时，需要先通过 $\mathbf R^{\mathsf T}$ 把它重新表达在反向目标坐标系，因此通常不能只写成 $-\mathbf t$。

自检可以使用变换与逆的双向乘积：

$$
\mathbf T\mathbf T^{-1}\approx\mathbf I,
\qquad
\mathbf T^{-1}\mathbf T\approx\mathbf I
$$

也可以对随机点进行正向再反向的往返测试。

## Q5：TF 树与全局修正（2 分）

TF 树的箭头描述“父帧 → 子帧”的拓扑关系。父帧 `base` 到子帧 `lidar` 的边对应子帧在父帧中的位姿。点坐标映射则从点当前所属的源帧走向目标帧，因此激光点的计算路径是 `lidar → base → odom → map`。

车体在 `odom` 中的局部位姿服务于控制、局部规划和运动补偿，需要保持连续；`odom` 允许长期漂移。回环、GNSS 或重定位产生的全局修正可以由 `map` 与 `odom` 的对齐关系吸收，再与局部位姿复合得到车体在地图中的全局位姿。

## Q6：时间与错误检查（1 分）

应查询或插值测量产生时刻 $12.0~\mathrm{s}$ 的动态 TF，而不是使用消息处理时刻的最新变换。

有效的最小测试包括：

- 用源坐标系原点检查平移；
- 用三个单位轴检查旋转方向；
- 检查变换与其逆的乘积是否接近单位矩阵；
- 比较逐段变换与复合变换；
- 对随机点执行正向与反向往返测试。

任写两种且能说明判断依据即可。

## 评分后怎么处理

1. 在工作簿中保留原始答案，不用本页覆盖。
2. 找到第一处错误，标记为概念、推理、计算、符号、坐标系、时间或工程边界错误。
3. 合上本页重新作答对应题目。
4. 把可复现错误写入 [mistakes.md](mistakes.md)。
5. 当场通过后将状态设为“待复习”，按计划完成延迟复测。
