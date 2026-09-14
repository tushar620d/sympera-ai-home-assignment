
import json
from pathlib import Path
import pandas as pd


# =========================================================
# 1. PROJECT PATHS
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_PATH = PROJECT_ROOT / "data" / "transactions.json"
OUTPUT_PATH = PROJECT_ROOT / "output" / "customer_segments.json"


# =========================================================
# 2. LOAD DATA
# =========================================================

df = pd.read_json(DATA_PATH)

print(f"Loaded {len(df)} transactions.")


# =========================================================
# 3. DATA QUALITY VALIDATION
# =========================================================

df["date"] = pd.to_datetime(df["date"])

missing_values = df.isnull().sum()
duplicate_count = df.duplicated().sum()

invalid_credits = df[
    (df["type"] == "Credit") &
    (df["amount"] <= 0)
]

invalid_debits = df[
    (df["type"] == "Debit") &
    (df["amount"] >= 0)
]

print("\nData Quality Validation")
print("-----------------------")
print("Missing Values:")
print(missing_values)

print(f"\nDuplicate Rows: {duplicate_count}")
print(f"Invalid Credits: {len(invalid_credits)}")
print(f"Invalid Debits: {len(invalid_debits)}")

print(
    f"Date Range: "
    f"{df['date'].min().date()} to "
    f"{df['date'].max().date()}"
)


# =========================================================
# 4. TRANSACTION PROFILING
# =========================================================

print("\nTransaction Type Count:")
print(df["type"].value_counts())

print("\nTransaction Count by Category:")
print(df["category"].value_counts())

category_summary = (
    df.groupby("category")
      .agg(
          transaction_count=("amount", "count"),
          net_amount=("amount", "sum")
      )
      .sort_values("net_amount", ascending=False)
)

print("\nCategory Summary:")
print(category_summary)


# =========================================================
# 5. ECONOMIC CLASSIFICATION
# =========================================================

category_mapping = {
    "Revenue": "Revenue",
    "Interest": "Other Income",
    "Inventory": "Material Expense",
    "Operations": "Operating Expense",
    "Equipment": "Operating Expense",
    "Tech/Growth": "Growth Investment",
    "Growth": "Growth Investment",
    "Savings": "Internal Transfer"
}

df["economic_bucket"] = df["category"].map(category_mapping)

if df["economic_bucket"].isnull().any():
    unknown_categories = df.loc[
        df["economic_bucket"].isnull(),
        "category"
    ].unique()

    raise ValueError(
        f"Unmapped categories found: {unknown_categories}"
    )


# =========================================================
# 6. CORE FINANCIAL METRICS
# =========================================================

revenue = df.loc[
    df["economic_bucket"] == "Revenue",
    "amount"
].sum()

other_income = df.loc[
    df["economic_bucket"] == "Other Income",
    "amount"
].sum()

material_expense = abs(
    df.loc[
        df["economic_bucket"] == "Material Expense",
        "amount"
    ].sum()
)

operating_expense = abs(
    df.loc[
        df["economic_bucket"] == "Operating Expense",
        "amount"
    ].sum()
)

growth_investment = abs(
    df.loc[
        df["economic_bucket"] == "Growth Investment",
        "amount"
    ].sum()
)

internal_transfer = abs(
    df.loc[
        df["economic_bucket"] == "Internal Transfer",
        "amount"
    ].sum()
)

core_operating_surplus = (
    revenue
    - material_expense
    - operating_expense
)

total_credits = df.loc[
    df["type"] == "Credit",
    "amount"
].sum()

total_debits = abs(
    df.loc[
        df["type"] == "Debit",
        "amount"
    ].sum()
)

net_cash_movement = total_credits - total_debits

material_to_revenue_pct = (
    material_expense / revenue
) * 100

operating_to_revenue_pct = (
    operating_expense / revenue
) * 100

growth_to_revenue_pct = (
    growth_investment / revenue
) * 100

core_cash_retention_pct = (
    core_operating_surplus / revenue
) * 100


# =========================================================
# 7. RESILIENCE ALPHA
# =========================================================

resilience_alpha = {
    "signal_name": "Resilience Alpha",
    "positive_signal": bool(
        net_cash_movement > 0 and growth_investment > 0
    ),
    "observed_metrics": {
        "revenue": int(revenue),
        "material_expense": int(material_expense),
        "material_burden_pct": round(
            float(material_to_revenue_pct), 2
        ),
        "core_operating_cash_surplus": int(
            core_operating_surplus
        ),
        "core_cash_retention_pct": round(
            float(core_cash_retention_pct), 2
        ),
        "net_cash_movement": int(net_cash_movement),
        "growth_investment": int(growth_investment)
    }
}


# =========================================================
# 8. GROWTH REINVESTMENT
# =========================================================

business_outflows = (
    material_expense
    + operating_expense
    + growth_investment
)

growth_outflow_share_pct = (
    growth_investment / business_outflows
) * 100

growth_vs_operating_pct = (
    growth_investment /
    (growth_investment + operating_expense)
) * 100

growth_reinvestment = {
    "signal_name": "Growth Reinvestment",
    "positive_signal": bool(growth_investment > 0),
    "observed_metrics": {
        "growth_investment": int(growth_investment),
        "growth_to_revenue_pct": round(
            float(growth_to_revenue_pct), 2
        ),
        "growth_share_of_business_outflows_pct": round(
            float(growth_outflow_share_pct), 2
        ),
        "growth_share_vs_operating_spend_pct": round(
            float(growth_vs_operating_pct), 2
        ),
        "internal_savings_transfer": int(internal_transfer)
    }
}


# =========================================================
# 9. REVENUE BREADTH
# =========================================================

revenue_df = df[
    df["economic_bucket"] == "Revenue"
]

revenue_transaction_count = len(revenue_df)

average_revenue_transaction = (
    revenue_df["amount"].mean()
)

largest_revenue_transaction = (
    revenue_df["amount"].max()
)

largest_revenue_share_pct = (
    largest_revenue_transaction / revenue
) * 100


# =========================================================
# 10. LIQUIDITY ALLOCATION
# =========================================================

savings_to_revenue_pct = (
    internal_transfer / revenue
) * 100


# =========================================================
# 11. FINAL RAG-READY JSON
# =========================================================

customer_segments = {
    "customer": "Elite Builds LLC",

    "demographic": {
        "industry": "Residential Construction",
        "location": "Utah",
        "business_size": "Small firm"
    },

    "behavioral": {
        "revenue_inflow": int(revenue),
        "material_spend": int(material_expense),
        "growth_investment": int(growth_investment),
        "net_cash_movement": int(net_cash_movement),
        "revenue_transactions": int(
            revenue_transaction_count
        ),
        "savings_transfer": int(internal_transfer)
    },

    "psychographic": {
        "growth_orientation": "High",
        "technology_adoption":
            "Observed via AutoCAD spend",
        "customer_acquisition_focus":
            "Observed via Local SEO",
        "liquidity_discipline":
            "Suggested by savings transfer"
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

    "data_scope":
        "20 transactions, March 2026"
}


# =========================================================
# 12. SAVE JSON
# =========================================================

OUTPUT_PATH.parent.mkdir(
    parents=True,
    exist_ok=True
)

with open(
    OUTPUT_PATH,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        customer_segments,
        f,
        indent=2
    )


print("\nCore Financial Metrics")
print("----------------------")
print(f"Revenue: ${revenue:,.2f}")
print(f"Material Expense: ${material_expense:,.2f}")
print(f"Operating Expense: ${operating_expense:,.2f}")
print(f"Growth Investment: ${growth_investment:,.2f}")
print(f"Net Cash Movement: ${net_cash_movement:,.2f}")

print("\nAnalysis completed successfully.")
print(f"JSON saved to: {OUTPUT_PATH}")
