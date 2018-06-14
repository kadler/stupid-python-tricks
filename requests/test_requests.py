import requests

payload = {
    'title': 'Python is great!',
    'userId': 1,
    'body': """Python is super cool.
You should really check it out!

https://www.python.org/"""
}

r = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload)
print(f"Post id: {r.json()['id']}")
