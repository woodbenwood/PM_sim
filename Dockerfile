FROM amazonlinux
#don't have to use amazonlinux but good when deploying to amazon

ENV PYTHONUNBUFFERED=1
#won't cache print commands, dumps it out rn, makes it run better

RUN yum update -y
# -y talks to yum to say Yes to all q's... we won't have an interface to answer y/n
RUN yum upgrade -y
#if you don't update first, you won't upgrade the most recent versions of stuff
RUN yum groupinstall "Development Tools" -y
##only ^^ req vv if we need the compilers (which we need for Fortuna)
RUN yum install python3-devel -y
##this ^^ only works on python 3.7 ... python dvlpmt toolkit ... need it to build python extensions
#RUN yum install which -y
## -y talks to yum so we don't need it any more
##only needed when we're using the pycharm services


#what we have in this dockerfile is contained, it can't see any outer files
#now we'd copy our app into our docker image, .env (didn't have in demo):
#COPY app app
#COPY .env .env
COPY requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip setuptools wheel
RUN python3 -m pip install --upgrade -r requirements.txt --no-cache-dir
#this grabs all the requirements in that file
#
#EXPOSE 8000
#CMD gunicorn app.main:APP --bind="0.0.0.0:8000"

CMD python3
#to pull up terminal, CMD bin/bash:
#CMD bin/bash
#gives me a slightly higher abstraction, lets me pip list and look at OS in more detail
#to run python IN bin/bash, just type "python3" to get it to run in bin/bash

#for IDE Integration, Pycharm Pro can make the system recognize you're using a Dockerfile,
#otherwise it's going to think we're using the Interpreter ----------------------------------- down there ----------------> v