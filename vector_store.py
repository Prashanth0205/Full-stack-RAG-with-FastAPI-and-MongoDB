
from retrieval_config import get_vectorstore

# async def lookup_contexts(message):
#     '''
#     Function used to lookup contexts from the vector store
#     '''
#     retriever = await get_vectorstore()
#     print(f"Completed getting the vector store")
#     retrieved_contexts = retriever.similarity_search(message)
#     return retrieved_contexts

async def lookup_contexts(messages):
    '''
    Function used to lookup contexts from the vector store
    '''
    retriever = await get_vectorstore()

    contexts = []
    for message in messages:
        # Process each message individually
        result = retriever.similarity_search(message)
        contexts.append(result)
    return contexts


# # Testing the function 
# import asyncio 

# message = ['Tell me something about the energy saving.']
# retrieved = asyncio.run(lookup_contexts(messages=message))
# print(retrieved)