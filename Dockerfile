FROM python:3.8-slim-buster AS build
ADD . /opt/
WORKDIR /opt/task/
ENTRYPOINT [“python”, “./src/main.py”]


FROM build AS testrunner
WORKDIR /opt/task/
ENTRYPOINT pytest tests