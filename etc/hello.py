import multiprocessing
bind = "0.0.0.0:8080"
pythonpath = '/home/box/web'
workers = multiprocessing.cpu_count() * 2 + 1
