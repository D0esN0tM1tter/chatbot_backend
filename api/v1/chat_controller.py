from fastapi import APIRouter 
from app.models.chat_schema import ChatRequest, ChatResponse 
from app.services.llm_service import LLMService 

router = APIRouter() 

# instanciate the LLMService : 
llm = LLMService()

@router.post("/chat" , response_model=ChatResponse) 
async def chat(request : ChatRequest) : 

    response = llm.generate(message=request.prompt)
    
    return {"response" : response}