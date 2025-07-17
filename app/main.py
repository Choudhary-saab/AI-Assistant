import streamlit as st
from pdf_Loader import extract_text_from_pdf
from qa_engine import create_chunks, embed_chunks, query_response
from summarizer import summarize_text

st.set_page_config(page_title="AI Learning Assistant", layout="wide")
st.title("📚 AI Learning Assistant")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    with st.spinner("Reading and processing..."):
        pdf_text = extract_text_from_pdf(uploaded_file)
        chunks = create_chunks(pdf_text)
        db = embed_chunks(chunks)
        st.success("PDF processed successfully!")

    query = st.text_input("Ask a question from your uploaded document:")

    if query:
        with st.spinner("Thinking..."):
            response = query_response(query, db)
            st.markdown("### 📖 Answer")
            st.write(response)
            


st.markdown("---")
st.markdown("### 📄 Summarize Document")

# ✅ Only run if a PDF is uploaded
if uploaded_file:
    pdf_text = extract_text_from_pdf(uploaded_file)

    if "Error" in pdf_text:
        st.error(pdf_text)
    elif st.button("Generate Summary"):
        if len(pdf_text.strip()) == 0:
            st.warning("PDF seems empty or unreadable.")
        else:
            with st.spinner("Summarizing..."):
                summary = summarize_text(pdf_text)
                st.success("Summary Ready!")
                st.markdown("### 🧠 Summary")
                st.write(summary)
    else:
        st.warning("Please upload a PDF to summarize.")