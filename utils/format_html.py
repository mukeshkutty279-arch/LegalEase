import html


def format_html_preview(document_text: str) -> str:
    """
    Convert legal document text into a styled HTML preview.
    """

    safe_text = html.escape(document_text)

    formatted_text = safe_text.replace(
        "\n",
        "<br>"
    )

    html_content = f"""
    <div style="
        background-color: #1e1e1e;
        color: #f5f5f5;
        padding: 25px;
        border-radius: 10px;
        max-height: 600px;
        overflow-y: auto;
        font-family: Arial, sans-serif;
        line-height: 1.7;
        border: 1px solid #444;
    ">
        {formatted_text}
    </div>
    """

    return html_content
