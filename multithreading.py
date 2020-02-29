import time 
import threading 
import queue 
import urllib.request as urllib 

class Consumer(threading.Thread): 
  def __init__(self, queue_1): 
    threading.Thread.__init__(self)
    self._queue = queue_1 

  def run(self):
    while True: 
      content = self._queue.get() 
      if isinstance(content, str) and content == 'quit':
        break
      response = urllib.urlopen(content)
    print ('Thanks!')


def Producer():
  urls = [
    'https://www.python.org', 'https://www.yahoo.com'
    'https://www.scala.org', 'https://www.google.com'
    # etc.. 
  ]
  queue_1 = queue.Queue()
  worker_threads = build_worker_pool(queue_1, 4)
  start_time = time.time()

  # Add the urls to process
  for url in urls: 
    queue_1.put(url)  
  # Add the poison pill
  for worker in worker_threads:
    queue_1.put('quit')
  for worker in worker_threads:
    worker.join()

  print ('Done! Time taken: {}'.format(time.time() - start_time))

def build_worker_pool(queue, size):
  workers = []
  for _ in range(size):
    worker = Consumer(queue)
    worker.start() 
    workers.append(worker)
  return workers

if __name__ == '__main__':
  Producer()