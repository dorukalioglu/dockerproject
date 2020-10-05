FROM arm32v7/python:3-buster
COPY main.py ./
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install python3-pip -y
RUN apt-get install -y apt-utils
RUN pip3 install --user python-dev-tools
RUN pip3 install --no-cache-dir OrangePi.GPIO
CMD ["python3", "main.py"]