# 学习笔记：坐标表达与变换

## 1. 几何对象与坐标不是一回事

空间中的点 $\mathbf p$ 是几何对象。它在坐标系 $A$ 下的数值表达记为 ${}^{A}\mathbf p$。换坐标系不会移动真实的点，只会改变描述它的数字。

本仓库使用列向量，车辆坐标系为右—前—上；右向轴记为 $x$，前向轴记为 $y$，上向轴记为 $z$。

## 2. 变换符号

${}^{A}\mathbf T_B$ 的下标 $B$ 是输入表达所在坐标系，上标 $A$ 是输出表达所在坐标系：

$$
{}^{A}\mathbf p = {}^{A}\mathbf T_B{}^{B}\mathbf p
$$

读作“坐标系 $B$ 在坐标系 $A$ 中的位姿”，也可读作“从坐标系 $B$ 映射到坐标系 $A$ 的变换”。遇到歧义时不要依赖自然语言，只检查等式两侧的坐标系标记。

## 3. 刚体变换

三维刚体变换由旋转 $\mathbf R$ 和平移 $\mathbf t$ 组成：

$$
{}^{A}\mathbf p = {}^{A}\mathbf R_B{}^{B}\mathbf p + {}^{A}\mathbf t_B
$$

其中 ${}^{A}\mathbf t_B$ 是坐标系 $B$ 原点在坐标系 $A$ 中的坐标。齐次形式把旋转和平移合并：

$$
{}^{A}\mathbf T_B =
\begin{bmatrix}
{}^{A}\mathbf R_B & {}^{A}\mathbf t_B\\
\mathbf 0^{\mathsf T} & 1
\end{bmatrix}
$$

点要扩展为 $[x,y,z,1]^{\mathsf T}$；纯方向向量扩展为 $[x,y,z,0]^{\mathsf T}$，因此不受平移影响。

## 4. 变换链

中间坐标系必须相邻消去：

$$
{}^{\mathrm{map}}\mathbf T_{\mathrm{base}}
= {}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}{}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}
$$

矩阵从右向左作用。一个实用检查方法是把坐标系名称写成点坐标的映射路径：
$\mathtt{base}\to\mathtt{odom}\to\mathtt{map}$。

## 5. 求逆

若已知 ${}^{A}\mathbf T_B$，反向映射是：

$$
{}^{B}\mathbf T_A = \left({}^{A}\mathbf T_B\right)^{-1}
$$

旋转矩阵的逆等于转置，但齐次变换的平移不能只改符号；它还要旋转到目标坐标系中。

## 6. 定位系统中的三层坐标系

- `base`：车体坐标系，传感器外参通常连接到这里。
- `odom`：局部连续坐标系。里程计输出 ${}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}$，短期平滑但长期漂移。
- `map`：全局一致坐标系。SLAM、GNSS 或重定位修正 ${}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}$。

于是：

$$
{}^{\mathrm{map}}\mathbf T_{\mathrm{base}}
= {}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}{}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}
$$

回环或全局测量到达时，保持局部变换
${}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}$ 连续，把全局修正放到
${}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}$，可以避免控制使用的局部位姿突然跳变。

## 7. 时间是变换的一部分

动态坐标系的变换随时间变化。对产生于 $t_L$ 的激光点，应查询或插值 $t_L$ 时刻的 TF，而不是处理该消息的当前时间。否则即使矩阵链的方向正确，也会产生运动畸变或融合偏差。

## 8. 三种快速自检

1. **单位变换**： ${}^{A}\mathbf T_A$ 必须是单位矩阵。
2. **闭环检查**： ${}^{A}\mathbf T_B{}^{B}\mathbf T_A$ 必须接近单位矩阵。
3. **简单点检查**：先用原点和坐标轴单位向量测试，再处理真实点云。
