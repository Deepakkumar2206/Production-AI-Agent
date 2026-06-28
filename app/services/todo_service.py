from app.ai_agent import AIAgent
from app.errors import AppError
from app.models.todo import Todo


def get_todo(todo_id: str):

    if not todo_id:
        raise AppError(
            "invalid_todo_id",
            "Todo id is required",
            status=400,
        )

    if todo_id != "1":
        raise AppError(
            "todo_not_found",
            f"Todo {todo_id} not found",
            status=404,
        )

    todo = Todo(
        id="1",
        title="Learn Claude Code",
        completed=False,
    )

    agent = AIAgent()

    return agent.process(todo)