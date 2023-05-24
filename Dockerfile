FROM python:3.8-slim-buster AS build
ADD . /opt/
WORKDIR /opt/task/
ENTRYPOINT [“python”, “./src/ParkingLot.py”]
RUN ["pip3", "install", "-r", "requirements.txt"]

FROM build AS testrunner
WORKDIR /opt/task/
ENTRYPOINT pytest tests