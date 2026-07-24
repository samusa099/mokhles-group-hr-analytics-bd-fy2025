# Looker Studio Calculated Fields

## Turnover Rate

```text
SUM(exits) / AVG(average_headcount)
```

Format as Percent.

## Offer Acceptance Rate

```text
SUM(hires) / SUM(offers)
```

## Training Assessment Improvement

```text
AVG(post_assessment_score) - AVG(pre_assessment_score)
```

## Female Representation

```text
SUM(CASE WHEN gender = "Female" THEN 1 ELSE 0 END) / COUNT_DISTINCT(employee_id)
```

## Regrettable Exit Rate

```text
SUM(CASE WHEN regrettable_exit = "Yes" THEN 1 ELSE 0 END) / COUNT_DISTINCT(employee_id)
```
