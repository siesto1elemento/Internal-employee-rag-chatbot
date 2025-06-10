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

# Future Work

To further enhance the capabilities and robustness of this RAG system :

* **Advanced Reranking Integration**:
    * Implement and evaluate `Cohere's reranking` model to improve the relevance and precision of retrieved chunks before feeding them to the LLM. This can significantly boost answer quality by prioritizing truly relevant information.

* **Agentic Capabilities and Tooling**:
    * Expand the system's intelligence by integrating `additional tools` (e.g., web search APIs, database query tools, calculator). This will allow the LLM to perform more complex tasks and answer questions requiring up-to-date external information or computations, moving towards more `autonomous agents`.

* **Multi-Document Ingestion and Management**:
    * Develop a robust mechanism for users to `upload and manage multiple documents` (e.g., PDFs, DOCX, structured data). This includes features for:
        * Automated document parsing and chunking for various formats.
        * Tagging or categorizing documents for selective querying.
        * Handling versioning of documents.

* **Continuous Learning and Feedback Loop**:
    * Implement a system for collecting user feedback on answers (e.g., upvotes/downvotes) to fine-tune the retrieval and generation components.
    * Explore techniques for `continual learning` or periodic retraining of embeddings/retrieval models based on new data or feedback.

* **Enhanced Error Handling and Robustness**:
    * Improve error handling for edge cases, malformed queries, or when relevant information cannot be found.
    * Implement more sophisticated fallbacks or "I don't know" responses when confidence in the answer is low.

* **Performance Optimization**:
    * Optimize the embedding generation and retrieval process for larger datasets.
    * Explore techniques for faster LLM inference, potentially leveraging smaller, specialized models for certain query types.

* **Knowledge Graph Integration**:
    * Integrating a `knowledge graph` for structured data to complement the unstructured text retrieval. This could provide more factual consistency and enable complex reasoning over entities and relationships.

* **Improved Frontend Features**:
    * Add features to the React frontend such as `chat history`, `search suggestions`, and a more intuitive interface for managing uploaded documents.


