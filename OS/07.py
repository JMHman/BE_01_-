from multiprocessing import Process
import os
import time

def coke():
  print('콜라 프로세스 아이디는 :', os.getpid())
  print('부모 프로세스 아이디는 :', os.getppid())
def cider():
  print('사이다 프로세스 아이디는 :', os.getpid())
  print('부모 프로세스 아이디는 :', os.getppid())
def juice():
  print('주스 프로세스 아이디는 :', os.getpid())
  print('부모 프로세스 아이디는 :', os.getppid())


if __name__ == '__main__':
  print('07.py 프로세스 아이디 :', os.getpid())
  child1 = Process(target=coke).start()
  child2 = Process(target=cider).start()
  child3 = Process(target=juice).start()