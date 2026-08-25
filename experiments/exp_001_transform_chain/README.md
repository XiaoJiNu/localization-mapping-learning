# 实验 001：坐标变换链

本实验属于[单元 01：坐标系与变换链](../../docs/units/01_coordinate_frames/README.md)，对应单元六步流程中的 **步骤 4：最小实践**。

开始本实验前，应已经：

1. 学完单元主课程 `lesson.md`；
2. 完成工作簿中的关键推导；
3. 在[工作簿](../../docs/units/01_coordinate_frames/workbook.md)中进入“步骤 4：最小实验”。

本实验内部只有五个小步骤：预测、正确基线、改变参数、注入故障、保存证据。完成后返回单元统一终测。

## 实验要回答的问题

已知一个点在 `base` 坐标系中的坐标，以及从 `base` 到 `odom`、从 `odom` 到 `map` 的两段变换：

1. 怎样把点依次变换到 `odom` 和 `map`？
2. 怎样复合得到从 `base` 到 `map` 的变换？
3. 为什么逐段计算与一次复合应当一致？
4. 哪些错误虽然不会触发矩阵维度异常，却会破坏坐标语义？
5. 改变一个旋转、平移或输入点后，怎样提前预测结果变化？

当前脚本只验证 `base → odom → map` 的两段变换。完整的 `lidar → base → odom → map` 链已经在单元课程和工作簿中推导；传感器时间错位代码实验放在后续时间与标定单元。

## 统一约定

- 右手坐标系；
- 列向量；
- 齐次变换左乘；
- 变换右下标表示源坐标系；
- 变换左上标表示目标坐标系。

点变换关系：

$$
{}^{A}\mathbf p={}^{A}\mathbf T_B{}^{B}\mathbf p
$$

正确复合关系：

$$
{}^{\mathrm{map}}\mathbf T_{\mathrm{base}}=
{}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}
{}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}
$$

## 小步骤 A：运行前预测

打开 `run.py` 阅读输入数值，但先不要执行。在工作簿中填写：

1. `p_base` 先变到 `odom` 后，各坐标大致怎样变化？
2. 再变到 `map` 后，各坐标大致怎样变化？
3. 逐段结果与复合结果应满足什么关系？
4. 差值应为严格的数学零，还是允许存在浮点误差？
5. 若交换两个变换的乘法顺序，为什么程序仍可能输出一个三维点？

没有运行前预测时，不进入下一步。

## 小步骤 B：运行正确基线

从仓库根目录执行：

```bash
python experiments/exp_001_transform_chain/run.py
```

程序会打印：

1. `T_odom_base`；
2. `T_map_odom`；
3. 正确复合的 `T_map_base`；
4. 输入点 `p_base`；
5. 中间结果 `p_odom`；
6. 逐段得到的 `p_map`；
7. 一次复合得到的 `p_map`；
8. 两条路径的差值；
9. 两种路径是否一致。

最后一行应为：

```text
两种路径是否一致: True
```

这一行只证明两条数值路径在设定容差内一致。还要在工作簿中解释：

- 每个矩阵的源和目标坐标系；
- 每个点当前表达在哪个坐标系；
- 两个 `p_map` 为什么应相等；
- 为什么浮点差值不一定严格为零；
- 实际输出是否符合运行前预测。

### 运行自动测试

```bash
PYTHONPATH=src python -m unittest tests/test_transforms.py -v
```

重点观察：

- `test_inverse_is_two_sided_identity`；
- `test_composition_matches_sequential_point_transform`。

需要说明：

1. 为什么逆变换要做双向单位矩阵检查；
2. 为什么逐段点变换与复合点变换一致；
3. 自动测试能够证明参考代码的哪些性质；
4. 为什么测试通过仍不能代替学习者自己的推导和解释。

## 小步骤 C：只改变一个参数

选择一个变量：输入点、某段平移或某个旋转角。保持其他量不变，先写变化方向预测，再运行变体。

下面的临时代码不修改仓库文件。示例把车体在 `odom` 中的第一维平移增加 1 米，并同时计算两个故障结果。执行前先预测四个输出之间的关系。

```bash
PYTHONPATH=src python - <<'PY'
import numpy as np

from localization_learning.geometry.transforms import (
    compose_transforms,
    invert_transform,
    make_transform,
    transform_points,
)


def rotation_z(angle_degrees):
    angle = np.deg2rad(angle_degrees)
    c = np.cos(angle)
    s = np.sin(angle)
    return np.array(
        [[c, -s, 0.0], [s, c, 0.0], [0.0, 0.0, 1.0]]
    )


t_odom_base = make_transform(rotation_z(30.0), [2.0, 1.0, 0.0])
t_odom_base_changed = make_transform(
    rotation_z(30.0), [3.0, 1.0, 0.0]
)
t_map_odom = make_transform(rotation_z(-10.0), [10.0, -3.0, 0.5])
p_base = np.array([1.0, 0.5, 0.2])

t_map_base = compose_transforms(t_map_odom, t_odom_base)
t_map_base_changed = compose_transforms(
    t_map_odom, t_odom_base_changed
)
t_wrong_order = compose_transforms(t_odom_base, t_map_odom)
t_wrong_direction = compose_transforms(
    t_map_odom, invert_transform(t_odom_base)
)

print("baseline:", transform_points(t_map_base, p_base))
print(
    "one parameter changed:",
    transform_points(t_map_base_changed, p_base),
)
print("wrong order:", transform_points(t_wrong_order, p_base))
print(
    "wrong direction:",
    transform_points(t_wrong_direction, p_base),
)
PY
```

记录：

- 改变了哪个量；
- 原值和新值；
- 运行前预测；
- 实际结果；
- 变化来自哪一段；
- 平移先在哪个坐标系中表达；
- 预测与实际不一致时的原因。

## 小步骤 D：注入一个故障

先保证正确基线已经运行并解释清楚，再从下面选择一个故障。第一次只注入一种，不要同时修改多个因素。

### 故障 1：交换复合顺序

错误做法是交换 `T_map_odom` 与 `T_odom_base` 的顺序。

运行前回答：

- 交换后相邻坐标系还能否衔接？
- 为什么两个 `4 × 4` 矩阵仍能相乘？
- 哪个简单测试点最容易暴露错误？

运行后记录：

- 与基线的差异；
- 坐标语义上的第一处错误；
- 最小修正；
- 防止复发的检查方法。

### 故障 2：把正向变换当作反向变换

错误做法是在需要 `base → odom` 时使用它的逆。

运行前回答：

- 逆变换真正接受哪个坐标系中的输入？
- 当前输入点是否满足该条件？
- 为什么结果仍可能是正常形状的数组？

运行后记录：

- 实际现象；
- 根因；
- 最小修正；
- 正向再反向的往返测试。

### 故障 3：时间错位思想实验

一帧传感器数据在时刻 `t0` 产生，在时刻 `t1` 才被处理，机器人在两时刻之间发生运动。

回答：

- 应使用哪个时刻的动态变换？
- 若使用另一个时刻，偏差与哪些运动量相关？
- 怎样构造一个最小的恒速或恒角速度实验？

完整的时间错位代码实验留到后续单元，本实验只要求建立正确判断。

## 小步骤 E：保存证据并返回单元

将以下内容保存到本次 `sessions/YYYY-MM-DD_attempt-N.md`：

- 仓库提交、Python 版本和实际命令；
- 运行前预测；
- 基线关键输出与逐项解释；
- 自动测试输出与含义；
- 单参数变化的预测和结果；
- 一个故障的预测、现象、根因、修正和防回归方法；
- 一个仍未解决的问题。

若结果不一致，使用[调试说明](debug.md)中的固定顺序排查，不要先交换矩阵碰碰运气。

实验完成后返回[单元 01 主页](../../docs/units/01_coordinate_frames/README.md)，进入 **步骤 5：统一考核**：

1. 完成[无答案终测](../../docs/units/01_coordinate_frames/quiz.md)；
2. 提交完整答案后再查看参考答案；
3. 完成 5 分钟费曼输出；
4. 归档并安排延迟复习。

程序成功退出不是实验或单元的完成标志。