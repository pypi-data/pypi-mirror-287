from .models import ConcreteDataObjectFactory, TransformerRegistry, InMemoryDataLake, ObjectDataAISystem
from .app import create_app
from .api import router as api_router

# Initialize your system components
data_object_factory = ConcreteDataObjectFactory()
transformer_registry = TransformerRegistry()
data_lake = InMemoryDataLake()
system = ObjectDataAISystem(data_object_factory, transformer_registry, data_lake)

# Create the FastAPI app
app = create_app()
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)