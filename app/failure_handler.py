import time


class FailureHandler:
    def __init__(self, retries: int = 3):
        self.retries = retries

    def run(self, func, *args, **kwargs):
        last_error = None

        for _ in range(self.retries):
            try:
                return func(*args, **kwargs)

            except Exception as e:
                last_error = e
                time.sleep(1)

        raise last_error