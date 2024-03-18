from multiprocessing import Process
import os
import time

def func():
  print('안녕, 나는 실험용으로 만들어본 함수야!')
  print('나의 프로세스 아이디는 :', os.getpid())
  print('나의 부모 프로세스 아이디는 :', os.getppid())


if __name__ == '__main__':
  print('06.py 프로세스 아이디 :', os.getpid())
  child1 = Process(target=func).start()
  child2 = Process(target=func).start()
  child3 = Process(target=func).start()
  child4 = Process(target=func).start()