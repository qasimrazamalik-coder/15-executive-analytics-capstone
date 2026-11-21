
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from analysis import load_data, build_summary, portfolio_kpis

def test_data_contract():
    df = load_data(); assert len(df) == 1200; assert df.record_id.is_unique
    assert df.quality_score.between(0, 100).all()

def test_reconciliation():
    df = load_data(); s = build_summary(df); k = portfolio_kpis(df)
    assert abs(s.revenue.sum() - k["revenue"]) < 0.02
    assert 0 <= k["risk_rate"] <= 1 and 0 <= k["margin_pct"] <= 1
