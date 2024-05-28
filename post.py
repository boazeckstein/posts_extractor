import json

class Post:
    def __init__(self, title, text, published, author):
        self.title = title
        self.text = text
        self.published = published
        self.author = author

    def to_dict(self):
        return {
            "title": self.title,
            "text": self.text,
            "published": self.published,
            "author": self.author
        }
    
    def to_json(self):
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=4)
