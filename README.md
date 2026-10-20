# 🎬 MXR Analytics

**MXR Analytics** is an AI-powered media analysis application built with **LangChain**, **Pydantic**, and **Streamlit**. It extracts structured movie metadata (Title, Director, Release Year, Ratings, Genres) and generates a concise summary directly from unstructured text paragraphs or articles.

---

## ✨ Features

- **Structured Metadata Extraction**: Automatically identifies and extracts movie attributes into validated data fields using Pydantic.
- **Concise Summarization**: Produces an executive summary strictly under 3 sentences based solely on the provided text.
- **Modern & Aesthetic UI**: Clean Streamlit dashboard with custom metric displays, styled summaries, and expandable JSON outputs.
- **Powered by Gemini**: Driven by `google_genai:gemini-3.5-flash-lite` for fast and accurate extraction.

---

## 🛠️ Tech Stack

- **Python**: Core programming language.
- **Streamlit**: Web interface for interactive data extraction.
- **LangChain**: AI orchestration and prompt management.
- **Pydantic**: Data validation and structured output schema.
- **python-dotenv**: Environment variable management.

---

## 🚀 Getting Started

### 1. Prerequisites

Make sure you have Python 3.9+ installed on your system.

### 2. Installation

Clone this repository and install the required dependencies:

```bash
# Clone the repository
git clone [https://github.com/your-username/mxr-analytics.git](https://github.com/munazir666/mxr-analytics.git)
```
# Install dependencies
```
pip install streamlit langchain-core langchain google-genai pydantic python-dotenv
```
### 3. Environment Setup
Create a .env file in the root directory and add your Google Gemini API key:

Code snippet
```
GEMINI_API_KEY=your_google_gemini_api_key_here
```
💻 Running the Application
Launch the Streamlit web app with the following command:

```
streamlit run app.py
```
Open your browser at http://localhost:8501 to use the app.

📂 Project Structure
```
Plaintext
├── app.py           # Main Streamlit application
├── .env             # Environment variables (API Key)
├── README.md        # Project documentation
├── pyproject.toml   # Information about dependencies
├── .gitignore       # Files to hide from git
```
### 📝 Usage
Paste any text paragraph or article describing a movie into the input text area.

Click Analyze Text.

View the structured extraction results (Title, Director, Year, Rating, Genres) alongside the generated summary.

Expand the View Raw JSON Output section to inspect the raw structured output.