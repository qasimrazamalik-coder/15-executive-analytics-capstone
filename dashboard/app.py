
from pathlib import Path
import sys
import plotly.express as px
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from analysis import load_data, build_summary, portfolio_kpis, DIMENSION

st.set_page_config(page_title="Executive Analytics Capstone", layout="wide")
st.title("Executive Analytics Capstone")
st.caption("Executive decision dashboard · synthetic portfolio data")
df = load_data(); options = sorted(df[DIMENSION].unique())
selected = st.sidebar.multiselect(DIMENSION.replace("_", " ").title(), options, default=options)
view = df[df[DIMENSION].isin(selected)]; k = portfolio_kpis(view)
cols = st.columns(4)
cols[0].metric("Revenue", f"${k['revenue']:,.0f}")
cols[1].metric("Margin", f"{k['margin_pct']:.1%}")
cols[2].metric("Quality", f"{k['avg_quality']:.1f}")
cols[3].metric("Risk rate", f"{k['risk_rate']:.1%}")
summary = build_summary(view)
left, right = st.columns(2)
left.plotly_chart(px.bar(summary, x=DIMENSION, y="revenue", color="margin_pct", title="Revenue and margin by segment"), use_container_width=True)
right.plotly_chart(px.scatter(summary, x="quality_score", y="risk_rate", size="revenue", color=DIMENSION, title="Quality-risk diagnostic"), use_container_width=True)
monthly = view.assign(month=view.date.dt.to_period("M").astype(str)).groupby("month", as_index=False).revenue.sum()
st.plotly_chart(px.line(monthly, x="month", y="revenue", markers=True, title="Monthly performance"), use_container_width=True)
st.dataframe(summary.style.format({"revenue":"${:,.0f}", "margin_pct":"{:.1%}", "risk_rate":"{:.1%}"}), use_container_width=True)
