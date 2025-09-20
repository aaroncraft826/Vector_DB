import load_json
from Vector_DB import Vector_DB, CompType
from Entry import Entry

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

db = Vector_DB()
db.set_comp_type(CompType.COSINE)
data = load_json.load_json_as_dict('blog.json')
for x in data:
    # print(x['id'], x['metadata']['text'], sep=" ")
    db.insert(Entry(x['metadata']['text']))
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:5173/",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Search endpoint to find k nearest entries based on the input text and comparison type
# Example: /search/LLMs/3/cosine
@app.get("/search/{text}/{k}/{type}")
def search(text: str, k: int, type: CompType):
    match type:
        case CompType.COSINE:
            db.set_comp_type(CompType.COSINE)
        case CompType.DOT:
            db.set_comp_type(CompType.DOT)
        case CompType.EUCLID:
            db.set_comp_type(CompType.EUCLID)
        case _:
            db.set_comp_type(CompType.COSINE)
    result = db.k_nearest(text, k)
    return {"result": result}

# Insert endpoint to add a new entry to the vector database
# Example: /insert/This is a new blog entry.
@app.get("/insert/{text}")
def insert(text: str):
    entry = Entry(text)
    db.insert(entry)
    return {"status": "success", "text": text}