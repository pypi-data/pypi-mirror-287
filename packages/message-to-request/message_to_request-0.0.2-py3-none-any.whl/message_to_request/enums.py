import enum


class MessageType(str, enum.Enum):
    INFO = "info"
    ERROR = "error"
