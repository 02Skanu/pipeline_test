import requests
import datetime
import json


now = datetime.datetime.now()
current_minute = now.minute


next_minute = (current_minute + 1) % 60
todo_id = next_minute if next_minute != 0 else 1


url = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"


response = requests.get(url)
data = response.json()


with open("test.json", "w") as f:
    json.dump(data, f, indent=2)

print(f"Saved todo item {todo_id} to test.json.")
