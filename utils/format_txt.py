def format_txt(document: str) -> bytes:
    """
    Convert generated document text into a downloadable TXT file.
    """
    return document.encode("utf-8")
