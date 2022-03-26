FROM python:3.9-alpine

# install nmap
RUN apk update

# setup the working directory
WORKDIR /code

# install python dependents
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy over app code
COPY ./app /code/app

# run the service
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
