# 🎥 AI Video Analyzer

An AI-powered video assistant that transforms YouTube videos and uploaded audio/video files into searchable, actionable knowledge. It uses local Whisper transcription, Sarvam for Hinglish-to-English translation, Mistral AI for summarization and information extraction, and a RAG pipeline for context-aware Q&A.

## ✨ Features

- 🎙️ **Audio/Video Transcription** — Transcribe English audio using local Whisper.
- 🌐 **Hinglish → English** — Translate Hinglish speech into English using Sarvam AI.
- 📝 **AI Summarization** — Generate concise, structured summaries using Mistral AI.
- ✅ **Action Item Extraction** — Extract tasks, owners, and deadlines.
- 📌 **Key Decision Extraction** — Identify important decisions from the transcript.
- ❓ **Question Extraction** — Detect open or unresolved questions.
- 🔎 **RAG-based Q&A** — Ask questions about the video and receive context-aware answers.
- 🗃️ **Vector Search** — Store transcript embeddings in ChromaDB for semantic retrieval.
- 💻 **Streamlit UI** — Simple interface for processing videos and interacting with results.

## 🏗️ Architecture

```text
YouTube URL / Uploaded File
            ↓
     Audio Processing
            ↓
       Audio Chunks
            ↓
   ┌────────┴─────────┐
   ↓                  ↓
Whisper           Sarvam AI
English STT     Hinglish → English
   └────────┬─────────┘
            ↓
        Transcript
            ↓
   ┌────────┴───────────┐
   ↓                    ↓
Summarization      Information
  (Mistral)         Extraction
   ↓                    ↓
Summary       Actions / Decisions /
              Open Questions
            ↓
       Transcript Chunks
            ↓
 HuggingFace Embeddings
   (all-MiniLM-L6-v2)
            ↓
         ChromaDB
            ↓
    Similarity Retriever
            ↓
        RAG + LCEL
            ↓
       Mistral AI
            ↓
      Context-Aware Q&A
```

## 🧰 Tech Stack

- **Language:** Python
- **Frontend:** Streamlit
- **LLM:** Mistral AI
- **Speech-to-Text:** OpenAI Whisper
- **Translation:** Sarvam AI
- **LLM Framework:** LangChain / LCEL
- **Embeddings:** HuggingFace `all-MiniLM-L6-v2`
- **Vector Database:** ChromaDB
- **Video/Audio Download:** yt-dlp
- **Audio Processing:** FFmpeg
- **Environment:** Python virtual environment

## 📂 Project Structure

```text
AI-Video-Analyzer/
│
├── app.py
├── main.py
├── test.py
├── requirements.txt
├── .gitignore
│
├── core/
│   ├── audio_processor.py
│   ├── transcriber.py
│   ├── summarize.py
│   ├── extractor.py
│   ├── vector_store.py
│   └── rag_engine.py
│
└── utils/
    └── ...
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/prachi094gitb/AI-Video-Analyzer.git
cd AI-Video-Analyzer
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv myenv6
myenv6\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg

FFmpeg is required for audio extraction and conversion.

Make sure `ffmpeg` is available in your system PATH.

### 5. Configure environment variables

Create a `.env` file in the project root:

```env
MISTRAL_API_KEY=your_mistral_api_key
SARVAM_API_KEY=your_sarvam_api_key
```

**Never commit your `.env` file or API keys to GitHub.**

## ▶️ Run the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

Then open the local Streamlit URL shown in your terminal.

## 🔄 How It Works

### 1. Input

The user provides a YouTube URL or uploads an audio/video file.

### 2. Audio Processing

The application extracts audio, converts it to WAV format, and splits long audio into manageable chunks.

### 3. Transcription

English audio is transcribed locally using Whisper. For Hinglish input, the application uses Sarvam AI to obtain an English transcript.

### 4. Summarization & Extraction

The transcript is processed by Mistral AI to generate:

- A structured summary
- Action items
- Owners and deadlines
- Key decisions
- Open questions

### 5. RAG Pipeline

The transcript is divided into smaller chunks and converted into vector embeddings using HuggingFace's `all-MiniLM-L6-v2`.

These embeddings are stored in ChromaDB. When a user asks a question, the system retrieves the most relevant transcript chunks and passes them as context to Mistral through a LangChain LCEL RAG chain.

### 6. Answer Generation

The LLM generates an answer based on the retrieved transcript context, allowing users to interact with the video content without manually searching through the entire transcript.

## 🧠 RAG Architecture

This project uses a **similarity-based RAG architecture**:

```text
Transcript
    ↓
Text Splitting
    ↓
HuggingFace Embeddings
    ↓
ChromaDB
    ↓
Similarity Retriever (Top-K)
    ↓
Retrieved Context
    ↓
LangChain LCEL Prompt
    ↓
Mistral AI
    ↓
Grounded Answer
```

## 🔐 Security

API keys are loaded through environment variables and should never be hardcoded.

Recommended `.gitignore` entries:

```gitignore
.env
myenv6/
__pycache__/
*.pyc
```

If an API key is accidentally exposed publicly, revoke/rotate it immediately.

## 🚀 Future Improvements

- Add speaker diarization
- Support more languages
- Add timestamp-based answers
- Improve retrieval with hybrid search
- Add conversation memory
- Add downloadable reports
- Deploy the application to the cloud
- Add authentication and persistent user sessions

## 👩‍💻 Author

**Prachi Sinha**

GitHub: https://github.com/prachi094gitb

---

⭐ If you find this project useful, consider giving the repository a star!
