# Notification Service

A simple python notification service for sending messages to your Rocket.Chat server.

## Installation

```bash
pip install python-rocketchat-sender
```
## Usage

```python
from python_rocketchat_sender import Sender

Sender.send('general', 'Hello, world!')
```