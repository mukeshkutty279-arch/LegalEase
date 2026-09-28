import streamlit as st
import requests

from utils.format_txt import format_txt
from utils.format_docx import format_docx
from utils.format_pdf import format_pdf
from utils.format_html import format_html_preview

BACKEND_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️",
    layout="centered"
)


st.title("⚖️ LegalEase")
st.subheader("AI-Powered Legal Document Generator")

st.write(
    "Generate professional legal documents using AI."
)


document_type = st.selectbox(
    "Document Type",
    [
        "Employment Contract",
        "Lease Agreement",
        "Non-Disclosure Agreement (NDA)",
        "Service Agreement",
        "Partnership Agreement"
    ]
)


parties = st.text_area(
    "Parties",
    placeholder="Example: Employer: ABC Technologies Pvt Ltd\nEmployee: Bala Murugan",
    height=120
)


terms = st.text_area(
    "Terms and Conditions",
    placeholder="Example: Salary: ₹25,000 per month\nWorking hours: 9 AM to 6 PM\nLeave: 12 days per year",
    height=180
)


dates = st.text_input(
    "Effective Date",
    placeholder="Example: 01-10-2026"
)


if st.button("Generate Document", use_container_width=True):

    if not parties.strip():
        st.warning("Please enter the parties.")

    elif not terms.strip():
        st.warning("Please enter the terms and conditions.")

    elif not dates.strip():
        st.warning("Please enter the effective date.")

    else:

        with st.spinner("Generating your legal document..."):

            try:

                response = requests.post(
                    f"{BACKEND_URL}/generate",
                    json={
                        "document_type": document_type,
                        "parties": parties,
                        "terms": terms,
                        "dates": dates
                    },
                    timeout=120
                )

                if response.status_code == 200:

                    result = response.json()

                    st.success("Document generated successfully!")

                    document_text = st.text_area(
                        "Generated Document",
                        value=result["document"],
                        height=500
                    )
                    st.subheader("Document Preview")

                    html_preview = format_html_preview(document_text)

                    st.components.v1.html(
                        html_preview,
                        height=600,
                        scrolling=True
                    )

                    if st.button("✏️ Click to Edit Document"):

                        edited_document = st.text_area(
                        "Edit Document",
                        value=document_text,
                        height=500
                    )
                    st.subheader("Download Document")

                    txt_file = format_txt(document_text)
                    docx_file = format_docx(document_text)
                    pdf_file = format_pdf(document_text)

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.download_button(
                            label="📄 Download TXT",
                            data=txt_file,
                            file_name="LegalEase_Document.txt",
                            mime="text/plain",
                            use_container_width=True
                        )

                    with col2:
                        st.download_button(
                            label="📝 Download DOCX",
                            data=docx_file,
                            file_name="LegalEase_Document.docx",
                            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                            use_container_width=True
                        )

                    with col3:
                        st.download_button(
                            label="📕 Download PDF",
                            data=pdf_file,
                            file_name="LegalEase_Document.pdf",
                            mime="application/pdf",
                            use_container_width=True
                        )

                else:

                    try:
                        error_message = response.json()["detail"]
                    except Exception:
                        error_message = "An unexpected backend error occurred."

                    st.error(
                        f"Backend Error: {error_message}"
                    )

            except requests.exceptions.ConnectionError:

                st.error(
                    "The LegalEase backend is not running."
                )

            except requests.exceptions.Timeout:

                st.error(
                    "The request took too long. Please try again."
                )

            except Exception as error:

                st.error(
                    f"Something went wrong: {error}"
                )
