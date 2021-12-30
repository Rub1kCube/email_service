import multiprocessing

from settings import settings

bind = f'{settings.HOST}:{settings.PORT}'
workers = settings.WORKERS or multiprocessing.cpu_count() * 2 + 1
accesslog = settings.ACCESS_LOG or '-'
errorlog = settings.ERROR_LOG or '-'
worker_class = 'uvicorn.workers.UvicornWorker'
