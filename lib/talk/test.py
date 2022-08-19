import requests
while True:
    a = input("输入你想说的话：")
    b = requests.get("http://api.qingyunke.com/api.php?key=free&appid=0&msg=" + a)
    c = b.text
    #print(b.text)
    str1 = c[23:]
    mylen = len(str1)
    thelen = mylen - 2
    str2 = str1[:thelen]
    print(str2)