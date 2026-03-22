from fastapi import APIRouter

router = APIRouter(prefix="/tasks")

tasks = []

@router.get("/")
def get_tasks():
    return tasks

@router.post("/")
def create_task(task: dict):
    tasks.append(task)
    return {"message": "Task created"}

@router.delete("/{task_id}")
def delete_task(task_id: int):
    if task_id < len(tasks):
        tasks.pop(task_id)
        return {"message": "Deleted"}
    return {"error": "Not found"}