# U05-L07：多维卡尔曼滤波的矩阵各自做什么？

- 预计用时：约 12 分钟（建议控制在 10～15 分钟）
- 本课目标：理解状态、观测矩阵、创新协方差和增益维度。
- 所属单元：[单元 05：概率与卡尔曼滤波](README.md)
- 上一课：[U05-L06：卡尔曼预测为什么必须加入过程噪声？](lesson_06_kalman_prediction_process_noise.md)
- 下一课：[U05-L08：EKF 怎样处理非线性模型？](lesson_08_ekf_linearization_consistency.md)

## 1 分钟：主动回忆

状态含位置和速度，但 GPS 只测位置。滤波器怎样把位置测量间接影响到速度估计？

先写下或说出当前答案，再继续阅读。这里不是正式考试；目的是让新知识连接到已经学过的内容。

## 7 分钟：本课微课程

测量模型：

\[
\mathbf z_k=\mathbf H_k\mathbf x_k+\mathbf v_k,
\qquad
\mathbf v_k\sim\mathcal N(0,\mathbf R_k)
\]

创新：

\[
\mathbf y_k
=\mathbf z_k-\mathbf H_k\hat{\mathbf x}_k^-
\]

创新协方差：

\[
\mathbf S_k
=\mathbf H_k\mathbf P_k^-\mathbf H_k^{\mathsf T}
+\mathbf R_k
\]

增益：

\[
\mathbf K_k
=\mathbf P_k^-\mathbf H_k^{\mathsf T}\mathbf S_k^{-1}
\]

更新：

\[
\hat{\mathbf x}_k^+
=\hat{\mathbf x}_k^-+\mathbf K_k\mathbf y_k
\]

协方差稳定写法可用 Joseph 形式：

\[
\mathbf P^+
=(\mathbf I-\mathbf K\mathbf H)\mathbf P^-
(\mathbf I-\mathbf K\mathbf H)^{\mathsf T}
+\mathbf K\mathbf R\mathbf K^{\mathsf T}
\]

位置与速度的交叉协方差使位置观测能修正速度。矩阵维度是很有效的接口检查。

## 3 分钟：最小练习

状态为 \([p,v]^{\mathsf T}\)，只测位置。写出 \(\mathbf H\) 的维度和元素。说明若先验协方差的 \(p-v\) 交叉项为零，单次位置更新对速度可能有什么影响。

不要只在脑中判断。至少写下一行推理、一个公式、一个草图或一组输入输出。

## 1 分钟：合上资料复述

按顺序解释创新、\(\mathbf S\)、\(\mathbf K\)、状态更新和协方差更新的物理意义。

第一次卡住的位置就是下一次复习的入口，不要用重新通读整篇来掩盖卡点。

## 本课完成标准

- [ ] 能用自己的话回答本课核心问题；
- [ ] 完成最小练习并保留判断过程；
- [ ] 合上资料后完成一分钟复述。

完成本课只表示形成了第一轮理解证据，不表示已经掌握。按导航进入下一课，并在本单元的[工作簿](workbook.md)中记录结果。
