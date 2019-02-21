FROM python:3
RUN apt-get update
RUN apt-get install -y vim
RUN git clone https://github.com/robertcsapo/cisco-dnac-ipam-smartsheet.git
WORKDIR /cisco-dnac-ipam-smartsheet/
RUN pip install -r requirements.txt
VOLUME /cisco-dnac-ipam-smartsheet/
CMD [ "python", "./run.py" ]
