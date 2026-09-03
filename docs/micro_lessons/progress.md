# 100 节微课进度表

本页只记录微课阅读与最小练习完成情况。单元状态仍以练习、实验、终测和延迟复习证据为准。

| 单元 | 课次 | 主题 | 状态 | 日期 | 一句话卡点 |
|---:|---:|---|---|---|---|
| 01 | 01 | [为什么同一个世界需要多个坐标系？](01_coordinate_frames/lesson_01_why_frames.md) | ⬜ |  |  |
| 01 | 02 | [同一个点为什么会有不同坐标？](01_coordinate_frames/lesson_02_object_vs_coordinates.md) | ⬜ |  |  |
| 01 | 03 | [RFU、右手系和列向量约定为什么必须先统一？](01_coordinate_frames/lesson_03_rfu_contract.md) | ⬜ |  |  |
| 01 | 04 | [点和方向向量为什么不能用同一套平移规则？](01_coordinate_frames/lesson_04_point_vs_vector.md) | ⬜ |  |  |
| 01 | 05 | [怎样一眼读懂变换记号的源和目标？](01_coordinate_frames/lesson_05_read_transform_notation.md) | ⬜ |  |  |
| 01 | 06 | [为什么点变换必然是旋转后加平移？](01_coordinate_frames/lesson_06_derive_rpt.md) | ⬜ |  |  |
| 01 | 07 | [旋转矩阵的每一列到底表示什么？](01_coordinate_frames/lesson_07_rotation_columns.md) | ⬜ |  |  |
| 01 | 08 | [齐次矩阵为什么能把旋转和平移合在一起？](01_coordinate_frames/lesson_08_homogeneous_transform.md) | ⬜ |  |  |
| 01 | 09 | [变换怎样组合、求逆并得到相对位姿？](01_coordinate_frames/lesson_09_compose_inverse_relative.md) | ⬜ |  |  |
| 01 | 10 | [怎样把 lidar 点一路变到 map，并检查时间？](01_coordinate_frames/lesson_10_localization_chain_review.md) | ⬜ |  |  |
| 02 | 01 | [三维姿态为什么不能当作普通三维向量相加？](02_rotation_pose/lesson_01_rotation_is_not_translation.md) | ⬜ |  |  |
| 02 | 02 | [轴角与 Rodrigues 公式在表达什么？](02_rotation_pose/lesson_02_axis_angle_rodrigues.md) | ⬜ |  |  |
| 02 | 03 | [欧拉角为什么必须连同旋转顺序一起写？](02_rotation_pose/lesson_03_euler_angles_order.md) | ⬜ |  |  |
| 02 | 04 | [怎样判断一个 3×3 矩阵是不是合法旋转？](02_rotation_pose/lesson_04_validate_rotation_matrix.md) | ⬜ |  |  |
| 02 | 05 | [四元数为什么用四个数表达三个自由度？](02_rotation_pose/lesson_05_quaternion_intuition.md) | ⬜ |  |  |
| 02 | 06 | [四元数乘法和向量旋转怎样理解？](02_rotation_pose/lesson_06_quaternion_operations.md) | ⬜ |  |  |
| 02 | 07 | [姿态插值为什么通常使用 SLERP？](02_rotation_pose/lesson_07_slerp_interpolation.md) | ⬜ |  |  |
| 02 | 08 | [刚体位姿中的旋转和平移怎样共同组合？](02_rotation_pose/lesson_08_se3_pose_composition.md) | ⬜ |  |  |
| 02 | 09 | [SO(3)、SE(3) 和李代数为什么适合优化？](02_rotation_pose/lesson_09_lie_group_intuition.md) | ⬜ |  |  |
| 02 | 10 | [工程中怎样选择旋转表示并完成单元复盘？](02_rotation_pose/lesson_10_representation_selection_review.md) | ⬜ |  |  |
| 03 | 01 | [一条传感器数据到底还缺哪些上下文？](03_sensors_time_calibration/lesson_01_measurement_state_frame_time.md) | ⬜ |  |  |
| 03 | 02 | [延迟、抖动和时钟漂移有什么区别？](03_sensors_time_calibration/lesson_02_clock_latency_jitter_drift.md) | ⬜ |  |  |
| 03 | 03 | [硬件同步和软件同步分别解决什么？](03_sensors_time_calibration/lesson_03_hardware_software_sync.md) | ⬜ |  |  |
| 03 | 04 | [异步传感器为什么需要位姿插值？](03_sensors_time_calibration/lesson_04_pose_interpolation.md) | ⬜ |  |  |
| 03 | 05 | [内参和外参分别在校准什么？](03_sensors_time_calibration/lesson_05_intrinsic_extrinsic.md) | ⬜ |  |  |
| 03 | 06 | [怎样验证外参方向没有写反？](03_sensors_time_calibration/lesson_06_extrinsic_direction_validation.md) | ⬜ |  |  |
| 03 | 07 | [为什么一帧点云内部也要做运动补偿？](03_sensors_time_calibration/lesson_07_motion_compensation.md) | ⬜ |  |  |
| 03 | 08 | [为什么某些运动无法标定出全部外参？](03_sensors_time_calibration/lesson_08_calibration_observability.md) | ⬜ |  |  |
| 03 | 09 | [怎样从点云和投影症状判断时间还是外参问题？](03_sensors_time_calibration/lesson_09_symptoms_diagnosis.md) | ⬜ |  |  |
| 03 | 10 | [怎样制定一套可复现的同步与标定验收方案？](03_sensors_time_calibration/lesson_10_validation_plan_review.md) | ⬜ |  |  |
| 04 | 01 | [方程无精确解时为什么要最小化残差？](04_least_squares/lesson_01_overdetermined_residual.md) | ⬜ |  |  |
| 04 | 02 | [正规方程为什么等价于残差正交？](04_least_squares/lesson_02_projection_normal_equation.md) | ⬜ |  |  |
| 04 | 03 | [秩、唯一性和病态为什么决定解是否可靠？](04_least_squares/lesson_03_rank_uniqueness_condition.md) | ⬜ |  |  |
| 04 | 04 | [不同测量精度不同时怎样加权？](04_least_squares/lesson_04_weighted_least_squares.md) | ⬜ |  |  |
| 04 | 05 | [非线性残差为什么要在当前点附近线性化？](04_least_squares/lesson_05_nonlinear_linearization.md) | ⬜ |  |  |
| 04 | 06 | [雅可比到底表示什么，怎样检查它？](04_least_squares/lesson_06_jacobian_meaning_check.md) | ⬜ |  |  |
| 04 | 07 | [Gauss-Newton 一步到底在解什么？](04_least_squares/lesson_07_gauss_newton.md) | ⬜ |  |  |
| 04 | 08 | [Levenberg-Marquardt 为什么在困难问题上更稳？](04_least_squares/lesson_08_lm_damping.md) | ⬜ |  |  |
| 04 | 09 | [为什么平方损失会被离群点支配？](04_least_squares/lesson_09_robust_loss_outlier.md) | ⬜ |  |  |
| 04 | 10 | [怎样用残差诊断一次位姿优化，而不只看最终数值？](04_least_squares/lesson_10_least_squares_review.md) | ⬜ |  |  |
| 05 | 01 | [均值、方差和协方差分别在描述什么？](05_probability_kalman/lesson_01_mean_variance_covariance.md) | ⬜ |  |  |
| 05 | 02 | [高斯分布和置信椭圆怎样读？](05_probability_kalman/lesson_02_gaussian_ellipse.md) | ⬜ |  |  |
| 05 | 03 | [Bayes 公式怎样把先验和测量合在一起？](05_probability_kalman/lesson_03_bayes_prior_likelihood_posterior.md) | ⬜ |  |  |
| 05 | 04 | [两个高斯测量为什么按逆方差加权？](05_probability_kalman/lesson_04_gaussian_fusion_precision.md) | ⬜ |  |  |
| 05 | 05 | [状态模型和过程噪声分别在预测什么？](05_probability_kalman/lesson_05_state_process_model.md) | ⬜ |  |  |
| 05 | 06 | [测量模型和创新为什么是更新的入口？](05_probability_kalman/lesson_06_measurement_innovation.md) | ⬜ |  |  |
| 05 | 07 | [Kalman 增益为什么决定相信预测还是测量？](05_probability_kalman/lesson_07_kalman_gain_scalar.md) | ⬜ |  |  |
| 05 | 08 | [状态更新后协方差为什么会变小，怎样保持一致性？](05_probability_kalman/lesson_08_covariance_update_consistency.md) | ⬜ |  |  |
| 05 | 09 | [EKF 如何把非线性系统变成局部 Kalman 更新？](05_probability_kalman/lesson_09_ekf_linearization.md) | ⬜ |  |  |
| 05 | 10 | [怎样拒绝异常测量并判断滤波器是否可信？](05_probability_kalman/lesson_10_gating_nis_review.md) | ⬜ |  |  |
| 06 | 01 | [加速度计为什么静止时不是零？](06_imu_wheel_odometry/lesson_01_accelerometer_specific_force.md) | ⬜ |  |  |
| 06 | 02 | [陀螺仪测到的角速度属于哪个坐标系？](06_imu_wheel_odometry/lesson_02_gyroscope_body_rate.md) | ⬜ |  |  |
| 06 | 03 | [怎样把加速度计读数变成世界运动加速度？](06_imu_wheel_odometry/lesson_03_gravity_compensation.md) | ⬜ |  |  |
| 06 | 04 | [陀螺积分为什么会让姿态漂移？](06_imu_wheel_odometry/lesson_04_gyro_integration_bias.md) | ⬜ |  |  |
| 06 | 05 | [加速度双积分为什么比姿态更容易失控？](06_imu_wheel_odometry/lesson_05_accel_double_integration.md) | ⬜ |  |  |
| 06 | 06 | [白噪声、零偏和随机游走怎样区分？](06_imu_wheel_odometry/lesson_06_bias_noise_random_walk.md) | ⬜ |  |  |
| 06 | 07 | [IMU 预积分为什么能减少优化重复计算？](06_imu_wheel_odometry/lesson_07_preintegration_intuition.md) | ⬜ |  |  |
| 06 | 08 | [轮速怎样变成车辆前向速度和转角运动？](06_imu_wheel_odometry/lesson_08_wheel_encoder_kinematics.md) | ⬜ |  |  |
| 06 | 09 | [轮胎打滑时轮式里程计为什么会自信地错？](06_imu_wheel_odometry/lesson_09_slip_failure_modes.md) | ⬜ |  |  |
| 06 | 10 | [怎样用 IMU 和轮速互补，并诊断失败？](06_imu_wheel_odometry/lesson_10_imu_wheel_fusion_review.md) | ⬜ |  |  |
| 07 | 01 | [里程计到底输出什么，为什么不等于全局定位？](07_local_odometry/lesson_01_odometry_definition.md) | ⬜ |  |  |
| 07 | 02 | [视觉里程计的完整数据流是什么？](07_local_odometry/lesson_02_vo_pipeline.md) | ⬜ |  |  |
| 07 | 03 | [特征法视觉里程计为什么依赖角点、描述子和几何验证？](07_local_odometry/lesson_03_feature_based_vo.md) | ⬜ |  |  |
| 07 | 04 | [直接法为什么不需要显式特征描述子？](07_local_odometry/lesson_04_direct_vo.md) | ⬜ |  |  |
| 07 | 05 | [LiDAR 里程计怎样通过配准估计运动？](07_local_odometry/lesson_05_lidar_registration.md) | ⬜ |  |  |
| 07 | 06 | [轮速和 IMU 里程计怎样提供运动先验？](07_local_odometry/lesson_06_wheel_imu_odometry.md) | ⬜ |  |  |
| 07 | 07 | [里程计退化时哪些自由度会失去约束？](07_local_odometry/lesson_07_degeneracy_observability.md) | ⬜ |  |  |
| 07 | 08 | [关键帧和局部地图为什么能兼顾精度与速度？](07_local_odometry/lesson_08_keyframes_local_map.md) | ⬜ |  |  |
| 07 | 09 | [ATE、RPE 和漂移率分别评价什么？](07_local_odometry/lesson_09_evaluation_metrics.md) | ⬜ |  |  |
| 07 | 10 | [怎样为自动驾驶、机器人和无人机选择局部里程计？](07_local_odometry/lesson_10_odometry_selection_review.md) | ⬜ |  |  |
| 08 | 01 | [滤波、平滑和批量优化有什么区别？](08_filtering_factor_graphs/lesson_01_filtering_vs_smoothing.md) | ⬜ |  |  |
| 08 | 02 | [递归 Bayes 滤波为什么能只保留上一时刻后验？](08_filtering_factor_graphs/lesson_02_recursive_bayes.md) | ⬜ |  |  |
| 08 | 03 | [EKF 状态向量应该包含哪些变量？](08_filtering_factor_graphs/lesson_03_ekf_state_design.md) | ⬜ |  |  |
| 08 | 04 | [误差状态滤波为什么适合处理姿态？](08_filtering_factor_graphs/lesson_04_eskf_error_injection.md) | ⬜ |  |  |
| 08 | 05 | [因子图中的变量节点和因子分别是什么？](08_filtering_factor_graphs/lesson_05_factor_graph_basics.md) | ⬜ |  |  |
| 08 | 06 | [MAP 估计为什么会变成加权非线性最小二乘？](08_filtering_factor_graphs/lesson_06_map_to_least_squares.md) | ⬜ |  |  |
| 08 | 07 | [稀疏性和滑动窗口怎样让优化实时运行？](08_filtering_factor_graphs/lesson_07_sparsity_sliding_window.md) | ⬜ |  |  |
| 08 | 08 | [边缘化怎样删除老状态却保留它的信息？](08_filtering_factor_graphs/lesson_08_marginalization_prior.md) | ⬜ |  |  |
| 08 | 09 | [Gauge freedom、可观测性和一致性怎样联系？](08_filtering_factor_graphs/lesson_09_observability_gauge_consistency.md) | ⬜ |  |  |
| 08 | 10 | [同一融合问题应选 EKF 还是因子图？](08_filtering_factor_graphs/lesson_10_ekf_vs_graph_review.md) | ⬜ |  |  |
| 09 | 01 | [SLAM 同时定位和建图到底输出什么？](09_slam_global_correction/lesson_01_slam_problem_outputs.md) | ⬜ |  |  |
| 09 | 02 | [SLAM 前端为什么本质上是在建立约束？](09_slam_global_correction/lesson_02_frontend_data_association.md) | ⬜ |  |  |
| 09 | 03 | [回环检测为什么要先检索候选地点？](09_slam_global_correction/lesson_03_loop_candidate_retrieval.md) | ⬜ |  |  |
| 09 | 04 | [回环候选为什么必须通过几何验证？](09_slam_global_correction/lesson_04_geometric_loop_verification.md) | ⬜ |  |  |
| 09 | 05 | [位姿图中的节点和边分别表示什么？](09_slam_global_correction/lesson_05_pose_graph_constraints.md) | ⬜ |  |  |
| 09 | 06 | [图优化怎样分配回环误差，为什么要固定 gauge？](09_slam_global_correction/lesson_06_graph_optimization_gauge.md) | ⬜ |  |  |
| 09 | 07 | [占据栅格、点云、特征和语义地图分别适合什么？](09_slam_global_correction/lesson_07_map_representations.md) | ⬜ |  |  |
| 09 | 08 | [回环后为什么通常改 map→odom 而不让 odom→base 跳变？](09_slam_global_correction/lesson_08_map_odom_global_correction.md) | ⬜ |  |  |
| 09 | 09 | [错误回环为什么危险，怎样降低它的破坏？](09_slam_global_correction/lesson_09_false_loop_robustness.md) | ⬜ |  |  |
| 09 | 10 | [怎样评估一套 SLAM，而不只看轨迹图和点云图？](09_slam_global_correction/lesson_10_slam_evaluation_review.md) | ⬜ |  |  |
| 10 | 01 | [重定位、回环和全局定位有什么区别？](10_relocalization_system_design/lesson_01_relocalization_loop_global.md) | ⬜ |  |  |
| 10 | 02 | [重定位为什么通常先检索地点候选？](10_relocalization_system_design/lesson_02_retrieval_candidates.md) | ⬜ |  |  |
| 10 | 03 | [候选地点怎样变成可信的 6DoF 位姿？](10_relocalization_system_design/lesson_03_geometric_verification_pose.md) | ⬜ |  |  |
| 10 | 04 | [视觉重定位的典型系统链是什么？](10_relocalization_system_design/lesson_04_visual_relocalization.md) | ⬜ |  |  |
| 10 | 05 | [LiDAR 重定位为什么常用描述子检索加子地图配准？](10_relocalization_system_design/lesson_05_lidar_relocalization.md) | ⬜ |  |  |
| 10 | 06 | [GNSS、语义、视觉和 LiDAR 怎样互相减少歧义？](10_relocalization_system_design/lesson_06_multimodal_priors.md) | ⬜ |  |  |
| 10 | 07 | [拓扑、Topometric 和 Metric 地图有什么区别？](10_relocalization_system_design/lesson_07_topological_topometric_metric.md) | ⬜ |  |  |
| 10 | 08 | [重定位置信度怎样决定接受、观察还是拒绝？](10_relocalization_system_design/lesson_08_confidence_recovery.md) | ⬜ |  |  |
| 10 | 09 | [量产重定位为什么离不开地图生命周期和版本管理？](10_relocalization_system_design/lesson_09_production_map_lifecycle.md) | ⬜ |  |  |
| 10 | 10 | [怎样完成一套可量产的重定位系统方案？](10_relocalization_system_design/lesson_10_system_design_final_review.md) | ⬜ |  |  |
