# Message to request library #

## Назначение ##
Отправляет текстовые сообщения http POST запросом 

## Установка ##
```
pip install message_to_request
```

## Использование ##

```python
from message_to_request import Sender, MessageType

sender = Sender(url="https://example.com/")

response = sender.send(
    text="test message",
    message_type=MessageType.ERROR,
)
```
