FROM python:3.6

ENV APP_HOME /app

WORKDIR $APP_HOME

COPY . .
RUN chmod +x docker-entrypoint.sh
RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "./docker-entrypoint.sh" ]