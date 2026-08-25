# 连续课程：从坐标表达走到完整变换链

这是单元 01 的**主要学习材料**。第一次学习时，从第 1 节按顺序读到第 16 节，不需要在每个小节后立刻考试。

## 这篇课程怎样使用

每完成一个知识块，只做三件事：

1. 在自己的[工作簿](workbook.md)中写一句“我现在怎样理解”；
2. 记录一个关键公式、几何关系或工程规则；
3. 写下仍然不明白的问题。

可以随时要求 AI 提供示意图、动画或更小的二维例子。这个阶段可以看课程和提问，不属于闭卷考试。学完整篇、完成练习和实验后，才打开[终测](quiz.md)。

## 课程地图

| 知识块 | 章节 | 要解决的问题 |
|---|---:|---|
| A. 建立二维直觉 | 1～6 | 同一个点为什么会有不同坐标？为什么点变换是 $\mathbf R\mathbf p+\mathbf t$？ |
| B. 掌握矩阵工具 | 7～11 | 旋转矩阵是什么？怎样写齐次矩阵、组合、求逆和相对位姿？ |
| C. 接入定位系统 | 12～14 | `sensor/base/odom/map` 怎样连接？TF 和时间戳怎样理解？ |
| D. 工程判断与检查 | 15～16 | 坐标变换和物体运动有何区别？怎样发现方向、顺序和时间错误？ |

---

## 1. 为什么定位建图离不开坐标系

激光雷达给出的点最初属于激光雷达坐标系，相机观测属于相机坐标系，里程计估计车体在局部坐标系中的运动，地图则使用全局坐标系。如果不说明一个数值属于哪个坐标系，`[1, 2, 0]` 没有完整的几何意义。

坐标变换首先是在回答：

> 同一个几何对象，如果改用另一个原点和另一组坐标轴描述，它的数值应是多少？

地图中的墙不会因为坐标数值改变而移动。改变的是描述墙的坐标数字。

## 2. 几何对象、坐标系和坐标表达

一个坐标系至少包含：

- 一个原点；
- 三条有方向的坐标轴；
- 长度和角度单位；
- 轴之间满足的手性约定。

空间中的几何点记作 $P$。同一点在坐标系 $A$ 和坐标系 $B$ 中的两组数值表达分别记作：

$$
{}^{A}\mathbf p,
\qquad
{}^{B}\mathbf p
$$

两组数字可能不同，但描述的是同一个物理点。左上标不是乘方，而是在说明“这组数字使用哪个坐标系表达”。

### 位置、姿态和位姿

- **位置**：原点在哪里，通常用平移向量表示；
- **姿态**：坐标轴朝向怎样，常用旋转矩阵、欧拉角或四元数表示；
- **位姿**：同时包含位置和姿态。

坐标系 $B$ 相对于坐标系 $A$ 的位姿，也可以作为把点坐标从 $B$ 映射到 $A$ 的变换。

## 3. 本仓库的轴和乘法约定

本仓库采用：

- $x$ 轴向右；
- $y$ 轴向前；
- $z$ 轴向上；
- 右手系；
- 点使用列向量；
- 变换矩阵左乘点坐标。

这套“右—前—上”约定可以简称 RFU。ROS [REP-103](https://www.ros.org/reps/rep-0103.html) 常见车体坐标轴是：

- $x$ 轴向前；
- $y$ 轴向左；
- $z$ 轴向上。

它可以简称 FLU。两者都是右手系，但轴名对应的物理方向不同，不能只修改帧名而不转换数值。

同一个方向向量满足：

$$
{}^{\mathrm{FLU}}\mathbf v=
\begin{bmatrix}
0&1&0\\
-1&0&0\\
0&0&1
\end{bmatrix}
{}^{\mathrm{RFU}}\mathbf v
$$

例如，RFU 中的“向右 1 米”为：

$$
\begin{bmatrix}
1\\0\\0
\end{bmatrix}
$$

在 FLU 中应写成：

$$
\begin{bmatrix}
0\\-1\\0
\end{bmatrix}
$$

接入 ROS、公开数据集或其他代码前，必须先逐轴阅读其坐标定义。

## 4. 点与方向向量为什么不同

点表示空间中的一个位置，会受到旋转和平移共同影响：

$$
{}^{A}\mathbf p =
{}^{A}\mathbf R_B{}^{B}\mathbf p+{}^{A}\mathbf t_B
$$

其中：

- ${}^{A}\mathbf R_B$：把方向的坐标表达从 $B$ 转换到 $A$；
- ${}^{A}\mathbf t_B$：坐标系 $B$ 的原点 $O_B$ 在坐标系 $A$ 中的坐标；
- ${}^{B}\mathbf p$：点 $P$ 相对 $O_B$ 的坐标；
- ${}^{A}\mathbf p$：同一点 $P$ 相对 $O_A$ 的坐标。

方向向量可以由两个点相减得到。两个端点同时平移后，平移相消，因此方向向量只受旋转影响：

$$
{}^{A}\mathbf v={}^{A}\mathbf R_B{}^{B}\mathbf v
$$

在齐次坐标中：

- 点的最后一维是 1；
- 方向向量的最后一维是 0。

这使同一个齐次矩阵能够自动区分二者。

## 5. 为什么点变换必然是 $\mathbf R\mathbf p+\mathbf t$

设两个坐标系原点分别为 $O_A$ 和 $O_B$，空间中有一个点 $P$。

纯几何关系为：

$$
\overrightarrow{O_AP}
=
\overrightarrow{O_AO_B}
+
\overrightarrow{O_BP}
$$

它表示：

```text
从 O_A 到 P
= 从 O_A 到 O_B
+ 从 O_B 到 P
```

其中：

$$
{}^{A}\mathbf p
=
[\overrightarrow{O_AP}]_A
$$

$$
{}^{A}\mathbf t_B
=
[\overrightarrow{O_AO_B}]_A
$$

但 ${}^{B}\mathbf p$ 是 $\overrightarrow{O_BP}$ 在 $B$ 中的坐标，不能直接与使用 $A$ 表达的平移相加。必须先转换表达坐标系：

$$
[\overrightarrow{O_BP}]_A
=
{}^{A}\mathbf R_B{}^{B}\mathbf p
$$

所以：

$$
\boxed{
{}^{A}\mathbf p
=
{}^{A}\mathbf R_B{}^{B}\mathbf p
+
{}^{A}\mathbf t_B
}
$$

“先旋转、再平移”在这里更准确地表示：

1. 先把 $\overrightarrow{O_BP}$ 从 $B$ 的坐标表达改为 $A$ 的坐标表达；
2. 再与同样使用 $A$ 表达的 $\overrightarrow{O_AO_B}$ 相加。

点 $P$ 本身没有因此发生物理运动。

## 6. 一个可以手算的二维例子

设：

- 坐标系 $B$ 的原点在 $A$ 中为 $[3,1]^{\mathsf T}$；
- $B$ 的坐标轴相对 $A$ 逆时针旋转 $90^\circ$；
- 点在 $B$ 中的坐标为 $[2,1]^{\mathsf T}$。

旋转矩阵和平移为：

$$
{}^{A}\mathbf R_B=
\begin{bmatrix}
0&-1\\
1&0
\end{bmatrix},
\qquad
{}^{A}\mathbf t_B=
\begin{bmatrix}
3\\
1
\end{bmatrix}
$$

先把 $\overrightarrow{O_BP}$ 用 $A$ 表达：

$$
{}^{A}\mathbf R_B{}^{B}\mathbf p
=
\begin{bmatrix}
0&-1\\
1&0
\end{bmatrix}
\begin{bmatrix}
2\\
1
\end{bmatrix}
=
\begin{bmatrix}
-1\\
2
\end{bmatrix}
$$

这个结果不是点在 $A$ 中的最终坐标，而是：

$$
\overrightarrow{O_BP}
$$

在 $A$ 中的坐标。再加上 $O_B$ 在 $A$ 中的位置：

$$
{}^{A}\mathbf p
=
\begin{bmatrix}
-1\\
2
\end{bmatrix}
+
\begin{bmatrix}
3\\
1
\end{bmatrix}
=
\begin{bmatrix}
2\\
3
\end{bmatrix}
$$

几何上是：

- 从 $O_A$ 到 $O_B$：向右 3、向上 1；
- 从 $O_B$ 到 $P$：在 $A$ 中看是向左 1、向上 2；
- 合计从 $O_A$ 到 $P$：向右 2、向上 3。

## 7. 旋转矩阵的本质与性质

二维情况下，若 $B$ 相对 $A$ 逆时针旋转 $\theta$，则：

$$
{}^{A}\mathbf R_B=
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}
$$

它的两列分别是：

$$
{}^{A}\mathbf e_{x_B}
=
\begin{bmatrix}
\cos\theta\\
\sin\theta
\end{bmatrix},
\qquad
{}^{A}\mathbf e_{y_B}
=
\begin{bmatrix}
-\sin\theta\\
\cos\theta
\end{bmatrix}
$$

因此应记住：

> ${}^{A}\mathbf R_B$ 的各列，就是 $B$ 的各坐标轴在 $A$ 中的坐标。

当：

$$
{}^{B}\mathbf p=
\begin{bmatrix}
x_B\\y_B
\end{bmatrix}
$$

矩阵乘法实际是在做：

$$
{}^{A}\mathbf R_B{}^{B}\mathbf p
=
x_B{}^{A}\mathbf e_{x_B}
+y_B{}^{A}\mathbf e_{y_B}
$$

合法旋转矩阵满足：

$$
\mathbf R^{\mathsf T}\mathbf R=\mathbf I
$$

$$
\det(\mathbf R)=1
$$

所以：

$$
\boxed{
\mathbf R^{-1}=\mathbf R^{\mathsf T}
}
$$

旋转还保持向量长度、两向量夹角和两点距离不变。

注意：是**正交旋转矩阵**的逆等于转置，不是任意可逆矩阵都满足这一关系。

## 8. 从普通形式到齐次变换

二维点写成齐次坐标：

$$
{}^{B}\bar{\mathbf p}=
\begin{bmatrix}
x_B\\y_B\\1
\end{bmatrix}
$$

二维齐次变换为：

$$
{}^{A}\mathbf T_B=
\begin{bmatrix}
{}^{A}\mathbf R_B&{}^{A}\mathbf t_B\\
\mathbf 0^{\mathsf T}&1
\end{bmatrix}
$$

于是：

$$
{}^{A}\bar{\mathbf p}
=
{}^{A}\mathbf T_B{}^{B}\bar{\mathbf p}
$$

三维情况下：

$$
{}^{A}\mathbf T_B=
\begin{bmatrix}
{}^{A}\mathbf R_B&{}^{A}\mathbf t_B\\
\mathbf 0^{\mathsf T}&1
\end{bmatrix}
\in\mathbb R^{4\times4}
$$

三维点和方向向量分别写成：

$$
{}^{B}\bar{\mathbf p}=
\begin{bmatrix}
{}^{B}\mathbf p\\1
\end{bmatrix},
\qquad
{}^{B}\bar{\mathbf v}=
\begin{bmatrix}
{}^{B}\mathbf v\\0
\end{bmatrix}
$$

矩阵乘法得到：

$$
{}^{A}\mathbf T_B{}^{B}\bar{\mathbf p}=
\begin{bmatrix}
{}^{A}\mathbf R_B{}^{B}\mathbf p+{}^{A}\mathbf t_B\\1
\end{bmatrix}
$$

$$
{}^{A}\mathbf T_B{}^{B}\bar{\mathbf v}=
\begin{bmatrix}
{}^{A}\mathbf R_B{}^{B}\mathbf v\\0
\end{bmatrix}
$$

最后一维为 0 时，平移列不会作用到方向向量。

## 9. 变换为什么按这个顺序组合

已知点先从坐标系 $C$ 映射到 $B$，再从 $B$ 映射到 $A$：

$$
{}^{B}\mathbf p={}^{B}\mathbf T_C{}^{C}\mathbf p
$$

$$
{}^{A}\mathbf p={}^{A}\mathbf T_B{}^{B}\mathbf p
$$

把第一式代入第二式：

$$
{}^{A}\mathbf p=
{}^{A}\mathbf T_B
{}^{B}\mathbf T_C
{}^{C}\mathbf p
$$

所以：

$$
\boxed{
{}^{A}\mathbf T_C=
{}^{A}\mathbf T_B{}^{B}\mathbf T_C
}
$$

采用列向量和左乘时，最靠近点的矩阵最先作用：

```text
C 中的点
  ↓  ᴮT꜀
B 中的点
  ↓  ᴬTᴮ
A 中的点
```

“相邻的 $B$ 可以消去”是一种快速检查方法：

$$
{}^{A}\mathbf T_{\cancel B}
{}^{\cancel B}\mathbf T_C
=
{}^{A}\mathbf T_C
$$

但真正原因是：前一段输出坐标系必须等于后一段输入坐标系。

即使两个错误顺序的 $4\times4$ 矩阵仍能相乘，数值库通常也不会报错。因此“维度能乘”不等于“坐标语义正确”。

组合后的旋转和平移分别为：

$$
{}^{A}\mathbf R_C
=
{}^{A}\mathbf R_B{}^{B}\mathbf R_C
$$

$$
{}^{A}\mathbf t_C
=
{}^{A}\mathbf R_B{}^{B}\mathbf t_C
+
{}^{A}\mathbf t_B
$$

平移部分再次出现 $\mathbf R\mathbf p+\mathbf t$，因为 ${}^{B}\mathbf t_C$ 必须先改用 $A$ 表达，才能与 ${}^{A}\mathbf t_B$ 相加。

## 10. 齐次刚体变换怎样求逆

从：

$$
{}^{A}\mathbf p=
{}^{A}\mathbf R_B{}^{B}\mathbf p
+{}^{A}\mathbf t_B
$$

开始，先移去平移：

$$
{}^{A}\mathbf p-{}^{A}\mathbf t_B
=
{}^{A}\mathbf R_B{}^{B}\mathbf p
$$

再左乘旋转的逆：

$$
{}^{B}\mathbf p
=
\left({}^{A}\mathbf R_B\right)^{\mathsf T}
\left({}^{A}\mathbf p-{}^{A}\mathbf t_B\right)
$$

所以：

$$
{}^{B}\mathbf R_A
=
\left({}^{A}\mathbf R_B\right)^{\mathsf T}
$$

$$
{}^{B}\mathbf t_A
=
-
\left({}^{A}\mathbf R_B\right)^{\mathsf T}
{}^{A}\mathbf t_B
$$

完整逆变换为：

$$
\boxed{
{}^{B}\mathbf T_A
=
\left({}^{A}\mathbf T_B\right)^{-1}
=
\begin{bmatrix}
\left({}^{A}\mathbf R_B\right)^{\mathsf T}
&
-\left({}^{A}\mathbf R_B\right)^{\mathsf T}{}^{A}\mathbf t_B\\
\mathbf 0^{\mathsf T}&1
\end{bmatrix}
}
$$

逆平移通常不是简单的 $-\mathbf t$。把方向反过来只完成了第一步，反向平移还必须重新表达在反向目标坐标系中。

还要区分：

$$
\mathbf R^{-1}=\mathbf R^{\mathsf T}
$$

但完整齐次变换一般不满足：

$$
\mathbf T^{-1}=\mathbf T^{\mathsf T}
$$

最直接的闭环检查是：

$$
{}^{A}\mathbf T_B{}^{B}\mathbf T_A
\approx\mathbf I
$$

以及把一个点正向变换后再逆向变换，应回到原坐标。

## 11. 根据两个全局位姿求相对位姿

设世界坐标系为 $W$，已知：

$$
{}^{W}\mathbf T_A,
\qquad
{}^{W}\mathbf T_B
$$

要求坐标系 $B$ 相对于 $A$ 的位姿：

$$
{}^{A}\mathbf T_B
$$

坐标路径为：

```text
B 坐标
  ↓  ᵂTᴮ
W 坐标
  ↓  ᴬTᵂ = (ᵂTᴬ)⁻¹
A 坐标
```

因此：

$$
\boxed{
{}^{A}\mathbf T_B
=
\left({}^{W}\mathbf T_A\right)^{-1}
{}^{W}\mathbf T_B
}
$$

这在工程中非常常见。

### 两帧车辆位姿求相对运动

$$
{}^{\mathrm{base}_k}\mathbf T_{\mathrm{base}_{k+1}}
=
\left({}^{\mathrm{map}}\mathbf T_{\mathrm{base}_k}\right)^{-1}
{}^{\mathrm{map}}\mathbf T_{\mathrm{base}_{k+1}}
$$

### 根据共同车体系位姿求相机到雷达外参

$$
{}^{\mathrm{camera}}\mathbf T_{\mathrm{lidar}}
=
\left({}^{\mathrm{base}}\mathbf T_{\mathrm{camera}}\right)^{-1}
{}^{\mathrm{base}}\mathbf T_{\mathrm{lidar}}
$$

判断公式时，不要背“谁减谁”，而要画清源到目标的坐标路径。

## 12. 定位系统中的完整坐标链

常见移动机器人定位系统包含：

| 坐标系 | 作用 | 常见性质 |
|---|---|---|
| `sensor` | 传感器产生原始观测的坐标系 | 与 `base` 之间通常是静态外参 |
| `base` | 机器人或车辆的机体坐标系 | 随机器人运动 |
| `odom` | 连续的局部参考系 | 短期平滑，长期可能漂移 |
| `map` | 全局一致参考系 | 全局修正时可相对 `odom` 变化 |

以激光点为例：

$$
{}^{\mathrm{map}}\mathbf p =
{}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}
{}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}
{}^{\mathrm{base}}\mathbf T_{\mathrm{lidar}}
{}^{\mathrm{lidar}}\mathbf p
$$

从右向左执行：

1. `lidar → base`；
2. `base → odom`；
3. `odom → map`。

只需要车体全局位姿时：

$$
{}^{\mathrm{map}}\mathbf T_{\mathrm{base}}
=
{}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}
{}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}
$$

如果全局定位给出车体在地图中的位姿，则：

$$
\boxed{
{}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}
=
{}^{\mathrm{map}}\mathbf T_{\mathrm{base}}
\left({}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}\right)^{-1}
}
$$

这样可以保持局部里程计 ${}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}$ 连续，把回环、GNSS 或重定位带来的全局修正放入 ${}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}$。

## 13. TF 树的边与点坐标映射不是同一种箭头

TF 树常按父帧到子帧画边：

```text
map → odom → base → lidar
```

例如 `base → lidar` 表示 `base` 是父帧，`lidar` 是子帧；子帧 `lidar` 在父帧 `base` 中的位姿对应：

$$
{}^{\mathrm{base}}\mathbf T_{\mathrm{lidar}}
$$

但是把激光点变到地图时，点坐标映射路径是：

```text
lidar → base → odom → map
```

两组箭头看起来相反，是因为：

- 前者表示树的父子拓扑；
- 后者表示点坐标从源到目标的计算路径。

不能只看到箭头就猜矩阵方向。最终应写完整等式：

$$
{}^{\mathrm{target}}\mathbf p
=
{}^{\mathrm{target}}\mathbf T_{\mathrm{source}}
{}^{\mathrm{source}}\mathbf p
$$

ROS 移动平台中 `map`、`odom` 和 `base_link` 的常见职责可参考 [REP-105](https://www.ros.org/reps/rep-0105.html)，tf2 的查询与缓存可参考 [ROS 2 tf2 文档](https://docs.ros.org/en/rolling/Concepts/Intermediate/About-Tf2.html)。

## 14. 时间戳为什么也是变换条件

静态外参理想情况下不随时间变化，例如：

$$
{}^{\mathrm{base}}\mathbf T_{\mathrm{lidar}}
$$

车体相对 `odom` 的位姿会随运动变化，应写成：

$$
{}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}(t)
$$

假设激光帧在 $12.0~\mathrm{s}$ 产生，在 $12.1~\mathrm{s}$ 才被程序处理。正确做法是查询或插值测量产生时刻 $12.0~\mathrm{s}$ 的动态变换，而不是直接使用处理时刻的最新变换。

即使方向和矩阵顺序完全正确，时间不一致仍会产生与线速度、角速度和时间差相关的偏移。

本单元只建立基本规则：

> 动态变换必须与测量时刻一致。

多传感器异频同步和点云帧内运动补偿在后续单元展开。

## 15. 坐标变换与物体真实运动不是一回事

相同的形式：

$$
\mathbf p'=\mathbf R\mathbf p+\mathbf t
$$

可能有两种不同语义。

### 被动变换：物理点不动，换坐标系描述

$$
{}^{A}\mathbf p
=
{}^{A}\mathbf T_B{}^{B}\mathbf p
$$

- 输入和输出描述同一个物理点；
- 坐标系发生变化；
- 改变的是坐标数字。

本单元主要讨论这种情况。

### 主动变换：坐标系不动，物体真的运动

$$
\mathbf p'=\mathbf T\mathbf p
$$

- 坐标系保持不变；
- $\mathbf p$ 和 $\mathbf p'$ 对应两个不同物理位置；
- 物体真的发生旋转或平移。

只看矩阵数值无法区分两种语义。必须检查输入、输出、坐标系和问题描述。

不够严谨的说法是“把点旋转到 $A$ 系”。更严谨的说法是：

> 将向量或点的坐标表达从 $B$ 系转换到 $A$ 系。

## 16. 常见错误与固定调试顺序

### 常见错误

1. 只凭 `T_ab` 变量名猜方向；
2. 把不同坐标系表达的数字直接相加；
3. 交换矩阵顺序，因为维度仍能相乘而没有发现；
4. 把完整齐次变换的逆直接写成转置；
5. 把逆平移直接写成 $-\mathbf t$；
6. 对方向向量错误地加入平移；
7. 混用行向量和列向量；
8. 混用 RFU 与 FLU；
9. 混用角度和弧度；
10. 使用处理时刻而不是测量时刻的动态 TF；
11. 把坐标表达变化误认为物体真实运动。

### 固定调试顺序

遇到点云偏移、方向翻转或两条路径不一致时：

1. 写清每个坐标系的原点、轴向、手性和单位；
2. 给每个点、向量和变换标出表达坐标系；
3. 写出完整点变换等式，确认源和目标；
4. 检查相邻坐标系是否正确衔接；
5. 用源坐标系原点测试平移；
6. 用各单位轴测试旋转方向；
7. 检查 $\mathbf R^{\mathsf T}\mathbf R\approx\mathbf I$ 和 $\det(\mathbf R)\approx1$；
8. 检查变换与逆的乘积是否接近单位矩阵；
9. 比较逐段变换与一次复合变换；
10. 核对单位、角度制和时间戳；
11. 最后才换成真实点云或复杂数据。

简单原点和单位轴比真实点云更容易解释。出现问题时，先退回可手算的二维反例。

## 学完本页以后做什么

现在不要打开终测答案。返回自己的[工作簿](workbook.md)，依次完成：

1. 关键练习与推导；
2. [实验 001](../../../experiments/exp_001_transform_chain/README.md)；
3. 一个参数变化和一个故障注入；
4. [闭卷终测](quiz.md)；
5. 5 分钟费曼输出；
6. 归档并安排延迟复习。

读完课程只是步骤 2 完成。练习、实验和终测结束后，才算完成本单元的第一轮学习。