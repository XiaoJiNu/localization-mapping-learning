# 实验 001：坐标变换链

## 要回答的问题

已知一个点在 `base` 坐标系中的坐标，以及从 `base` 到 `odom`、从 `odom` 到 `map` 的两段变换：

1. 如何把点依次变换到 `odom` 和 `map` 坐标系？
2. 如何复合得到从 `base` 到 `map` 的变换？
3. 为什么逐步计算与直接计算应当一致？

## 约定

- 使用右手坐标系、列向量和齐次变换左乘。
- 变换的下标表示源坐标系，左上标表示目标坐标系；点变换关系如下。

$$
{}^{A}\mathbf p = {}^{A}\mathbf T_B{}^{B}\mathbf p
$$

- 因此可得下式。

$$
{}^{\mathrm{map}}\mathbf T_{\mathrm{base}}
= {}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}
  {}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}
$$

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
