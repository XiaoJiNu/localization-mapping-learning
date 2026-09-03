# U01-L08：刚体变换怎样求逆并计算相对位姿？

- 预计用时：约 12 分钟（建议控制在 10～15 分钟）
- 本课目标：推导齐次刚体变换的逆，并由两个全局位姿得到相对位姿。
- 所属单元：[单元 01：坐标系与变换链](README.md)
- 上一课：[U01-L07：变换为什么必须按这个顺序相乘？](lesson_07_compose_transforms_order.md)
- 下一课：[U01-L09：`sensor/base/odom/map` 怎样组成动态变换链？](lesson_09_sensor_base_odom_map_time.md)

## 1 分钟：主动回忆

为什么齐次刚体变换的逆不是简单写成整个 \(4\times4\) 矩阵的转置？

先写下或说出当前答案，再继续阅读。这里不是正式考试；目的是让新知识连接到已经学过的内容。

## 7 分钟：本课微课程

若：

\[
{}^A\mathbf T_B=
\begin{bmatrix}
\mathbf R&\mathbf t\\
\mathbf 0^{\mathsf T}&1
\end{bmatrix}
\]

由 \({}^A\mathbf p=\mathbf R{}^B\mathbf p+\mathbf t\) 解出 \({}^B\mathbf p\)：

\[
{}^B\mathbf p=\mathbf R^{\mathsf T}({}^A\mathbf p-\mathbf t)
\]

因此：

\[
{}^B\mathbf T_A=
({}^A\mathbf T_B)^{-1}
=
\begin{bmatrix}
\mathbf R^{\mathsf T}&-\mathbf R^{\mathsf T}\mathbf t\\
\mathbf 0^{\mathsf T}&1
\end{bmatrix}
\]

只有旋转块的逆等于转置；平移必须先取负，再换到逆变换的坐标表达中。

若已知同一参考系 \(W\) 中的两个位姿 \({}^W\mathbf T_A\)、\({}^W\mathbf T_B\)，则 \(B\) 相对 \(A\) 的变换为：

\[
{}^A\mathbf T_B
=({}^W\mathbf T_A)^{-1}{}^W\mathbf T_B
\]

可以用恒等检查验证：

\[
{}^A\mathbf T_B{}^B\mathbf T_A=\mathbf I
\]

## 3 分钟：最小练习

取二维 \(\mathbf R\) 为逆时针 90°、\(\mathbf t=[3,1]^{\mathsf T}\)。写出逆变换中的旋转和平移，并解释为什么逆平移不是简单的 \([-3,-1]^{\mathsf T}\)。

不要只在脑中判断。至少写下一行推理、一个公式、一个草图或一组输入输出。

## 1 分钟：合上资料复述

无稿写出刚体变换求逆公式，再说明“两个全局位姿求相对位姿”为什么要先逆掉参考系中的第一个位姿。

第一次卡住的位置就是下一次复习的入口，不要用重新通读整篇来掩盖卡点。

## 本课完成标准

- [ ] 能用自己的话回答本课核心问题；
- [ ] 完成最小练习并保留判断过程；
- [ ] 合上资料后完成一分钟复述。

完成本课只表示形成了第一轮理解证据，不表示已经掌握。按导航进入下一课，并在本单元的[工作簿](workbook.md)中记录结果。
