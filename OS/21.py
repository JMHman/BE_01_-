import tracemalloc # python 3.4 ~~

tracemalloc.start()

data = [b'%d' % num for num in range(1,10001)]
joined_data = b''.join(data)

current, peak = tracemalloc.get_traced_memory()
print(f'현재 메모리 사용량: {current / 10 ** 6} MB')
print(f'최대 메모리 사용량: {peak / 10 ** 6} MB')

tracemalloc.stop() # 시작이 있으면 끝도 있는 법/ 끝났다는 것은 다시 시작된다는 것을

trace = tracemalloc.get_tracemalloc_memory() # 트레이스말록을 사용하느라 사용한 메모리 알아보기

print(trace / 10 ** 6) # 10 ** 6 을 붙이면 MB로 나온다