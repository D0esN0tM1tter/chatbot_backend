# defining the data models
from pydantic import BaseModel 
from typing import List 

class ChatRequest(BaseModel) : 
    prompt : str
    history : List[str] = [] 

class ChatResponse(BaseModel) : 
    response : str