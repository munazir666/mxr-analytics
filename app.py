from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from typing import List, Optional
import streamlit as st

load_dotenv()

# Page Setup
st.set_page_config(
    page_title="MXR Analytics",
    page_icon="🎬",
    layout="centered"
)

# 1. Professional Pydantic schema 
class MovieMetadata(BaseModel):
    title: Optional[str] = Field(None, description="Official title of the movie.")
    director: Optional[str] = Field(None, description="Director or filmmaker.")
    release_year: Optional[int] = Field(None, description="The theatrical release year.")
    ratings: Optional[float] = Field(None, description="IMDB Ratings")
    genres: List[str] = Field(default_factory=list, description="Movie genres.")
    summary: str = Field(..., description="A concise summary strictly under 3 sentences.")

# UI Title & Header
st.title("🎬 MXR Analytics")
st.caption("Extract structured movie metadata and summaries using AI.")

st.divider()

# Input area
text_input = st.text_area(
    "Enter Movie Paragraph / Article Text",
    placeholder="Paste your text about a movie here...",
    height=200
)

# Process Button
if st.button("Analyze", type="primary", use_container_width=True):
    if not text_input.strip():
        st.warning("Please enter a movie's paragraph to analyze.")
    else:
        with st.spinner("Analyzing text..."):
            # 2. Initialize model with structured output
            base_model = init_chat_model("google_genai:gemini-3.5-flash-lite")
            model = base_model.with_structured_output(MovieMetadata)

            # 3. Professional prompts
            prompt = ChatPromptTemplate.from_messages([
                ("system", "You are an expert media analyst. Extract structured movie metadata accurately and objectively based solely on the text."),
                ("human", "Analyze this text:\n---\n{text_input}\n---")
            ])

            # 4. Execution
            final_prompt = prompt.invoke({"text_input": text_input})
            result: MovieMetadata = model.invoke(final_prompt)

            st.success("Extraction Complete!")
            st.subheader("Extracted Movie Metadata")

            # Aesthetic Metrics Display
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Title", result.title or "N/A")
                st.metric("Director", result.director or "N/A")
            with col2:
                st.metric("Release Year", result.release_year or "N/A")
                st.metric("Rating", f"⭐ {result.ratings}" if result.ratings else "N/A")
            with col3:
                st.write("**Genres**")
                if result.genres:
                    st.write(", ".join(result.genres))
                else:
                    st.write("N/A")

            # Summary Card
            st.markdown("---")
            st.subheader("Executive Summary")
            st.info(result.summary)

            # Option to expand JSON output
            with st.expander("View Raw JSON Output"):
                st.json(result.model_dump())