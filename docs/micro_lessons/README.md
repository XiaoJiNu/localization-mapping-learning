# 定位建图 20 小时微课程

## 100 课 × 每课约 12 分钟 = 20 小时

本目录参考 `XiaoJiNu/microeconomicsLearning` 的日课结构，把原路线中的十个 2 小时单元拆成 100 个 10～15 分钟微课。

每一课只解决一个核心问题，固定采用：

```text
1 分钟主动回忆
→ 7～8 分钟核心讲解
→ 2～3 分钟最小练习
→ 1 分钟无稿复述
```

## 当前下一步

> [单元 01 · 第 01 课：为什么同一个世界需要多个坐标系？](01_coordinate_frames/lesson_01_why_frames.md)

第一次学习时按课号连续推进。完成某课后才进入下一课；不需要一次完成整个 2 小时单元。

## 20 小时课程地图

| 单元 | 主题 | 微课数量 | 核心问题 | 入口 |
|---:|---|---:|---|---|
| 01 | 坐标系与变换链 | 10 × 12 分钟 | [一个传感器点怎样在不改变物理位置的前提下，被正确表达在地图坐标系中？](01_coordinate_frames/README.md) | [第 01 课](01_coordinate_frames/lesson_01_why_frames.md) |
| 02 | 旋转与刚体位姿 | 10 × 12 分钟 | [二维和三维旋转应怎样表示、组合、插值并在工程中保持数值合法？](02_rotation_pose/README.md) | [第 01 课](02_rotation_pose/lesson_01_rotation_is_not_translation.md) |
| 03 | 传感器、时间与标定 | 10 × 12 分钟 | [多传感器数据怎样在同一坐标、同一时间和可信标定下进入融合系统？](03_sensors_time_calibration/README.md) | [第 01 课](03_sensors_time_calibration/lesson_01_measurement_state_frame_time.md) |
| 04 | 最小二乘基础 | 10 × 12 分钟 | [当测量比未知量多且彼此矛盾时，怎样用残差、雅可比和权重求出最合理的状态？](04_least_squares/README.md) | [第 01 课](04_least_squares/lesson_01_overdetermined_residual.md) |
| 05 | 概率与卡尔曼更新 | 10 × 12 分钟 | [当预测和多个带噪测量互相矛盾时，怎样用概率和协方差决定相信谁？](05_probability_kalman/README.md) | [第 01 课](05_probability_kalman/lesson_01_mean_variance_covariance.md) |
| 06 | IMU 与轮式推算 | 10 × 12 分钟 | [IMU 和轮速实际测到什么，怎样从测量积分出姿态、速度和位置，又为什么必然漂移？](06_imu_wheel_odometry/README.md) | [第 01 课](06_imu_wheel_odometry/lesson_01_accelerometer_specific_force.md) |
| 07 | 局部里程计 | 10 × 12 分钟 | [局部里程计怎样连续估计相邻时刻运动，它为什么平滑却会长期漂移？](07_local_odometry/README.md) | [第 01 课](07_local_odometry/lesson_01_odometry_definition.md) |
| 08 | 滤波与因子图 | 10 × 12 分钟 | [滤波和因子图怎样用不同计算方式解决同一个状态估计问题？](08_filtering_factor_graphs/README.md) | [第 01 课](08_filtering_factor_graphs/lesson_01_filtering_vs_smoothing.md) |
| 09 | SLAM 与全局修正 | 10 × 12 分钟 | [SLAM 怎样把局部里程计、回环约束和地图表示连接起来，形成长期一致的轨迹与地图？](09_slam_global_correction/README.md) | [第 01 课](09_slam_global_correction/lesson_01_slam_problem_outputs.md) |
| 10 | 重定位与综合系统设计 | 10 × 12 分钟 | [系统丢失或启动时，怎样在已有地图中恢复可信位姿，并把它安全接回局部定位链？](10_relocalization_system_design/README.md) | [第 01 课](10_relocalization_system_design/lesson_01_relocalization_loop_global.md) |

## 每课怎样学习

1. 不看正文，先回答标题问题；
2. 阅读核心讲解，重点理解机制、输入输出、坐标系、时间和失败条件；
3. 完成一个最小练习，保留推理过程；
4. 看工程例子，把概念接到自动驾驶、机器人或无人机；
5. 合上资料，用一句话复述；
6. 在[微课进度表](progress.md)中勾选，并记录一个卡点。

## 两种学习节奏

### 每天约 12 分钟

每天完成 1 课，约 100 天完成第一轮。

### 每周 5 课

工作日每天 1 课，20 周完成第一轮；周末用于复习、实验和费曼分享。

## 单元与延迟复习

每完成一个 10 课单元：

- 当天：用 5 分钟画知识链；
- D1：闭卷重做最关键练习；
- D3：换一个数值或工况；
- D7：完成单元变式题；
- D14：连接到下一个系统模块；
- D30：做一次混合故障诊断。

微课阅读完成不等于掌握。进入 `已掌握` 前仍需要练习、实验、终测和延迟复习。

## 与原 2 小时单元的关系

- 本目录提供低门槛的连续学习入口；
- 原 `docs/units/` 保留工作簿、实验、终测和完整单元闭环；
- 微课完成 10 课后，应回到对应 2 小时单元完成实验和统一考核；
- 单元 02～10 的微课内容已经完整，但原仓库的专项代码实验仍需按后续开发计划逐步补齐。

## 内容边界

课程依据仓库既定十单元路线组织。单元 01 沿用已有坐标变换课程的符号、RFU 坐标约定和 `sensor/base/odom/map` 体系；单元 02～10 根据既定学习地图扩写为基础课程，不替代具体论文综述、产品手册或真实项目验证。
