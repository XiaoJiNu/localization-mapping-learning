# 公开项目索引

这些仓库用于阅读实现、复现实验和比较设计，不作为“直接复制即可工作”的方案。

| 项目 | 适合观察的内容 | 使用建议 |
|---|---|---|
| [GTSAM](https://github.com/borglab/gtsam) | 因子、变量、噪声模型和非线性优化 | 从二维 Pose2 小例子开始 |
| [Ceres Solver](https://github.com/ceres-solver/ceres-solver) | 残差块、自动求导和鲁棒损失 | 对照手写最小二乘实验 |
| [robot_localization](https://github.com/cra-ros-pkg/robot_localization) | ROS 多传感器 EKF/UKF 配置与坐标系处理 | 重点阅读状态、坐标和时间配置 |
| [RTAB-Map](https://github.com/introlab/rtabmap) | 图优化、回环与多传感器 SLAM | 先梳理模块输入输出再运行 |
| [Cartographer](https://github.com/cartographer-project/cartographer) | 局部轨迹、子地图和全局约束 | 对照前端/后端结构阅读 |
| [evo](https://github.com/MichaelGrupp/evo) | 轨迹对齐与 APE/RPE 评估 | 用合成轨迹理解指标后再评真实结果 |

## 阅读代码时的五个问题

1. 状态变量是什么，表达在哪个坐标系？
2. 每个输入的时间戳与噪声模型是什么？
3. 残差或更新方程连接了哪些状态？
4. 系统如何处理异常值、延迟和缺失数据？
5. 输出由什么指标验证，失败时有哪些可观察信号？

公开仓库的版本和接口会变化；复现实验时记录提交哈希与环境，不依赖模糊的“最新版”。
