# MAMO
This is a framework for multi-agent collaboration to complete molecular optimization.

## 🚀 快速开始
| 方式 | 步骤 |
|---|---|
| **Docker（推荐）** | 1. 克隆仓库<br>`git clone https://github.com/langgenius/dify.git`<br>2. 进入目录<br>`cd dify/docker`<br>3. 一键启动<br>`docker compose up -d`<br>4. 访问 http://localhost/install 完成初始化 |
| **本地源码** | 1. 安装 Poetry（Python 3.10+）<br>`pip install poetry`<br>2. 安装依赖<br>`poetry install`<br>3. 复制环境变量<br>`cp .env.example .env` 并修改<br>4. 初始化数据库<br>`poetry run flask db upgrade`<br>5. 启动服务<br>`poetry run flask run --host 0.0.0.0 --port 5001` |

> 安装完成后，浏览器打开 http://localhost 即可进入 Dify 控制台。
