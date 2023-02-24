import uuid
from datetime import datetime


class Note:

    def __init__(self, title: str, content: str):
        self._id = str(uuid.uuid4())
        self._title = title
        self._content = content
        self._time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def to_dict(self):
        return {
            'id': self._id,
            'title': self._title,
            'content': self._content,
            'time_stamp': self._time_stamp
        }





