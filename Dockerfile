FROM python:3.13-slim

RUN apt-get update && \
  apt-get install -y htop

RUN pip3 install pipenv

ENV PROJECT_DIR /SMSNOTIFIER/sinchSMSNotifier

WORKDIR ${PROJECT_DIR}

COPY Pipfile .
COPY Pipfile.lock .

# Install dependencies
RUN pipenv install --deploy --ignore-pipfile

COPY . .

CMD ["pipenv", "run", "python", "main.py"]
