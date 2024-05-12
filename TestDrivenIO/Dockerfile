# pull official base image
FROM python:3.11.2-slim-buster

# set working directory
WORKDIR /usr/src/TestDrivenIO

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# updated
# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# # new
# # copy entrypoint.sh
# COPY ./entrypoint.sh /usr/src/TestDrivenIO/entrypoint.sh
# RUN chmod +x /usr/src/TestDrivenIO/entrypoint.sh

# # add app
# COPY . .

# # new
# # run entrypoint.sh
# ENTRYPOINT ["/usr/src/TestDrivenIO/entrypoint.sh"]
