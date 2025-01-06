# AI-Powered Backend Service with FastAPI and RAG

This project demonstrates the creation of an AI-powered backend service that integrates advanced technologies like retrieval-augmented generation (RAG), semantic caching, and vector databases. The service is designed to handle APIs, process payloads, implement secure authentication, and provide intelligent data retrieval capabilities.

---

## Key Skills and Technologies

- **Backend Development**: Leveraging **FastAPI** for rapid and efficient API development.
- **Data Validation**: Using **Pydantic** to define and validate robust data schemas.
- **Vector Search**: Creating a retriever vector store for efficient data retrieval from scraped web data and PDF documents.
- **RAG Implementation**: Developing an agentic **retrieval-augmented generation** pipeline with **LangGraph** for intelligent chatbot responses.
- **Database Integration**: Connecting to **Atlas MongoDB** for scalable and cloud-based storage solutions.
- **Semantic Caching**: Implementing caching mechanisms to optimize large language model (LLM) queries and reduce redundancy.
- **Containerization**: Dockerizing the backend service for streamlined deployment and scalability.
- **Unit Testing**: Validating APIs and payload processing with comprehensive test cases.

---

## What This Project Does

1. **Backend Service**:
   - Develops RESTful APIs for managing incoming requests and responses.
   - Processes payloads with strong data validation and error handling.

2. **Data Storage and Retrieval**:
   - Builds a vector store containing data from web scraping and PDF documents.
   - Pushes vectorized data to a database and facilitates semantic search.

3. **AI-Powered Features**:
   - Implements retrieval-augmented generation (RAG) to produce intelligent, context-aware responses.
   - Reduces redundant calls to the LLM using semantic caching mechanisms.

4. **Secure and Scalable**:
   - Implements authentication to secure API access.
   - Deploys the service using Docker, ensuring it runs reliably in different environments.

5. **Testing and Optimization**:
   - Validates endpoints with unit tests.
   - Evaluates payload examples to ensure the application meets expected performance.

---

## How to Use

1. **Run Locally**:
   - Clone the repository:
     ```bash
     git clone https://github.com/Prashanth0205/Full-stack-RAG-with-FastAPI-and-MongoDB.git
     cd Full-stack-RAG-with-FastAPI-and-MongoDB
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Start the FastAPI server:
     ```bash
     uvicorn main:app --reload
     ```

2. **Run with Docker**:
   - Build the Docker image:
     ```bash
     docker build -t ai-backend-service .
     ```
   - Run the container:
     ```bash
     docker run -p 8000:8000 ai-backend-service
     ```

---