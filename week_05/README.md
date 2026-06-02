# NHANES Depression Screener Dataset

## Dataset Selection Rationale

This project uses two publicly available files from the **National Health and Nutrition Examination Survey (NHANES)**, cycle August 2021 - August 2023, merged by participant ID (`SEQN`):

| File | Description | Download |
|------|-------------|----------|
| `DPQ_L.xpt` | Mental Health - Depression Screener (PHQ-9) | [CDC link](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DPQ_L.xpt) |
| `DEMO_L.xpt` | Demographic Variables and Sample Weights | [CDC link](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DEMO_L.xpt) |

Full codebook documentation:
- DPQ_L: https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DPQ_L.htm
- DEMO_L: https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DEMO_L.htm

---

## Assignment Constraints - Compliance Check

### Health/medical domain
Both files are part of NHANES, a national health and nutrition survey conducted by the CDC/NCHS. The depression screener (PHQ-9) is a validated clinical instrument used in medical practice and research to assess depressive symptoms according to DSM-IV diagnostic criteria.

### Ability to train a model (tabular data)
Both datasets are structured tabular data in SAS transport format (`.xpt`). After merging on `SEQN`, the combined dataset contains ordinal symptom scores (DPQ010-DPQ090), demographic variables, and a derived total PHQ-9 score (0-27) that can serve as a regression target or be binarised/categorised for classification. The dataset contains roughly 6,000+ rows, which can be considered sufficient for training and evaluating machine learning models.

### Fairness metrics make sense
The dataset contains several sensitive demographic attributes, including race/ethnicity, sex, age, income-to-poverty ratio, education, and country of birth. There is well-documented evidence in psychiatric literature that depression screening tools behave differently across racial, gender, and socioeconomic groups - making fairness evaluation not only possible but highly meaningful. The PHQ-9 itself has been studied for measurement invariance across sex, race/ethnicity, and education level in NHANES data.

### Publicly available with rights to use
NHANES is a U.S. federal government program. All data in the public-use files are freely available with no registration required. There are no copyright restrictions - data are released under a public domain / open government data policy by the CDC/NCHS.

---

## Dataset Documentation

### Who created the dataset?
The National Center for Health Statistics (NCHS), part of the Centers for Disease Control and Prevention (CDC), United States federal government.

### When was the dataset created?
Data collection: August 2021 - August 2023. First published: September 2024.

### Who funded the dataset creation?
The U.S. federal government through the CDC/NCHS as part of the ongoing national health monitoring program.

### Where is the data from?
NHANES samples the non-institutionalized civilian U.S. population residing in all 50 states and Washington D.C. Participants are selected from counties across the country (15 counties visited per year). Active-duty military personnel and U.S. citizens living abroad are excluded.

### How was the dataset collected?

**DPQ_L (Depression Screener):** Questions were administered at a Mobile Examination Center (MEC) using an Audio Computer-Assisted Personal Interview (ACASI) system, participants answered privately on a computer. This format was chosen because of the sensitive nature of the questions. Interviews were available in English and Spanish. Participants requiring a proxy informant or interpreter were excluded.

**DEMO_L (Demographics):** Family and sample person demographics questionnaires were administered by trained interviewers using a Computer-Assisted Personal Interview (CAPI) system, either in the participant's home or by telephone. Participants 16 years and older were interviewed directly; a proxy provided information for those under 16 or those unable to answer themselves.

### How is the data sampled?
NHANES uses a multi-year, stratified, clustered, four-stage probability sample of the U.S. civilian non-institutionalized population. For this cycle, 30 primary sampling units (counties) were selected. Within counties, area segments, dwelling units, and individuals were sampled sequentially.

An important design change in 2021-2023 relative to prior cycles: **no oversampling by race/ethnicity or income** was applied. In previous cycles, minority racial groups and low-income households were deliberately oversampled to ensure statistical precision for those subgroups. This change was made to reduce in-person contact during the COVID-19 pandemic. As a result, some demographic subgroups have noticeably fewer participants than in previous cycles.

### Does the sampling make sense?
Yes, stratified probability sampling is one of the best approaches for national health surveys. However, the absence of racial/ethnic oversampling in this cycle is a limitation specifically relevant to fairness analysis, as some minority subgroups will have smaller sample sizes and thus wider confidence intervals.

### What processing was done on the data?
- Frequency counts and skip patterns were verified; plausibility of responses was reviewed.
- Several variables were recoded to reduce disclosure/re-identification risk:
  - Age 80+ is coded as `80`
  - Marital status collapsed from 6 to 3 categories
  - Country of birth collapsed to 2 categories (USA / other)
  - Income-to-poverty ratio capped at `5.00`
  - Household size capped at `7 or more`
  - Pregnancy status released only for women aged 20-44

### Does the dataset make any assumptions?
The PHQ-9 assumes participants can reliably self-report symptom frequency over a two-week recall period. Participants requiring a proxy or interpreter were excluded, which introduces systematic bias against some language minorities and individuals with severe cognitive impairment. The instrument was developed and validated primarily in English-speaking clinical populations.

### Were there data points specifically left out?
Yes. The public-use DPQ_L file includes only participants aged 18 and older. Data for youth aged 12-17 are available only through the NCHS Research Data Center (RDC). Additionally, some demographic variables (full household reference person data for adults 20+, detailed income variables) are withheld from the public file for confidentiality reasons and require an RDC application to access.

### Are there any known errors or inconsistencies?
No known data errors are documented.

### Are there missing values?
Yes. Missing values appear in three forms:
- `.` - Missing (participant did not respond or was not eligible)
- `7` - Refused
- `9` - Don't know

### Is the meaning behind every attribute clear?
Yes. NCHS provides a full codebook with English-language question text, response codes, value labels, target age groups, and frequency distributions for every variable. All documentation is publicly accessible.

### Does the dataset contain metadata?
Yes. Each NHANES file is accompanied by a detailed documentation page including: component description, eligible sample, interview protocol, quality assurance procedures, analytic notes, references, and a complete codebook with frequencies.

---

## Attributes Reference

### DPQ_L - Depression Screener Variables

| Variable | Label | Scale |
|----------|-------|-------|
| `SEQN` | Respondent sequence number (merge key) | - |
| `DPQ010` | Little interest in doing things | 0-3 |
| `DPQ020` | Feeling down, depressed, or hopeless | 0-3 |
| `DPQ030` | Trouble sleeping or sleeping too much | 0-3 |
| `DPQ040` | Feeling tired or having little energy | 0-3 |
| `DPQ050` | Poor appetite or overeating | 0-3 |
| `DPQ060` | Feeling bad about yourself | 0-3 |
| `DPQ070` | Trouble concentrating on things | 0-3 |
| `DPQ080` | Moving or speaking slowly or too fast | 0-3 |
| `DPQ090` | Thought you would be better off dead | 0-3 |
| `DPQ100` | Difficulty these problems have caused | 0-3 |

Response coding for DPQ010-DPQ090: `0` = Not at all, `1` = Several days, `2` = More than half the days, `3` = Nearly every day. Total PHQ-9 score (sum of DPQ010-DPQ090) ranges from 0 to 27.

Standard PHQ-9 severity thresholds: 0-4 none, 5-9 mild, 10-14 moderate, 15-19 moderately severe, 20-27 severe depression.

### DEMO_L - Demographic Variables

| Variable | Label | Notes |
|----------|-------|-------|
| `SEQN` | Respondent sequence number (merge key) | - |
| `RIAGENDR` | Gender | 1 = Male, 2 = Female |
| `RIDAGEYR` | Age in years at screening | 80+ coded as 80 |
| `RIDRETH1` | Race/Hispanic origin | - |
| `RIDRETH3` | Race/Hispanic origin incl. NH Asian | 6 categories |
| `DMDEDUC2` | Education level (adults 20+) | 5 categories |
| `DMDMARTZ` | Marital status (adults 20+) | 3 categories |
| `DMDBORN4` | Country of birth | 1 = USA, 2 = Other |
| `DMDYRUSR` | Years living in the US | 6 categories (immigrants only) |
| `INDFMPIR` | Ratio of family income to poverty | 0.0-5.0+ |
| `DMDHHSIZ` | Total people in household | 1-7+ |
| `DMQMILIZ` | Active duty military service | Binary |
| `RIDEXPRG` | Pregnancy status at exam | Women 20-44 only |
| `WTMEC2YR` | 2-year MEC exam sample weight | Required for weighted analysis |
| `SDMVSTRA` | Masked variance pseudo-stratum | For SE estimation |
| `SDMVPSU` | Masked variance pseudo-PSU | For SE estimation |

Race/ethnicity categories in `RIDRETH3`: 1 = Mexican American, 2 = Other Hispanic, 3 = Non-Hispanic White, 4 = Non-Hispanic Black, 6 = Non-Hispanic Asian, 7 = Other/Multiracial.

---

## Protected Attributes

The following attributes are considered sensitive for fairness evaluation:

| Attribute | Variable | Justification |
|-----------|----------|---------------|
| Sex/Gender | `RIAGENDR` | Depression prevalence and PHQ-9 scores differ significantly by gender |
| Race/Ethnicity | `RIDRETH3` | Well-documented disparities in depression diagnosis and treatment access by race |
| Age | `RIDAGEYR` | Symptom presentation and screening validity vary across age groups |
| Income | `INDFMPIR` | Lower income is strongly associated with higher depression risk and lower care access |
| Education | `DMDEDUC2` | Education level influences both symptom reporting and healthcare engagement |
| Country of birth | `DMDBORN4` | Immigrant status correlates with access barriers and cultural expression of symptoms |

---

## Features: Proportions and Distributions

**Sample size:** DPQ_L contains approximately 6,337 records (adults 18+); after merging with DEMO_L on `SEQN`, the effective analysis sample will be slightly smaller due to participants who completed the interview but not the MEC exam.

**Class imbalance:** Depression symptoms follow a strongly right-skewed distribution. For `DPQ010` (Little interest in doing things) approximately 67% of respondents scored 0 ("Not at all"), while only ~5% scored 3 ("Nearly every day"). 

**Demographic distribution note:** Due to the removal of racial/ethnic oversampling in this cycle, minority subgroups (particularly Hispanic and Asian populations) are less represented than in prior NHANES cycles, which reduces statistical power for fairness comparisons within those groups.

**Income distribution:** `INDFMPIR` values capped at 5.00 (top-coded) and missing for respondents who did not provide income details. Income-to-poverty ratios below 1.0 indicate household income below the federal poverty line.

---

## Research Questions

1. **Prediction:** Can depressive symptom severity (PHQ-9 score) be predicted from sociodemographic and lifestyle factors available in NHANES?

2. **Fairness across groups:** Does model performance (accuracy, sensitivity, specificity) differ significantly across racial/ethnic groups, sexes, or income levels? Which groups are systematically misclassified?

3. **Healthcare disparities:** Do demographic groups that score high on the PHQ-9 also systematically receive less treatment? Can the model identify under-served populations?

4. **Income and depression risk:** How does the income-to-poverty ratio (`INDFMPIR`) interact with PHQ-9 scores, and how does this relationship vary by race/ethnicity?

5. **Immigrant mental health:** Do foreign-born participants (`DMDBORN4 = 2`) show different symptom patterns than U.S.-born participants, and is the PHQ-9 equally effective as a screener for this group?

6. **Somatic vs. cognitive symptoms:** Do certain demographic groups endorse somatic PHQ-9 items (sleep, fatigue, appetite) more than cognitive/affective items (hopelessness, self-worth), and does this affect model predictions?

---

## References

- Kroenke K, Spitzer RL, Williams JB. The PHQ-9: Validity of a brief depression severity measure. *J Gen Intern Med* 2001; 16:606-13.
- Terry AL et al. Plan and operations of the National Health and Nutrition Examination Survey, August 2021-August 2023. *Vital Health Stat* 1(66). 2024. https://stacks.cdc.gov/view/cdc/151927
- Patel JS et al. Measurement invariance of the PHQ-9 across sex, race/ethnicity, and education level: NHANES 2005-2016. *Depression and Anxiety* 2019; 36(9):813-823.
- NHANES Analytic Guidelines: https://wwwn.cdc.gov/nchs/nhanes/analyticguidelines.aspx
- NHANES Tutorial: https://wwwn.cdc.gov/nchs/nhanes/tutorials/