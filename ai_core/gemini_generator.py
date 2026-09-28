import os
from dotenv import load_dotenv
from google import genai


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in the .env file")


client = genai.Client(api_key=API_KEY)


def generate_document(
    document_type: str,
    parties: str,
    terms: str,
    dates: str
) -> str:

    prompt = f"""
You are LegalEase, an AI-powered legal document generator.

Generate a professional and clearly structured legal document based on the
following user-provided information.

Document Type:
{document_type}

Parties:
{parties}

Terms and Conditions:
{terms}

Effective Dates:
{dates}

Requirements:
- Create the complete document.
- Use clear professional legal language.
- Include an appropriate title.
- Include sections and clauses relevant to the document type.
- Clearly identify the parties.
- Include the provided terms and dates.
- Do not invent personal information that was not provided.
- Do not invent specific laws, sections, case numbers, or legal citations.
- If important information is missing, use a clear placeholder such as
  [Information Required].
- Add a general legal-information disclaimer at the end.
- Return only the document content.
"""

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    return response.text
