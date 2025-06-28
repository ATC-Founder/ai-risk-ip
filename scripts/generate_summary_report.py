import pandas as pd
import markdown2
from pathlib import Path

def generate_report(df: pd.DataFrame, output_md="reports/summary.md", output_html="reports/summary.html", output_pdf="reports/summary.pdf"):
    total = len(df)
    counts = df['risk_level'].value_counts()
    dept_counts = df['department'].value_counts()

    lines = [
        "# 🛡️ Risk Summary Report\n",
        f"- Total Records: {total}\n",
    ]

    for level in ['High', 'Medium', 'Low']:
        if level in counts:
            lines.append(f"- {level} Risk Users: {counts[level]:,}\n")

    lines.append("\n## 🏢 Users by Department\n")
    for dept, count in dept_counts.items():
        lines.append(f"- {dept}: {count:,} users\n")

    # Write markdown
    Path(output_md).write_text("\n".join(lines))
    print(f"✅ Markdown written to {output_md}")

    # Convert to HTML
    html = markdown2.markdown(Path(output_md).read_text())
    Path(output_html).write_text(html)
    print(f"✅ HTML written to {output_html}")

    # Convert to PDF
    try:
        import weasyprint
        weasyprint.HTML(string=html).write_pdf(output_pdf)
        print(f"✅ PDF written to {output_pdf}")
    except Exception as e:
        print(f"⚠️ PDF conversion failed: {e}")

