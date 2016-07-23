# encoding=utf-8
import json
import base64
import requests

"""
输入你的微博账号和密码，可去淘宝买，一元七个。
建议买几十个，微博限制的严，太频繁了会出现302转移。
或者你也可以把时间间隔调大点。
"""
myWeiBo = [
    {'no': 'benjamin.yuan@citizenpace.com', 'psw': 'yuanbin12'}
    # {'no': 'nykvlnp2@163.com', 'psw': '1q967q38uj'},
    # {'no': 'nylok34931331@163.com', 'psw': '8mjo81mfmp'},
    # {'no': 'nymxew41@163.com', 'psw': '3qjjgdzpon'},
    # {'no': 'nyqj58582958@163.com', 'psw': '8lVqwuUx3B'},
    # {'no': 'nyr46436887@163.com', 'psw': '0kyy5h3bey'},
    # {'no': 'nyseb18@163.com', 'psw': '6vssn2nfgh'},
    # {'no': 'nytnuj960618@163.com', 'psw': '8rH5cNyZjb'},
    # {'no': 'oafalk55741@163.com', 'psw': '5kNZbm59DS'},
    # {'no': 'oagd607548xnh@163.com', 'psw': '5wGI7MF9AL'},
    # {'no': 'oagenjg30970@163.com', 'psw': '1pua8m0lrn'},
    # {'no': 'oahvwwqmk18@163.com', 'psw': '2lktenqho0'},
    # {'no': 'oakcwo897016@163.com', 'psw': '6tgvq9cxs2'},
    # {'no': 'oamafs4850iqg@163.com', 'psw': '5f6hpsfls4'},
    # {'no': 'oarwnsmrxt1mj@163.com', 'psw': '0tc2bzbg8m'},
    # {'no': 'oaspnl9036@163.com', 'psw': '6i7hndu4u0'},
    # {'no': 'oauphwdiheh92@163.com', 'psw': '7lmhcmwsp5'},
    # {'no': 'oawlrtb79635xn@163.com', 'psw': '4msv7amq2p'},
    # {'no': 'obbkbc44@163.com', 'psw': '7wyppw42rk'},
    # {'no': 'obble6956808@163.com', 'psw': '6l98t5cnyw'},
    # {'no': 'obgiqhjred729@163.com', 'psw': '1pc8b27w02'},
    # {'no': 'obgt527@163.com', 'psw': '3fu6nucmeg'},
    # {'no': 'obld8721750qri@163.com', 'psw': '2nlhn9ld0a'},
    # {'no': 'obnmbx969@163.com', 'psw': '6kIR1t6toU'},
    # {'no': 'obo7867@163.com', 'psw': '5r7fobr2u4'},
    # {'no': 'obrvhp4050@163.com', 'psw': '0eVAFyAcKM'},
    # {'no': 'obvfihbw461@163.com', 'psw': '6l3usluqew'},
    # {'no': 'obwdto3500@163.com', 'psw': '2qe3d03ko6'},
    # {'no': 'obxynl75@163.com', 'psw': '3sr2p4jb29'},
    # {'no': 'oby2460850@163.com', 'psw': '4hRP80RBb2'},
    # {'no': 'ocbmleeghw65@163.com', 'psw': '5e51uxjux4'},
    # {'no': 'ocebtsqgtplt612@163.com', 'psw': '5xJbGhNJHg'},
    # {'no': 'oceofohcd08@163.com', 'psw': '2ctmsezjgj'},
    # {'no': 'ocgelmm827095@163.com', 'psw': '8bkhgrz4hi'},
    # {'no': 'ocgsul1@163.com', 'psw': '2pnq62oih4'},
    # {'no': 'ockrlru588658@163.com', 'psw': '2bp578yi95'},
    # {'no': 'ocmgbfw270@163.com', 'psw': '4yykky3ih9'},
    # {'no': 'ocscd8585147128@163.com', 'psw': '7ihr7ks5aw'},
    # {'no': 'ocsp1158@163.com', 'psw': '1vWEtPxAAc'},
    # {'no': 'ocuh4509@163.com', 'psw': '4djvzgu464'},
    # {'no': 'odbr82145626@163.com', 'psw': '2aY8J6q0zX'},
    # {'no': 'odduuyorbqv47@163.com', 'psw': '7f1hftev7v'},
    # {'no': 'odejej5@163.com', 'psw': '3kxg8eqk6q'},
    # {'no': 'odgy136938@163.com', 'psw': '1jmrfwztnz'},
    # {'no': 'odlxo19350@163.com', 'psw': '5avsuv7303'},
    # {'no': 'odmwrl9@163.com', 'psw': '7vupj75ddi'},
    # {'no': 'odsoei9742003@163.com', 'psw': '2wKTe8dvj6'},
    # {'no': 'odtdu9395097@163.com', 'psw': '1umgqbgld3'},
    # {'no': 'odxjjw889@163.com', 'psw': '1xu1nd696i'},
    # {'no': 'oeci958@163.com', 'psw': '5jk249diz9'},
    # {'no': 'oegag38783891ft@163.com', 'psw': '5yt3vnkgzq'},
    # {'no': 'oegw108@163.com', 'psw': '7bTscGdIoP'},
    # {'no': 'oehkpdde06@163.com', 'psw': '6xwtsienr3'},
    # {'no': 'oeikwb78423@163.com', 'psw': '0ki0mte4jn'},
    # {'no': 'oelkv7656@163.com', 'psw': '2prjdd0li3'},
    # {'no': 'oeqiuc8826674@163.com', 'psw': '2j5vhdpbjl'},
    # {'no': 'oes55430@163.com', 'psw': '8l8fzx4wfb'},
    # {'no': 'oesu27086@163.com', 'psw': '5rgkj9m0cp'},
    # {'no': 'oevpkkf554@163.com', 'psw': '1hYqW6aQaR'},
    # {'no': 'ofif026480546@163.com', 'psw': '8yYtusZVvR'},
    # {'no': 'ofoqdbkdsd849@163.com', 'psw': '0bDipHOvxU'}
]


def getCookies(weibo):
    """ 获取Cookies """
    cookies = []
    loginURL = r'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)'
    for elem in weibo:
        account = elem['no']
        password = elem['psw']
        print account
        print password
        username = base64.b64encode(account.encode('utf-8')).decode('utf-8')
        postData = {
            "entry": "sso",
            "gateway": "1",
            "from": "null",
            "savestate": "30",
            "useticket": "0",
            "pagerefer": "",
            "vsnf": "1",
            "su": username,
            "service": "sso",
            "sp": password,
            "sr": "1440*900",
            "encoding": "UTF-8",
            "cdult": "3",
            "domain": "sina.com.cn",
            "prelt": "0",
            "returntype": "TEXT",
        }
        session = requests.Session()
        print session
        r = session.post(loginURL, data=postData)
        jsonStr = r.content.decode('gbk')
        info = json.loads(jsonStr)
        print info
        if info["retcode"] == "0":
            print
            "Get Cookie Success!( Account:%s )" % account
            cookie = session.cookies.get_dict()
            cookies.append(cookie)
        else:
            print
            "Failed!( Reason:%s )" % info['reason']
    return cookies

print 'start'
cookies = getCookies(myWeiBo)
print
"Get Cookies Finish!( Num:%d)" % len(cookies)
