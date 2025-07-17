from transformers import pipeline

# Load pre-trained summarizer
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text, max_length=200, min_length=50):
    # Limit input size due to model constraints
    chunk_size = 1000
    text_chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    summaries = []
    for chunk in text_chunks[:3]:  # Process only first 3 chunks to save time
        summary = summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)
        summaries.append(summary[0]['summary_text'])

    return "\n\n".join(summaries)
