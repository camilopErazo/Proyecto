FROM python:3.8
RUN apt-get update && apt-get install -y dos2unix
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN python3 -m pip install -r requirements.txt
RUN apt-get --purge remove -y dos2unix && rm -rf /var/lib/apt/lists/*
CMD ["python3", "app_faker.py"]