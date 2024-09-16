# Svelte Frontend with FastAPI Backend

This project is a boilerplate for starting a web application with a Svelte frontend and a FastAPI backend, containerized using Docker. It serves as a starter project with a knowledge base optimized for [**cursor**](https://cursor.com) and others AI driven IDEs.

## Project Description

This application consists of two main parts:
1. A Svelte frontend that displays a simple "Hello World" message.
2. A FastAPI backend that provides a "Hello World" API endpoint.

The project is containerized using Docker, allowing for easy deployment and consistent environments across different systems.

## Features

- Svelte frontend for a reactive and efficient user interface
- FastAPI backend for a fast and modern Python API
- Docker containerization for easy deployment and scaling
- Docker Compose for orchestrating multi-container applications
- Knowledge base included for reference language models

## Project Structure

The project is organized into two main directories:

1. `frontend/`: Contains the Svelte application
   - `src/`: Source files for the Svelte app
   - `public/`: Public assets
   - `Dockerfile`: Docker configuration for the frontend

2. `backend/`: Contains the FastAPI application
   - `app/`: Source files for the FastAPI app
   - `Dockerfile`: Docker configuration for the backend

3. `docker-compose.yml`: Defines and configures the services

4. `knowledge/`: Contains markdown files with documentation on various technologies used in the project

## Getting Started

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <project-directory>
   ```

2. Build and run the containers:
   ```
   docker-compose up --build
   ```

3. Access the applications:
   - Frontend: http://localhost:8080
   - Backend: http://localhost:8181
   - API Documentation: http://localhost:8181/docs

## Development

### Frontend (Svelte)

The Svelte application is located in the `frontend/` directory. To make changes:

1. Navigate to the `frontend/` directory
2. Edit files in the `src/` directory
3. The changes will be automatically reflected in the running container

### Backend (FastAPI)

The FastAPI application is located in the `backend/` directory. To make changes:

1. Navigate to the `backend/` directory
2. Edit files in the `app/` directory
3. The changes will be automatically reflected in the running container

## Knowledge Base

The `knowledge/` directory contains markdown files with detailed information about the technologies used in this project. These files serve as a reference for language models and can be useful for developers working on the project.

## Deployment

To deploy this application:

1. Ensure Docker and Docker Compose are installed on your server
2. Clone the repository on your server
3. Run `docker-compose up -d` to start the containers in detached mode

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open-source and available under the [MIT License](LICENSE).
