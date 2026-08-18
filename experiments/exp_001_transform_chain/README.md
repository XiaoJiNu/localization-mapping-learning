# 实验 001：坐标变换链

## 要回答的问题

已知在 $\mathrm{base}$ 坐标系中表示的点 ${}^{\mathrm{base}}\mathbf p$、
${}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}$ 和
${}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}$：

1. 如何把点依次变换到 `odom` 和 `map` 坐标系？
2. 如何复合得到 ${}^{\mathrm{map}}\mathbf T_{\mathrm{base}}$？
3. 为什么逐步计算与直接计算应当一致？

## 约定

- 使用右手坐标系、列向量和齐次变换左乘。
- ${}^{A}\mathbf T_B$ 把在坐标系 $B$ 中表示的点变换到坐标系 $A$，关系如下。

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
