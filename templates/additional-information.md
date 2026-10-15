# I-129 free-text fields

Each block is within the online form's 500-character limit after substitution; check the counter on
the page.

## Duties (Employment information)

```
{{duties_500}}
```

## Present occupation (Beneficiary information)

```
{{present_occupation_500}}
```

## Controlling interest explanation (H-1B data collection)

```
The beneficiary owns {{company_role.ownership_pct}}% of the petitioner's issued stock, is its {{company_role.director_title_lower}} and serves as its {{petitioner.signer.title}}. This petition is filed under 8 CFR 214.2(h)(9)(iii)(E). The beneficiary will spend the majority of working time ({{petition.specialty_hours_pct}}%) on specialty occupation duties and the remainder on duties directly related to owning and directing the business. The requested validity period is within the 18-month limit.
```

## Additional Information (numbered entries, each tagged with its page/part)

```
1. Part 5, H-1B Data Collection, "Rate of pay per year": the position is part-time at {{lca.hours_per_week}} hours per week at {{lca.wage_rate_fmt}} per hour under certified LCA {{lca.number}}. The annual figure entered ({{petition.annualized_pay_fmt}}) is that hourly wage annualized ({{lca.wage_rate_fmt}} x {{lca.hours_per_week}} x 52).
```

```
2. Part 2, Numerical limitation: the beneficiary was previously counted against the H-1B cap ({{prior_receipts_inline}}). This petition is exempt from the cap under INA 214(g)(7).
```

```
3. Part 3, Beneficiary's current status: the beneficiary's current H-1B period under receipt {{beneficiary.latest_receipt}} is valid to {{beneficiary.status_valid_until_long}} (I-94 expiry). The petition requests a change of employer with an extension of stay to {{petition.end_long}}.
```

```
4. Part 2, Requested period: the requested start date {{petition.start_long}} is later than the LCA validity start ({{lca.valid_from_long}}) to allow for receipt of this petition; employment under 8 CFR 214.2(h)(2)(i)(H) begins no earlier than the start date stated in the offer letter.
```
