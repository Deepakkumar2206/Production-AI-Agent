from dataclasses import dataclass


@dataclass
class CaseFacts:
    customer_name: str = ""
    todo_id: str = ""
    todo_title: str = ""
    completed: bool = False

    def update(self, todo):
        self.todo_id = todo.id
        self.todo_title = todo.title
        self.completed = todo.completed

    def format_case_facts(self) -> str:
        return (
            f"Todo ID: {self.todo_id}\n"
            f"Title: {self.todo_title}\n"
            f"Completed: {self.completed}"
        )