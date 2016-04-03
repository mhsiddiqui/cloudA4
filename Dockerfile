FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /cloudA4
WORKDIR /cloudA4
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["cloudA4.py", "0.0.0.0"]
