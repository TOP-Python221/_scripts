from datetime import date, time, datetime as dt

date1 = date(year=2022, 
             month=6, 
             day=19)
date_today = date.today()
print(type(date1))
print(f"{date1!r}\t{date1!s}")
print(f"{date_today!r}\t{date_today!s}\n")

td1 = date_today - date1
print(type(td1))
print(f"{td1!r}\t{td1!s}\n")

dt1 = dt(year=2022,
         month=6,
         day=19,
         hour=10,
         minute=0)
dt2 = dt(year=2022,
         month=6,
         day=19,
         hour=13,
         minute=0)
print(type(dt1))
print(f"{dt1!r}\t{dt1!s}")
print(f"{dt2!r}\t{dt2!s}\n")

td2 = dt2 - dt1
print(type(td2))
print(f"{td2!r}\t{td2!s}\n")


print(f"{dt1.strftime('%d.%m.%y %H:%M') = }")
print(f"{dt2.strftime('%d %b %y %H:%M') = }\n")
