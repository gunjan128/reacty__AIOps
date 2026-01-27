# TypedDict ---> It will fix the structure of our dictionary 
# Annotated ---> It will attach extra behaviour . 
# add_messages ----> It will tell the langgraph like how messages will merge . 
# operator.add --> It will add or merge the list . 
# dataclass ---> It will create Lightweight class . 

from __future__ import annotations 
from dataclasses import dataclass, field 
from typing import TypedDict 
from langgraph.graph import add_messages 
from typing_extensions import Annotated 

import operator 

class OverallState(TypedDict):
    messages: Annotated[list,add_messages] 
    search_query: Annotated[list,operator.add] 
    web_research_result: Annotated[list, operator.add] 
    sources_gathered: Annotated[list, operator.add] 
    initial_search_query_count: int 
    max_research_loops: int 
    reasoing_model: str 