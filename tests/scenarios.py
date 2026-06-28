from app.ai_agent import AIAgent
from app.models.todo import Todo


def run_scenarios():

    agent = AIAgent()

    scenarios = [

        # Scenario 1 - Normal Pending Todo
        Todo(
            id="1",
            title="Learn Claude Code",
            completed=False
        ),

        # Scenario 2 - Completed Todo
        Todo(
            id="2",
            title="Build AI Todo Assistant",
            completed=True
        ),

        # Scenario 3 - AI Planning
        Todo(
            id="3",
            title="Design Multi-Agent Workflow",
            completed=False
        ),

        # Scenario 4 - Context Management
        Todo(
            id="4",
            title="Fix Lost Context Issue",
            completed=False
        ),

        # Scenario 5 - Provenance Check
        Todo(
            id="5",
            title="Verify Source Attribution",
            completed=True
        ),

        # Scenario 6 - Escalation Logic
        Todo(
            id="6",
            title="Review Escalation Policy",
            completed=False
        ),

        # Scenario 7 - Failure Recovery
        Todo(
            id="7",
            title="Handle Agent Failure Gracefully",
            completed=False
        ),

        # Scenario 8 - Final Production Validation
        Todo(
            id="8",
            title="Production Reliability Validation",
            completed=True
        ),

    ]

    print("=" * 50)
    print("Running Stage 5 Production Scenarios")
    print("=" * 50)

    for todo in scenarios:

        result = agent.process(todo)

        print("\n" + "=" * 50)
        print(f"Scenario : {todo.id}")
        print(f"Title    : {todo.title}")
        print(f"Done     : {todo.completed}")
        print("-" * 50)
        print(result)

    print("\n" + "=" * 50)
    print("All 8 production scenarios completed successfully.")
    print("=" * 50)


if __name__ == "__main__":
    run_scenarios()