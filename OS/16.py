from multiprocessing import Process, Value, Lock
import threading

def counter1(snum, cut, lock):
  lock.acquire()
  try:
    for i in range(cut):
      snum.value += 1
  finally:
    lock.release()

def counter2(snum, cut, lock):
  lock.acquire()
  try:
    for i in range(cut):
      snum.value -= 1
  finally:
    lock.release()

if __name__ == "__main__":

  lock = Lock()
  shared_number = Value('i', 0)
  t1 = threading.Thread(target=counter1, args=(shared_number, 5000, lock))
  t1.start()

  t2 = threading.Thread(target=counter2, args=(shared_number, 5000, lock))
  t2.start()

  t1.join()
  t2.join()

  print("finally,number is",shared_number.value)