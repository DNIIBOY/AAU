import socket
import json

HOST = "0.0.0.0"
PORT = 8888
BUFFER_SIZE = 1024

MONEY = 100


def send_data(data: dict) -> dict | int:
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((HOST, PORT))
    clientsocket.send(json.dumps(data).encode())
    response = clientsocket.recv(BUFFER_SIZE)
    clientsocket.close()
    try:
        return int(response.decode())
    except ValueError:
        return json.loads(response.decode())


def list_items() -> None:
    items = send_data({"action": "get"})
    for item in items:
        print(f"{item['id']}: {item['name']} - {item['price']}")


def add_item() -> None:
    name = input("Enter name: ")
    price = float(input("Enter price: "))
    data = send_data({"action": "add", "name": name, "price": price})
    if data == 200:
        print("Item added")
    else:
        print("Failed to add item")


def remove_item() -> None:
    id = int(input("Enter id: "))
    data = send_data({"action": "remove", "id": id})
    if data == 404:
        print("Item not found")
        return
    print(f"Purchased item: {data['name']} - {data['price']}")
    global MONEY
    MONEY -= data["price"]


def main():
    global MONEY
    print(f"Money: {MONEY}")
    print("1. List items")
    print("2. Add item")
    print("3. Buy item")
    print("4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        list_items()
    elif choice == "2":
        add_item()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        exit(0)
    else:
        print("Invalid choice")


if __name__ == "__main__":
    while True:
        main()
