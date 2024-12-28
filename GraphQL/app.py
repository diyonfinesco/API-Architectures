import requests

url = "https://countries.trevorblades.com/" 

query = """
query {
  country(code: "US") {
    name
    capital
    currency
  }
}
"""

def graphql_example():
    response = requests.post(url, json={"query": query})
    if response.status_code == 200:
        print("GraphQL Response:", response.json())
    else:
        print(f"Query failed with status code {response.status_code}")

if __name__ == "__main__":
    graphql_example()