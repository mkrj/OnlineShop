这是一个基于Django2.2的前后端分离的商城项目。

[TOC]

## 功能特点(TODO)
- 支持使用 docker 进行本地开发、部署
- 实现基于 xadmin 的后台管理系统
- 支持使用微信第三方登录
- 支持微信支付
- 同步更新的接口说明文档

## 本地开发环境搭建 (DEV)

安装 docker-desktop (步骤略过，根据官方文档安装), 然后 cd 至项目根目录下

### 启动基础服务
运行命令 `docker-compose up -d`

### 构建镜像
运行命令 `docker build -t python:3.7-pipenv ./docker/dev`

作用是根据 dev 文件夹下的 Dockerfile 在本地构建一个 python:3.7-pipenv 的 image

### 设置快捷短语
通过在 bash 的配置文件中设置快捷短语，可以省却每次调试时都要重复写的长长的命令了。
步骤如下：

- 编辑 .bash_aliases文件 

`vim ~/.bash_aliases`

- 设置快捷短语 

```
alias py37='docker run --rm -v "$PWD":/usr/src/myapp -p 8000:8000 --network onlineshop_default -w /usr/src/myapp -e PIPENV_VENV_IN_PROJECT=true python:3.7-pipenv'`
```
- 保存之后 source 

`source .bash_aliases`

### 用法示例
#### 在本地启动项目
##### 初次运行
**记得要创建相应数据库**
```
docker-compose up -d
py37 pipenv install
py37 pipenv run python manage.py migrate
py37 pipenv run python manage.py runserver 0.0.0.0:8000
```
##### 非初次运行
```
docker-compose up -d
py37 pipenv run python manage.py runserver 0.0.0.0:8000
```

### QA
#### 如何通过 docker 创建 superuser?
- 启动项目后, 运行命令 
```
docker exec -it your_project_containerID pipenv run python manage.py createsuperuser
``` 

- 进入到交互式操作环境中，输入 user, mail, password，就创建成功了

#### 如何查看项目的容器 ID？
运行命令 `docker ps`，显示全部正在运行的容器
