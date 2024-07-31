class ScenarioError(Exception):
    def __init__(self, message: str, request: str = "") -> None:
        self.request = request
        super().__init__(message)
