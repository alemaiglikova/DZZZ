import time
print("Через сколько минут?")
text = str(input())
local_time = float(input())
local_time = local_time * 60
time.sleep(local_time)
print(text)