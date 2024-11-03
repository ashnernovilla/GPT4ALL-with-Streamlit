# GPT-with-Streamlit
To develop a streamlined ChatGPT-powered application using custom documents on Streamlit, providing users with a responsive and intuitive interface for engaging with tailored, document-specific insights.

# 📚 Web Content Query Tool

A Streamlit application that allows users to query content dynamically. Users can enter any PDF File, and the app will scrape the content, process it, and allow them to ask questions based on the extracted information.

## 🎯 Features

- **Dynamic URL Input**: Enter any Web page URL to scrape and query content.
- **Contextual Questioning**: Ask questions about the page content and get detailed answers.
- **Document Processing**: Utilizes LangChain to handle and process text efficiently.
- **Real-Time Interaction**: Engaging user interface with chat-like functionality.

## ⚙️ Technology Stack

- **Frontend**: Streamlit for interactive web applications.
- **PDF Scraping**: PyPDF2 for PDF parsing.
- **Natural Language Processing**: LangChain for LLM and embedding management.
- **Vector Store**: FAISS for efficient similarity search and document retrieval.
- **LLM**: OpenAI for generating human-like responses.

## 📦 Installation

To run this project, you need to have Python installed on your machine. Follow the steps below to set up the environment:

1. Clone the repository:
   ```bash
   git clone https://github.com/ashnernovilla/GPT4ALL-with-Streamlit.git
   cd wikipedia-query-tool
   
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:
   ```bash
   pip install -r requirements.txt

4. Run the Streamlit application:
   ```bash
   streamlit run app.py
