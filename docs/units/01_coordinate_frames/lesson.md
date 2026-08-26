# 单元 01：坐标变换图解课

> **一句话目标：** 看完以后，你应该能把坐标变换理解成“换一把尺子重新读数”，而不是把真实世界中的点搬来搬去。

## 先打开图解版

推荐先用浏览器打开：

- [lesson_eli5.html：大图、少字、可交互的坐标变换图解](lesson_eli5.html)

GitHub 文件页面不会直接运行 HTML。请下载该文件后，用 Chrome、Edge 或 Firefox 打开。

本页是同一内容的 Markdown 备份，也是进入推导和实验前的最小公式卡。第一次学习不需要同时逐字阅读两个版本：**优先看 HTML；需要复制公式或快速复习时再看本页。**

---

## 先记住总答案

坐标变换只做两件事：

1. **用旋转矩阵统一坐标轴方向；**
2. **用平移向量补上两个原点之间的差。**

所以：

$$
{}^{A}\mathbf p =
{}^{A}\mathbf R_B{}^{B}\mathbf p
+
{}^{A}\mathbf t_B
$$

它不是在说点先真的旋转、再真的平移。

它在说：

> 同一个点原本用坐标系 $B$ 表达；现在改用坐标系 $A$ 表达。

---

## 图 1：坐标只是“尺子的读数”

想象桌上有一个没有移动的点 $P$，旁边放了两把尺子：

- 尺子 $A$ 从原点 $O_A$ 开始量；
- 尺子 $B$ 从另一个原点 $O_B$ 开始量。

同一个点，可能得到两组不同数字：

$$
{}^{A}\mathbf p
\neq
{}^{B}\mathbf p
$$

变化的是读数，不是点。

### 只记住

> **物理点是对象；坐标是对象在某个坐标系下的数字说明。**


### 位置、姿态和位姿

- **位置：** 原点在哪里；
- **姿态：** 坐标轴朝哪里；
- **位姿：** 位置和姿态放在一起。

坐标系 $B$ 相对于坐标系 $A$ 的位姿，也就是把点坐标从 $B$ 表达到 $A$ 的变换。


---

## 图 2：点和方向向量不一样

### 点

点要回答：

> 我离坐标系原点多远？

所以换原点时，点会受到平移影响：

$$
{}^{A}\mathbf p =
{}^{A}\mathbf R_B{}^{B}\mathbf p
+
{}^{A}\mathbf t_B
$$

### 方向向量

方向向量只回答：

> 朝哪里？走多长？

方向向量可以由两个点相减得到：

$$
\mathbf v =
\mathbf p_2-\mathbf p_1
$$

两个端点一起平移后：

$$
(\mathbf p_2+\mathbf t) -
(\mathbf p_1+\mathbf t) =
\mathbf p_2-\mathbf p_1
$$

平移抵消，所以：

$$
{}^{A}\mathbf v =
{}^{A}\mathbf R_B{}^{B}\mathbf v
$$

### 只记住

- 点会吃到平移；
- 方向向量不会吃到平移。

---

## 图 3：为什么一定是 $R\mathbf p+\mathbf t$

三个点分别是：

- $O_A$：坐标系 $A$ 的原点；
- $O_B$：坐标系 $B$ 的原点；
- $P$：空间中的点。

纯几何关系只有一句：

$$
\overrightarrow{O_AP} =
\overrightarrow{O_AO_B}
+
\overrightarrow{O_BP}
$$

也就是：

```text
从 O_A 到 P
=
先从 O_A 到 O_B
+
再从 O_B 到 P
```

其中：

$$
{}^{A}\mathbf t_B =
[\overrightarrow{O_AO_B}]_A
$$

而输入坐标：

$$
{}^{B}\mathbf p =
[\overrightarrow{O_BP}]_B
$$

第二段向量现在用 $B$ 表达，无法直接和用 $A$ 表达的平移向量相加。

先把它改用 $A$ 表达：

$$
[\overrightarrow{O_BP}]_A =
{}^{A}\mathbf R_B{}^{B}\mathbf p
$$

于是：

$$
{}^{A}\mathbf p =
{}^{A}\mathbf R_B{}^{B}\mathbf p
+
{}^{A}\mathbf t_B
$$

### 只记住

> 旋转矩阵负责统一方向，平移向量负责补原点差。


### 一个 90° 的最小例子

已知：

$$
{}^{A}\mathbf R_B =
\begin{bmatrix}
0 & -1\\
1 & 0
\end{bmatrix},
\qquad
{}^{A}\mathbf t_B =
\begin{bmatrix}
3\\
1
\end{bmatrix},
\qquad
{}^{B}\mathbf p =
\begin{bmatrix}
2\\
1
\end{bmatrix}
$$

先统一方向：

$$
{}^{A}\mathbf R_B{}^{B}\mathbf p =
\begin{bmatrix}
-1\\
2
\end{bmatrix}
$$

它表示从 $O_B$ 到 $P$，在 $A$ 看来是“向左 1、向上 2”。

再补原点差：

$$
{}^{A}\mathbf p =
\begin{bmatrix}
-1\\
2
\end{bmatrix}
+
\begin{bmatrix}
3\\
1
\end{bmatrix} =
\begin{bmatrix}
2\\
3
\end{bmatrix}
$$


---

## 图 4：旋转矩阵其实是几根坐标轴

二维旋转矩阵为：

$$
{}^{A}\mathbf R_B =
\begin{bmatrix}
\cos\theta & -\sin\theta\\
\sin\theta & \cos\theta
\end{bmatrix}
$$

不要先把它看成四个数。

把它看成两列箭头：

$$
{}^{A}\mathbf R_B =
\begin{bmatrix}
\vert & \vert\\
{}^{A}\mathbf e_{x_B}
&
{}^{A}\mathbf e_{y_B}\\
\vert & \vert
\end{bmatrix}
$$

- 第一列：坐标系 B 的 x 轴在坐标系 A 中朝哪里；
- 第二列：坐标系 B 的 y 轴在坐标系 A 中朝哪里。

如果：

$$
{}^{B}\mathbf p =
\begin{bmatrix}
x_B\\
y_B
\end{bmatrix}
$$

那么矩阵乘法是在做：

$$
{}^{A}\mathbf R_B{}^{B}\mathbf p =
x_B{}^{A}\mathbf e_{x_B}
+
y_B{}^{A}\mathbf e_{y_B}
$$

### 合法旋转矩阵的三个检查

$$
\mathbf R^{\mathsf T}\mathbf R =
\mathbf I
$$

$$
\det(\mathbf R) =
1
$$

$$
\mathbf R^{-1} =
\mathbf R^{\mathsf T}
$$

旋转不会改变向量长度、夹角、两点距离和刚体形状。


### 本仓库 RFU 与 ROS 常见 FLU

本仓库采用“右—前—上”：

| 约定 | $x$ 轴 | $y$ 轴 | $z$ 轴 |
|---|---|---|---|
| 本仓库 RFU | 右 | 前 | 上 |
| ROS 常见 FLU | 前 | 左 | 上 |

两者都是右手系，但同一个三元组不表示同一个物理方向。

例如，本仓库中的“向右 1 米”为：

$$
\begin{bmatrix}
1\\
0\\
0
\end{bmatrix}_{\mathrm{RFU}}
$$

在 FLU 中应写成：

$$
\begin{bmatrix}
0\\
-1\\
0
\end{bmatrix}_{\mathrm{FLU}}
$$

接入 ROS、公开数据集或其他代码前，必须逐轴核对，不能只改坐标系名称。


---

## 图 5：齐次坐标的最后一位是“平移开关”

齐次变换把旋转和平移放入一个矩阵：

$$
{}^{A}\mathbf T_B =
\begin{bmatrix}
{}^{A}\mathbf R_B
&
{}^{A}\mathbf t_B\\
\mathbf 0^{\mathsf T}
&
1
\end{bmatrix}
$$

### 点：最后一位为 1

$$
{}^{B}\bar{\mathbf p} =
\begin{bmatrix}
{}^{B}\mathbf p\\
1
\end{bmatrix}
$$

所以平移列会乘上 1：

$$
{}^{A}\mathbf T_B{}^{B}\bar{\mathbf p} =
\begin{bmatrix}
{}^{A}\mathbf R_B{}^{B}\mathbf p
+
{}^{A}\mathbf t_B\\
1
\end{bmatrix}
$$

### 方向向量：最后一位为 0

$$
{}^{B}\bar{\mathbf v} =
\begin{bmatrix}
{}^{B}\mathbf v\\
0
\end{bmatrix}
$$

所以平移列会乘上 0：

$$
{}^{A}\mathbf T_B{}^{B}\bar{\mathbf v} =
\begin{bmatrix}
{}^{A}\mathbf R_B{}^{B}\mathbf v\\
0
\end{bmatrix}
$$

### 只记住

> 末位 1：平移打开。末位 0：平移关闭。

---

## 图 6：多个变换像接力传球

假设点先从 $C$ 变到 $B$：

$$
{}^{B}\mathbf p =
{}^{B}\mathbf T_C{}^{C}\mathbf p
$$

再从 $B$ 变到 $A$：

$$
{}^{A}\mathbf p =
{}^{A}\mathbf T_B{}^{B}\mathbf p
$$

代入得到：

$$
{}^{A}\mathbf p =
{}^{A}\mathbf T_B
{}^{B}\mathbf T_C
{}^{C}\mathbf p
$$

所以：

$$
{}^{A}\mathbf T_C =
{}^{A}\mathbf T_B{}^{B}\mathbf T_C
$$

采用列向量和左乘时，最靠近点的矩阵最先作用。

```text
C 中的点
  ↓
B 中的点
  ↓
A 中的点
```

“中间坐标系可以消去”是检查方法。真正原因是：

> 前一段的输出坐标系，必须等于后一段的输入坐标系。

---

## 图 7：逆变换不是简单地把平移变负

正向变换：

$$
{}^{A}\mathbf p =
{}^{A}\mathbf R_B{}^{B}\mathbf p
+
{}^{A}\mathbf t_B
$$

反向求解：

$$
{}^{B}\mathbf p =
\left({}^{A}\mathbf R_B\right)^{\mathsf T}
\left(
{}^{A}\mathbf p -
{}^{A}\mathbf t_B
\right)
$$

所以：

$$
{}^{B}\mathbf T_A =
\left({}^{A}\mathbf T_B\right)^{-1} =
\begin{bmatrix}
\left({}^{A}\mathbf R_B\right)^{\mathsf T}
& -
\left({}^{A}\mathbf R_B\right)^{\mathsf T}
{}^{A}\mathbf t_B\\
\mathbf 0^{\mathsf T}
&
1
\end{bmatrix}
$$

为什么不是简单的 $-\mathbf t$？

因为反向走以后，平移向量还要改用反向目标坐标系表达。

### 自检

$$
{}^{A}\mathbf T_B{}^{B}\mathbf T_A
\approx
\mathbf I
$$

也可以让一个点正向变换，再逆向变换，检查是否回到原坐标。

---

## 图 8：两个全局位姿怎样得到相对位姿

世界坐标系记为 $W$。

已知：

$$
{}^{W}\mathbf T_A
$$

和：

$$
{}^{W}\mathbf T_B
$$

要求 $B$ 相对于 $A$ 的位姿。

画路径：

```text
B → W → A
```

先从 $B$ 到 $W$，再用 $A$ 的全局位姿的逆从 $W$ 到 $A$：

$$
{}^{A}\mathbf T_B =
\left({}^{W}\mathbf T_A\right)^{-1}
{}^{W}\mathbf T_B
$$

不要背“谁减谁”。先画源到目标的坐标路径。

---

## 图 9：定位系统中的四层坐标系

| 坐标系 | 像什么 | 主要任务 |
|---|---|---|
| `sensor` | 眼睛和耳朵 | 原始观测从这里产生 |
| `base` | 车身 | 描述机器人自身 |
| `odom` | 平滑记事本 | 短期连续，但长期会漂 |
| `map` | 城市地图 | 全局一致，可以被回环或重定位修正 |

激光点到地图的完整链：

$$
{}^{\mathrm{map}}\mathbf p =
{}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}
{}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}
{}^{\mathrm{base}}\mathbf T_{\mathrm{lidar}}
{}^{\mathrm{lidar}}\mathbf p
$$

从右向左执行：

```text
lidar → base → odom → map
```

车体全局位姿：

$$
{}^{\mathrm{map}}\mathbf T_{\mathrm{base}} =
{}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}
{}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}
$$

回环、GNSS 或重定位到来时，通常保持：

$$
{}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}
$$

连续，把全局修正放进：

$$
{}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}
$$

这样局部控制不会因为全局修正突然跳变。

### TF 树为什么箭头看起来相反

TF 树通常按父帧到子帧画：

```text
map → odom → base → lidar
```

点坐标计算却从点所在的源帧走向目标帧：

```text
lidar → base → odom → map
```

前者画拓扑，后者画坐标计算路径。不要只看箭头猜方向，要写完整等式。

---

## 图 10：时间也是变换的一部分

动态位姿应该写成：

$$
{}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}(t)
$$

假设激光帧在 12.0 秒产生，在 12.1 秒才被程序处理。

应使用：

> 12.0 秒，也就是测量产生时刻的动态变换。

不能直接使用处理时刻的最新变换。

即使矩阵方向和顺序完全正确，时间错位仍会产生与线速度、角速度和时间差相关的偏移。

最简单的平移误差直觉：

$$
\Delta x
\approx
v\Delta t
$$

例如：

$$
v=10~\mathrm{m/s},
\qquad
\Delta t=0.1~\mathrm{s}
$$

则仅平移误差就可能达到：

$$
\Delta x
\approx
1~\mathrm m
$$

---


## 图 11：同一个矩阵，可能讲两个不同故事

### 被动变换：点不动，换坐标系描述

$$
{}^{A}\mathbf p =
{}^{A}\mathbf T_B{}^{B}\mathbf p
$$

输入和输出是同一个物理点，只是坐标表达不同。

### 主动变换：坐标系不动，物体真的运动

$$
\mathbf p' =
\mathbf T\mathbf p
$$

输入和输出对应两个不同的物理位置。

只看矩阵数值无法区分两种语义。必须检查：

- 输入和输出属于哪个坐标系；
- 点是否真的运动；
- 矩阵表示坐标系位姿，还是物体运动增量。

> 本单元主要讨论被动变换：物理点不动，换坐标系重新读数。

---

## 最后：固定调试顺序

矩阵能相乘，只说明维度允许，不说明坐标语义正确。

出现点云偏移、方向翻转或两条路径不一致时，按这个顺序检查：

1. 写清每个坐标系的原点、轴向、手性和单位；
2. 给每个点、向量和变换标出表达坐标系；
3. 写出完整点变换等式，确认源和目标；
4. 检查相邻坐标系是否正确衔接；
5. 用源坐标系原点测试平移；
6. 用各单位轴测试旋转方向；
7. 检查 $\mathbf R^{\mathsf T}\mathbf R\approx\mathbf I$ 和 $\det(\mathbf R)\approx1$；
8. 检查 $\mathbf T\mathbf T^{-1}\approx\mathbf I$；
9. 比较逐段变换与一次复合变换；
10. 核对单位、角度制和时间戳；
11. 最后才换成真实点云或复杂数据。

### 最终口令

遇到任何坐标变换，先问三句话：

> **源坐标系是谁？目标坐标系是谁？这是哪个时刻？**

---

## 学完以后做什么

本页只完成“建立直觉”。

接下来按顺序完成：

1. 返回[工作簿](workbook.md)，独立完成关键推导；
2. 完成[实验 001](../../../experiments/exp_001_transform_chain/README.md)；
3. 修改一个参数并提前预测变化；
4. 注入一个错序或错方向故障；
5. 最后再打开[闭卷终测](quiz.md)；
6. 完成 5 分钟费曼讲解和延迟复习安排。

不要提前打开终测答案。
