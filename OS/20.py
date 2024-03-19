import psutil
import os

print("메모리 사용량 초회하기")

memory_dict = dict(psutil.virtual_memory()._asdict())
print(memory_dict)

total = memory_dict['total']
available = memory_dict['available']
percent = memory_dict['percent']

print(f"총 사용량 : {total}")
print(f"사용 가능량 : {available}")
print(f"사용률 : {percent} %")

pid = os.getpid()
current_process = psutil.Process(pid)

kb = current_process.memory_info()[0] / 2 ** 20
print(f"Memory  사용량 : {kb:.2f}") # .2f 는 소수점 2자리 까지 출력하라는 뜻
