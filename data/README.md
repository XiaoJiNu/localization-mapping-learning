# 数据目录

仓库只提交体积小、许可清晰的合成示例。真实数据集通过下载脚本或外部链接获取，不纳入 Git 历史。

## 当前示例

`sample_transform_chain.csv` 是人为构造的坐标变换序列，用于验证：

- 点坐标沿
  $\mathtt{lidar}\to\mathtt{base}\to\mathtt{odom}\to\mathtt{map}$
  的映射与变换复合；
- 动态变换按时间戳配对；
- 静态外参与动态位姿的区别；
- 修改 ${}^{\mathrm{map}}\mathbf T_{\mathrm{odom}}$ 时，如何保持
  ${}^{\mathrm{odom}}\mathbf T_{\mathrm{base}}$ 连续。

每行的 `target_frame` 和 `source_frame` 表示
${}^{\mathrm{target}}\mathbf T_{\mathrm{source}}$。平移列 `x_m`、`y_m`、`z_m`
表达在目标坐标系中；`yaw_rad` 表示绕目标坐标系 $+z$ 轴的旋转，坐标轴为
右—前—上。数据是纯合成值，不对应任何车辆、地点或真实项目。

## 数据管理规则

- 禁止提交公司数据、内部地图、真实车辆日志、标定参数和个人信息。
- 大型公开数据放在本地 `data/raw/`，预处理结果放在 `data/processed/`，两者应由 `.gitignore` 排除。
- 每个实验记录数据来源、许可、校验值、处理脚本和坐标约定。
- 可复现实验优先提供小型合成数据与生成方法。
