import time

# 获取系统当地时间
localT = time.localtime(time.time())
print('现在本地时间为：', localT)

# 获取格式化时间
formatT = time.asctime(time.localtime(time.time()))
print('本地格式化时间为：', formatT)

# 获取格式化日期
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 格式2000-01-01 11:11:11
print(time.strftime("%Y %a %b %d %H:%M:%S", time.localtime()))  # 格式2000 Sat Mar 11 11:11:11
print(time.time())  #输出时间戳


