release: python manage.py migrate
web: daphne commutify.asgi:channel_layer --port $PORT --bind 0.0.0.0 -v2
chatworker: python manage.py runworker --settings=commutify.settings -v2