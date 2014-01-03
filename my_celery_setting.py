# coding:utf-8

# Ubuntu 下關閉 RabbitMQ Server, stop/start
# sudo invoke-rc.d rabbitmq-server stop

BACK_END='database'
CELERY_TIMEZONE='Asia/Taipei'
CELERY_ENABLE_UTC=True

# Broker 的 URL, 相當於 inline 設定的 broker 屬性。
# 參考：http://docs.celeryproject.org/en/latest/getting-started/brokers/sqlalchemy.html#broker-sqlalchemy
# MySQL
# BROKER_URL = 'sqla+mysql://root:t0036659@localhost/for_celery'
# SQLite
BROKER_URL = 'sqla+sqlite:///celerydb.sqlite'


# 用來存放結果的 URL
# 參考：http://docs.celeryproject.org/en/latest/configuration.html#conf-database-result-backend
# MySQL
# CELERY_RESULT_BACKEND = 'db+mysql://root:t0036659@localhost/for_celery'
# SQLite
# CELERY_RESULT_BACKEND = 'db+sqlite:///celerydb.sqlite'
