from datetime import datetime, timezone, timedelta;
datetime.now(); #2023-09-05 05:21:14.527091 .now() is naive, local time of machine
datetime.now(timezone.utc); #2023-09-05 09:22:44.864679+00:00 actual time based on location

today = datetime.now(timezone.utc); #2023-09-05 09:59:37.503054+00:00
tomorrow = today + timedelta(days=1); #2023-09-06 09:59:37.503054+00:00 Tomorrow
today.strftime('%d-%m-%Y %H:%M:%S'); #05-09-2023 10:01

user_date = input('Enter the date in YYYY-mm-dd format: ');
user_date = datetime.strptime(user_date, '%Y-%m-%d') #input -> 2023-09-05 -> returns 2023-09-05 00:00:00