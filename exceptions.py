class StreamNotFoundException(Exception):
    """
    Exception raised when a downloadable stream is not found

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, link: str):
        self.link = link

    def __str__(self):
        return f"StreamNotFoundException: Could not find a suitable stream to download from the link '{self.link}'"
