import argparse
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
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text
    print(query_rag(query_text))


def query_rag(query_text: str):
    # Prepare the DB.
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=1)

    context_text = "\n\n---\n\n".join([f"Document: {doc.page_content}\nScore: {_score}" for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    print(prompt)

    model = Ollama(model="llama3.1:8b")
    response_text = model.invoke(prompt)
    
    sources = [doc.metadata.get("id", None) for doc, _score in results]
    formatted_response = f"Sources: {sources}"
    print(formatted_response)
    return response_text


if __name__ == "__main__":
    main()
