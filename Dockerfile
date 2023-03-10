FROM python:3.11

WORKDIR /app

RUN apt update
RUN apt install -y git
RUN apt install -y libsasl2-dev python3-dev libldap2-dev libssl-dev

# install openjdk-11
RUN apt install -y openjdk-11-jdk-headless

# install jpype and other python packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# install R
RUN apt install -y r-base 

# install R and rjava and java sdk
RUN apt install -y r-base r-cran-rjava
RUN Rscript install_rjava.r

