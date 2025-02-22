# Book MX

This project is a Django application that uses gRPC for communication.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/book_mx.git
    cd book_mx
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Apply the migrations:
    ```bash
    python manage.py migrate
    ```

2. Run the development server:
    ```bash
    python manage.py runserver
    ```

3. Run the gRPC server:
    ```bash
    python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. book_mx/protos/book.proto
    python book_mx/grpc_server.py
    ```

## Testing

Run the tests using the following command:
```bash
python manage.py test
```

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin my-feature-branch`.
5. Submit a pull request.
