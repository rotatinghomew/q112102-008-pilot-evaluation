# 数据说明

社区服务试点资格、服务暴露、观察结果和决策记录。

下列文件仅包含合成记录。空值按 CSV 空单元格保存；时间字段使用当地业务记录时间，不预设统计结论。

## `eligibility.csv`

字段：`person_ref`、`rule_version`、`eligible_from`、`eligible_to`、`basis`。当前演练样本 4 条。

## `exposure.csv`

字段：`event_id`、`person_ref`、`service_code`、`occurred_at`、`grid_ref`、`source`。当前演练样本 4 条。

## `outcomes.csv`

字段：`outcome_id`、`person_ref`、`measure`、`observed_at`、`value`、`maturity`。当前演练样本 4 条。

## `decisions.csv`

字段：`decision_id`、`analysis_version`、`decided_at`、`action`、`reason`。当前演练样本 2 条。
