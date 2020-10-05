FROM arm32v7/python:3-buster
ENV docker /docker
WORKDIR ${docker}
ADD . ${docker}
#RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get update 
#RUN apt-get install sudo -y
RUN apt-get upgrade -y
RUN apt-get install -y apt-utils 
RUN apt-get install python3 -y
RUN apt-get install git -y
RUN apt-get install python3-pip -y
RUN apt-get install python3-setuptools
RUN pip install wheel
RUN pip install OrangePi.GPIO
#RUN pip install pyA20
#RUN ls
#COPY deneme.py ./
#COPY led.py ./
#COPY pyA20 ./
#COPY setup.py ./
COPY blink_led.py ./
COPY hello_world.py ./
#RUN ls
#RUN python3 install setup.py
#RUN ls
#CMD ["python", "led.py"]
RUN python3 blink_led.py 
RUN python3 hello_world.py