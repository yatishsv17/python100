"""
EPF Tax Calculator — Finance Act 2021 (CBDT Notification 95/2021)
=================================================================
Rule    : Interest on employee EPF contributions exceeding Rs 2,50,000 per
          financial year is taxable as 'Income from Other Sources' (Sec 194A).
Accounts: CBDT mandates two virtual accounts — non-taxable (≤ Rs 2.5L/FY) and
          taxable (excess above Rs 2.5L/FY). Interest on each account is
          credited/taxed separately.
Interest: EPFO calculates interest monthly on the closing balance of each month
          (annual rate ÷ 12) and credits the total at financial year-end.
Compound: Each year-end balance (principal + credited interest) becomes the
          opening balance for the next year, earning interest again — this is
          the compound effect for both accounts.

CSV format expected (append new rows for future years; script auto-detects AY):
    month, employee_monthly_contribution, epf_rate
    23-Apr, 7970, 8.25
    ...

Future-proof: append upcoming FY rows → script recalculates for the new AY.
"""

import csv
import sys
from collections import defaultdict
from typing import Dict, List, Tuple

# ── Constants ─────────────────────────────────────────────────────────────────
THRESHOLD = 250_000   # Rs 2,50,000 / FY — Finance Act 2021 limit
TAX_RATE  = 0.30      # 30% income-tax slab (employee's slab)
TDS_RATE  = 0.10      # TDS u/s 194A deducted by EPFO on taxable interest
TDS_LIMIT = 5_000     # TDS triggered only if annual taxable interest > Rs 5,000
CESS_RATE = 0.04      # 4% Health & Education Cess on income tax

MON = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4,  'May': 5,  'Jun': 6,
       'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}


# ── Helpers ───────────────────────────────────────────────────────────────────

def parse_month(s: str) -> Tuple[int, int]:
    """'23-Apr' → (2023, 4)"""
    yy, mon = s.strip().split('-')
    return 2000 + int(yy), MON[mon]


def fy_label(year: int, month: int) -> str:
    """(2023, 4) → '2023-24';  (2024, 1) → '2023-24'"""
    sy = year if month >= 4 else year - 1
    return f"{sy}-{str(sy + 1)[2:]}"


def fy_month_seq(month: int) -> int:
    """Position of month within FY: Apr→0, May→1, … Mar→11"""
    return (month - 4) % 12


def inr(v: float, w: int = 14) -> str:
    """Format as Indian Rupee with fixed width."""
    return f"Rs {v:>{w},.2f}"


# ── Data Loading ──────────────────────────────────────────────────────────────

def load(path: str) -> Dict[str, List[dict]]:
    """
    Read CSV and return {fy_label: [monthly_rows_sorted_Apr_to_Mar]}.
    Each row: {'seq': int, 'contrib': float, 'rate': float}
    """
    fy_data: Dict[str, List[dict]] = defaultdict(list)
    with open(path, newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            m = row.get('month', '').strip()
            if not m:
                continue
            yr, mo = parse_month(m)
            fy_data[fy_label(yr, mo)].append({
                'seq':    fy_month_seq(mo),
                'contrib': float(row['employee_monthly_contribution']),
                'rate':    float(row['epf_rate']) / 100,
            })
    for fy in fy_data:
        fy_data[fy].sort(key=lambda x: x['seq'])
    return dict(sorted(fy_data.items()))


# ── Core Calculation ──────────────────────────────────────────────────────────

def calculate(fy_data: Dict[str, List[dict]]) -> Tuple[List[dict], dict]:
    """
    Process all financial years and return (yearly_breakdown, summary).

    For each FY:
      1. Contributions are added month by month.
         — Cumulative ≤ Rs 2.5L  →  goes to non-taxable (NT) account
         — Cumulative > Rs 2.5L  →  excess goes to taxable (T) account
      2. Monthly interest = closing balance of that month × (annual_rate / 12).
         Accumulated across 12 months and credited at year-end.
      3. Year-end balance (with credited interest) becomes opening balance for
         the next FY → compound growth in both accounts.
      4. Interest on the taxable account is taxable every year (including
         interest on the prior years' taxable balance — this is the compound
         taxable interest that grows year over year).
    """
    nt_bal = 0.0   # Non-taxable account balance (carries forward each year)
    t_bal  = 0.0   # Taxable account balance (carries forward each year)
    yearly = []

    for fy, months in fy_data.items():
        fy_rate       = months[0]['rate']   # EPF rate for this FY
        monthly_rate  = fy_rate / 12

        cum_contrib   = 0.0   # Cumulative contribution within this FY
        nt_contrib_fy = 0.0   # NT contributions this FY
        t_contrib_fy  = 0.0   # Taxable contributions this FY

        nt_running = nt_bal   # Running NT balance (starts from prior year closing)
        t_running  = t_bal    # Running T  balance (starts from prior year closing)
        nt_int_fy  = 0.0      # NT interest accumulated this FY
        t_int_fy   = 0.0      # Taxable interest accumulated this FY

        for m in months:
            c = m['contrib']
            cum_contrib += c

            # Split this month's contribution into NT and T portions
            if cum_contrib <= THRESHOLD:
                nt_c, t_c = c, 0.0
            elif cum_contrib - c < THRESHOLD:
                # Threshold crossed mid-month
                nt_c = THRESHOLD - (cum_contrib - c)
                t_c  = c - nt_c
            else:
                nt_c, t_c = 0.0, c

            nt_contrib_fy += nt_c
            t_contrib_fy  += t_c

            # Deposit contribution, then compute interest on closing balance
            nt_running += nt_c
            t_running  += t_c
            nt_int_fy  += nt_running * monthly_rate
            t_int_fy   += t_running  * monthly_rate

        # Year-end: credit accumulated interest to balances
        nt_bal = nt_running + nt_int_fy
        t_bal  = t_running  + t_int_fy

        yearly.append({
            'fy':         fy,
            'rate_pct':   fy_rate * 100,
            'total_c':    nt_contrib_fy + t_contrib_fy,
            'nt_c':       nt_contrib_fy,
            't_c':        t_contrib_fy,
            'nt_int':     nt_int_fy,
            't_int':      t_int_fy,
            'nt_bal':     nt_bal,
            't_bal':      t_bal,
        })

    # Add cumulative running totals (shows compound growth over the years)
    cum_nt = cum_t = 0.0
    for e in yearly:
        cum_nt += e['nt_int']
        cum_t  += e['t_int']
        e['cum_nt_int'] = cum_nt
        e['cum_t_int']  = cum_t

    # Tax computation
    total_t_int = cum_t
    tds         = total_t_int * TDS_RATE if total_t_int > TDS_LIMIT else 0.0
    tax_30      = total_t_int * TAX_RATE
    cess        = tax_30 * CESS_RATE
    gross_tax   = tax_30 + cess
    net_tax     = max(0.0, gross_tax - tds)

    summary = {
        'total_c':    sum(e['total_c'] for e in yearly),
        'nt_c':       sum(e['nt_c']    for e in yearly),
        't_c':        sum(e['t_c']     for e in yearly),
        'nt_int':     cum_nt,
        't_int':      total_t_int,
        'nt_bal':     nt_bal,
        't_bal':      t_bal,
        'tds':        tds,
        'tax_30':     tax_30,
        'cess':       cess,
        'gross_tax':  gross_tax,
        'net_tax':    net_tax,
    }
    return yearly, summary


# ── Report Generation ─────────────────────────────────────────────────────────

def build_report(yearly: List[dict], S: dict, ay: str) -> str:
    W  = 118
    ln = []
    a  = ln.append

    def sec(title: str):
        a('')
        a(f"  {title}")
        a('  ' + '-' * W)

    a('=' * W)
    a(f"  EPF TAX REPORT  |  Assessment Year: {ay}  |  Finance Act 2021 / CBDT Notification 95/2021")
    a(f"  Threshold: Rs 2,50,000/FY  |  Slab: 30%  |  TDS @10% (Sec 194A)  |  Cess @4%  |  Interest: EPFO monthly method")
    a('=' * W)

    # ── Section 1: Contribution split ────────────────────────────────────────
    sec("SECTION 1 — YEAR-WISE CONTRIBUTION SPLIT")
    a(f"  {'FY':<10} {'EPF%':>6}  {'Total Contrib':>18}  {'Non-Taxable (≤ Rs 2.5L)':>26}  {'Taxable (> Rs 2.5L)':>22}")
    a('  ' + '-' * W)
    for e in yearly:
        a(f"  {e['fy']:<10} {e['rate_pct']:>5.2f}%  "
          f"{inr(e['total_c'])}  {inr(e['nt_c'], 22)}  {inr(e['t_c'])}")
    a('  ' + '-' * W)
    a(f"  {'TOTAL':<10} {'':>6}  "
      f"{inr(S['total_c'])}  {inr(S['nt_c'], 22)}  {inr(S['t_c'])}")

    # ── Section 2: Annual interest + running account balances ─────────────────
    sec("SECTION 2 — YEAR-WISE INTEREST & RUNNING ACCOUNT BALANCES")
    a(f"  (Interest on the taxable account's opening balance is ALSO taxable — this is the compound effect)")
    a(f"  {'FY':<10}  {'NT Interest':>18}  {'Taxable Interest':>18}  {'NT Account Balance':>20}  {'Taxable Account Balance':>22}")
    a('  ' + '-' * W)
    for e in yearly:
        a(f"  {e['fy']:<10}  "
          f"{inr(e['nt_int'])}  {inr(e['t_int'])}  "
          f"{inr(e['nt_bal'], 16)}  {inr(e['t_bal'], 18)}")
    a('  ' + '-' * W)
    a(f"  {'TOTAL':<10}  {inr(S['nt_int'])}  {inr(S['t_int'])}")

    # ── Section 3: Cumulative taxable interest (compound growth) ──────────────
    sec("SECTION 3 — CUMULATIVE TAXABLE INTEREST TILL ASSESSMENT YEAR (compound growth)")
    a(f"  (Each year's taxable balance compounds: prior year interest earns interest in subsequent years)")
    a(f"  {'FY':<10}  {'NT Int (This FY)':>18}  {'Tax Int (This FY)':>18}  {'Cum NT Interest':>18}  {'Cum Taxable Interest':>20}")
    a('  ' + '-' * W)
    for e in yearly:
        a(f"  {e['fy']:<10}  "
          f"{inr(e['nt_int'])}  {inr(e['t_int'])}  "
          f"{inr(e['cum_nt_int'])}  {inr(e['cum_t_int'], 16)}")
    a('  ' + '-' * W)
    a(f"  {'TOTAL':<10}  {inr(S['nt_int'])}  {inr(S['t_int'])}  "
      f"{inr(S['nt_int'])}  {inr(S['t_int'], 16)}")

    # ── Section 4: Final account balances ────────────────────────────────────
    sec("SECTION 4 — FINAL EPF ACCOUNT BALANCES (at end of last FY in data)")
    a(f"  Non-Taxable Account  — principal + tax-exempt interest:    {inr(S['nt_bal'], 16)}")
    a(f"  Taxable Account      — principal + taxable interest:        {inr(S['t_bal'], 16)}")
    a(f"  Compound Growth — Non-Taxable (= total NT interest):        {inr(S['nt_bal'] - S['nt_c'], 16)}")
    a(f"  Compound Growth — Taxable     (= total taxable interest):   {inr(S['t_bal']  - S['t_c'],  16)}")

    # ── Section 5: Tax computation ────────────────────────────────────────────
    sec(f"SECTION 5 — TAX COMPUTATION FOR AY {ay}")
    a(f"  Total Taxable EPF Interest  (add to 'Income from Other Sources' in ITR):  {inr(S['t_int'], 16)}")
    a(f"")
    a(f"  Income Tax @ 30%  :                                                         {inr(S['tax_30'], 16)}")
    a(f"  Health & Education Cess @ 4% on income tax :                                {inr(S['cess'], 16)}")
    a(f"  Gross Tax Liability  (income tax + cess) :                                  {inr(S['gross_tax'], 16)}")
    a(f"  Less: TDS already deducted by EPFO @ 10% (Form 26AS / AIS) :               {inr(S['tds'], 16)}")
    a('  ' + '-' * W)
    a(f"  *** NET TAX PAYABLE for AY {ay}  :                                          {inr(S['net_tax'], 16)} ***")
    a('=' * W)

    a('')
    a("  IMPORTANT NOTES:")
    a("  1. Finance Act 2021 rule applies from FY 2021-22. All EPF accumulations before")
    a("     01-Apr-2021 remain fully exempt under Sec 10(11) / 10(12) — add as initial")
    a("     balance in code if you have a pre-2021-22 EPF corpus.")
    a("  2. TDS @10% (Sec 194A) is deducted by EPFO when annual taxable interest > Rs 5,000.")
    a("     If PAN is not linked to your UAN, EPFO deducts TDS @20% instead.")
    a("  3. Report total taxable EPF interest under 'Income from Other Sources' in your ITR.")
    a("     Claim the TDS amount (Form 26AS / AIS) as an advance tax / TDS credit.")
    a("  4. Surcharge (10% / 15% / 25% / 37%) may apply on top, based on your total income.")
    a("  5. Employer contributions > Rs 7.5L / year are taxed separately as perquisite")
    a("     (Sec 17(2)(vii)) — this calculator covers only the employee's side.")
    a("  6. FUTURE YEARS: just append the new FY's monthly rows to contributions.csv.")
    a("     The script will auto-detect the new assessment year and recalculate everything.")
    a('')

    return '\n'.join(ln)


# ── Assessment Year Detection ─────────────────────────────────────────────────

def assessment_year(fy_data: Dict) -> str:
    """
    Derive assessment year from the latest FY in the data.
    Latest FY '2025-26' → ends in 2026 → AY '2026-27'.
    """
    last_fy  = max(fy_data.keys())       # e.g. '2025-26'
    end_year = int(last_fy.split('-')[0]) + 1   # 2025 + 1 = 2026
    return f"{end_year}-{str(end_year + 1)[2:]}"  # '2026-27'


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    csv_path    = 'contributions.csv'
    report_path = 'epf_tax_report.txt'

    try:
        fy_data = load(csv_path)
    except FileNotFoundError:
        sys.exit(f"Error: '{csv_path}' not found. Run from the same directory as the CSV.")

    if not fy_data:
        sys.exit("Error: No valid rows found in CSV.")

    ay             = assessment_year(fy_data)
    yearly, summary = calculate(fy_data)
    report         = build_report(yearly, summary, ay)

    print(report)

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"  Report saved to '{report_path}'")


if __name__ == '__main__':
    main()
