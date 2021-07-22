FROM python:3.9-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./

# copy entrypoint.sh
COPY entrypoint.sh ./

# install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]