# 定位建图 20 小时微课程

## 100 节 × 每节约 12 分钟

原路线由 10 个两小时单元组成。本目录把每个单元拆成 10 节 10～15 分钟微课程，统一按约 12 分钟设计：

$$
10~\text{个单元}
\times 10~\text{节/单元}
\times 12~\text{分钟/节}
=1200~\text{分钟}
=20~\text{小时}
$$

这里的“20 小时”是第一轮学习预算，不包含 D1、D3、D7、D14、D30 的延迟复习。

## 现在从哪里开始

> [U01-L01：同一个点为什么会有不同坐标？](01_coordinate_frames/lesson_01_same_point_different_coordinates.md)

第一次开始时：

1. 打开[单元 01 主页](01_coordinate_frames/README.md)；
2. 复制该单元的[工作簿](01_coordinate_frames/workbook.md)；
3. 只学习当天的一节，不提前浏览后续答案或把十节一次性读完；
4. 完成最小练习和一分钟无稿复述后即可停止；
5. 下一次从课程页底部的“下一课”继续。

## 为什么这样拆分

本结构参考 `microeconomicsLearning` 中“每天只解决一个核心问题”的日课方式，但针对定位建图增加了公式、坐标、时间、输入输出和工程失败模式。

每节不是一段被机械切开的长文，而是一个完整的最小学习闭环：

| 环节 | 时间 | 作用 |
|---|---:|---|
| 主动回忆 | 1 分钟 | 先暴露当前理解，而不是直接重读 |
| 聚焦讲解 | 7 分钟 | 只讲清一个核心机制及其工程含义 |
| 最小练习 | 3 分钟 | 形成计算、判断、草图或输入输出证据 |
| 无稿复述 | 1 分钟 | 检查能否脱离原文重新组织语言 |

详细执行规则见[微课程学习流程](../00_learning_system/micro_lesson_workflow.md)。

## 20 小时完整目录

| 单元 | 主题 | 核心问题 | 微课数 | 第一轮预算 | 入口 |
|---:|---|---|---:|---:|---|
| 01 | [坐标系与变换链](01_coordinate_frames/README.md) | 一个点如何从传感器坐标系正确变换到地图坐标系？ | 10 | 120 分钟 | [开始](01_coordinate_frames/lesson_01_same_point_different_coordinates.md) |
| 02 | [旋转与刚体位姿](02_rotations_rigid_poses/README.md) | 旋转矩阵、欧拉角、四元数与李群分别解决什么问题？ | 10 | 120 分钟 | [开始](02_rotations_rigid_poses/lesson_01_position_orientation_pose.md) |
| 03 | [传感器、时间与标定](03_sensors_time_calibration/README.md) | 时间戳、内外参与噪声怎样影响多传感器融合？ | 10 | 120 分钟 | [开始](03_sensors_time_calibration/lesson_01_measurement_contract.md) |
| 04 | [最小二乘](04_least_squares/README.md) | 残差、雅可比与正规方程怎样把测量变成状态估计？ | 10 | 120 分钟 | [开始](04_least_squares/lesson_01_residual_overdetermined.md) |
| 05 | [概率与卡尔曼滤波](05_probability_kalman/README.md) | 均值、协方差与卡尔曼增益怎样表达“相信谁”？ | 10 | 120 分钟 | [开始](05_probability_kalman/lesson_01_mean_variance_covariance.md) |
| 06 | [IMU 与轮式推算](06_imu_wheel_odometry/README.md) | IMU 和轮速究竟测到什么，误差为什么会快速累积？ | 10 | 120 分钟 | [开始](06_imu_wheel_odometry/lesson_01_imu_measurements.md) |
| 07 | [局部里程计](07_local_odometry/README.md) | 连续位姿怎样由相邻观测产生，漂移和退化怎样被发现？ | 10 | 120 分钟 | [开始](07_local_odometry/lesson_01_odometry_contract.md) |
| 08 | [滤波与因子图](08_filtering_factor_graphs/README.md) | 递推滤波与滑窗/因子图怎样描述同一个估计问题？ | 10 | 120 分钟 | [开始](08_filtering_factor_graphs/lesson_01_same_estimation_problem.md) |
| 09 | [SLAM 与全局修正](09_slam_global_correction/README.md) | 前端、后端、回环与图优化分别修正什么？ | 10 | 120 分钟 | [开始](09_slam_global_correction/lesson_01_slam_modules.md) |
| 10 | [重定位与系统设计](10_relocalization_system_design/README.md) | 系统丢失后怎样恢复全局位姿，并安全地接入定位链？ | 10 | 120 分钟 | [开始](10_relocalization_system_design/lesson_01_localization_relocalization_loop.md) |

合计：**10 个单元、100 节微课程、约 1200 分钟。**

## 十个单元怎样连接

```text
坐标系与变换链
→ 旋转与刚体位姿
→ 传感器、时间与标定
→ 最小二乘
→ 概率与卡尔曼滤波
→ IMU 与轮式推算
→ 局部里程计
→ 滤波与因子图
→ SLAM 与全局修正
→ 重定位与系统设计
```

这条主线依次回答：

1. 测量中的点和位姿怎样统一表达；
2. 不同传感器怎样在正确时刻和正确坐标系下对齐；
3. 怎样从带噪测量估计状态并表达不确定性；
4. 怎样连续产生局部轨迹；
5. 怎样通过回环、地图和重定位恢复全局一致性；
6. 怎样把算法组成可评审、可降级、可量产的系统。

## 每个单元包含什么

每个单元目录固定包含：

```text
NN_unit_name/
├── README.md       # 十节目录、顺序、目标和完成标准
├── workbook.md     # 个人学习证据与延迟复习记录
└── lesson_01～10   # 十节完整微课程
```

课程正文与工作簿分离。仓库中的文字不能代替学习者自己的练习、复述和错误记录。

## 第一轮完成标准

完成全部 100 节后，至少应留下：

- 100 条一句话结论或主动回忆记录；
- 100 个最小练习结果；
- 10 次单元级无稿综合复述；
- 每个单元至少一个工程应用和一个失败模式；
- 10 组延迟复习日期；
- 一份最终系统方案主线。

使用[20 小时进度表](progress.md)记录完成度。首次完成只能标记为 `待复习`；经过延迟复习、变化条件和综合任务后，才考虑标记为 `已掌握`。

## 与原有两小时学习路径的关系

原仓库的两小时流程仍适合集中学习、完整推导、实验和正式终测。本分支新增的是一条可每天执行的微课程路径：

| 路径 | 适合场景 | 单次时长 | 主要证据 |
|---|---|---:|---|
| 微课程路径 | 每天持续学习、降低启动成本 | 10～15 分钟 | 主动回忆、最小练习、无稿复述 |
| 原两小时路径 | 集中训练、实验、推导和终测 | 约 120 分钟 | 完整工作簿、实验、故障分析、终测 |

两条路径不是两套冲突的知识体系。可先完成微课程建立结构，再用原路径中的实验和终测加深；也可以把一个两小时单元分散到十天完成。
