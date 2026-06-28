class ContextManager:
    def __init__(self):
        self._context = []

    def add_context(self, text: str):
        self._context.append(text)

    def get_context(self):
        return self._context

    def clear(self):
        self._context.clear()