# coding:utf-8

# Ubuntu 下關閉 RabbitMQ Server, stop/start
# sudo invoke-rc.d rabbitmq-server stop

CELERY_TIMEZONE='Asia/Taipei'
CELERY_ENABLE_UTC=True

# Broker 的 URL, 相當於 inline 設定的 broker 屬性。
# 參考：http://docs.celeryproject.org/en/latest/getting-started/brokers/sqlalchemy.html#broker-sqlalchemy
# MySQL
# BROKER_URL = 'sqla+mysql://root:t0036659@localhost/for_celery'
# SQLite
BROKER_URL = 'sqla+sqlite:///celerydb.sqlite'	# 只有這個是必要資訊


# 用來存放結果的 URL, 如果沒設定將無法存取或調用 .get() / .result 的方法或屬性 (非必要設定)
# 參考：http://docs.celeryproject.org/en/latest/configuration.html#conf-database-result-backend
# MySQL
# CELERY_RESULT_BACKEND = 'db+mysql://root:t0036659@localhost/for_celery'
# SQLite
CELERY_RESULT_BACKEND = 'db+sqlite:///celerydb.sqlite'
