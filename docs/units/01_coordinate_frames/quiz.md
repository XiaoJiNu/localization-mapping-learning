# 单元测验

先独立作答，再展开答案。需要写出推理过程，不能只给矩阵结果。

## 问题

1. ${}^{\mathrm{map}}\mathbf T_{\mathrm{lidar}}$ 的输入坐标和输出坐标分别是什么？
2. 已知 ${}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}$ 与 ${}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}$，如何得到 ${}^{\mathrm{map}}\mathbf T_{\mathrm{base}}$？
3. 为什么 $\left({}^{A}\mathbf T_B\right)^{-1}$ 的平移部分通常不是简单的 $-\mathbf t$？
4. 一个向量扩展成齐次坐标时最后一维为什么可以取 0？
5. 回环发生后，为什么一般不直接跳变 ${}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}$？
6. 激光帧产生于 $t=12.0\,\mathrm{s}$，但在 $t=12.1\,\mathrm{s}$ 才被处理，应查询哪个时刻的 TF？为什么？
7. 下面的乘法是否有效：${}^{\mathrm{map}}\mathbf T_{\mathrm{base}}{}^{\mathrm{camera}}\mathbf T_{\mathrm{lidar}}$？若无效，缺少什么？
8. 写出至少三种可以自动发现变换方向错误的测试。

<details>
<summary>参考答案</summary>

1. 输入是激光坐标系中的列向量，输出是地图坐标系中的列向量。
2. ${}^{\mathrm{map}}\mathbf T_{\mathrm{base}}={}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}{}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}$。
3. 反向平移必须先表达在反向变换的目标坐标系中，所以是 $-\mathbf R^{\mathsf T}\mathbf t$。
4. 最后一维为 0 会消去平移项，只保留旋转，符合纯方向量的性质。
5. ${}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}$ 服务局部控制，需要连续；全局修正可由 ${}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}$ 吸收。
6. 查询或插值 $12.0\,\mathrm{s}$ 的 TF，因为坐标变换必须与测量产生时刻一致。
7. 无效，中间坐标系 `base` 和 `camera` 不能消去；还缺少
   ${}^{\mathrm{base}}\mathbf T_{\mathrm{camera}}$。完整链为
   ${}^{\mathrm{map}}\mathbf T_{\mathrm{base}}{}^{\mathrm{base}}\mathbf T_{\mathrm{camera}}{}^{\mathrm{camera}}\mathbf T_{\mathrm{lidar}}$。
8. 单位变换、变换与逆的闭环、复合与逐段变换对比、原点与单位轴测试、随机点往返测试均可。

</details>

## 评分

- 7～8 题：可以进入下一个单元，但仍需完成代码验收。
- 5～6 题：复习求逆、变换链和时间同步。
- 0～4 题：重新做简单二维示例，再回到三维齐次变换。
