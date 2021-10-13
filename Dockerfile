FROM python:3.7.0

WORKDIR /home/

RUN echo "upgrade pip"

#RUN git clone https://github.com/matt700395/sandbox2.git
RUN git clone https://github.com/dk7648/CafeForYou.git

WORKDIR /home/CafeForYou/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=CafeForYou.settings.deploy && python manage.py migrate --settings=CafeForYou.settings.deploy && gunicorn CafeForYou.wsgi --env DJANGO_SETTINGS_MODULE=CafeForYou.settings.deploy --bind 0.0.0.0:8000"]

