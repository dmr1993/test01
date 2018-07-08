# _*_ coding:utf-8 _*_

# import requests
# import re

class Employee:
    employ = 0

    def setEmploy(self, employ):
       self.employ = employ

    def getEmploy(self):
        return self.employ


# start_url = 'http://'
if __name__ == '__main__':
    emp = Employee()
    emp.setEmploy(99)
    print emp.getEmploy()
