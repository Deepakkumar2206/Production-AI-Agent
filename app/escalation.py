class Escalation:

    def __init__(self):
        self.reason = None

    def check(self, confidence_score: float) -> bool:
        if confidence_score < 0.80:
            self.reason = "Low confidence"
            return True

        return False

    def build_handoff_summary(self, todo):
        return {
            "escalate": True,
            "reason": self.reason,
            "summary": {
                "todo_id": todo.id,
                "title": todo.title,
                "completed": todo.completed,
            },
        }