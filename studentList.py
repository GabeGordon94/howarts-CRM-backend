from student import Student
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

STUDENTS = [
    Student(100001, 'Gabe', 'Gordon', '08/01/2020 11:04:07', '08/01/2020 11:04:07',
            {'Alchemy': '5'}, {'Healing': '3'}, ['Dating with magic']),
    Student(100002, 'Lex', 'Dubinsky', '08/01/2020 11:04:07', '08/01/2020 11:04:07',
            {'Elemental': '3'}, {'Disintegration': '5'}, ['Dating with magic']),
    Student(100003, 'Yinon', 'Vahan', '08/01/2020 11:04:07', '08/01/2020 11:04:07',
            {'Healing': '1'}, {'Conjuror': '3'}, ['Dating with magic']),
    Student(100004, 'Aaron', 'Karas', '08/01/2019 11:04:07', '08/01/2019 11:04:07',
            {'Disintegration': '5'}, {'Illusion': '3'}, ['Alchemy advanced']),
    Student(100005, 'Michael', 'Harris', '08/05/2019 11:04:07', '08/06/2019 11:04:07',
            {'Immortality': '3'}, {'Illusion': '3'}, ['Alchemy advanced'])
]
