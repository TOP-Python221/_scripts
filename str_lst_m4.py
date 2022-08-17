from pprint import pprint

s = '''root:!:0:0::/:/usr/bin/ksh
daemon:!:1:1::/etc:
bin:!:2:2::/bin:
sys:!:3:3::/usr/sys: 
adm:!:4:4::/var/adm:
uucp:!:5:5::/usr/lib/uucp: 
guest:!:100:100::/home/guest:
nobody:!:4294967294:4294967294::/:
lpd:!:9:4294967294::/:
lp:*:11:11::/var/spool/lp:/bin/false 
invscout:*:200:1::/var/adm/invscout:/usr/bin/ksh
nuucp:*:6:5:uucp login user:/var/spool/uucppublic:/usr/sbin/uucp/uucico
paul:!:201:1::/home/paul:/usr/bin/ksh
jdoe:*:202:1:John Doe:/home/jdoe:/usr/bin/ksh
'''

users = []
# узнать количество символов '\n' и повторить тело цикла столько раз
for _ in range(s.count('\n')):
    # узнать индекс первого символа '\n' в строке s
    i = s.index('\n')
    # в user_s сохраняем срез от начала строки до первого символа '\n'
    user_s, user_l = s[:i], []
    # узнать количество символов ':' и повторить тело вложенного цикла столько раз
    for _ in range(user_s.count(':')):
        # узнать индекс первого символа ':' в строке user_s
        j = user_s.index(':')
        # взять срез от начала строки до первого символа ':', составить из получившейся подстроки список с одним элементом, конкатенировать этот список со списком user_l
        user_l += [user_s[:j]]
        # переписать переменную user_s срезом от символа, следующего за первым символом ':', до конца строки user_s
        user_s = user_s[j+1:]
    # добавить к списку user_l подстроку от последнего символа ':' до конца строки
    user_l += [user_s]
    # добавить список user_l в качестве отдельного элемента (вложенный список) в конец списка users
    users.append(user_l)
    # переписать переменную s срезом от символа, следующего за первым символом '\n', до конца строки s
    s = s[i+1:]


# users = s.split('\n')
# for i in range(len(users)):
    # users[i] = users[i].split(':')


pprint(users)