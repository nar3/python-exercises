class Checkin:
    username='fan'
    password='123456'
    def check(self,a,b):
        if a==self.username and b==self.password:
            print('Correct')
        else:
            print('Not correct')

us=input('enter username:')
pa=input('enter password:')
user=Checkin()
user.check(us,pa)