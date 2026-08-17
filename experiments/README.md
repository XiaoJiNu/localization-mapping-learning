# 实验目录

这里存放可以独立复现的小实验。每个实验应包含问题、坐标约定、运行方法、
预期结果和调试记录，避免只留下无法解释的代码片段。

当前实验：

- [`exp_001_transform_chain`](exp_001_transform_chain/)：验证
  `base → odom → map` 逐步变换与直接复合变换一致。

从仓库根目录运行：

```bash
python experiments/exp_001_transform_chain/run.py
```
