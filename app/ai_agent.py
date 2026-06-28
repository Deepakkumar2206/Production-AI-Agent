from app.provenance import Provenance
from app.context_manager import ContextManager
from app.confidence import ConfidenceChecker
from app.action_checker import ActionChecker
from app.failure_handler import FailureHandler
from app.case_facts import CaseFacts
from app.escalation import Escalation


class AIAgent:

    def __init__(self):
        self.context = ContextManager()
        self.provenance = Provenance()
        self.confidence = ConfidenceChecker()
        self.action = ActionChecker()
        self.failure = FailureHandler()
        self.case_facts = CaseFacts()
        self.escalation = Escalation()

    def process(self, todo):

        # Store current case information
        self.case_facts.update(todo)

        # Record context
        self.context.add_context(f"Retrieved Todo {todo.id}")

        # Record source
        self.provenance.add_source("TodoService")

        # Confidence evaluation
        confidence = self.confidence.evaluate()

        # Action validation
        action = self.action.check("retrieve_todo")

        # Escalation check
        escalate = self.escalation.check(confidence["score"])

        response = {
            "todo": {
                "id": todo.id,
                "title": todo.title,
                "completed": todo.completed,
            },
            "case_facts": self.case_facts.format_case_facts(),
            "context": self.context.get_context(),
            "sources": self.provenance.get_sources(),
            "confidence": confidence,
            "action": action,
            "escalate": escalate,
        }

        if escalate:
            response["handoff"] = self.escalation.build_handoff_summary(todo)

        return response