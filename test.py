# coding: utf-8
import urllib
import random
import json


def getComcode(num):
    url = 'http://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text='
    url = url + num
    return url


def getInfor(comp, num):
    url = 'http://www.kuaidi100.com/query?type=' \
          + comp \
          + '&postid=' \
          + num + '&temp=' \
          + str(random.random())
    return url


if __name__ == '__main__':
    print "hello"
    num = '498486281838'
    url = getComcode('498486281838')
    print url
    response = urllib.urlopen(url)
    resCompCode = response.read()
    resClass = json.loads(resCompCode)
    re = (resClass['auto'])
    print re[0]['comCode']
    strCom = re[0]['comCode']
    resInfo = getInfor(strCom, num)
    res = urllib.urlopen(resInfo)
    res = res.read()
    resClass = json.loads(res)
    lis = resClass['data']
    for item in lis:
        print item['context'] + '; time:' + item['ftime']
    print resClass


