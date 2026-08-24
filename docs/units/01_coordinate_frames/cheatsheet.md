# 坐标变换速查表

本页是完成首次闭卷推导后的参考卡片，不是课程正文，也不能作为学习者证据。第一次作答和推导请使用[无答案工作簿](workbook.md)。

## 默认约定

- 坐标轴：右—前—上；右向轴记为 $x$，前向轴记为 $y$，上向轴记为 $z$
- 向量：列向量
- 变换记号的下标表示源坐标系，左上标表示目标坐标系

## 与 ROS 常见轴约定的区别

| 约定 | $x$ 轴 | $y$ 轴 | $z$ 轴 |
|---|---|---|---|
| 本仓库 RFU | 右 | 前 | 上 |
| ROS REP-103 常见 FLU | 前 | 左 | 上 |

两者都是右手系，但同一个三元组不代表相同物理方向。接入 ROS 或公开数据前先完成显式轴转换，不能只修改帧名。

## 高频公式

| 操作 | 规则 |
|---|---|
| 点变换 | 变换的源坐标系必须与点当前的表达坐标系一致 |
| 变换复合 | 相邻的中间坐标系必须一致 |
| 齐次变换 | 见下方独立公式 |
| 逆变换 | 见下方独立公式 |
| 全局车体位姿 | 先从车体映射到里程计坐标系，再映射到地图坐标系 |
| 全局修正 | 用全局车体位姿消去局部车体位姿 |

点变换为：

$$
{}^{A}\mathbf p={}^{A}\mathbf T_B{}^{B}\mathbf p
$$

变换复合为：

$$
{}^{A}\mathbf T_C={}^{A}\mathbf T_B{}^{B}\mathbf T_C
$$

定位系统中的全局车体位姿为：

$$
{}^{\mathrm{map}}\mathbf T_{\mathrm{base}}
={}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}
{}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}
$$

相应的全局修正为：

$$
{}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}
={}^{\mathrm{map}}\mathbf T_{\mathrm{base}}
\left({}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}\right)^{-1}
$$

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
5. 检查变换与其逆的乘积是否接近单位矩阵。
6. 比较“逐段变换”与“一次复合变换”。

第五项使用下面的判据：

$$
\mathbf T\mathbf T^{-1}\approx\mathbf I
$$

## 常见红旗

- 矩阵维度正确不代表坐标系链正确。
- 逆变换的平移通常不是 $-\mathbf t$。
- 度和弧度混用会产生看似合理的错误。
- 静态外参也可能方向写反；动态 TF 还必须匹配测量时间。
