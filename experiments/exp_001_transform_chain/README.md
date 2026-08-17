# 实验 001：坐标变换链

## 要回答的问题

已知 `base` 中的点、`T_odom_base` 和 `T_map_odom`：

1. 如何把点依次变换到 `odom`、`map`？
2. 如何复合得到 `T_map_base`？
3. 为什么逐步计算与直接计算应当一致？

## 约定

- 使用右手坐标系、列向量和齐次变换左乘。
- `T_a_b` 把 B 系坐标变换到 A 系：`p_a = T_a_b p_b`。
- 因此 `T_map_base = T_map_odom T_odom_base`。

## 运行

在仓库根目录执行：

```bash
python experiments/exp_001_transform_chain/run.py
```

程序会打印两个变换、逐步计算结果、直接计算结果和两者差值。最后一行应为：

```text
两种路径是否一致: True
```

若不一致，先检查矩阵乘法顺序、变换方向和点是按行还是按列组织，再查看
[`debug.md`](debug.md) 中的调试清单。
