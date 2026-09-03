# U01-L04：点变换公式怎样从几何路径推导？

- 预计用时：约 12 分钟（建议控制在 10～15 分钟）
- 本课目标：从原点到点的向量相加关系推导旋转和平移项。
- 所属单元：[单元 01：坐标系与变换链](README.md)
- 上一课：[U01-L03：怎样读懂 \({}^{A}\mathbf T_B\)？](lesson_03_read_transform_notation.md)
- 下一课：[U01-L05：旋转矩阵的每一列代表什么？](lesson_05_rotation_matrix_columns.md)

## 1 分钟：主动回忆

为什么 \({}^{A}\mathbf p={}^A\mathbf R_B{}^B\mathbf p+{}^A\mathbf t_B\) 中不能直接写成 \({}^B\mathbf p+{}^A\mathbf t_B\)？

先写下或说出当前答案，再继续阅读。这里不是正式考试；目的是让新知识连接到已经学过的内容。

## 7 分钟：本课微课程

设 \(O_A\)、\(O_B\) 是两个坐标系原点，\(P\) 是空间中的同一点。纯几何路径为：

\[
\overrightarrow{O_AP}
=\overrightarrow{O_AO_B}
+\overrightarrow{O_BP}
\]

第一段在 \(A\) 中的表达是：

\[
{}^A\mathbf t_B=[\overrightarrow{O_AO_B}]_A
\]

第二段的已知坐标却在 \(B\) 中：

\[
{}^B\mathbf p=[\overrightarrow{O_BP}]_B
\]

两个使用不同坐标轴表达的数字不能直接相加。先用旋转矩阵把第二段改写到 \(A\)：

\[
[\overrightarrow{O_BP}]_A
={}^A\mathbf R_B{}^B\mathbf p
\]

于是得到：

\[
{}^{A}\mathbf p
={}^A\mathbf R_B{}^B\mathbf p+{}^A\mathbf t_B
\]

“先旋转、再平移”不是说物理点先转再移，而是先统一坐标表达，再进行同一坐标系中的向量相加。平移向量 \({}^A\mathbf t_B\) 的含义是“\(B\) 的原点在 \(A\) 中的坐标”，不是随便加上的位移。

## 3 分钟：最小练习

画一条三段文字路径：

```text
O_A → O_B → P
```

在每一段旁写出几何向量、它当前使用的坐标系，以及为了相加是否需要旋转。最后独立写出完整公式。

不要只在脑中判断。至少写下一行推理、一个公式、一个草图或一组输入输出。

## 1 分钟：合上资料复述

不看资料，从 \(\overrightarrow{O_AP}=\overrightarrow{O_AO_B}+\overrightarrow{O_BP}\) 开始，用三句话推到点变换公式。

第一次卡住的位置就是下一次复习的入口，不要用重新通读整篇来掩盖卡点。

## 本课完成标准

- [ ] 能用自己的话回答本课核心问题；
- [ ] 完成最小练习并保留判断过程；
- [ ] 合上资料后完成一分钟复述。

完成本课只表示形成了第一轮理解证据，不表示已经掌握。按导航进入下一课，并在本单元的[工作簿](workbook.md)中记录结果。
