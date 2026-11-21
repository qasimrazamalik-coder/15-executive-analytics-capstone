
from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DIMENSION = "business_unit"

def load_data(path=ROOT / "data/raw/observations.csv"):
    df = pd.read_csv(path, parse_dates=["date"])
    required = {"record_id", "date", DIMENSION, "volume", "revenue", "cost", "quality_score", "risk_flag"}
    missing = required - set(df.columns)
    if missing: raise ValueError(f"Missing columns: {sorted(missing)}")
    if df["record_id"].duplicated().any(): raise ValueError("record_id must be unique")
    if (df[["volume", "revenue", "cost"]] < 0).any().any(): raise ValueError("negative commercial values")
    if not df["quality_score"].between(0, 100).all(): raise ValueError("quality_score outside 0-100")
    return df

def build_summary(df):
    df = df.copy()
    df["margin"] = df["revenue"] - df["cost"]
    df["month"] = df["date"].dt.to_period("M").astype(str)
    grouped = df.groupby(DIMENSION, as_index=False).agg(
        records=("record_id", "count"), volume=("volume", "sum"), revenue=("revenue", "sum"),
        cost=("cost", "sum"), quality_score=("quality_score", "mean"), risk_rate=("risk_flag", "mean"))
    grouped["margin"] = grouped["revenue"] - grouped["cost"]
    grouped["margin_pct"] = grouped["margin"] / grouped["revenue"]
    return grouped.sort_values("revenue", ascending=False)

def portfolio_kpis(df):
    margin = df["revenue"].sum() - df["cost"].sum()
    return {"records": int(len(df)), "revenue": round(df.revenue.sum(), 2),
            "margin_pct": round(margin / df.revenue.sum(), 4),
            "avg_quality": round(df.quality_score.mean(), 2), "risk_rate": round(df.risk_flag.mean(), 4)}

if __name__ == "__main__":
    df = load_data(); summary = build_summary(df); kpis = portfolio_kpis(df)
    out = ROOT / "data/processed"; out.mkdir(parents=True, exist_ok=True)
    summary.to_csv(out / "segment_summary.csv", index=False)
    (out / "portfolio_kpis.json").write_text(json.dumps(kpis, indent=2))
    print(json.dumps(kpis, indent=2))
