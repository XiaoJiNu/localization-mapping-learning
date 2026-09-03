# ChatGPT 辅助定位建图系统学习与工程实践

> 当前分支：`feat/20h-micro-lessons`

本分支参考 `microeconomicsLearning` 的每日短课结构，把定位建图第一轮 **20 小时**课程完整拆成 **100 节 10～15 分钟微课程**。目标不是把长文切碎，而是让每次学习只解决一个核心问题，并形成最小可验证证据。

## 30 秒开始

1. 打开[20 小时微课程总目录](docs/micro_courses/README.md)；
2. 进入[单元 01：坐标系与变换链](docs/micro_courses/01_coordinate_frames/README.md)；
3. 复制该单元的[工作簿](docs/micro_courses/01_coordinate_frames/workbook.md)；
4. 学习[第一课：同一个点为什么会有不同坐标？](docs/micro_courses/01_coordinate_frames/lesson_01_same_point_different_coordinates.md)；
5. 完成最小练习和一分钟无稿复述后停止，下次沿“下一课”继续。

## 课程规模

$$
10~\text{个单元}
\times 10~\text{节/单元}
\times 12~\text{分钟/节}
=20~\text{小时}
$$

| 单元 | 主题 | 微课数 | 第一轮预算 |
|---:|---|---:|---:|
| 01 | [坐标系与变换链](docs/micro_courses/01_coordinate_frames/README.md) | 10 | 约 2 h |
| 02 | [旋转与刚体位姿](docs/micro_courses/02_rotations_rigid_poses/README.md) | 10 | 约 2 h |
| 03 | [传感器、时间与标定](docs/micro_courses/03_sensors_time_calibration/README.md) | 10 | 约 2 h |
| 04 | [最小二乘](docs/micro_courses/04_least_squares/README.md) | 10 | 约 2 h |
| 05 | [概率与卡尔曼滤波](docs/micro_courses/05_probability_kalman/README.md) | 10 | 约 2 h |
| 06 | [IMU 与轮式推算](docs/micro_courses/06_imu_wheel_odometry/README.md) | 10 | 约 2 h |
| 07 | [局部里程计](docs/micro_courses/07_local_odometry/README.md) | 10 | 约 2 h |
| 08 | [滤波与因子图](docs/micro_courses/08_filtering_factor_graphs/README.md) | 10 | 约 2 h |
| 09 | [SLAM 与全局修正](docs/micro_courses/09_slam_global_correction/README.md) | 10 | 约 2 h |
| 10 | [重定位与系统设计](docs/micro_courses/10_relocalization_system_design/README.md) | 10 | 约 2 h |

## 每节怎样学

| 环节 | 时间 | 产出 |
|---|---:|---|
| 主动回忆 | 1 分钟 | 当前理解或前一课主线 |
| 聚焦讲解 | 7 分钟 | 一个核心机制、公式与工程含义 |
| 最小练习 | 3 分钟 | 手算、判断、草图、输入输出或故障预测 |
| 无稿复述 | 1 分钟 | 一分钟讲解和第一个卡点 |

完整规则见[微课程学习流程](docs/00_learning_system/micro_lesson_workflow.md)。

## 两条学习路径

| 路径 | 适合场景 | 入口 |
|---|---|---|
| 10～15 分钟微课程 | 每天持续推进，降低启动成本 | [100 节微课程](docs/micro_courses/README.md) |
| 原两小时集中路径 | 完整课程、推导、实验和正式终测 | [传统学习单元](docs/units/README.md) |

两条路径共享同一知识主线。微课程负责逐步建立结构；原路径中的实验与终测负责更严格验证。

## 学习证据

“看过文件”不算完成。每节至少留下：

- 一句话结论；
- 一个可检查的最小练习；
- 一次合上资料后的复述；
- 第一个卡点或未解决问题。

每单元第 10 节完成一次综合复述。全部进度记录在[20 小时进度表](docs/micro_courses/progress.md)。

## 五种目标能力

1. 画清传感器、坐标系、时间和数据流；
2. 解释主要算法的问题、输入、输出和假设；
3. 使用关键公式并说明变量、单位、坐标系和时刻；
4. 观察中间结果，复现失败并定位根因；
5. 根据传感器、场景、算力和精度要求完成方案取舍。

## 现有实验与代码

需要 Python 3.10 或更高版本。

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
pytest
python experiments/exp_001_transform_chain/run.py
```

原有实验、源码、测试、学习系统、文章与参考资料均保留。新增微课程只改变学习入口和颗粒度，不删除原材料。

## 文档与许可

- 源代码使用 [MIT License](LICENSE)；
- 文档、文章和图示使用 [CC BY 4.0](LICENSE-DOCS)；
- 提交 Markdown 前可运行 `make markdown`；
- 课程结构可运行 `pytest tests/test_micro_course_structure.py` 校验。
