import urllib.request, json

class BasePost():
    def __init__(self, userId, id, title, body):
        self.userId = userId
        self.id = id
        self.title = title
        self.body = body
    
    def __repr__(self):
        return f"{self.title}"

    def __str__(self):
        return f"{self.id}"

url = "https://jsonplaceholder.typicode.com/posts"

dict = {}

with urllib.request.urlopen(url) as url:
    data = json.loads(url.read().decode()) # This is a list of dictionaries.
    for i in data: # iterate through the list
        dict[i["id"]] = BasePost(i["userId"], i["id"], i["title"], i["body"])
        

print(dict)

