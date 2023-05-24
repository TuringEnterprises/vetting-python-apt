FROM python:3.8-slim-buster AS build
ADD . /opt/
WORKDIR /opt/tasks/
ENTRYPOINT [“python”, “./src/main.py”]


FROM build AS testrunner
WORKDIR /opt/tasks/
ENTRYPOINT pytest tests