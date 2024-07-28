# MongoDB Client

A Python module to interact with a MongoDB database via HTTP requests.

## Features

- **Sign In**: Authenticate using email and password to receive an access token.
- **CRUD Operations**: Create, Read, Update, and Delete records in the MongoDB database.
- **Flexible Authentication**: Use the access token for authentication in subsequent requests.

## Installation

You can install this module directly from the GitHub repository:

```bash
pip install git+https://github.com/yourusername/mongodb_client.git
```

## Usage

### 1. Import and Initialize the Client

First, import the `MongoDB` class from the module and initialize it with the base URL of your MongoDB HTTP server:

```python
from mongodb_client.mongodb import MongoDB

client = MongoDB(base_url="http://localhost:8080")
```

### 2. Sign In

Sign in with your email and password to receive an access token:

```python
success = client.signin("email@example.com", "password")
if success:
    print("Signed in successfully!")
else:
    print("Failed to sign in.")
```

### 3. Perform CRUD Operations

#### Get Records

Retrieve records from a specific database and collection:

```python
records = client.get_records("mydatabase", "mycollection")
print(records)
```

#### Get Record by ID

Retrieve a specific record by its ID:

```python
record = client.get_record_by_id("mydatabase", "mycollection", "record_id")
print(record)
```

#### Create Records

Create new records in a specific database and collection:

```python
new_record = {"name": "John Doe", "email": "john@example.com"}
response = client.create_records("mydatabase", "mycollection", new_record)
print(response)
```

#### Update Record

Update an existing record by its ID:

```python
updated_data = {"name": "Jane Doe"}
response = client.update_record("mydatabase", "mycollection", "record_id", updated_data)
print(response)
```

#### Delete Record

Delete a specific record by its ID:

```python
response = client.delete_record("mydatabase", "mycollection", "record_id")
print(response)
```

#### Delete Records

Delete all records in a specific database and collection:

```python
response = client.delete_records("mydatabase", "mycollection")
print(response)
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.