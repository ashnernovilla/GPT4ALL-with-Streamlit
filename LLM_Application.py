# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 20:41:13 2024

@author: AI GENERATOR
"""

import requests
from bs4 import BeautifulSoup
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import GPT4All
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.faiss import FAISS
from langchain.schema.runnable import RunnablePassthrough

# URL of the webpage to scrape
url = "https://en.wikipedia.org/wiki/Harry_Potter_and_the_Prisoner_of_Azkaban_(film)"

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the page content with BeautifulSoup and extract body text
    soup = BeautifulSoup(response.text, 'html.parser')
    body_content = soup.body.get_text(separator=" ")  # Get body text with spaces
    
    # Split the text for document processing
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=100)
    document_chunks = text_splitter.create_documents([body_content])
else:
    print("Failed to retrieve the webpage.")
    document_chunks = []

# Define the prompt template
template = """Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that you don't know, don't try to make up an answer. 
Provide details.
{context}
Question: {question}
Helpful Answer:"""

prompt = PromptTemplate.from_template(template)

# Initialize embeddings and LLM with callbacks
embeddings = HuggingFaceEmbeddings(model_name='all-mpnet-base-v2')
callbacks = [StreamingStdOutCallbackHandler()]
llm = GPT4All(model="C:\\Users\\ASHNER_NOVILLA\\.cache\\gpt4all\\Meta-Llama-3.1-8B-Instruct.Q4_0.gguf",
              callbacks=callbacks,
              verbose=True,
              n_threads=8,
              max_tokens=300)

# Build LLM chain
llm_chain = LLMChain(prompt=prompt, llm=llm)

# Store document embeddings in FAISS vector store
vectorstore = FAISS.from_documents(documents=document_chunks, embedding=embeddings)

# Set up the retriever and retrieval-augmented generation (RAG) chain
retriever = vectorstore.as_retriever()
rag_chain = {"context": retriever, "question": RunnablePassthrough()} | llm_chain



# query = "who is Harry Potter"
# docs = vectorstore.similarity_search(query)
# print(docs[0].page_content)


# Define a query and get the result
query = "who is Hermione?"
result_query = rag_chain.invoke(query)

# Display the result
print(result_query)
