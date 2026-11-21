# 分波邀请与干扰下的试点评估：资料契约

网格为随机分配单位，`block` 为原始区组，`registrants` 为分配前登记人群；年龄等个人资料不进入业务。`wave_plan` 的 `max_global` 是自然波次总容量，`quotas` 指各区组应发邀请数。已经冻结的邀请不能改。可随机化的许可集合由当时可选网格、各区组配额、全域容量、既有邀请及观测支持下限共同界定；每个在许可集合中的完整分配等可能，以公开的 `seed` 和冻结名册复现抽签。对历史波次使用该行冻结日与事实计算，而非后来资料。`relations` 无向；任一端接受提前邀请影响另一端的潜在邻接分组。实际暴露另由 `contacts` 记录。
`study` 的 `min_direct_units`、`min_unexposed_units` 对每个区组有效：前者要求至少这么多早邀请网格及同量尚未邀请网格，后者只计算既未邀请且在观察窗内无登记邻接/共用网格被邀请的网格。波次角色相对已冻结的早邀请批次，保护直到该批主要结果成熟。主要结局 `stable` 是二元结果，风险差为获益尺度；失访与无记录不等于阴性。`signal` 为扩大考虑的最小获益（百分点）；按许可集重随机化并对未确定结局表明推断界限。完成全部观测以 `days` 为成熟窗，以各波邀请日期为早邀请及其对照的观察起点。

## 输入表

- `grids.csv`：`grid`、`block`、`ready_on`
- `relations.csv`：`left`、`right`、`kind`、`registered_on`
- `wave_plan.csv`：`wave`、`invite_on`、`freeze_on`、`max_global`、`seed`
- `quotas.csv`：`wave`、`block`、`quota`
- `assignments.csv`：`wave`、`grid`、`status`、`notified_on`
- `study.csv`：`primary`、`days`、`min_direct_units`、`min_unexposed_units`、`signal`
- `contacts.csv`：`person`、`grid`、`kind`、`at`
- `registrants.csv`：`person`、`grid`、`eligible`、`registered_on`
- `outcomes.csv`：`person`、`status`、`stable`、`observed_on`、`available_on`
