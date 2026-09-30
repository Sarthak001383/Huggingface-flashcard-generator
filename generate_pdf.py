import os
import time
from fpdf import FPDF
from huggingface_hub import InferenceClient

# 1. Generate Content via Hugging Face API
client = InferenceClient(
    api_key=os.environ["HF_TOKEN"],
    provider="auto"
)

topic = input("Enter a topic for the PDF report: ")

prompt = f"""
Create 5 study flashcards about {topic}.

For each flashcard:
1. Write a question.
2. Write a short answer.

Keep the answers suitable for a 2nd-year computer science student.
"""

start_time = time.time()
completion = client.chat.completions.create(
    model="meta-llama/Llama-3.1-8B-Instruct",
    messages=[{"role": "user", "content": prompt}]
)
end_time = time.time()
latency = end_time - start_time
response_text = completion.choices[0].message.content

# 2. Build PDF Document
class FlashcardPDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 16)
        self.cell(0, 10, "Hugging Face Flashcard Report", border=False, new_x="LMARGIN", new_y="NEXT", align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 9)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

pdf = FlashcardPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=11)

# Report Metadata
pdf.set_font("Helvetica", "B", 12)
pdf.cell(0, 8, f"Topic: {topic}", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Helvetica", size=10)
pdf.cell(0, 6, f"Model: meta-llama/Llama-3.1-8B-Instruct", new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 6, f"Latency: {latency:.2f} seconds", new_x="LMARGIN", new_y="NEXT")
pdf.ln(5)

# Flashcard Content Body
pdf.set_font("Helvetica", "B", 12)
pdf.cell(0, 8, "Generated Flashcards:", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Helvetica", size=10)

# Multi-line cell for response content
pdf.multi_cell(0, 6, response_text)

# Save PDF Output
output_filename = f"flashcards_{topic.lower().replace(' ', '_')}.pdf"
pdf.output(output_filename)

print(f"\nReport successfully generated and saved as: {output_filename}")