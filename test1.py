import urllib2
import urllib
import json
import cookielib

url = 'https://passport.jiayuan.com/dologin.php?pre_url=http://search.jiayuan.com/v2/'
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
#opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'),('Connection', 'keep-alive')]
urllib2.install_opener(opener)
data = {}
data['name'] = 'tianyi.zhang12@gmail.com'
data['password'] = '64761137'
data['remem_pass'] = 'on'
data = urllib.urlencode(data)
response = opener.open(url, data)
url = 'http://search.jiayuan.com/v2/search_v2.php'
data = {}
data['sex'] = 'f'
data['stc']='1:31,2:19.20,3:155.170,24:1,23:1'
data['key']=''
data['sn']='default'
data['sv']='1'
data['f']='select'
data['listStyle']='bigPhoto'
data['pri_uid']='0'
data['jsversion']='v5'
data['p'] = '1'
data  = urllib.urlencode(data)
response = opener.open(url, data)
print response.read()