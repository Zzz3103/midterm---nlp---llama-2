import requests

url = "https://www.cs.cmu.edu/~vijayv/stories42M.pt"
response = requests.get(url)

with open("stories42M.pt", "wb") as file:
    file.write(response.content)

print("Tải xong!")
