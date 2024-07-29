Sure! Below is the formatted `README.md` content that you can copy directly into your `.md` file.

```markdown
# wv_store

A simple file storage server with a command-line interface (CLI). This application allows you to upload, delete, and list files using a FastAPI server and a CLI.

## Features

- Upload files
- Delete files
- List uploaded files

## Installation

### Using Docker

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/wv_store.git
   cd wv_store
   ```

2. **Build and Run the Docker Containers**

   ```bash
   docker-compose build
   docker-compose up -d
   ```

3. **Access the FastAPI Server**

   Open your browser and go to `http://localhost:8000/docs` to see the Swagger UI and interact with the API.

4. **Use the CLI**

   Get the container ID of the CLI container:

   ```bash
   docker ps
   ```

   Exec into the CLI container:

   ```bash
   docker exec -it <cli_container_id> /bin/sh
   ```

   Inside the container, you can now use the CLI commands:

   ```bash
   wv_store upload-file path/to/your/file.txt
   wv_store list-files
   wv_store delete-file file.txt
   ```

### Using pip

1. **Install the Package**

   ```bash
   pip install wv_store
   ```

2. **Run the FastAPI Server**

   ```bash
   uvicorn fs_store.main:app --host 0.0.0.0 --port 8000
   ```

3. **Access the FastAPI Server**

   Open your browser and go to `http://localhost:8000/docs` to see the Swagger UI and interact with the API.

4. **Use the CLI**

   From your terminal, you can use the following CLI commands:

   ```bash
   wv_store upload-file path/to/your/file.txt
   wv_store list-files
   wv_store delete-file file.txt
   ```

## Project Structure

```
fs_store/
│
├── fs_store/
│   ├── __init__.py
│   ├── cli.py
│   └── main.py
├── Dockerfile
├── Dockerfile.cli
├── docker-compose.yml
├── requirements.txt
├── setup.py
├── MANIFEST.in
└── README.md
```

- **`fs_store/`**: Contains the FastAPI server and CLI code.
  - **`__init__.py`**: Marks the directory as a Python package.
  - **`cli.py`**: Contains the CLI commands.
  - **`main.py`**: Contains the FastAPI server code.
- **`Dockerfile`**: Defines the Docker image for the FastAPI server.
- **`Dockerfile.cli`**: Defines the Docker image for the CLI.
- **`docker-compose.yml`**: Manages the services for running the FastAPI server and CLI.
- **`requirements.txt`**: Lists the Python dependencies.
- **`setup.py`**: Defines the project setup and CLI entry point.
- **`MANIFEST.in`**: Ensures necessary files are included in the package.
- **`README.md`**: Provides information about the project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Author

[Imam Aris Munandar](https://github.com/imamaris)
```

### Instructions Summary

1. **Clone the Repository and Run with Docker**
   - Build and run the application using Docker.
   - Access the FastAPI server through `http://localhost:8000/docs`.
   - Use the CLI from within the Docker container.

2. **Install and Run using pip**
   - Install the package via pip.
   - Run the FastAPI server with `uvicorn`.
   - Access the FastAPI server through `http://localhost:8000/docs`.
   - Use the CLI from your terminal.

This `README.md` file provides comprehensive instructions for users to get started with your project, ensuring they can install, run, and interact with the file storage server and CLI effectively.
```