# FastAPI User Manual

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Creating Your First API](#creating-your-first-api)
4. [Interactive API Documentation](#interactive-api-documentation)
   - [Swagger UI](#swagger-ui)
   - [ReDoc](#redoc)
5. [Path Parameters](#path-parameters)
6. [Query Parameters](#query-parameters)
7. [Request Body](#request-body)
8. [Response Models](#response-models)
9. [Error Handling](#error-handling)
10. [Dependency Injection](#dependency-injection)
11. [Security](#security)
12. [Middleware](#middleware)
13. [Background Tasks](#background-tasks)
14. [Conclusion](#conclusion)

---

## Introduction

FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints. It is designed to be easy to use and to help developers build robust and high-performance APIs quickly.

**Key Features:**

- **High Performance:** As fast as NodeJS and Go (thanks to Starlette and Pydantic).
- **Easy to Learn:** Intuitive and short learning curve.
- **Validation:** Automatic request validation with Pydantic.
- **Documentation:** Auto-generated interactive API docs.

---

## Installation

To install FastAPI, you need Python 3.7 or above.

```bash
pip install fastapi
pip install "uvicorn[standard]"
```

- **FastAPI:** The core framework.
- **Uvicorn:** An ASGI server to run the application.

---

## Creating Your First API

Create a file named `main.py` with the following content:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

Run the application using Uvicorn:

```bash
uvicorn main:app --reload
```

- `--reload` option restarts the server after code changes.

---

## Interactive API Documentation

FastAPI automatically generates interactive API documentation. Once the server is running, navigate to:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Swagger UI

- Provides an interactive interface to test your API endpoints.
- Allows you to input parameters and view responses directly in the browser.

### ReDoc

- Another documentation interface with a different style.
- Useful for understanding complex APIs with extensive documentation.

---

## Path Parameters

Define dynamic URL paths using path parameters.

```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

- **Type Annotation (`item_id: int`):** Validates and converts `item_id` to an integer.

---

## Query Parameters

Specify optional parameters in the query string.

```python
@app.get("/items/")
def read_items(page: int = 1, size: int = 10):
    return {"page": page, "size": size}
```

- **Default Values:** If not provided, `page` defaults to `1` and `size` defaults to `10`.

---

## Request Body

Use Pydantic models to define and validate request bodies.

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.post("/items/")
def create_item(item: Item):
    return item
```

- **Automatic Validation:** Ensures the request body matches the `Item` model schema.

---

## Response Models

Define the structure of the response data.

```python
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    return item
```

- **Response Model:** FastAPI will use the `Item` model to serialize the response.

---

## Error Handling

Handle errors and exceptions gracefully.

```python
from fastapi import HTTPException

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id > 1000:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id}
```

- **HTTPException:** Raise HTTP errors with custom status codes and messages.

---

## Dependency Injection

Reuse code with dependencies.

```python
from fastapi import Depends

def get_db():
    db = "Database Connection"
    try:
        yield db
    finally:
        pass  # Close the database connection

@app.get("/users/")
def read_users(db=Depends(get_db)):
    return {"db": db}
```

- **Depends:** Declare a dependency that FastAPI will resolve.

---

## Security

Implement authentication and authorization.

```python
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    return {"token": token}
```

- **OAuth2PasswordBearer:** A flow to handle OAuth2 authentication.

---

## Middleware

Execute code before or after requests.

```python
from starlette.middleware.base import BaseHTTPMiddleware

@app.middleware("http")
async def add_process_time_header(request, call_next):
    response = await call_next(request)
    response.headers["X-Process-Time"] = "0.001s"
    return response
```

- **Middleware:** Modify requests or responses globally.

---

## Background Tasks

Run tasks after returning a response.

```python
from fastapi import BackgroundTasks

def write_log(message: str):
    with open("log.txt", "a") as log:
        log.write(message)

@app.post("/send-notification/")
def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, f"Notification sent to {email}\n")
    return {"message": "Notification sent"}
```

- **BackgroundTasks:** Schedule tasks to run after the response is sent.

---

## Conclusion

FastAPI is a powerful and intuitive framework for building APIs with Python. Its automatic validation, interactive documentation, and high performance make it an excellent choice for both beginners and experienced developers.

---

**References:**

- Official Documentation: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)