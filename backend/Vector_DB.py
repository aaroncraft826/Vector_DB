from sentence_transformers import SentenceTransformer
import torch
from enum import Enum

# Comparison types for vector embeddings
class CompType(Enum):
    COSINE = "cosine"
    DOT = "dot"
    EUCLID = "euclid"

# Vector database to store sentence embeddings
# entries are stored in a dictionary with their embeddings, with the text as the key to prevent duplication
# the transformer is responisble for encoding the sentences into embeddings
# comp_type determines how two vector embeddings are compared: cosine similarity, dot product, and euclidean distance
class Vector_DB:
    def __init__(self):
        self.entries = {}
        self.transformer = SentenceTransformer('TaylorAI/bge-micro')
        self.comp_type = CompType.COSINE
    
    # inserts an entry into the vector database (key is the blog id)
    def insert(self, entry):
        entry.set_vector(self.transformer.encode(entry.get_text()))
        self.entries[entry.get_text()] = entry

    # returns the k most similar sentences to the input string (blog_id, similarity score)
    def k_nearest(self, str, k):
        embed = self.transformer.encode(str)
        ents = []
        for key in self.entries:
            match self.comp_type:
                case CompType.COSINE:
                    sim_score = torch.nn.functional.cosine_similarity(torch.tensor(embed), torch.tensor(self.entries[key].get_vector()), dim=0)
                case CompType.DOT:
                    sim_score = torch.dot(torch.tensor(embed), torch.tensor(self.entries[key].get_vector()))
                case CompType.EUCLID:
                    sim_score = torch.nn.functional.pairwise_distance(torch.tensor(embed), torch.tensor(self.entries[key].get_vector()))
            # ents.append((key, sim_score.item()))
            ents.append(Result(key, sim_score.item()))
        if self.comp_type == CompType.EUCLID:
            ents = sorted(ents, key=lambda x: x.get_score())
        else:
            ents = sorted(ents, key=lambda x: x.get_score(), reverse=True)
        return ents[:k]
    
    # sets the comparison type for the vector database
    def set_comp_type(self, comp_type):
        self.comp_type = comp_type
    
    # returns the dictionary of vectors
    def get_vectors(self):
        return self.entries
    
# Result object to store search results with text and similarity score
class Result:
    def __init__(self, text, score):
        self.text = text
        self.score = score

    def get_text(self):
        return self.text
    
    def get_score(self):
        return self.score