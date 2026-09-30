# Hugging Face Flashcard Generator

A Python application that uses the Hugging Face `InferenceClient` API to automatically generate study flashcards on any topic and analyze latency across different text-generation models.

## Features
- Generates 5 structured study flashcards tailored for CS students.
- Uses environment variables for secure API key authentication.
- Measures and prints response latency in seconds.
- Supports switching between Hugging Face model endpoints.

## Requirements
- Python 3.8+
- `huggingface_hub`

## Setup & Installation

1. Clone the repository:
   ```bash
   git clone <YOUR_GITHUB_REPOSITORY_URL>
   cd huggingface_flashcards