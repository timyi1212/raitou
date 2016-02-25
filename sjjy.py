#-*- coding:utf-8 -*-
import urllib2
import urllib
import json
import cookielib

#http://www.jiayuan.com/88534291?fxly=search_v2_index






def down_pics(userinfo):
	for index in range(len(userinfo)):
		uid = userinfo[index]['uid']
		image = userinfo[index]['image']
		urllib.urlretrieve(image,'%s.jpg' % uid)

def get_userinfo(search_html):
	html_dict = json.loads(search_html)
	userinfo = html_dict['userInfo']
	return userinfo

def get_pages(search_html):
	html_dict = json.loads(search_html)
	pageTotal = html_dict['pageTotal']
	return pageTotal

def get_count(search_html):
	html_dict = json.loads(search_html)
	count = html_dict['count']

def get_searchresult(pageNum):
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
	data['p'] = pageNum
	data  = urllib.urlencode(data)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	search_html = response.read()
	return search_html[11:-13]



def init_urlopen():
	cookie = cookielib.CookieJar()
	handler = urllib2.HTTPCookieProcessor(cookie)
	opener = urllib2.build_opener(handler)
	#opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'),('Connection', 'keep-alive')]
	urllib2.install_opener(opener)
	#验证码url
	url = 'http://login.jiayuan.com/antispam_v2.php?v=2'
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	with open('validatep.jpg','wb') as file:
		image = response.read()
		file.write(image)
	cookies = ''
	#这里要从
	for index, cookie in enumerate(cookie):
		cookies = cookies+cookie.name+"="+cookie.value+";";
	print "###########################"
	cookie = cookies[:-1]
	print "cookies:",cookie
	username = 'tianyi.zhang12@gmail.com'
	password = '64761137'
	validate_pass = raw_input('请输入验证码:')
	postData = {   
	'name':username,	
	'password':password,
	'remem_pass': 'on',
    'validate_code':validate_pass, 
    'ljg_login':'1',    
	'm_p_l':'1',
	}
	#opener.addheaders = [('Cookie', cookies)]
	#urllib2.install_opener(opener)
	headers = {
 	'Cookie':cookie,
	#'Content-Type':	'application/x-www-form-urlencoded',
	#'Content-Length' :474,
    'Connection' : 'Keep-Alive'
	}
	data = urllib.urlencode(postData)
	url = 'https://passport.jiayuan.com/dologin.php?pre_url=http://search.jiayuan.com/v2/'
	#response = opener.open(url, data)
	#print response.read()
	request = urllib2.Request(url,data,headers)
	#response = urllib2.urlopen(request)
	#lprint response.read()



	'''



	data = {}
	validatepic = 'http://login.jiayuan.com/antispam_v2.php?v=2'
	with open('fuck.jpg','wb') as file:
		image = opener.open(validatepic).read()
		file.write(image)
	url = 'https://passport.jiayuan.com/dologin.php?pre_url=http://search.jiayuan.com/v2/'
	data['name'] = 'tianyi.zhang12@gmail.com'
	data['password'] = '64761137'
	data['remem_pass'] = 'on'
	validate_code = raw_input('验证码：')
	data['channel'] = '200'
	data['position'] = '204'
	data['validate_code'] = validate_code
	#data['_s_x_id'] = 'a623d8ef63342cac56fb1632825a2c9a'
	data['ljg_login'] = '1'
	data['m_p_l'] = '1'
	data  = urllib.urlencode(data)
	print opener.open(url, data)

	urllib2.install_opener(opener)

	'''

if __name__ == '__main__':
	init_urlopen()
	pageNum = 1
	search_html = get_searchresult(str(pageNum))
	totalPage = get_pages(search_html)
	#print totalPage
	#print search_html
	
	while pageNum <= totalPage:
		search_html = get_searchresult(str(pageNum))
		print search_html
		userinfo =  get_userinfo(search_html)
		#down_pics(userinfo)
		pageNum = pageNum + 1
		print '==============================='
	

'''
url = 'http://search.jiayuan.com/v2/search_v2.php'
data = {}
data['sex'] = 'f'
data['stc']='1:31,2:20.32,3:155.170,24:1,23:1'
data['key']=''
data['sn']='default'
data['sv']='1'
data['f']='select'
data['listStyle']='bigPhoto'
data['pri_uid']='0'
data['jsversion']='v5'
data['p'] = '1'

page_count = 1
while page_count < 100:
    data['p']= str(page_count)
    page_count = page_count + 1
    data  = urllib.urlencode(data)
    req = urllib2.Request(url, data)
    data = {}
    data['sex'] = 'f'
    data['stc']='1:31,2:22.26,3:155.170,24:1,23:1'
    data['key']=''
    data['sn']='default'
    data['sv']='1'
    data['f']='select'
    data['listStyle']='bigPhoto'
    data['pri_uid']='0'
    data['jsversion']='v5'
    response = urllib2.urlopen(req)
    the_page = response.read()
    if len(the_page) < 3000:
    	break
    	
    the_page = the_page[11:-13]
    page_dict = json.loads(the_page)
    user_list = page_dict["userInfo"]

    for index in range(len(user_list)):
         print index
         name =user_list[index]['nickname'].encode('utf8')
         uid = user_list[index]['uid']
         image =  user_list[index]['image']
         print name
         urllib.urlretrieve(image,'%s.jpg' % uid)

         print "==================================================="
'''
        