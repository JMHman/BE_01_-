import psutil

for proc in psutil.process_iter():
  try:
      ps_name = proc.name()
  except psutil.NoSuchProcess:
      # 프로세스가 더 이상 존재하지 않음
      continue

  if "Chrome" in ps_name :
    child = proc.children()
    print(ps_name, proc.status(), proc.parent(), child)

    if child :
      print(f'{ps_name}의 자식 프로세스', child)
      
