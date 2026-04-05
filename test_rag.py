from query_data import query_rag

def test():
    question = 'Give me Jaina Solo MRN'
    result = query_rag(query_text = question)
    return result

print(test())


