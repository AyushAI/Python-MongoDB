# Python MongoDB Operations

## Introduction

Welcome to the **Python MongoDB Operations** repository! This repository provides a collection of scripts and examples demonstrating various MongoDB operations using Python. It covers a wide range of tasks including document deletion, data retrieval, insertion, and updates, making it a valuable resource for learning and mastering MongoDB interactions with Python.

## Repository Structure

- **`delete_many_docs.py`**: Script for deleting multiple documents from a MongoDB collection.
- **`delete_db.py`**: Script for deleting an entire MongoDB database.
- **`find_data_without_id.py`**: Script for finding documents in a MongoDB collection without specifying an ID.
- **`find_operations_with_modifiers.py`**: Script for performing find operations with query modifiers.
- **`insert_many_docs.py`**: Script for inserting multiple documents into a MongoDB collection.
- **`insert_one_doc.py`**: Script for inserting a single document into a MongoDB collection.
- **`show_db_collection.py`**: Script for listing collections in a MongoDB database.
- **`change_id.py`**: Script for changing the ID of a document in a MongoDB collection.
- **`list_all_dbs.py`**: Script for listing all databases in the MongoDB instance.
- **`read_data_from_db.py`**: Script for reading data from a MongoDB database.
- **`update_many_docs.py`**: Script for updating multiple documents in a MongoDB collection.
- **`update_one_doc.py`**: Script for updating a single document in a MongoDB collection.

## Getting Started

### 1. Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/AyushAi/python-mongoDb.git
cd python-mongoDb
```
### 2. Set Up MongoDB
Ensure that you have MongoDB installed and running on your local machine or a remote server.

### 3. Install Required Libraries
Install the necessary Python libraries using pip:

```bash
pip install pymongo
```

### 4. Run Scripts
You can run any of the provided scripts to perform the corresponding MongoDB operations. For example, to delete multiple documents, execute:

```bash
python delete_many_docs.py
```

## Usage

- Deleting Documents: Use delete_many_docs.py and delete_db.py for removing documents and databases.
- Finding Data: Utilize find_data_without_id.py, find_operations_with_modifiers.py for querying documents.
- Inserting Documents: Insert data using insert_many_docs.py and insert_one_doc.py.
- Managing Collections: List collections with show_db_collection.py and change document IDs using change_id.py.
- Database Management: List all databases with list_all_dbs.py and read data with read_data_from_db.py.
- Updating Documents: Update documents with update_many_docs.py and update_one_doc.py.

## Contributing
If you have suggestions for additional operations or improvements, feel free to open an issue or submit a pull request. Contributions are welcome!

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
- PyMongo: For providing the Python driver for MongoDB.
- MongoDB: For being the database technology demonstrated in these scripts.
