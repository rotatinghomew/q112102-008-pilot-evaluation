# 接送资格边界与过渡名额：资料契约

`regimes` 的 `at` 到下一条同地域生效记录之前适用，`cutoff` 含等号。`score_revisions` 的 `recorded_at` 是评分签发日期；资格分析用申请 `freeze_on` 前最后实际签发的 `initial` 或 `correction`，不能使用后来 `void` 所指向的不再适用证据做当前证据结论，同时可按所知时点复原原判断。`profile` 的 `prior_failed`、`mobility` 为事前特征，评分是整数。`results` 以 `took_ride`、`abandoned` 表示实际使用与成熟结局，空值为未观察，不当作零。比较使用每个片区当期的书面门槛。可由实测相邻取窗与支持范围区分是否具备迁移到拟改变人群的证据；估计方法由分析人员选用，不把一次观察结论外推到未覆盖分数段。
`analytic_policy` 的 `windows` 为门槛两侧分别以分值之差选取的观测窗（含端点），`min_distinct_per_side` 为每侧最少分数取值，`max_adjacent_ratio` 为门槛相邻分数人数之比（较大除以较小），`max_prior_gap` 为两侧既往弃约率允许差值；`min_uptake_jump` 是接送取得比例差值下限。`plan_policy` 用下降的弃约比例作为正获益，并限制一对有效服务确认窗内新增开支；`pilot_slots` 是维持旧线时每周可增加的最大补证名额。已有承诺和签认例外先占用可匹配车次。`trips` 中 `pool` 相同的车次是同一时段的替代用途，不可并用；`link` 相同的 `leg=first/second` 可构成两段接续，只有前段到达早于后段出发且整个行程落入可用窗口时才算一次；`single` 单段即为完整行程。`vehicle` 是最低乘坐类型，`无障碍` 车型兼容 `常规`，反之不行。报价按实际占用车次相加。所有时段当地时间，左闭右开。

## 输入表

- `regimes.csv`：`region`、`at`、`cutoff`、`rubric`
- `profile.csv`：`resident`、`region`、`applied_at`、`freeze_on`、`prior_failed`、`mobility`、`exception`
- `score_revisions.csv`：`revision`、`resident`、`score`、`state`、`recorded_at`
- `results.csv`：`resident`、`took_ride`、`abandoned`、`observed_at`
- `analytic_policy.csv`：`rubric`、`windows`、`min_distinct_per_side`、`max_adjacent_ratio`、`max_prior_gap`、`min_uptake_jump`、`maturity_days`
- `plan_policy.csv`：`week`、`budget`、`minimum_gain`、`pilot_slots`
- `planning_requests.csv`：`request`、`region`、`score`、`vehicle`、`start`、`end`
- `trips.csv`：`trip`、`region`、`vehicle`、`start`、`end`、`pool`、`link`、`leg`、`cost`
- `prior_promises.csv`：`id`、`request`、`trips`、`notified_at`
- `planning_changes.csv`：`id`、`kind`、`subject`、`at`
- `proposals.csv`：`id`、`region`、`candidate_cutoff`、`week`
