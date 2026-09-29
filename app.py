import os
import time
from huggingface_hub import InferenceClient

# Initialize client using environment variable token
client = InferenceClient(
    api_key=os.environ["HF_TOKEN"],  # <-- Keep this exact text: "HF_TOKEN"
    provider="auto"
)

# Get topic from user
topic = input("Enter a topic: ")

# Construct the prompt
prompt = f"""
Create 5 study flashcards about {topic}.

For each flashcard:
1. Write a question.
2. Write a short answer.

Keep the answers suitable for a 2nd-year computer science student.
"""

start_time = time.time()

# Make API request to Model 1
completion = client.chat.completions.create(
    model="Qwen/Qwen2.5-72B-Instruct",
    messages=[{"role": "user", "content": prompt}]
)

end_time = time.time()
latency = end_time - start_time

# Print outputs
print("\nGenerated Flashcards:\n")
print(completion.choices[0].message.content)
print(f"\nResponse time: {latency:.2f} seconds")