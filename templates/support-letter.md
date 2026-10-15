<!-- Print on company letterhead. Signed by the company officer named in case.json petitioner.signer. Delete this comment. -->

**{{petitioner.legal_name}}**
{{petitioner.address_line}}

{{today_long}}

U.S. Citizenship and Immigration Services
California Service Center

**RE: Form I-129, Petition for a Nonimmigrant Worker (H-1B)**

| | |
|---|---|
| **Petitioner** | {{petitioner.legal_name}} |
| **Beneficiary** | {{beneficiary.full_name}} |
| **Position** | {{lca.job_title}}, {{schedule_phrase}} |
| **SOC / O*NET code** | {{lca.soc_code}}, {{lca.soc_title}}, Level {{lca.wage_level}} |
| **Wage** | {{lca.wage_rate_fmt}} per hour |
| **Certified LCA** | {{lca.number}} |
| **Period requested** | {{petition.start_long}} to {{petition.end_long}} |
| **Basis for classification** | {{basis_phrase}} |
| **Numerical limitation** | Not subject to the cap; the Beneficiary was previously counted (INA § 214(g)(7)) |

Dear Sir or Madam:

{{petitioner.legal_name}} ("the Company") respectfully submits this petition to employ {{beneficiary.full_name}} ("the Beneficiary") in the specialty occupation of {{lca.job_title}} on a {{schedule_phrase}} basis. The Beneficiary is in the United States in H-1B status and was previously counted against the H-1B numerical limitation. The Company requests a {{basis_phrase_lower}}. Under 8 C.F.R. § 214.2(h)(2)(i)(H), the Beneficiary may begin employment with the Company upon the filing of this petition.

Part I describes the Company. Part II establishes that the position is a specialty occupation. Part III establishes that the Beneficiary is qualified. Part IV addresses the Beneficiary's ownership interest and the requested validity period. Part V addresses the Company's ability to pay the offered wage.

# I. The Petitioner

{{petitioner.legal_name}} is a {{petitioner.state_of_incorporation}} {{petitioner.entity_type_lower}} incorporated on {{petitioner.date_incorporated_long}}, registered to transact business in {{lca.worksite.state_name}}, and operating from {{lca.worksite_line}}. Its Federal Employer Identification Number is {{petitioner.ein}}. The Company has a legal presence in the United States and is amenable to service of process here. (Exhibits A through D.)

The Company is {{petitioner.one_line_description}}. It is developing {{petitioner.product_description}}.

[DRAFT: one paragraph on the market and the plan — a cited market-size figure, when first revenue is planned, when the company plans to raise, and that the Business Plan at Exhibit E describes product, market, operations and projections.]

# II. The Position Is a Specialty Occupation

## A. The regulatory standard

Section 214(i)(1) of the Immigration and Nationality Act defines a specialty occupation as one that requires the theoretical and practical application of a body of highly specialized knowledge and the attainment of a bachelor's or higher degree in the specific specialty, or its equivalent, as a minimum for entry. Under 8 C.F.R. § 214.2(h)(4)(iii)(A), as amended effective January 17, 2025, a position qualifies if it meets at least one of four criteria: (1) a bachelor's or higher degree in a directly related specific specialty is normally the minimum requirement for entry into the position; (2) the degree requirement is common to the industry in parallel positions among similar organizations, or the position is so complex or unique that it can be performed only by an individual with such a degree; (3) the employer normally requires such a degree for the position; or (4) the specific duties are so specialized and complex that the knowledge required to perform them is usually associated with such a degree. A position may accept a range of qualifying degree fields, provided each is directly related to the duties. 89 Fed. Reg. 103054 (Dec. 18, 2024).

The position meets criteria 1, 2 and 4. The Company does not rely on criterion 3, because this is the first time it has filled the position.

## B. The position and its duties

The complete job description is submitted at Exhibit F. The duties and weekly time allocation are:

{{duties_table}}

Duties 1 through {{position.duty_count}} are the specialty occupation duties and occupy {{petition.specialty_hours_pct}}% of the schedule. Duty {{position.owner_duty_n}} consists of activities directly related to owning and directing the business and is addressed in Part IV.

## C. The duties require a degree in a specific specialty

Duties 1 through {{position.duty_count}} require theoretical and practical knowledge in the following areas, each acquired through a baccalaureate course of study in computer science or a directly related field:

{{knowledge_table}}

{{why_degree_paragraphs}}

## D. The degree requirement is normal for the occupation and common to the industry

{{position.ooh_sentence}} (Exhibit G.) A description in the Handbook of a bachelor's degree as the usual, though not universal, requirement satisfies the first criterion, which asks whether such a degree is "normally" the minimum requirement for entry.

[DRAFT: if job postings (Exhibit H) or an expert opinion letter (Exhibit I) are submitted, one sentence each; otherwise delete this paragraph and the exhibits.]

## E. The qualifying degree fields are directly related to the duties

The position requires {{petition.degree_requirement}}. Each accepted field is a course of study in the knowledge areas listed in Part II.C and is therefore directly related to the duties. A degree in a field that does not cover those areas, such as business administration or the liberal arts, does not qualify.

## F. The Level {{lca.wage_level}} wage is consistent with a specialty occupation

The certified Labor Condition Application states Wage Level {{lca.wage_level}}. That designation follows from the minimum requirements of the position: a bachelor's or higher degree in a specific specialty, {{experience_phrase}}, no supervisory responsibility, and no professional certification. A Level I wage denotes an entry-level position within an occupation; it does not indicate that the occupation lacks a degree requirement.

# III. The Beneficiary Is Qualified

Under 8 C.F.R. § 214.2(h)(4)(iii)(C)(1), a beneficiary is qualified to perform services in a specialty occupation if {{beneficiary.pronoun_subject}} holds a United States baccalaureate or higher degree required by the specialty occupation from an accredited college or university.

The Beneficiary holds a **{{education.highest_degree}} in {{education.highest_field}} from {{education.highest_school}}**, an accredited U.S. institution, conferred in {{education.highest_year}}. (Exhibit J.) {{education.highest_field}} is a specialty the position requires, and the degree meets or exceeds the minimum the position requires. The Beneficiary therefore qualifies on the basis of {{beneficiary.pronoun_possessive}} degree alone.

In addition, and beyond the minimum requirements of the position, the Beneficiary worked {{beneficiary.experience_summary}}. (Exhibit K; see also the accompanying prior H-1B approval notices and pay records at Exhibit O.) This experience is stated to show that {{beneficiary.pronoun_subject}} will perform the duties competently; it is not a requirement of the position.

# IV. Ownership Interest and Validity Period

The Company discloses that the Beneficiary owns {{company_role.ownership_pct}}% of its issued and outstanding stock, is its {{company_role.director_title_lower}}, and serves as its {{petitioner.signer.title}}. (Exhibits B and C.) This petition is therefore filed under 8 C.F.R. § 214.2(h)(9)(iii)(E), which permits an H-1B petition on behalf of a beneficiary who holds a controlling interest in the petitioner and limits the validity of the initial petition to eighteen months. Consistent with that limit, the Company requests a validity period of **{{petition.start_long}} through {{petition.end_long}}**.

**The job offer is bona fide.** The Company has adopted a written job description (Exhibit F), obtained a certified Labor Condition Application (Exhibit L), and issued a written offer of employment (Exhibit M). The Beneficiary will be paid {{petition.pay_frequency}} by direct deposit, with wages reported on Form W-2. The position exists because the Company's product requires the work described in Part II.B.

**Specialty occupation duties occupy the majority of the Beneficiary's time.** Of the {{lca.hours_per_week}} weekly hours, {{petition.specialty_hours}} hours ({{petition.specialty_hours_pct}}%) are devoted to the specialty occupation duties in Part II.B. The remaining {{petition.owner_hours}} hours ({{petition.owner_hours_pct}}%) are devoted to customer discovery and sales, investor outreach, and administration, which are duties directly related to owning and directing the business. The regulation permits a beneficiary-owner to perform such duties provided that the beneficiary performs specialty occupation duties a majority of the time. 89 Fed. Reg. 103054. All {{lca.hours_per_week}} hours are paid at the required wage.

# V. Ability to Pay the Offered Wage

The certified Labor Condition Application requires a wage of {{lca.wage_rate_fmt}} per hour, the prevailing wage for SOC {{lca.soc_code}}, Level {{lca.wage_level}}, in the {{lca.worksite.msa}} area. At {{lca.hours_per_week}} hours per week, the annual wage is **{{petition.annualized_pay_fmt}}**, and the wage over the {{petition.months_words}}-month period is **{{petition.period_wage_fmt}}**. Including employer payroll taxes and workers' compensation insurance, the cost of the position over that period is approximately **{{petition.period_cost_fmt}}**.

The Beneficiary contributed {{funding.founder_contribution_fmt}} in cash to the Company in {{funding.contribution_month}}. From that capital the Company paid the fees for this petition, and as of {{funding.balance_date_long}} it holds {{funding.bank_balance_fmt}} in its operating account, with no debt and no other payroll obligations. (Exhibit N.) This capital funds payroll and operating costs from the start of employment. Customer revenue is planned from {{funding.revenue_start}}, and a {{funding.raise_amount_fmt}} financing round is targeted for {{funding.raise_month}}; together they fund the remainder of the period and the Company's first additional hires. The Business Plan (Exhibit E) sets out the {{petition.months_words}}-month funding plan, the multi-year projections, and the Company's response if revenue or financing arrives later than planned.

In every scenario, the Company will pay the required wage for all scheduled hours before any discretionary spending, as required by 20 C.F.R. § 655.731.

# VI. Conclusion

The position is a specialty occupation under INA § 214(i)(1) and 8 C.F.R. § 214.2(h)(4)(iii)(A). The Beneficiary holds a U.S. degree in a specialty the position requires. The Company has obtained a certified Labor Condition Application, has disclosed the Beneficiary's controlling interest, has requested a validity period within the eighteen-month limit of 8 C.F.R. § 214.2(h)(9)(iii)(E), and will pay the offered wage. The Company respectfully requests that the petition be approved for the period {{petition.start_long}} through {{petition.end_long}}{{extension_clause}}.

Should any question arise, the undersigned may be reached at {{petitioner.phone}} or {{petitioner.email}}.

Respectfully submitted,

\
\
_________________________________
{{petitioner.signer.name}}
Founder, {{petitioner.signer.title}}
{{petitioner.legal_name}}

# Index of Exhibits

{{exhibit_index_table}}
