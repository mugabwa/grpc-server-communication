# gRPC Server-to-Server Communication

This project demonstrates server-to-server communication using gRPC in a Django application. The `book_accounts` project works as the gRPC client, while the `book_mx` project works as the gRPC server.

## Prerequisites

- Python 3.8+
- Django 3.2+
- grpcio 1.39.0+
- grpcio-tools 1.39.0+

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/grpc-server-communication.git
    cd grpc-server-communication
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Generate gRPC code from the `.proto` file:
    ```sh
    python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/your_service.proto
    ```

2. Run the Django server:
    ```sh
    python manage.py runserver
    ```

3. Start the gRPC server (`book_mx`):
    ```sh
    python grpc_server.py
    ```

4. Start the gRPC client (`book_accounts`):
    ```sh
    python grpc_client.py
    ```

## Project Structure

- `protos/`: Contains the `.proto` files defining the gRPC services and messages.
- `grpc_server.py`: The gRPC server implementation (`book_mx`).
- `grpc_client.py`: The gRPC client implementation (`book_accounts`).
- `your_django_app/`: The Django application directory.

## Acknowledgements

- [gRPC](https://grpc.io/)
- [Django](https://www.djangoproject.com/)

## Additional Resources

- [book_accounts README](book_accounts/Readme.md)
- [book_mx README](book_mx/Readme.md)
