FROM python:3
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive git clone https://github.com/robertcsapo/cisco-dnac-ipam-smartsheet.git
WORKDIR /cisco-dnac-ipam-smartsheet/
RUN DEBIAN_FRONTEND=noninteractive pip install -r requirements.txt
VOLUME /cisco-dnac-ipam-smartsheet/
ENTRYPOINT [ "python", "./run.py" ]
