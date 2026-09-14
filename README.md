# Sympera AI Home Assignment

## Objective

This project analyzes the recent banking activity of **Elite Builds LLC**, a Utah-based construction firm, and combines transaction-level banking signals with the supplied construction-industry context.

The objective is to identify positive growth signals that can help a **Bank Relationship Manager (RM)** identify relevant commercial opportunities.

---

## Data

The analysis uses the **20 banking transactions** supplied in the assignment, covering **March 2026**.

The transaction dataset contains the following fields:

- `date`
- `description`
- `category`
- `amount`
- `type`

### Market Context

The supplied Q1 2026 market context states that:

- Residential construction costs have increased by **15%** due to supply-chain volatility.
- Average net margins for mid-sized construction firms have declined to **4%**.
- Banks are tightening credit for firms showing high **Expense Velocity**.

---

# Analytical Approach

The analysis follows these steps:

1. Load and inspect the supplied banking transactions.
2. Validate data quality.
3. Check missing values and duplicate transactions.
4. Validate Credit/Debit amount signs.
5. Review transaction categories.
6. Reclassify transactions into economically meaningful buckets.
7. Calculate key cash-flow and spending metrics.
8. Engineer positive customer signals.
9. Create a compact RAG-ready customer segmentation JSON.
10. Identify a relevant banking-product opportunity for the Relationship Manager.
11. Create an RM-ready customer engagement hook.

---

# Data Validation

The supplied transaction dataset was checked for:

- Missing values
- Duplicate records
- Debit/Credit sign inconsistencies
- Date coverage
- Transaction-category consistency

### Validation Result

- Total Transactions: **20**
- Credit Transactions: **5**
- Debit Transactions: **15**
- Missing Values: **0**
- Exact Duplicate Transactions: **0**
- Date Range: **1 March 2026 to 31 March 2026**
- Credit/Debit sign inconsistencies: **None identified**

---

# Transaction Profiling

The transaction categories supplied in the data are:

| Category | Transaction Count |
|---|---:|
| Operations | 6 |
| Revenue | 4 |
| Inventory | 4 |
| Tech/Growth | 2 |
| Equipment | 1 |
| Interest | 1 |
| Savings | 1 |
| Growth | 1 |

---

# Economic Classification

For analytical purposes, transactions were grouped into the following economic buckets:

| Original Category | Economic Bucket |
|---|---|
| Revenue | Revenue |
| Interest | Other Income |
| Inventory | Material Expense |
| Operations | Operating Expense |
| Equipment | Operating Expense |
| Tech/Growth | Growth Investment |
| Growth | Growth Investment |
| Savings | Internal Transfer |

The **Internal Transfer to Savings** is not treated as a business expense because it represents movement of funds rather than economic consumption.

---

# Key Financial Metrics

| Metric | Value |
|---|---:|
| Observed Revenue | $112,000 |
| Other Income | $120 |
| Material Expense | $30,800 |
| Operating Expense | $20,950 |
| Growth Investment | $10,650 |
| Internal Savings Transfer | $5,000 |
| Core Operating Cash Surplus | $60,250 |
| Net Observed Cash Movement | +$44,720 |
| Material Expense / Revenue | 27.50% |
| Operating Expense / Revenue | 18.71% |
| Growth Investment / Revenue | 9.51% |

### Important Interpretation

The **Core Operating Cash Surplus** is a transaction-based analytical measure calculated from the supplied banking activity.

It should **not** be interpreted as:

- Accounting profit
- Net income
- EBITDA
- Net margin

The assignment does not provide a complete income statement or full financial history.

---

# Positive Signal Engineering

## 1. Resilience Alpha

Elite Builds generated strong project inflows while operating in a construction industry facing significant raw-material cost pressure.

Within the observed March 2026 transaction period:

- Revenue: **$112,000**
- Material Expense: **$30,800**
- Material Expense / Revenue: **27.50%**
- Core Operating Cash Surplus: **$60,250**
- Net Observed Cash Movement: **+$44,720**
- Growth Investment: **$10,650**

This suggests that the business continued generating positive observed cash movement while absorbing material and operating expenses and continuing to invest in growth.

### Interpretation

**Positive Signal:** Elite Builds demonstrates observed cash-flow resilience despite operating in a market environment characterized by higher construction input costs.

### Limitation

The supplied dataset does not contain historical company-level raw-material costs.

Therefore, this analysis does **not** claim that Elite Builds itself experienced or directly outperformed a 15% cost increase.

The **15% figure is an industry-level market benchmark supplied in the assignment.**

---

## 2. Growth Reinvestment

Elite Builds allocated **$10,650** toward identifiable growth-related activity.

Observed growth-related transactions include:

- AutoCAD software subscription
- Local SEO marketing
- New equipment down payment

### Growth Metrics

- Growth Investment: **$10,650**
- Growth Investment / Revenue: **9.51%**
- Growth Share of Identified Business Outflows: **17.07%**
- Growth Share vs. Operating + Growth Spend: **33.70%**

### Interpretation

A portion of the company's observed spending appears directed toward:

- Technology adoption
- Customer acquisition
- Capacity expansion

rather than only routine operating expenditure.

This represents a **Growth Reinvestment** signal.

---

## 3. Revenue Breadth

The supplied transaction history contains **four project-related revenue transactions** totaling **$112,000**.

### Revenue Metrics

- Revenue Transactions: **4**
- Average Revenue Transaction: **$28,000**
- Largest Revenue Transaction: **$45,000**
- Largest Transaction Share of Revenue: **40.18%**

### Interpretation

Observed revenue activity is supported by multiple project-related payments rather than a single transaction.

### Limitation

The underlying customer identities are not provided.

Therefore, this analysis does not claim proven customer diversification.

---

## 4. Liquidity Allocation

Elite Builds transferred **$5,000** to savings while the observed transaction period still showed positive net cash movement of **$44,720**.

### Metrics

- Savings Transfer: **$5,000**
- Savings Transfer / Revenue: **4.46%**
- Net Observed Cash Movement: **+$44,720**

### Interpretation

The savings transfer may indicate deliberate liquidity allocation rather than operating expenditure.

### Limitation

The dataset does not contain:

- Savings-account balances
- Current-account balances
- Credit-line availability
- Debt obligations
- Total liquidity position

Therefore, this should not be interpreted as proof of strong overall liquidity.

---

# RAG-Ready Customer Segmentation

The final RAG-ready output is stored in:

`output/customer_segments.json`

The structure includes:

- Demographic segmentation
- Behavioral segmentation
- Psychographic segmentation
- Positive signals
- Market context
- Data scope

Example structure:

```json
{
  "customer": "Elite Builds LLC",
  "demographic": {
    "industry": "Residential Construction",
    "location": "Utah",
    "business_size": "Small firm"
  },
  "behavioral": {
    "revenue_inflow": 112000,
    "material_spend": 30800,
    "growth_investment": 10650,
    "net_cash_movement": 44720,
    "revenue_transactions": 4,
    "savings_transfer": 5000
  },
  "psychographic": {
    "growth_orientation": "High",
    "technology_adoption": "Observed via AutoCAD spend",
    "customer_acquisition_focus": "Observed via Local SEO",
    "liquidity_discipline": "Suggested by savings transfer"
  },
  "positive_signals": [
    "Resilience Alpha",
    "Growth Reinvestment",
    "Revenue Breadth",
    "Liquidity Allocation"
  ],
  "market_context": {
    "material_cost_inflation_pct": 15,
    "industry_net_margin_pct": 4
  },
  "data_scope": "20 transactions, March 2026"
}
```

The final JSON is designed to remain within the assignment's **300-token requirement**.

---

# Banking Product Recommendation

## Equipment Financing / Equipment Term Loan

A potential banking opportunity identified from the supplied transaction activity is:

**Equipment Financing / Equipment Term Loan**

### Supporting Evidence

Elite Builds has:

- A **$10,000 new-equipment down payment**
- An existing **$2,200 excavator lease payment**
- **$10,650** of identified growth-related investment
- Positive observed net cash movement of **$44,720**

These transactions suggest potential capacity expansion.

### Customer Benefit

Equipment financing could allow the company to finance future equipment purchases while preserving more working liquidity for:

- Inventory purchases
- Payroll
- Day-to-day operations
- Project execution

during a period of elevated construction input costs.

### Important Limitation

This recommendation represents a **Relationship Manager opportunity signal**.

It is **not** a:

- Credit approval
- Underwriting decision
- Creditworthiness assessment

because information such as credit history, existing debt, collateral, balances, and repayment capacity was not provided.

---

# RM Hook

> "Elite Builds appears to be maintaining strong project inflows while continuing to invest in technology and new equipment despite higher construction input costs. An equipment financing facility could help preserve working liquidity while supporting further capacity expansion."

---

# Exact System Prompt

The following System Prompt was designed to generate the customer segmentation summary for the RAG use case.

```text
You are a Banking Growth Intelligence Analyst supporting a
Relationship Manager (RM).

Your task is to convert customer banking activity and supplied
market context into a concise, evidence-based customer segmentation
summary for use in a RAG system.

Instructions:

1. Focus on positive, commercially relevant signals without ignoring
   material risks or limitations.

2. Identify signals from the transaction data that indicate:
   - financial resilience,
   - growth reinvestment,
   - revenue behaviour,
   - liquidity behaviour.

3. Compare observed customer behaviour with the supplied market
   context where the data supports the comparison.

4. Create three customer segments:
   - demographic,
   - behavioral,
   - psychographic.

5. Demographic information must use only facts explicitly provided.

6. Psychographic attributes may be inferred from transaction behaviour,
   but clearly distinguish inference from observed fact.

7. Never invent customer facts, historical trends, financial ratios,
   creditworthiness, balances, or business characteristics that are not
   supported by the supplied data.

8. Do not treat internal transfers as operating expenses.

9. Do not describe transaction-based cash surplus as accounting profit
   or net margin.

10. Use a professional, concise, commercially useful tone appropriate
    for a bank Relationship Manager.

11. Return valid JSON only.

12. Keep the complete JSON response below 300 tokens.

Required JSON structure:

{
  "customer": "",
  "demographic": {},
  "behavioral": {},
  "psychographic": {},
  "positive_signals": [],
  "market_context": {},
  "data_scope": ""
}
```

---

# Assumptions and Limitations

The following assumptions were applied:

1. The analysis uses only the **20 transactions supplied in the assignment**.
2. The observed transaction period is **March 2026**.
3. The supplied transactions are not assumed to represent the customer's complete banking history.
4. Internal transfers are not treated as operating expenses.
5. Transaction-based cash surplus is not treated as accounting profit.
6. Historical expense data is unavailable.
7. Therefore, **Expense Velocity cannot be calculated as a true time-series trend**.
8. Psychographic attributes are inferred only where observable banking behavior provides supporting evidence.
9. Customer creditworthiness is not inferred.
10. Product recommendations represent commercial opportunity signals rather than lending approval decisions.
11. The industry 15% raw-material cost increase and 4% average net margin are treated as supplied external market context.

---

# Repository Structure

```text
Sympera_construction_company_p1/
│
├── data/
│   └── transactions.json
│
├── scripts/
│   └── signal_extraction.py
│
├── output/
│   └── customer_segments.json
│
└── README.md
```

---

# Running the Analysis

## Requirements

Python 3.x

Pandas

Install Pandas if required:

```bash
pip install pandas
```

Run the analysis script:

```bash
python scripts/signal_extraction.py
```

The script performs:

- Data loading
- Data-quality validation
- Transaction profiling
- Economic classification
- Financial metric calculation
- Positive-signal engineering
- RAG-ready customer segmentation generation

---

# Final Deliverables

The repository contains:

### `/scripts`

Python logic used for:

- Transaction validation
- Metric calculation
- Positive-signal engineering
- JSON generation

### `/output/customer_segments.json`

Compact RAG-ready customer segmentation output.

### `README.md`

Documents:

- Analytical approach
- Assumptions
- Positive signals
- Product recommendation
- RM Hook
- Exact System Prompt
- Project execution instructions
