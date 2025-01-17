import pandas as pd
df = pd.read_csv('./dataset1.csv')

from sentence_transformers import SentenceTransformer
# Assuming your DataFrame is already loaded as 'df'

context_data = []

for i in range(len(df)):
    context = f"Question: {df.iloc[i]['Questions']} Answer: {df.iloc[i]['Answers']}"
    context_data.append(context)

# Embed the contexts
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
context_embeddings = embedding_model.encode(context_data)

import os

# Get the secret key from the environment
groq_api_keys = os.environ.get('groq_api_keys')

## LLM used for RAG
from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.1-70b-versatile", api_key=groq_api_keys)

## Embedding model!
from langchain_huggingface import HuggingFaceEmbeddings
embed_model = HuggingFaceEmbeddings(model_name="mixedbread-ai/mxbai-embed-large-v1")

# Create vector store
from langchain_chroma import Chroma

vectorstore = Chroma(
    collection_name="medical_dataset_store",
    embedding_function=embed_model,
    persist_directory="./",
)

# Add data to vector store
vectorstore.add_texts(context_data)

retriever = vectorstore.as_retriever()

from langchain_core.prompts import PromptTemplate

template = (""""You are a professional, empathetic mental health support AI assistant. 
Your role is to offer supportive, informative responses while maintaining appropriate 
boundaries and encouraging professional help when needed.

Context from mental health research: {context}

User Message: {question}

Please provide a response that:
1. Shows empathy and understanding
2. Provides relevant information based on research data when applicable
3. Encourages professional help when appropriate
4. Offers practical coping strategies when suitable
5. Maintains appropriate boundaries and disclaimers
    Context: {context}
    Question: {question}
    Answer:""")

rag_prompt = PromptTemplate.from_template(template)

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | rag_prompt
    | llm
    | StrOutputParser()
)

import gradio as gr

def rag_memory_stream(message, history):
    partial_text = ""
    for new_text in rag_chain.stream(message):
        partial_text += new_text
        yield partial_text

# Updated, more interesting examples
examples = [
    "How can I handle panic attacks effectively?",
    "What are the early signs of postpartum depression?",
    "Any strategies for coping with burnout at work?",
    "Can insomnia be linked to stress or anxiety?",
    "What are some natural ways to manage depression?"
]

# Updated UI title and description
title = "Mindful Moments: Your Mental Health AI Companion"
description = (
    "Empower yourself with real-time AI insights about mental health. "
    "This interactive demo is for learning purposes only and is not a substitute for professional help."
)

demo = gr.ChatInterface(
    fn=rag_memory_stream,
    type="messages",
    title=title,
    description=description,
    fill_height=True,
    examples=examples,
    theme="soft",  # Updated theme for a fresh, friendly look
)

if __name__ == "__main__":
    demo.launch()
