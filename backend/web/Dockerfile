# 建立 python 3.9环境
FROM python:3.9
 
 
# 安装netcat
RUN apt-get update && apt install -y netcat
 
 
# 镜像作者大江狗
MAINTAINER DJG
 
 
# 设置 python 环境变量
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
 
 
# 可选：设置镜像源为国内
COPY pip.conf /root/.pip/pip.conf
 
 
# 容器内创建 meiduo_mall 文件夹
ENV APP_HOME=/var/www/html/meiduo_mall
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME
 
 
# 将上下文的项目根目录meiduo_mall加入到容器的工作目录中（. 表示当前目录）
ADD ./meiduo_mall  $APP_HOME

 
# 更新pip版本
RUN /usr/local/bin/python -m pip install --upgrade pip
 
 
# 安装项目依赖

RUN pip install -r docs/requirements

# 安装ＦＤＦＳ客户端，因为不能直接pip install 有ｂｕｇ，所以单独安装（fdfs_client-py-master.zip已经放在根目录中了）

RUN pip install fdfs_client-py-master.zip
 
# 移除\r in windows
RUN sed -i 's/\r//' docs/start.sh
 
 
# 给start.sh可执行权限
RUN chmod +x docs/start.sh
 
RUN apt-get install tcl tk expect -y 
# 数据迁移，并使用uwsgi启动服务
ENTRYPOINT /bin/bash docs/start.sh
