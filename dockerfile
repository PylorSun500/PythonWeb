FROM python:3.14-slim-bookworm

# 系统工具包（Flask 开发无需 C 编译依赖，仅保留调试工具）
RUN apt-get update && apt install -y --no-install-recommends \
    git vim \
    netcat-openbsd dnsutils iproute2 \
    neofetch \
    # MySQL 客户端工具（容器内调试用：mysql -h mysql -u dev -p）
    default-mysql-client \
    && rm -rf /var/lib/apt/lists/*

# 工作目录
WORKDIR /workspace

# Python 依赖 — 先装 Flask 全家桶，再装开发工具
RUN pip install --no-cache-dir \
    flask flask-cors flask-sqlalchemy flask-wtf \
    pymysql requests \
    numpy \
    pytest black flake8

# Flask 开发常用端口
EXPOSE 5000 5001

# 默认进入交互式 Shell（docker-compose 可覆盖）
CMD ["/bin/bash"]