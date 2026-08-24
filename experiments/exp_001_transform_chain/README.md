# 实验 001：坐标变换链

本实验属于[单元 01：坐标系与变换链](../../docs/units/01_coordinate_frames/README.md)。请先在单元[工作簿](../../docs/units/01_coordinate_frames/workbook.md)中完成运行前预测，再执行命令。

仓库已有代码和测试通过，只证明参考实现满足当前测试，不能证明学习者已经掌握。本人预测、运行、解释、故障定位和延迟复验才是学习证据。

## 实验要回答的问题

已知一个点在 `base` 坐标系中的坐标，以及从 `base` 到 `odom`、从 `odom` 到 `map` 的两段变换：

1. 如何把点依次变换到 `odom` 和 `map`？
2. 如何复合得到从 `base` 到 `map` 的变换？
3. 为什么逐段计算与一次复合应当一致？
4. 哪些错误虽然不会触发矩阵维度异常，却会破坏坐标语义？
5. 改变一个旋转、平移或输入点后，怎样提前预测结果变化？

当前脚本只验证 `base → odom → map` 的两段变换。完整的 `lidar → base → odom → map` 链在单元课程和工作簿中推导，传感器时间错位实验留到后续时间与标定单元。

## 统一约定

- 使用右手坐标系、列向量和齐次变换左乘。
- 变换的右下标表示源坐标系，左上标表示目标坐标系。
- 点变换关系为：

$$
{}^{A}\mathbf p={}^{A}\mathbf T_B{}^{B}\mathbf p
$$

- 正确复合关系为：

$$
{}^{\mathrm{map}}\mathbf T_{\mathrm{base}}=
{}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}
{}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}
$$

## 第 1 步：运行前预测

打开 `run.py` 阅读输入数值，但先不要执行。把以下内容写入工作簿：

1. `p_base` 先变到 `odom` 后，各坐标大致怎样变化？
2. 再变到 `map` 后，各坐标大致怎样变化？
3. 逐段结果与复合结果应满足什么关系？
4. 差值应为严格的数学零，还是允许存在浮点误差？
5. 若交换两个变换的乘法顺序，为什么程序仍可能输出一个三维点？

没有预测记录时，不进入下一步。

## 第 2 步：运行正确基线

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

这一行只能证明两条数值路径在设定容差内一致。还必须逐项解释每个矩阵和点的源、目标坐标系，并比较运行前预测与实际结果。

## 第 3 步：验证关键性质

运行刚体变换测试：

```bash
PYTHONPATH=src python -m unittest tests/test_transforms.py -v
```

需要解释：

- 为什么逆变换要做双向单位矩阵检查；
- 为什么逐段点变换与复合点变换一致；
- 自动测试能够证明什么，不能证明什么。

重点观察 `test_inverse_is_two_sided_identity` 和
`test_composition_matches_sequential_point_transform`。其余测试用于检查旋转合法性、
输入形状和非有限数值等边界条件。

仓库测试通过不能替代本人闭卷推导。

## 第 4 步：只改变一个参数

先选择一个变量：输入点、某段平移或某个旋转角。保持其他量不变，先在工作簿写出变化方向预测，再运行变体。

下面的临时代码不修改仓库文件。示例只把 `odom` 中的车体平移在第一维增加 1 米，并同时生成两个故障结果。运行前先预测四个输出之间的关系。

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
    return np.array([[c, -s, 0.0], [s, c, 0.0], [0.0, 0.0, 1.0]])


t_odom_base = make_transform(rotation_z(30.0), [2.0, 1.0, 0.0])
t_odom_base_changed = make_transform(rotation_z(30.0), [3.0, 1.0, 0.0])
t_map_odom = make_transform(rotation_z(-10.0), [10.0, -3.0, 0.5])
p_base = np.array([1.0, 0.5, 0.2])

t_map_base = compose_transforms(t_map_odom, t_odom_base)
t_map_base_changed = compose_transforms(t_map_odom, t_odom_base_changed)
t_wrong_order = compose_transforms(t_odom_base, t_map_odom)
t_wrong_direction = compose_transforms(t_map_odom, invert_transform(t_odom_base))

print("baseline:", transform_points(t_map_base, p_base))
print("one parameter changed:", transform_points(t_map_base_changed, p_base))
print("wrong order:", transform_points(t_wrong_order, p_base))
print("wrong direction:", transform_points(t_wrong_direction, p_base))
PY
```

不要只记录四个数值。说明变化来自哪一段、平移先在哪个坐标系中表达，以及故障结果为什么“数值有限但语义无效”。

## 第 5 步：故意注入错序和错方向

### 故障 A：交换复合顺序

错误候选写法为把 `T_map_odom` 与 `T_odom_base` 的先后顺序交换。执行上一步临时代码前先回答：

- 交换后相邻坐标系还能否衔接？
- 为什么两个 $4\times4$ 矩阵仍能相乘？
- 什么测试点最容易暴露错误？

运行后将故障输出与基线比较，并在工作簿中写出坐标语义上的第一处错误。

### 故障 B：把正向变换当作反向变换

错误候选写法为在需要 `base → odom` 时使用它的逆。执行前先回答：

- 逆变换真正接受哪个坐标系中的输入？
- 当前输入点是否满足该条件？
- 为什么结果仍可能是一个正常形状的数组？

运行后写出最小修正和一个可以防止复发的往返测试。

故障注入必须建立在正确基线上。若基线尚未解释清楚，不应同时尝试多个错误。

## 第 6 步：保存证据

把以下内容保存到本次 `sessions/YYYY-MM-DD_attempt-N.md`：

- 仓库提交、Python 版本和实际命令；
- 运行前预测；
- 基线关键输出与逐项解释；
- 单参数变化的预测和结果；
- 错序与错方向的预测、现象、根因和修正；
- 测试输出；
- 一个仍未解决的问题。

若结果不一致，使用 [debug.md](debug.md) 的固定顺序排查，不要先交换矩阵碰碰运气。

## 第 7 步：返回单元闭环

实验完成后返回[单元控制面板](../../docs/units/01_coordinate_frames/README.md)：

1. 在工作簿完成故障注入结论；
2. 将真实错误写入[错误记录](../../docs/units/01_coordinate_frames/mistakes.md)；
3. 完成[无答案终测](../../docs/units/01_coordinate_frames/quiz.md)；
4. 输出 5 分钟讲解；
5. 安排延迟复习。

实验运行成功不是单元结束标志。
