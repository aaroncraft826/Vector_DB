# Entry object contains text and its corresponding vector representation.
class Entry:
    def __init__(self, text):
        self.text = text
        self.vector = None

    def set_vector(self, vector):
        self.vector = vector

    def get_vector(self):
        return self.vector
    
    def get_text(self):
        return self.text
    
    def get_id(self):
        return self.id