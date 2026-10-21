from typing import TypedDict,Literal
TaskStatus = Literal["todo","doing","done"]
TaskPriority = Literal[1,2,3]
class TaskDict(TypedDict):
    id:int
    title:str
    status:TaskStatus
    priority:TaskPriority
    tags:list[str]
    due_date:str | None

def create_task(
    title:str,
    priority:TaskPriority = 2,
) -> TaskDict:
    return{
        "id":1,
        "title":title,
        "status":"todo",
        "priority":priority,
        "tags":[],
        "due_date":None,
    }
create_task("学习类型系统",priority=3)
