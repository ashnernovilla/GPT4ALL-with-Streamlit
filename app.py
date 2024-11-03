from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import time


# Response Generator for Streaming
def response_generator(chain, docs, query):
    response = chain.run(input_documents=docs, question=query)
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat PDF")
    st.header("🤖💬 OpenAI Chatbot")
    
    # Initialize chat history in session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Upload PDF file
    pdf = st.file_uploader("Upload your PDF file", type="pdf")
    
    # Extract the text
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        # Split into chunks
        char_text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000,
                                                   chunk_overlap=200, length_function=len)
        text_chunks = char_text_splitter.split_text(text)
        
        # Create embeddings
        embeddings = OpenAIEmbeddings(api_key="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")
        docsearch = FAISS.from_texts(text_chunks, embeddings)
        llm = OpenAI(api_key="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")
        chain = load_qa_chain(llm, chain_type="stuff")

        # Display chat history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Accept user input for questions
        if prompt := st.chat_input("Ask a question about the PDF content:"):
            # Add user message to chat history and display it immediately
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Prepare for assistant's response display
            with st.chat_message("assistant"):
                response = ""
                response_container = st.empty()

                # Retrieve relevant documents and stream response
                docs = docsearch.similarity_search(prompt)
                for chunk in response_generator(chain, docs, prompt):
                    response += chunk
                    response_container.markdown(response)  # Update assistant's response as it streams

                # Add assistant's full response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})


if __name__ == '__main__':
    main()
