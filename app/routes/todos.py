from flask import Blueprint

from app.errors import AppError
from app.responses import json_error, json_ok
from app.services.todo_service import get_todo

bp = Blueprint("todos", __name__)


@bp.get("/<todo_id>")
def get_todo_route(todo_id: str):
    try:
        response = get_todo(todo_id)
        return json_ok(response)

    except AppError as e:
        return json_error(
            e.code,
            e.message,
            status=e.status,
        )

    except Exception as e:
        return json_error(
            "internal_error",
            str(e),
            status=500,
        )