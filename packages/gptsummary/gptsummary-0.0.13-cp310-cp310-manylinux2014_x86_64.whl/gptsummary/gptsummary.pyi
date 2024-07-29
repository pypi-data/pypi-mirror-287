# AISummary.pyi
class AISummary:
    base_url: str
    api_key: str
    model_id: str
    def __init__(self, base_url: str, api_key: str, model_id: str = "") -> None: ...

    def extract(self, content: str, prompt: str, length: int = 200) -> dict: ...

    def refined_title(self, content, prompt="", length=200) -> dict: ...
