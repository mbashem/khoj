class IndexResult:
    def __init__(self, text: str, depth: int, url: str, page_url: str, data_type: str):
        self.text = text
        self.depth = depth
        self.url = url
        self.page_url = page_url
        self.data_type = data_type
