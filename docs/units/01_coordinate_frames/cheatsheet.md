# 坐标变换速查表

## 默认约定

- 坐标轴：右—前—上；右向轴记为 $x$，前向轴记为 $y$，上向轴记为 $z$
- 向量：列向量
- ${}^{A}\mathbf T_B$：将坐标系 $B$ 中的坐标映射到坐标系 $A$

## 高频公式

| 操作 | 公式 |
|---|---|
| 点变换 | ${}^{A}\mathbf p={}^{A}\mathbf T_B{}^{B}\mathbf p$ |
| 变换复合 | ${}^{A}\mathbf T_C={}^{A}\mathbf T_B{}^{B}\mathbf T_C$ |
| 齐次变换 | 见下方独立公式 |
| 逆变换 | 见下方独立公式 |
| 全局车体位姿 | ${}^{\mathrm{map}}\mathbf T_{\mathrm{base}}={}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}{}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}$ |
| 全局修正 | ${}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}={}^{\mathrm{map}}\mathbf T_{\mathrm{base}}\left({}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}\right)^{-1}$ |

齐次变换为：

$$
\mathbf T=
\begin{bmatrix}
\mathbf R&\mathbf t\\
\mathbf 0^{\mathsf T}&1
\end{bmatrix}
$$

它的逆变换为：

$$
\mathbf T^{-1}=
\begin{bmatrix}
\mathbf R^{\mathsf T}&-\mathbf R^{\mathsf T}\mathbf t\\
\mathbf 0^{\mathsf T}&1
\end{bmatrix}
$$

## 下标检查

写成点坐标从源到目标的映射路径：

$$
\mathtt{sensor}\to\mathtt{base}\to\mathtt{odom}\to\mathtt{map}
$$

相邻坐标系应能消去；最终只保留目标坐标系和源坐标系。

## 调试顺序

1. 明确坐标轴、单位和列/行向量约定。
2. 在每个量上标注表达坐标系。
3. 检查时间戳是否一致。
4. 用原点和三个单位轴验证旋转、平移方向。
5. 检查 $\mathbf T\mathbf T^{-1}\approx\mathbf I$。
6. 比较“逐段变换”与“一次复合变换”。

## 常见红旗

- 矩阵维度正确不代表坐标系链正确。
- 逆变换的平移通常不是 $-\mathbf t$。
- 度和弧度混用会产生看似合理的错误。
- 静态外参也可能方向写反；动态 TF 还必须匹配测量时间。
