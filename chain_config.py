import os

from dotenv import find_dotenv, load_dotenv
from langchain import hub
from langchain_core.documents import Document 
from langchain_core.globals import set_llm_cache
from langchain_mongodb.cache import MongoDBAtlasSemanticCache
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langgraph.graph import START, StateGraph
from retrieval_config import get_vectorstore
from typing_extensions import List, TypedDict

from collection_config import get_query_results

CONN_STRING = os.getenv("CONN_STRING2")
DATABASE_NAME = "ai-chatbot"
COLLECTION_NAME = "semantic_cache"
INDEX_NAME = "vector_embeddings"
_ = load_dotenv(find_dotenv(), override=True)

prompt = hub.pull('rlm/rag-prompt')

llm = OllamaLLM(
    model='llama3.1',
    temperature=0
)

class State(TypedDict):
    question: str
    context: List[Document]
    answer: str

def retrieve(state: State):
    '''
    This state is meant fore retrieving content from the vectorstore
    '''
    retrieved_docs = get_query_results(state['question'])
    return {'context': retrieved_docs}

def generate(state: State):
    '''
    The LLM is used to generate a summary of relevant contents 
    from the retrieved contexts
    '''
    docs_contents = "\n\n".join(doc.page_content for doc in state['context'])
    messages = prompt.invoke({'question': state['question'], 'context': docs_contents})
    response = llm.invoke(messages)
    return {'answer': response}

def get_graph():
    '''
    returns the compiled graph builder object as a RAG system
    '''
    graph_builder = StateGraph(State).add_sequence([retrieve, generate])
    graph_builder.add_edge(START, "retrieve")
    setup_semantic_cache()
    graph = graph_builder.compile()
    return graph

def setup_semantic_cache():
    try:
        embeddings = OllamaEmbeddings(
            model="llama3.1"
        )

        set_llm_cache(
            MongoDBAtlasSemanticCache(
                connection_string=CONN_STRING,
                database_name=DATABASE_NAME,
                collection_name=COLLECTION_NAME,
                embedding=embeddings,
                index_name=INDEX_NAME,
                score_threshold=0.95
            )
        )
        return True
    except Exception as e:
        print(e)
        return False

# from IPython.display import Image, display

# graph = get_graph()
# image_data = graph.get_graph().draw_mermaid_png()
# with open("graphFlow.png", "wb") as f:
#     f.write(image_data)

# # Testing the LangGraph pipeline
# question = "Tell me something about energy saving."
# async def main():
#     result = await graph.ainvoke({'question': question})
#     print(result['answer'])

# import asyncio
# asyncio.run(main())
