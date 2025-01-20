# 使用 Ubuntu 22.04 作為基礎映像
FROM ubuntu:22.04

# 設置環境變數
ENV PYTHON_TA_LIB_VERSION "0.4.24"

# 更新並安裝必要的系統工具和依賴
RUN apt-get update && apt-get install -y \
    wget \
    build-essential \
    gcc \
    make \
    zlib1g-dev \
    libssl-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    libffi-dev \
    curl \
    xz-utils \
    tk-dev \
    && apt-get clean

# 下載並安裝 Python 3.12.8
WORKDIR /tmp
RUN wget https://www.python.org/ftp/python/3.12.8/Python-3.12.8.tgz \
    && tar -xzf Python-3.12.8.tgz \
    && cd Python-3.12.8 \
    && ./configure --enable-optimizations \
    && make -j$(nproc) \
    && make altinstall \
    && cd .. \
    && rm -rf Python-3.12.8 Python-3.12.8.tgz

# 安裝 TA-Lib 的 C 庫
RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz \
    && tar -zxf ta-lib-0.4.0-src.tar.gz \
    && cd ta-lib \
    && ./configure --prefix=/usr \
    && make \
    && make install \
    && cd .. \
    && rm -rf ta-lib ta-lib-0.4.0-src.tar.gz

# 安裝 Python 的必要工具和 TA-Lib 套件
RUN python3.12 -m ensurepip --upgrade \
    && python3.12 -m pip install --no-cache-dir --upgrade pip setuptools numpy \
    && python3.12 -m pip install --no-cache-dir ta-lib==${PYTHON_TA_LIB_VERSION}

# 設置工作目錄並將本地檔案複製到容器內
WORKDIR /app
COPY . /app

# 設定默認執行指令
CMD ["python", "test.py"]
