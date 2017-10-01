#import mypackage.user
import mypackage.user as mymodule #packageからの名前を作成


#from user import AdiminUser, User //AdiminUserとUserだけ取得
#from mypackage.user import AdiminUser, User //AdiminUserとUserだけ取得

izumi = mymodule.AdminUser("Izumi", 20) #モジュール名忘れない

print(izumi.name)

izumi.say_hi()

izumi.say_hello()
