# api.py
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Dict, Any, List, Optional
from .models import ObjectDataAISystem, DataObject

router = APIRouter()

# api.py
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Dict, Any, List, Optional
from .models import ObjectDataAISystem, DataObject

router = APIRouter()

class CreateObjectRequest(BaseModel):
    data_type: str
    source: str
    content: Union[str, bytes, None]
    metadata: Optional[Dict[str, Any]] = None
    context: Optional[str] = None

class ObjectResponse(BaseModel):
    id: str
    type: str
    source: str
    content: Union[str, bytes, None]
    metadata: Dict[str, Any]
    context: Optional[str]
    transformers: Optional[List[str]]

class TransformerRequest(BaseModel):
    transformer_name: str

def get_system():
    from .main import system
    return system

@router.post("/objects/", response_model=Dict[str, str])
async def create_object(request: CreateObjectRequest, system: ObjectDataAISystem = Depends(get_system)):
    try:
        obj_id = system.create_and_store(
            request.data_type,
            source=request.source,
            content=request.content,
            metadata=request.metadata or {},
            context=request.context
        )
        return {"id": obj_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/objects/{obj_id}", response_model=ObjectResponse)
async def get_object(obj_id: str, system: ObjectDataAISystem = Depends(get_system)):
    obj = system.data_lake.retrieve(obj_id)
    if obj is None:
        raise HTTPException(status_code=404, detail="Object not found")
    return ObjectResponse(
        id=obj.id,
        type=obj.type,
        source=obj.source,
        content=obj.content,
        metadata=obj.metadata,
        context=obj.context,
        transformers=obj.transformers
    )

@router.post("/objects/{obj_id}/process", response_model=ObjectResponse)
async def process_object(obj_id: str, system: ObjectDataAISystem = Depends(get_system)):
    processed_obj = system.retrieve_and_process(obj_id)
    if processed_obj is None:
        raise HTTPException(status_code=404, detail="Object not found")
    return ObjectResponse(
        id=processed_obj.id,
        metadata=processed_obj.get_metadata(),
        content=processed_obj.load_content()
    )

@router.post("/objects/{obj_id}/transform", response_model=ObjectResponse)
async def transform_object(obj_id: str, request: TransformerRequest, system: ObjectDataAISystem = Depends(get_system)):
    transformed_obj = system.apply_transformer(obj_id, request.transformer_name)
    if transformed_obj is None:
        raise HTTPException(status_code=404, detail="Object not found")
    return ObjectResponse(
        id=transformed_obj.id,
        metadata=transformed_obj.get_metadata(),
        content=transformed_obj.load_content()
    )

@router.get("/transformers/", response_model=List[str])
async def list_transformers(system: ObjectDataAISystem = Depends(get_system)):
    return list(system.transformer_registry.transformers.keys())

@router.post("/transformers/", response_model=Dict[str, str])
async def register_transformer(
    name: str,
    function: str,
    system: ObjectDataAISystem = Depends(get_system)
):
    try:
        # Note: Evaluating functions from strings is unsafe in a real-world scenario
        # This is just for demonstration purposes
        transformer_func = eval(function)
        system.transformer_registry.register(name, transformer_func)
        return {"message": f"Transformer '{name}' registered successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))