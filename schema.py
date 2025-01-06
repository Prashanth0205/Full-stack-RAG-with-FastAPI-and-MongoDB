'''
All data model are defined in this library 
'''

from typing import List, Dict, Optional
from pydantic import BaseModel


# Models 
class Message(BaseModel):
    message: str    

class SessionData(BaseModel):
    session_id: str
    messages: List[str]

class SummaryRequest(BaseModel):
    session_id: str
    # contexts: List[str]
    message_history: List[str]

class SaveRequest(BaseModel):
    session_id: str
    summary: str

