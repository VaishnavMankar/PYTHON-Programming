#raise error example 2

class Mobile:
    def __init__(self,name):
        self.name = name

class MobileStore:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self, new_mobile):
        if isinstance(new_mobile, Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError('new mobile should be object of Mobile class')


oneplus = Mobile('one plus 6')
samsung = 'samsung galaxcy s8'
mobilestore = MobileStore()
print(mobilestore.mobiles)
mobilestore.add_mobile(oneplus)
mobo_phones = mobilestore.mobiles
print(mobo_phones[0].name)



