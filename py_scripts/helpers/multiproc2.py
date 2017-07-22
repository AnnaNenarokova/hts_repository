#!/usr/bin/python
from multiprocessing import Pool

def foo(file):
  #do something

THREADS_COUNT = 32
pool = Pool(threads_count)
files = [file_1, file_2, file_3]

for _ in tqdm(pool.imap(foo, files), total=len(files)):
  pass
