FROM python:3.9.6-alpine3.14

# Change user
RUN adduser --disabled-password default -s /bin/sh -h /home/app

# Main application setup
WORKDIR /application

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

USER default

EXPOSE 5000

COPY ./application .

CMD ["python3", "__init__.py"]
