name: Run Full Market SEPA Screener

on:
  workflow_dispatch: # 讓你在手機上可以隨時手動點按鈕執行

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install yfinance pandas numpy requests lxml

      - name: Run screener script
        run: python sepa_screener.py

      - name: Commit and push results back to repo
        run: |
          git config --global user.name "github-actions[bot]"
          git config --global user.email "github-actions[bot]@users.noreply.github.com"
          git add sepa_full_market_results.csv
          git commit -m "Update daily SEPA scan results" || exit 0
          git push
