release: python twitterdisplay/manage.py migrate
web: gunicorn twitterdisplay.wsgi:application --log-file - --log-level debug
python twitterdisplay/manage.py collectstatic --noinput
twitterdisplay/manage.py migrate
