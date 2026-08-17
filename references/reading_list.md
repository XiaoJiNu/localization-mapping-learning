# 阅读清单

原则：优先阅读教材、论文和官方文档；每份材料都要带着问题阅读，并留下推导或实验产物。

## 第一轮核心资源

第一次诊断后，第一轮只选择五个主要事实锚点，不要求从头通读；每次围绕当前单元的问题按需查阅，并留下推导或实验。

| 资源 | 对应问题 | 第一轮使用方式 |
|---|---|---|
| Gilbert Strang, *Introduction to Linear Algebra* | 列空间、正交投影、秩与最小二乘 | 重做诊断中的投影与残差题 |
| Timothy D. Barfoot, [*State Estimation for Robotics*](https://asrl.utias.utoronto.ca/~tdb/bib/barfoot_ser24.pdf) | 几何、概率、滤波、优化和 IMU 的统一框架 | 作为第一轮主线教材，按单元查阅 |
| [tf2 文档](https://docs.ros.org/en/rolling/Concepts/Intermediate/About-Tf2.html)与 [REP-105](https://www.ros.org/reps/rep-0105.html) | 坐标树、时间查询以及 `map`、`odom`、`base_link` 约定 | 用官方定义校核符号和系统行为 |
| [GTSAM 文档](https://gtsam.org/) | 残差、噪声模型、因子图与非线性优化 | 从二维小例子连接公式与代码 |
| [RTAB-Map 文档](https://introlab.github.io/rtabmap/) | 里程计、回环、图优化和重定位的系统关系 | 先梳理输入输出，再运行最小示例 |

其余资料作为对应单元的补充，不因为“可能有用”就全部加入第一轮。

## 基础数学

1. Gilbert Strang, *Introduction to Linear Algebra*：列空间、正交投影与最小二乘。
2. Timothy D. Barfoot, *State Estimation for Robotics*：概率估计、三维几何、滤波与优化的统一视角。
3. Simo Särkkä, *Bayesian Filtering and Smoothing*：Bayesian 滤波的系统推导。

## 状态估计与 SLAM

1. Thrun, Burgard, Fox, *Probabilistic Robotics*：机器人概率模型和经典定位方法。
2. Dellaert and Kaess, “Factor Graphs for Robot Perception”：因子图建模与推断。
3. Cadena et al., “Past, Present, and Future of Simultaneous Localization and Mapping”：SLAM 全景综述。
4. Forster et al., “On-Manifold Preintegration for Real-Time Visual-Inertial Odometry”：IMU 预积分。

## 工程文档

- [ROS 2 文档](https://docs.ros.org/en/rolling/)：消息、时间、QoS 和工具链。
- [tf2 文档](https://docs.ros.org/en/rolling/Concepts/Intermediate/About-Tf2.html)：坐标树、时间缓存与查询。
- [REP-105](https://www.ros.org/reps/rep-0105.html)：`map`、`odom`、`base_link` 坐标系约定。
- [GTSAM 文档](https://gtsam.org/)：因子图与非线性优化示例。

## 阅读记录模板

```text
材料：
要解决的问题：
三个关键结论：
一个未解决疑问：
推导或实验链接：
复习日期：
```
