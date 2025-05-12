import io
import pypdf
def extract_text_from_pdf(pdf_file):
    """Extract Text from a PDF file."""
    if isinstance(pdf_file, (str,bytes)):
        # If pdf_file is a file path or bytes
        pdf_reader=pypdf.PdfReader(pdf_file)
    else:
        #If pdf_file is a file-like object (ex: from st.file_uploader)
        pdf_bytes=io.BytesIO(pdf_file.getvalue())
        pdf_reader=pypdf.PdfReader(pdf_bytes)

    text=""

    for page_num in range(len(pdf_reader.pages)):
        page=pdf_reader.pages[page_num]
        text+=page.extract_text()+"\n\n"
    return text


