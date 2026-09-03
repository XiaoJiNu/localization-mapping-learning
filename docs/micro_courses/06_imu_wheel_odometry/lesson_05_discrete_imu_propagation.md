# U06-L05：一个离散 IMU 传播步骤包含哪些状态？

- 预计用时：约 12 分钟（建议控制在 10～15 分钟）
- 本课目标：理解姿态、速度、位置和偏置的联合传播。
- 所属单元：[单元 06：IMU 与轮式推算](README.md)
- 上一课：[U06-L04：加速度双积分为什么会快速漂移？](lesson_04_acceleration_double_integration.md)
- 下一课：[U06-L06：IMU 预积分为什么能连接关键帧？](lesson_06_imu_preintegration.md)

## 1 分钟：主动回忆

只积分位置而不维护姿态和偏置，能否正确使用 IMU？为什么？

先写下或说出当前答案，再继续阅读。这里不是正式考试；目的是让新知识连接到已经学过的内容。

## 7 分钟：本课微课程

常见 IMU 导航状态包括：

\[
\mathbf x=
(\mathbf R,\mathbf p,\mathbf v,\mathbf b_g,\mathbf b_a)
\]

给定时间间隔 \(\Delta t\)，简化传播为：

\[
\mathbf R_{k+1}
=\mathbf R_k\operatorname{Exp}
((\tilde{\boldsymbol\omega}_k-\mathbf b_g)\Delta t)^\wedge
\]

\[
\mathbf a_k^W
=\mathbf R_k(\tilde{\mathbf f}_k-\mathbf b_a)+\mathbf g
\]

\[
\mathbf p_{k+1}
=\mathbf p_k+\mathbf v_k\Delta t+\frac12\mathbf a_k^W\Delta t^2
\]

\[
\mathbf v_{k+1}
=\mathbf v_k+\mathbf a_k^W\Delta t
\]

偏置常建模为随机游走。更高精度实现会使用中值积分、考虑地球旋转或杆臂效应。

传播不仅更新均值，还要传播协方差。丢包、重复时间戳或时间倒退必须显式处理，不能用默认 \(\Delta t\) 悄悄继续。

## 3 分钟：最小练习

写出一条 IMU 样本进入传播器后的检查顺序：时间戳、单位、轴向、去偏置、姿态更新、重力补偿、速度位置更新。为每步写一个可观测的错误现象。

不要只在脑中判断。至少写下一行推理、一个公式、一个草图或一组输入输出。

## 1 分钟：合上资料复述

闭卷说出 IMU 导航状态的五类变量，并按顺序描述一次传播。

第一次卡住的位置就是下一次复习的入口，不要用重新通读整篇来掩盖卡点。

## 本课完成标准

- [ ] 能用自己的话回答本课核心问题；
- [ ] 完成最小练习并保留判断过程；
- [ ] 合上资料后完成一分钟复述。

完成本课只表示形成了第一轮理解证据，不表示已经掌握。按导航进入下一课，并在本单元的[工作簿](workbook.md)中记录结果。
