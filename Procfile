release: python manage.py migrate
web: daphne commutify.asgi:application --port $PORT --bind 0.0.0.0 -v2
chatworker: python manage.py runworker channels --settings=commutify.settings -v2
