from io import BytesIO
import textwrap

from fpdf import FPDF


def format_pdf(document_text: str) -> bytes:
    """
    Convert generated legal document text into a PDF file.
    """

    safe_text = document_text.replace("₹", "Rs.")
    safe_text = safe_text.replace("—", "-")
    safe_text = safe_text.replace("–", "-")
    safe_text = safe_text.replace("“", '"')
    safe_text = safe_text.replace("”", '"')
    safe_text = safe_text.replace("’", "'")

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    pdf.set_font("Arial", size=11)

    page_width = pdf.w - pdf.l_margin - pdf.r_margin

    for raw_line in safe_text.splitlines():

        line = raw_line.strip()

        if not line:
            pdf.ln(6)
            continue

        wrapped_lines = textwrap.wrap(
            line,
            width=80,
            break_long_words=True,
            break_on_hyphens=False
        )

        for wrapped_line in wrapped_lines:
            pdf.multi_cell(
                page_width,
                7,
                wrapped_line
            )

    output = BytesIO()
    pdf.output(output)

    return output.getvalue()
