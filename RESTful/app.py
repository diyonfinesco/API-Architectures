import requests

def rest_example():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    print(f"GET Response: {response}")

    data = {"userId": 1, "title": "blah", "body": "Woow"}
    response = requests.post("https://jsonplaceholder.typicode.com/posts", data)
    print(f"POST Response {response}")

if __name__ == "__main__":
    print("RESTful example")
    rest_example()