FROM python:3.7

RUN python -m pip install --upgrade pip\
&& pip config set global.index-url http://mirrors.aliyun.com/pypi/simple\
&& pip config set install.trusted-host mirrors.aliyun.com\
&& pip install pipenv
