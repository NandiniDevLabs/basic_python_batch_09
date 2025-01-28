# This is an example class

class Person:
    print("Person class")
    def __init__(self,name,age,mobile,aadhar):
        print("This is Person initializer")
        self.name = name
        self.age = age
        self.mobile = mobile
        self.aadhar = aadhar
    
    def update_mobile(self,mobile_num):
        print("Person class: update_mobile function")
        self.mobile = mobile_num

    def get_person_attributes(self):
        print("Person class: get_person_attributes function")
        return [self.name, self.age, self.mobile, self.aadhar]
#End of Person Class


