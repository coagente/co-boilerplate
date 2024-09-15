# Docker Compose User Manual

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Getting Started with Docker Compose](#getting-started-with-docker-compose)
4. [Defining Services in `docker-compose.yml`](#defining-services-in-docker-composeyml)
5. [Common Docker Compose Commands](#common-docker-compose-commands)
6. [Environment Variables](#environment-variables)
7. [Networking](#networking)
8. [Volumes and Persistent Data](#volumes-and-persistent-data)
9. [Scaling Services](#scaling-services)
10. [Compose in Production](#compose-in-production)
11. [Conclusion](#conclusion)

---

## Introduction

Docker Compose is a tool that simplifies the process of defining and running multi-container Docker applications. With a single YAML file, you can configure all your application's services, networks, and volumes, and manage them together using simple commands.

**Key Features:**

- **Multi-Container Deployment:** Define and run multiple containers as a single service.
- **Simplified Configuration:** Use YAML files to configure your application's services.
- **Environment Management:** Manage environment variables and configurations easily.
- **Networking:** Automatically sets up networking between containers.
- **Scaling:** Easily scale services up or down.

---

## Installation

### Prerequisites

- **Docker Engine:** Docker Compose relies on Docker Engine to run containers. Ensure you have Docker installed on your system.

### Installing Docker Compose

#### On Linux

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose
```

#### On macOS and Windows

Docker Desktop for Mac and Windows includes Docker Compose, so no additional installation is necessary.

#### Verify Installation

```bash
docker-compose --version
```

---

## Getting Started with Docker Compose

### Example Application Structure

Suppose you have a simple web application that uses a Python Flask backend and a Redis database.

**Directory Structure:**

```
myapp/
├── app.py
├── requirements.txt
└── docker-compose.yml
```

### Sample `app.py`

```python
from flask import Flask
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = cache.incr('hits')
    return f'Hello World! This page has been visited {count} times.'
```

### Sample `requirements.txt`

```
flask
redis
```

---

## Defining Services in `docker-compose.yml`

Create a `docker-compose.yml` file to define your application's services.

```yaml
version: '3'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - redis
  redis:
    image: "redis:alpine"
```

**Explanation:**

- **version:** Specifies the Compose file format version.
- **services:** Defines the services (containers) to run.
  - **web:** The name of the first service.
    - **build:** Tells Compose to build an image from the current directory.
    - **ports:** Maps port 5000 on the host to port 5000 in the container.
    - **depends_on:** Specifies dependencies; `web` depends on `redis`.
  - **redis:** The second service using the official Redis image.

---

## Common Docker Compose Commands

### Build Services

```bash
docker-compose build
```

- Builds images for services defined in the `docker-compose.yml`.

### Start Services

```bash
docker-compose up
```

- Builds, (re)creates, starts, and attaches to containers.

### Run in Detached Mode

```bash
docker-compose up -d
```

- Runs containers in the background.

### Stop Services

```bash
docker-compose stop
```

- Stops running containers without removing them.

### Remove Services

```bash
docker-compose down
```

- Stops and removes containers, networks, images, and volumes created by `up`.

### View Running Services

```bash
docker-compose ps
```

- Lists containers managed by Compose.

### View Logs

```bash
docker-compose logs -f
```

- Shows real-time logs from services.

---

## Environment Variables

### Using `.env` File

You can store environment variables in a `.env` file.

**Example `.env` File:**

```
WEB_PORT=8000
REDIS_PORT=6379
```

**Usage in `docker-compose.yml`:**

```yaml
services:
  web:
    ports:
      - "${WEB_PORT}:5000"
  redis:
    ports:
      - "${REDIS_PORT}:6379"
```

### Inline Environment Variables

```bash
WEB_PORT=8000 docker-compose up
```

---

## Networking

Docker Compose automatically creates a default network for your application, allowing services to communicate using service names as hostnames.

**Connecting to Another Service:**

In `app.py`, connect to Redis using the service name `redis`.

```python
cache = redis.Redis(host='redis', port=6379)
```

---

## Volumes and Persistent Data

Use volumes to persist data and share it between containers and the host.

**Example in `docker-compose.yml`:**

```yaml
services:
  db:
    image: "mysql:5.7"
    volumes:
      - db_data:/var/lib/mysql

volumes:
  db_data:
```

- **volumes:** Defines named volumes.
- **db_data:** A named volume used by the `db` service.

---

## Scaling Services

You can run multiple instances of a service and load balance between them.

**Scale Command:**

```bash
docker-compose up --scale web=3
```

**Note:** Ensure your application can handle multiple instances (e.g., stateless services).

---

## Compose in Production

While Docker Compose is often used for development, it can also be used in production with caution.

- **Use Compose Files for Production:** Create separate Compose files for production with appropriate settings.
- **Docker Swarm and Kubernetes:** For more complex deployments, consider using orchestration tools like Docker Swarm or Kubernetes.

---

## Conclusion

Docker Compose simplifies the process of managing multi-container applications. By defining services, networks, and volumes in a single `docker-compose.yml` file, you can efficiently build, run, and scale your applications.

---

**References:**

- Official Documentation: [https://docs.docker.com/compose/](https://docs.docker.com/compose/)
- Compose File Reference: [https://docs.docker.com/compose/compose-file/](https://docs.docker.com/compose/compose-file/)
- Command-Line Reference: [https://docs.docker.com/compose/reference/](https://docs.docker.com/compose/reference/)