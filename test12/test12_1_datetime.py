from datetime import datetime, timedelta, timezone

now = datetime.now()
print(now, type(now))  # 当前时间

d = datetime(2016, now.month, now.day, now.hour, now.minute, now.second)
timestamp = d.timestamp()
print(timestamp)

print(datetime.fromtimestamp(timestamp))  # timestamp转datetime
print(datetime.utcfromtimestamp(timestamp))  # 转为utc的时间

strptime = datetime.strptime('2016-11-08 21:07:08', '%Y-%m-%d %H:%M:%S')
print(strptime, type(strptime))

print(strptime.strftime('%Y.%m.%d %H:%M---%a'))

print(strptime + timedelta(days=1))
print(strptime + timedelta(hours=3))
print(strptime + timedelta(days=1, hours=3))
print(strptime - timedelta(days=1, hours=3))

# 转换为utc时间
t = timezone(timedelta(hours=8))
now = datetime.now()
print(now)
utc_dt = now.replace(tzinfo=t)  # 直接设置时区
print(utc_dt)

utc_time = datetime.utcnow().replace(tzinfo=timezone.utc)
astimezone_bj = utc_time.astimezone(timezone(timedelta(hours=8)))  # 北京时间
astimezone_dj = utc_time.astimezone(timezone(timedelta(hours=9)))  # 东京时间
astimezone_bj2dj = astimezone_bj.astimezone(timezone(timedelta(hours=9)))  # 北京时间转东京时区时间
print(astimezone_bj)
print(astimezone_dj)
print(astimezone_bj2dj)
