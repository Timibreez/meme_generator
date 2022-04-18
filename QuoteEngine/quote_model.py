class QuoteModel():
    """Creating a new quote"""

    def __init__(self, body, author) -> None:
        """Initialization"""
        self.body = body
        self.author = author

    def __repr__(self) -> str:
        """Returning a str with a 'quote body text' - author."""
        return f"{self.body} - {self.author}"
