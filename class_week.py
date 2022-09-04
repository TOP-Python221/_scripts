from datetime import datetime as dt, timedelta as td

class Week(dict):
    def __init__(self):
        super().__init__()
        day_of_week = dt.now().isoweekday()
        self['Понедельник'] = (dt.now() - td(days=day_of_week-1)).day
        self['Вторник'] = (dt.now() - td(days=day_of_week-2)).day
        self['Среда'] = (dt.now() - td(days=day_of_week-3)).day
        self['Четверг'] = (dt.now() - td(days=day_of_week-4)).day
        self['Пятница'] = (dt.now() - td(days=day_of_week-5)).day
        self['Суббота'] = (dt.now() - td(days=day_of_week-6)).day
        self['Воскресение'] = (dt.now() - td(days=day_of_week-7)).day

    def __str__(self):
        line1 = 'Пн Вт Ср Чт Пт Сб Вс'
        line2 = ' '.join(f'{day:>2}' for day in self.values())
        return f'{line1}\n{line2}'


current_week = Week()
print(current_week)
