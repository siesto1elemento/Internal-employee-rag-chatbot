# RAG System Overview

![Watch the Demo Video](https://github.com/siesto1elemento/Internal-employee-rag-chatbot/blob/master/docs/demo.gif)

This document outlines the architecture and workflow of my Retrieval-Augmented Generation (RAG) system, designed to provide intelligent answers based on a business policy template.

## Workflow Steps

1.  **Document Ingestion and Parsing**:
    * Initially, the raw business policy template document was converted and parsed using `OpenParse` to extract structured content.

2.  **Chunking**:
    * The parsed content was then divided into smaller, manageable text `chunks` suitable for embedding and retrieval.

3.  **Embedding Creation**:
    * Embeddings for each chunk were generated using `OpenAI's small text embedding model`.

4.  **Vector Store Upload (FAISS)**:
    * These embeddings were subsequently uploaded to a `FAISS vector store` for efficient similarity search.
    * **Optimization**: To avoid redundant embedding generation, these embeddings were also `saved as a .pkl file`. This allows for quick reloading of the vector store without re-processing the entire document.

5.  **Query and Retrieval**:
    * When a user query is received, the system queries this `FAISS vector database` to find the `k nearest matches` (chunks) that are most semantically similar to the query.

6.  **Contextualized LLM Generation**:
    * The retrieved relevant chunks are then fed as context to a `Large Language Model (LLM)`.
    * The LLM uses this context to generate a comprehensive and accurate answer to the user's query.

## Technology Stack

* **Frontend**: Built with `React` for a dynamic and responsive user interface.
* **Backend**: Developed using `FastAPI`, providing robust API endpoints.
    * Utilizes `WebSocket streaming` for real-time token delivery from the LLM, enhancing the user experience.
* **Vector Database**: `FAISS` for efficient similarity search.
* **Embedding Model**: `OpenAI Text Embeddings` (small model).
* **Parsing**: `OpenParse`.


