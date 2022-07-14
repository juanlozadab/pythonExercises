#to get current date and time we need to use the datetime library
from datetime import datetime , timedelta
#the now function returns current date and time as a datetime object
today = datetime.now()
#timedelta is use to add or remove days, weeks to a date
one_day = timedelta(days=1)
yesterday = today - one_day
#convert to string to concat
print('yesterday was ' + str(yesterday))
current_date = datetime.now()

print('Day: ' + str(current_date.day))
print('month: ' + str(current_date.month))
print('year: ' + str(current_date.year))

birthday = input('When is your birthday (dd/mm/yyyy)?  ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('birthday: ' + str(birthday_date))