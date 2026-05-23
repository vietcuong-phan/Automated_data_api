import pandas as pd # type: ignore
from app.database.connection import engine

def generate_daily_sales_report():

    query = """
    SELECT *
    FROM sales
    """

    df = pd.read_sql(query, engine)

    df["revenue"] = df["quantity"] * df["price"]

    summary = (
        df.groupby("category")
          .agg(
              total_quantity=("quantity", "sum"),
              total_revenue=("revenue", "sum")
          )
          .reset_index()
    )

    summary.to_csv(
        "reports/daily_sales.csv",
        index=False
    )

    return summary

def generate_daily_sales_report():

    print("Pipeline is running...")