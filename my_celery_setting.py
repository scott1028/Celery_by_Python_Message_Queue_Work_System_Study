# coding:utf-8

BACK_END='database'
CELERY_TIMEZONE='Asia/Taipei'
CELERY_ENABLE_UTC=True

# Broker 的 URL
# 參考：http://docs.celeryproject.org/en/latest/getting-started/brokers/sqlalchemy.html#broker-sqlalchemy
BROKER_URL = 'sqla+mysql://root:t0036659@localhost/for_celery'

# 用來存放結果的 URL
# 參考：http://docs.celeryproject.org/en/latest/configuration.html#conf-database-result-backend
CELERY_RESULT_BACKEND = 'db+mysql://root:t0036659@localhost/for_celery'
