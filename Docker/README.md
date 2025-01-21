## 安裝與配置 Docker

### 確認版本

請先安裝 Docker，並確認版本：

```sh
docker --version
docker-compose --version
```

### 配置 Docker-compose

將 Docker 放入對應的應用程式資料夾中，如有需要可更改 Docker-compose 服務中的 `web` 或 `account` 的 build 路徑。

### 修改 DATABASES 配置

1. 修改 `DATABASES` 配置：

   ```python
   DATABASES = {
        'default': {
             'ENGINE': 'django.db.backends.postgresql_psycopg2',
             'NAME': "mydb",
             'USER': "test",
             'PASSWORD': "mypassword",
             'HOST': "postgres",
             'PORT': "5432"
        }
   }
   ```

### 生成 requirements.txt

2. 使用 `pipreqs` 生成 `requirements.txt`：

   ```sh
   pip install pipreqs
   pipreqs ./
   ```

   需要額外修改的部分：

   - 在 `web` 專案中註解掉 `talib`
   - 在 `accounts` 的 `requirements.txt` 中不要指定 `psycopg2-binary` 的版本

### 啟動與關閉 Docker-compose

完成後在根目錄使用：

```sh
docker-compose up
docker-compose down
```
