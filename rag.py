import faiss
import numpy as np
import pickle
from openai import OpenAI
from dotenv import load_dotenv
from fastapi import FastAPI, WebSocket


app = FastAPI()

load_dotenv()
client = OpenAI()

# Load stored data
with open("embeddings.pkl", "rb") as f:
    embeddings, nodes_text = pickle.load(f)

# Rebuild FAISS index
dimension = len(embeddings[0])
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings).astype('float32'))

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        query = await websocket.receive_text()

        query_response = client.embeddings.create(
            input=query,
            model="text-embedding-3-small"
        )
        query_embedding = query_response.data[0].embedding

        # Search and print
        D, I = index.search(np.array([query_embedding]).astype('float32'), k=3)

        embedding_context = []
        for idx in I[0]:
            embedding_context.append(nodes_text[idx])
            # print(f"node{idx}---------------------------")
            # print(nodes_text[idx])

        context_string = "\n\n".join(embedding_context)

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that answers questions based only on the provided context."},
                {"role": "user", "content": f"""Only answer from the context,

        Context:
        {context_string}

        Question: {query}
        """}
            ]
        )

        answer = response.choices[0].message.content
        
        await websocket.send_text(answer)




# Creating the embeddings

# import openparse
# import faiss
# import numpy as np
# import pickle
# from openai import OpenAI
# from dotenv import load_dotenv


# load_dotenv()

# client = OpenAI()

# basic_doc_path = "./Small_Business_policy_template.pdf"
# parser = openparse.DocumentParser()
# parsed_basic_doc = parser.parse(basic_doc_path)


# embeddings = []
# nodes_text = []

# for node in parsed_basic_doc.nodes:
#     response = client.embeddings.create(
#     input=node.text,
#     model="text-embedding-3-small"
#     )
#     embeddings.append(response.data[0].embedding)
#     nodes_text.append(node.text)

# with open("embeddings.pkl", "wb") as f:
#     pickle.dump((embeddings, nodes_text), f)

# dimension = len(embeddings[0])
# index = faiss.IndexFlatL2(dimension)
# index.add(np.array(embeddings).astype('float32'))


# query = "what is the leave policy"
# query_response = client.embeddings.create(
#     input=query,
#     model="text-embedding-3-small"
# )


# query_embedding = query_response.data[0].embedding
# D, I = index.search(np.array([query_embedding]).astype('float32'), k=3)

# for idx in I[0]:
#     print(f"{idx}-----------------------")
#     node = nodes_text[idx]
#     print(node)





    
