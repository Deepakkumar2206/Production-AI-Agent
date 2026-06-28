class Provenance:
    def __init__(self):
        self._sources = []

    def add_source(self, source: str):
        self._sources.append(source)

    def get_sources(self):
        return self._sources

    def clear(self):
        self._sources.clear()