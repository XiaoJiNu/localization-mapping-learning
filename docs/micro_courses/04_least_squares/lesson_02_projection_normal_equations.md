# U04-L02：正规方程从哪里来？

- 预计用时：约 12 分钟（建议控制在 10～15 分钟）
- 本课目标：从梯度和正交投影两种角度理解 \(\mathbf A^{\mathsf T}\mathbf A\mathbf x=\mathbf A^{\mathsf T}\mathbf b\)。
- 所属单元：[单元 04：最小二乘](README.md)
- 上一课：[U04-L01：为什么测量多于未知量时需要最小二乘？](lesson_01_residual_overdetermined.md)
- 下一课：[U04-L03：最小二乘解什么时候唯一？](lesson_03_rank_uniqueness.md)

## 1 分钟：主动回忆

最小二乘解为什么要求最终残差与 \(\mathbf A\) 的每一列正交？

先写下或说出当前答案，再继续阅读。这里不是正式考试；目的是让新知识连接到已经学过的内容。

## 7 分钟：本课微课程

目标函数：

\[
J(\mathbf x)=\frac12\|\mathbf A\mathbf x-\mathbf b\|_2^2
\]

梯度为：

\[
\nabla J
=\mathbf A^{\mathsf T}(\mathbf A\mathbf x-\mathbf b)
\]

在极小点令梯度为零：

\[
\mathbf A^{\mathsf T}\mathbf A\mathbf x
=\mathbf A^{\mathsf T}\mathbf b
\]

这就是正规方程。令 \(\mathbf r=\mathbf A\mathbf x^*-\mathbf b\)，则：

\[
\mathbf A^{\mathsf T}\mathbf r=0
\]

说明残差与 \(\mathbf A\) 的列空间正交。几何上，\(\mathbf A\mathbf x^*\) 是 \(\mathbf b\) 在列空间上的正交投影；无法由模型解释的部分留在残差中。

正规方程便于理解，但数值实现不一定直接计算 \((\mathbf A^{\mathsf T}\mathbf A)^{-1}\)。形成 \(\mathbf A^{\mathsf T}\mathbf A\) 会放大条件数，工程上更常用 QR、SVD 或稀疏分解。

## 3 分钟：最小练习

给定

\[
\mathbf A=\begin{bmatrix}1\\1\\1\end{bmatrix},
\quad
\mathbf b=\begin{bmatrix}1\\2\\3\end{bmatrix}
\]

求 \(x^*\) 和残差 \(\mathbf r\)，验证 \(\mathbf A^{\mathsf T}\mathbf r=0\)。

不要只在脑中判断。至少写下一行推理、一个公式、一个草图或一组输入输出。

## 1 分钟：合上资料复述

从“梯度为零”和“正交投影”两条路径分别解释正规方程，并说明为什么不建议显式求逆。

第一次卡住的位置就是下一次复习的入口，不要用重新通读整篇来掩盖卡点。

## 本课完成标准

- [ ] 能用自己的话回答本课核心问题；
- [ ] 完成最小练习并保留判断过程；
- [ ] 合上资料后完成一分钟复述。

完成本课只表示形成了第一轮理解证据，不表示已经掌握。按导航进入下一课，并在本单元的[工作簿](workbook.md)中记录结果。
