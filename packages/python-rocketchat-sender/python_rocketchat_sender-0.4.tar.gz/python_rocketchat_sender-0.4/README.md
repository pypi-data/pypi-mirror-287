# Notification Service

A simple python notification service for sending messages to your Rocket.Chat server.

## Installation

```bash
pip install python-rocketchat-sender
```
## Usage

Environment variables must be set before using the service.
- ROCKETCHAT_SERVER_URL
- USER_ID
- AUTH_TOKEN

```python
from python_rocketchat_sender import Sender

Sender.send('general', 'Hello, world!')
```