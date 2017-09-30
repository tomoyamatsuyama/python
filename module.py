import user

#from user import AdiminUser, User //AdiminUserとUserだけ取得

izumi = user.AdiminUser("Izumi", 20) #モジュール名忘れない

print(izumi.name)

izumi.say_hi()

izumi.say_hello()
