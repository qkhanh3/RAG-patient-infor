import streamlit as st
from langchain.vectorstores.chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama

from get_embedding_function import get_embedding_function

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Write a referral letter based on the following context:

{context}

---

Some patient information: {question}
"""

def main():
    st.title("Referral Letter Generator")
    query = st.text_input("Enter your query")

    if st.button("Generate Referral Letter"):
        if query:
            response = query_rag(query)
            st.text_area("Referral Letter", response, height=300)
        else:
            st.warning("Please enter a query.")

def query_rag(query_text: str):
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    #search db
    results = db.similarity_search_with_score(query_text, k=3)

    context_text = "\n\n---\n\n".join([f"Document: {doc.page_content}\nScore: {_score}" for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    #st.write("Generated Prompt:", prompt)

    model = Ollama(model="llama3.1:8b")
    response_text = model.invoke(prompt)
    
    sources = [doc.metadata.get("id", None) for doc, _score in results]
    formatted_response = f"Sources: {sources}"
    #st.write("Sources:", formatted_response)
    return response_text

if __name__ == "__main__":
    main()
