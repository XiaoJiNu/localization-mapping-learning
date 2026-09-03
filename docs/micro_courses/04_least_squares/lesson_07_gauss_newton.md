# U04-L07：高斯—牛顿怎样产生一次更新？

- 预计用时：约 12 分钟（建议控制在 10～15 分钟）
- 本课目标：从线性化残差推导增量正规方程，并理解迭代流程。
- 所属单元：[单元 04：最小二乘](README.md)
- 上一课：[U04-L06：雅可比在几何上表示什么？](lesson_06_jacobian_meaning_check.md)
- 下一课：[U04-L08：鲁棒核怎样降低离群值影响？](lesson_08_robust_loss_outliers.md)

## 1 分钟：主动回忆

非线性最小二乘每轮为什么求的是 \(\delta\mathbf x\)，而不是直接一次求出最终 \(\mathbf x\)？

先写下或说出当前答案，再继续阅读。这里不是正式考试；目的是让新知识连接到已经学过的内容。

## 7 分钟：本课微课程

线性化后：

\[
\mathbf r(\mathbf x+\delta\mathbf x)
\approx \mathbf r+\mathbf J\delta\mathbf x
\]

高斯—牛顿求：

\[
\delta\mathbf x^*
=\arg\min_{\delta\mathbf x}
\frac12\|\mathbf r+\mathbf J\delta\mathbf x\|^2
\]

对应方程：

\[
\mathbf J^{\mathsf T}\mathbf J\,\delta\mathbf x
=-\mathbf J^{\mathsf T}\mathbf r
\]

再更新状态并重新计算残差和雅可比。典型循环：

```text
初始化
→ 计算残差/J
→ 解增量
→ 更新状态
→ 判断收敛
```

\(\mathbf H=\mathbf J^{\mathsf T}\mathbf J\) 是高斯—牛顿近似海森矩阵。若问题退化或尺度差，\(\mathbf H\) 可能病态。Levenberg–Marquardt 会加入阻尼：

\[
(\mathbf H+\lambda\mathbf I)\delta\mathbf x=-\mathbf g
\]

在远离解时更保守。

收敛不能只看迭代次数，应同时观察代价变化、增量大小、梯度和物理合法性。

## 3 分钟：最小练习

继续使用 \(r(x)=x^2-4\)，从 \(x_0=3\) 做两轮高斯—牛顿更新，记录每轮残差、雅可比和增量。

不要只在脑中判断。至少写下一行推理、一个公式、一个草图或一组输入输出。

## 1 分钟：合上资料复述

无稿写出高斯—牛顿增量方程，并说明阻尼为何能在初值较差或病态时提高稳定性。

第一次卡住的位置就是下一次复习的入口，不要用重新通读整篇来掩盖卡点。

## 本课完成标准

- [ ] 能用自己的话回答本课核心问题；
- [ ] 完成最小练习并保留判断过程；
- [ ] 合上资料后完成一分钟复述。

完成本课只表示形成了第一轮理解证据，不表示已经掌握。按导航进入下一课，并在本单元的[工作簿](workbook.md)中记录结果。
