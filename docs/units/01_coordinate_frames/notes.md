# 参考笔记：坐标表达与变换

本页是单元 01 的压缩参考笔记，不是主课程。第一次学习应以[lesson.md](lesson.md)为主。

使用本页的两个时机：

1. 学习 `lesson.md` 时，某个概念仍然不清楚，需要另一种简短表述；
2. 完成课程和首次练习后，用于复习和核对遗漏。

个人理解、推导、实验和终测应写入[工作簿](workbook.md)的会话副本。本页不能替代自己的过程。

## 1. 几何对象与坐标不是一回事

空间中的点 $P$ 是几何对象。它在坐标系 $A$ 下的一组数字记作：

$$
{}^{A}\mathbf p
$$

更换坐标系不会移动真实的点，只会改变描述它的数字。

本仓库采用右—前—上、右手系、列向量和左乘。

## 2. 变换符号

$$
{}^{A}\mathbf p =
{}^{A}\mathbf T_B{}^{B}\mathbf p
$$

从等式直接读取：

- 输入点表达在坐标系 $B$；
- 输出点表达在坐标系 $A$；
- 变换的源坐标系是 $B$；
- 目标坐标系是 $A$。

自然语言出现歧义时，以完整等式为准。

## 3. 为什么点变换包含旋转和平移

纯几何关系为：

$$
\overrightarrow{O_AP} =
\overrightarrow{O_AO_B} +
\overrightarrow{O_BP}
$$

把所有向量统一用坐标系 $A$ 表达：

$$
{}^{A}\mathbf p =
{}^{A}\mathbf t_B +
{}^{A}\mathbf R_B{}^{B}\mathbf p
$$

通常写成：

$$
{}^{A}\mathbf p =
{}^{A}\mathbf R_B{}^{B}\mathbf p +
{}^{A}\mathbf t_B
$$

其中平移向量表示 $O_B$ 在坐标系 $A$ 中的坐标。

## 4. 点与方向向量

齐次点和方向向量分别写成：

$$
\bar{\mathbf p} =
\begin{bmatrix}
\mathbf p\\
1
\end{bmatrix},
\qquad
\bar{\mathbf v} =
\begin{bmatrix}
\mathbf v\\
0
\end{bmatrix}
$$

因此：

$$
\mathbf T\bar{\mathbf p} =
\begin{bmatrix}
\mathbf R\mathbf p + \mathbf t\\
1
\end{bmatrix}
$$

$$
\mathbf T\bar{\mathbf v} =
\begin{bmatrix}
\mathbf R\mathbf v\\
0
\end{bmatrix}
$$

点受旋转和平移影响；方向向量只受旋转影响。

## 5. 旋转矩阵

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

完整齐次矩阵一般不满足“逆等于转置”。

## 6. 变换组合

$$
{}^{A}\mathbf T_C =
{}^{A}\mathbf T_B{}^{B}\mathbf T_C
$$

采用列向量时，矩阵从右向左作用。真正的判断依据是：前一段输出坐标系必须等于后一段输入坐标系。

“中间坐标系可以消去”是一种快速检查方法。

## 7. 求逆

若齐次变换为：

$$
\mathbf T =
\begin{bmatrix}
\mathbf R & \mathbf t\\
\mathbf 0^{\mathsf T} & 1
\end{bmatrix}
$$

则逆变换为：

$$
\mathbf T^{-1} =
\begin{bmatrix}
\mathbf R^{\mathsf T} & -\mathbf R^{\mathsf T}\mathbf t\\
\mathbf 0^{\mathsf T} & 1
\end{bmatrix}
$$

逆平移通常不是简单的负平移，因为它还要重新表达在逆变换的目标坐标系中。

## 8. 两个全局位姿求相对位姿

已知坐标系 $A$ 和 $B$ 在世界坐标系 $W$ 中的位姿，则：

$$
{}^{A}\mathbf T_B =
\left({}^{W}\mathbf T_A\right)^{-1}
{}^{W}\mathbf T_B
$$

坐标路径为：

```text
B → W → A
```

## 9. 定位系统坐标链

$$
{}^{\mathrm{map}}\mathbf p =
{}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}
{}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}
{}^{\mathrm{base}}\mathbf T_{\mathrm{sensor}}
{}^{\mathrm{sensor}}\mathbf p
$$

- `sensor`：原始观测坐标系；
- `base`：车体坐标系；
- `odom`：局部连续但可能漂移；
- `map`：全局一致参考系。

全局车体位姿为：

$$
{}^{\mathrm{map}}\mathbf T_{\mathrm{base}} =
{}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}
{}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}
$$

全局修正可以更新：

$$
{}^{\mathrm{map}}\mathbf T_{\mathrm{odom}} =
{}^{\mathrm{map}}\mathbf T_{\mathrm{base}}
\left({}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}\right)^{-1}
$$

从而保持局部里程计输出连续。

## 10. TF 与时间

TF 树常按父帧到子帧画：

```text
map → odom → base → lidar
```

点坐标映射则从源到目标计算：

```text
lidar → base → odom → map
```

动态变换必须使用测量产生时刻。处理时间晚于测量时间时，不能直接使用处理时刻的最新 TF。

## 11. 三种快速自检

1. 用源坐标系原点检查平移；
2. 用单位轴检查旋转方向；
3. 检查正反变换和逐段/复合结果。

正反闭环应满足：

$$
\mathbf T\mathbf T^{-1} \approx \mathbf I
$$

## 12. 怎样使用本页

1. 第一次学习时，先读[lesson.md](lesson.md)；
2. 某个概念仍不清楚时，只查看本页对应小节；
3. 完成课程后，合上资料完成[工作簿](workbook.md)中的练习；
4. 完成独立尝试后，再用本页核对遗漏；
5. 真实错误写入[mistakes.md](mistakes.md)，不要把本页复制成个人总结。
