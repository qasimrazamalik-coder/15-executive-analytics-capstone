
# Installation — Executive Analytics Capstone

## Requirements
Python 3.11+, Git, and 500 MB free disk space.

## Setup
```bash
git clone https://github.com/qasimrazamalik-coder/15-executive-analytics-capstone.git
cd 15-executive-analytics-capstone
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python src/analysis.py
pytest -q
streamlit run dashboard/app.py
```

The dashboard opens at `http://localhost:8501`. Processed outputs are written to `data/processed/`.
