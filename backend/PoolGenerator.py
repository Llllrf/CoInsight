import multiprocessing as mp

pool = None

def init_pool():
    global pool
    pool = mp.Pool(mp.cpu_count())


    