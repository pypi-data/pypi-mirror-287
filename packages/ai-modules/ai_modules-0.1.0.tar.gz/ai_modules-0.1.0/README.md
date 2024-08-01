# Object Data AI System

## Overview

The Object Data AI System is a flexible and extensible framework for managing, processing, and transforming various types of data objects using AI techniques. It provides a RESTful API built with FastAPI for interacting with the system.

## Project Structure

```
/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api.py
│   ├── app.py
│   └── models/
│       ├── __init__.py
│       └── models.py
├── Dockerfile
└── docker-compose.yml
```

- `/app/`: Contains the main application code
  - `__init__.py`: Initializes the app package
  - `main.py`: Entry point of the application
  - `api.py`: Defines the API routes
  - `app.py`: Creates and configures the FastAPI application
  - `models/`: Contains the data models
    - `__init__.py`: Initializes the models package
    - `models.py`: Defines the data object models and system components
- `Dockerfile`: Defines the Docker image for the application
- `docker-compose.yml`: Defines the services for running the application

## Key Components

1. **Data Objects**: The system supports various types of data objects, including:
   - TextData: For textual content
   - MediaData: For images, audio, and video content
   - CodeData: For source code content

2. **ObjectDataAISystem**: The core system that manages data objects, transformers, and storage.

3. **DataObjectFactory**: Responsible for creating appropriate data objects based on the input type.

4. **TransformerRegistry**: Manages a collection of transformers that can be applied to data objects.

5. **DataLake**: Provides storage and retrieval capabilities for data objects.

6. **API**: A RESTful API for interacting with the system, including endpoints for creating, retrieving, processing, and transforming data objects.

## Setup and Running

### Prerequisites

- Docker
- Docker Compose

### Running the Application

1. Clone the repository to your local machine.
2. Navigate to the root directory of the project.
3. Build and run the Docker containers:

   ```bash
   docker-compose up --build
   ```

4. The API will be available at `http://localhost:8000`.

## API Usage

The API provides the following main endpoints:

- `POST /objects/`: Create a new data object
- `GET /objects/{obj_id}`: Retrieve a data object
- `POST /objects/{obj_id}/process`: Process a data object
- `POST /objects/{obj_id}/transform`: Apply a transformer to a data object
- `GET /transformers/`: List available transformers
- `POST /transformers/`: Register a new transformer

For detailed API documentation, visit `http://localhost:8000/docs` when the application is running.

## Extending the System

To extend the system:

1. Add new data object types in `app/models/models.py`.
2. Implement new transformers and register them with the `TransformerRegistry`.
3. Extend the `ObjectDataAISystem` with new processing capabilities.
4. Add new API endpoints in `app/api.py` as needed.


## Proto Buffer (gRPC)
 
To use this proto file:

1. Save it as `object_data_ai.proto` in your project directory.
2. Use the protobuf compiler (`protoc`) to generate the necessary code for your chosen programming language.
3. Implement the service defined in the proto file in your backend.
4. Use the generated client code to interact with your service from other parts of your application or from separate client applications.

For Python, you might generate the code like this:

```bash
protoc -I=. --python_out=. --grpc_python_out=. object_data_ai.proto
```

This will generate `object_data_ai_pb2.py` (containing message classes) and `object_data_ai_pb2_grpc.py` (containing service classes).

Remember to install the necessary gRPC and protobuf libraries in your Python environment:

```bash
pip install grpcio grpcio-tools
```

## Contributing

Contributions to the Object Data AI System are welcome. Please ensure that your code adheres to the project's coding standards and include appropriate tests for new features.

## License