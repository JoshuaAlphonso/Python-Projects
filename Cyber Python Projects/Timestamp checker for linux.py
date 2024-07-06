import datetime

timestamp = 15651
epoch = datetime.datetime.utcfromtimestamp(0)
last_password_change_date = epoch + datetime.timedelta(days=timestamp)
print(last_password_change_date)
