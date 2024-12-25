# VOCAL-SENSE: Decoding Speech, Summarizing Thoughts, and Detecting Emotions

## Project Overview
VOCAL-SENSE is an AI-powered application designed to process and analyze audio data efficiently. The project focuses on three core functionalities:
1. **Audio Transcription**: Converting spoken audio into accurate text transcriptions.
2. **Text Summarization**: Generating concise and meaningful summaries of transcribed text.
3. **Emotion Detection**: Analyzing the emotional tone of speech to extract sentiments.

By automating these tasks, VOCAL-SENSE improves efficiency, accuracy, and usability for handling large volumes of audio content in real-time or file-based formats.

## Key Features
- **Audio Transcription**:
  - Powered by OpenAI's Whisper model.
  - Supports real-time and file-based transcription.
  - Handles multiple languages with high accuracy.

- **Text Summarization**:
  - Abstractive Summarization using the pre-trained BART model.
  - Extractive Summarization using algorithms like TextRank, BM25, TF-IDF-Cosine, and LCS.
  - Fine-tuned T5 model for domain-specific summaries (e.g., medical complaints).

- **Emotion Detection**:
  - Implemented using the Wav2Vec Transformer model.
  - Extracts emotional context from audio data.

- **User Interface**:
  - Interactive and user-friendly.
  - Allows toggling between abstractive and extractive summaries.
  - Displays transcription, summary, and emotional analysis results clearly.

## Objectives
- Enable real-time, precise audio transcription.
- Provide versatile summarization options (abstractive and extractive).
- Detect emotional tones in speech for sentiment analysis.
- Build an intuitive interface for seamless user interaction.

## Technical Stack
- **Programming Language**: Python
- **Libraries/Frameworks**: Flask, NLTK, Hugging Face Transformers
- **Models**: Whisper, BART, T5, Wav2Vec
- **Tools**: Docker, Gladia API

## Results
- **Audio Transcription**: Whisper model delivered accurate and fast transcriptions for both real-time and file-based audio.
- **Text Summarization**:
  - Achieved high ROUGE scores (ROUGE-1: 0.604, ROUGE-2: 0.3749, ROUGE-L: 0.4206) using TF-IDF-Cosine.
  - Fine-tuned T5 model performed well on medical datasets for SOAP format summaries.
- **Emotion Detection**: Wav2Vec model demonstrated effective emotional tone detection.

## Future Enhancements
- Extend emotion detection to include more nuanced sentiments.
- Enhance summarization with additional domain-specific datasets.
- Optimize UI for better accessibility and cross-platform support.
