#-*- coding:utf-8 -*-
from Tkinter import *
import urllib, urllib2, sys
import json


# def weather():
#     city = entry.get()
#     print(city)

if __name__ == '__main__':
    # print "hello"
    # root = Tk()
    # root.title("hello")
    # root.geometry("400x500")
    # lable = Label(root, text="hello")
    # lable.grid(row=0, column=0)
    # entry = Entry(root, font=(None, 20))
    # entry.grid(row=0, column=1)
    # lis = Listbox(root, font=(None, 15), width=120, height=10)
    # lis.grid(row=2, column=0)
    # #
    # # button = Button(root, text='search', width=10, command = weather)
    # # button.grid(row=3, column=0, sticky=E)
    # # button1 = Button(root, text='quit', width=10, commond=root.quit())
    # # button1.grid(row=3, column=1, sticky=W)
    # root.mainloop()
    host = 'http://jisutqybmf.market.alicloudapi.com'
    path = '/weather/query'
    method = 'GET'
    appcode = '4b2e883476ab4c4fb890b714fefd4bb8'
    querys = 'city=福州' \
             +'&citycode=citycode&cityid=cityid&ip=ip&location=location'
    bodys = {}
    url = host + path + '?' + querys
    print url

    request = urllib2.Request(url)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    response = urllib2.urlopen(request)
    content = response.read()
    if (content):
        print(content)
