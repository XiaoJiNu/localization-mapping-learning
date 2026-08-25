# 坐标变换速查表

本页只在完成主课程和首次练习后使用。它不是课程正文，也不能代替学习者自己的推导和实验。

第一次学习请先看[lesson.md](lesson.md)，个人过程写入[工作簿](workbook.md)。

## 默认约定

- 坐标轴：右—前—上（RFU）；
- 手性：右手系；
- 向量：列向量；
- 变换：左乘；
- 变换右下标表示源坐标系，左上标表示目标坐标系。

## 核心几何关系

$$
\overrightarrow{O_AP} =
\overrightarrow{O_AO_B} +
\overrightarrow{O_BP}
$$

统一使用坐标系 $A$ 表达后：

$$
{}^{A}\mathbf p =
{}^{A}\mathbf R_B{}^{B}\mathbf p +
{}^{A}\mathbf t_B
$$

## 点与方向向量

点受旋转和平移影响：

$$
{}^{A}\mathbf p =
{}^{A}\mathbf R_B{}^{B}\mathbf p +
{}^{A}\mathbf t_B
$$

方向向量只受旋转影响：

$$
{}^{A}\mathbf v =
{}^{A}\mathbf R_B{}^{B}\mathbf v
$$

齐次坐标中，点的最后一维为 1，方向向量的最后一维为 0。

## 旋转矩阵

旋转矩阵的各列，是源坐标系各坐标轴在目标坐标系中的坐标。

合法旋转矩阵满足：

$$
\mathbf R^{\mathsf T}\mathbf R = \mathbf I
$$

$$
\det(\mathbf R) = 1
$$

因此：

$$
\mathbf R^{-1} = \mathbf R^{\mathsf T}
$$

## 齐次变换与逆

$$
\mathbf T =
\begin{bmatrix}
\mathbf R & \mathbf t\\
\mathbf 0^{\mathsf T} & 1
\end{bmatrix}
$$

$$
\mathbf T^{-1} =
\begin{bmatrix}
\mathbf R^{\mathsf T} & -\mathbf R^{\mathsf T}\mathbf t\\
\mathbf 0^{\mathsf T} & 1
\end{bmatrix}
$$

完整齐次矩阵一般不满足“逆等于转置”。

## 变换组合

$$
{}^{A}\mathbf T_C =
{}^{A}\mathbf T_B{}^{B}\mathbf T_C
$$

采用列向量时，从右向左作用。前一段的输出坐标系必须等于后一段的输入坐标系。

## 两个全局位姿求相对位姿

已知坐标系 $A$ 和 $B$ 在世界坐标系 $W$ 中的位姿，则：

$$
{}^{A}\mathbf T_B =
\left({}^{W}\mathbf T_A\right)^{-1}
{}^{W}\mathbf T_B
$$

坐标路径：

```text
B → W → A
```

## 定位系统完整坐标链

$$
{}^{\mathrm{map}}\mathbf p =
{}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}
{}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}
{}^{\mathrm{base}}\mathbf T_{\mathrm{sensor}}
{}^{\mathrm{sensor}}\mathbf p
$$

点坐标映射路径：

```text
sensor → base → odom → map
```

TF 父子树常画成：

```text
map → odom → base → sensor
```

前者是点的计算路径，后者是坐标系父子拓扑。

## 全局车体位姿与全局修正

$$
{}^{\mathrm{map}}\mathbf T_{\mathrm{base}} =
{}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}
{}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}
$$

$$
{}^{\mathrm{map}}\mathbf T_{\mathrm{odom}} =
{}^{\mathrm{map}}\mathbf T_{\mathrm{base}}
\left({}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}\right)^{-1}
$$

## 时间规则

动态变换必须使用测量产生时刻：

$$
{}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}
\left(t_{\mathrm{measurement}}\right)
$$

不能因为消息在稍后被处理，就直接使用处理时刻的最新 TF。

## 固定调试顺序

1. 核对原点、轴向、手性和单位；
2. 给每个量标出表达坐标系；
3. 写完整点变换等式；
4. 检查相邻坐标系是否衔接；
5. 用原点检查平移；
6. 用单位轴检查旋转；
7. 检查旋转矩阵的正交性和行列式；
8. 检查正变换与逆变换的乘积；
9. 比较逐段变换与一次复合；
10. 核对角度制、单位和时间戳。

正反闭环应满足：

$$
\mathbf T\mathbf T^{-1} \approx \mathbf I
$$

## 常见红旗

- 矩阵维度正确，不代表坐标链正确；
- 不同坐标系表达的数字不能直接相加；
- 逆平移通常不是简单的负平移；
- 方向向量不应受到平移；
- RFU 与 ROS 常见 FLU 不能只改帧名；
- 坐标表达变化不等于物体真实运动；
- 静态外参可能方向写反，动态 TF 还必须匹配时间。
