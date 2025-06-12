import os
from fluent import sender

logger = sender.FluentSender('hello_app', host=os.getenv("FLUENTD_HOST"), port=int(os.getenv("FLUENTD_PORT", 24224)))

def logevent(message):
    data = {
        'message': message
    }
    logger.emit('event', data)