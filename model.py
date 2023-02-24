from datetime import datetime
import uuid


class Note:

    def __init__(self, title: str, content: str):
        self.id = str(uuid.uuid4())
        self._heading = title
        self._body = content
        self._time_stamp = datetime




