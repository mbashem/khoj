class IndexResult:
    def __init__(self, text: str, depth: int, url: str, page_url: str, data_type: str):
        self.text = text
        self.depth = depth
        self.url = url
        self.page_url = page_url
        self.data_type = data_type

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, IndexResult):
            return self.text == other.text and self.depth == other.depth and self.url == other.url and self.page_url == other.page_url and self.data_type == other.data_type
        return False
      
    def __key(self):
        return (self.text, self.depth, self.url, self.page_url, self.data_type)

    def __hash__(self):
        return hash(self.__key())