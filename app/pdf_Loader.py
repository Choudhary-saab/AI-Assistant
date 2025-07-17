import fitz  # PyMuPDF
import io

def extract_text_from_pdf(file):
    try:
        # ✅ Read file bytes only once
        file_bytes = file.read()

        # 🔁 Reset file pointer (so Streamlit can still use it later if needed)
        file.seek(0)

        # ✅ Use PyMuPDF from bytes
        doc = fitz.open(stream=io.BytesIO(file_bytes), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        return f"Error reading PDF: {e}"
