FROM hleong25/mjpeg-streamer as builder-mjpeg-streamer

FROM python:3.9-slim-bullseye

RUN apt update
RUN apt install -y libjpeg-dev

COPY --from=builder-mjpeg-streamer /mjpg-streamer_*.deb /
RUN dpkg -i /mjpg-streamer_*.deb

# setup the working directory
WORKDIR /code

# install python dependents
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy over app code
COPY ./app /code/app

# run the service
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
