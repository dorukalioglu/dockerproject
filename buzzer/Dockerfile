FROM arm32v7/python:3-buster
RUN apt-get update 
RUN apt-get upgrade -y
RUN apt-get install -y apt-utils 
RUN apt-get install python3 -y
RUN apt-get install git -y
RUN apt-get install python3-pip -y
RUN apt-get install python3-setuptools
RUN pip install wheel
RUN pip install OrangePi.GPIO
COPY buzzer.py /
RUN python3 hello_world.py