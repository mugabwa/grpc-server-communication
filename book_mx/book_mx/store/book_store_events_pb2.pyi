from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EventRequest(_message.Message):
    __slots__ = ("event_type", "event_data", "event_id")
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    event_type: str
    event_data: str
    event_id: str
    def __init__(self, event_type: _Optional[str] = ..., event_data: _Optional[str] = ..., event_id: _Optional[str] = ...) -> None: ...

class EventResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...
