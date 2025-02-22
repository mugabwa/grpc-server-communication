# Book Accounts

This project is a Django application that uses gRPC for communication between services.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/book_accounts.git
    ```
2. Navigate to the project directory:
    ```bash
    cd book_accounts
    ```
3. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```
4. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```
5. Install the dependencies:
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

## gRPC

To start the gRPC server, run:
```bash
python manage.py grpcserver
```

## Testing

To run the tests, use:
```bash
python manage.py test
```

## Contributing

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-branch
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Description of changes"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-branch
    ```
5. Create a pull request.
