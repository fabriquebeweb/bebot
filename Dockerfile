FROM python:3.8-buster
EXPOSE 80
RUN apt update
RUN apt install -y apt-utils curl git gnupg nano software-properties-common unzip zsh

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-key C99B11DEB97541F0
RUN apt-add-repository https://cli.github.com/packages
RUN apt update
RUN apt install -y gh

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

RUN git clone -b docker --single-branch https://github.com/fabriquebeweb/bebot.git ~/tmp
RUN for file in ~/tmp/.*; do mv $file ~; done
RUN rm -Rf ~/tmp
RUN chsh -s /bin/zsh

RUN git clone https://github.com/fabriquebeweb/bebot /root/bebot
WORKDIR /root/bebot