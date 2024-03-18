# 내 파이썬 프로그램의 이름을 알아보자
import psutil
from multiprocessing import Process
import os

pid = os.getpid()
print("프로세스 아이디 :",pid)
pyprocess = psutil.Process(pid)
# psutil.Process() - 특정 프로세스를 가져올때 사용
# psutil.Process_iter() - 모든 프로세스를 가져올때 사용 / 반복문으로 사용
print("프로세스 정보들 :",pyprocess)
pyname = pyprocess.name()
print("프로세스 이름 :",pyname)

# 함수로 만들어서 걸과를 받을게 아니기 때문에 필요 없음
# if __name__ == "__main__":
  # pid = os.getpid()
  # print(pid)