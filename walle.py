# -*- coding:utf8 -*-
import urllib,urllib2,re
import cookielib

if __name__=='__main__':
    loginUrl='http://www.douban.com/accounts/login'
    cookie=cookielib.CookieJar()
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    params={
        'form_email':'',
        'form_password':'',
        'source':'index_nav'
    }
    response=opener.open(loginUrl,urllib.urlencode(params))
    topicUrl='http://www.douban.com/group/topic/52497515/'
    if response.geturl()=='http://www.douban.com/accounts/login':
        html=response.read()
        imgUrl=re.search('<img id="captcha_image" src="(.*?)" alt="captcha" class="captcha_image"/>',html)
        if imgUrl:
            url=imgUrl.group(1)
            res=urllib.urlretrieve(url,'v.jpg')
            captcha=re.search('<input type="hidden" name="captcha-id" value="(.*?)"/>',html)
            if captcha:
                vcode=raw_input('Please input the code : ')
                params["captcha-solution"]=vcode
                params["captcha-id"]=captcha.group(1)
                params["user_login"]="登录"
                response=opener.open(loginUrl,urllib.urlencode(params))
                if response.geturl()=='http://www.douban.com/':
                    print 'Login Success!'
                    print 'It\'s time to say something~'
                    p={"ck":""}
                    c=[c.value for c in list(cookie) if c.name=='ck']
                    if len(c)>0:
                        p["ck"]=c[0].strip('"')
                    p["rv_comment"]='dust to dust,earth to earth'
                    p["submit_btn"]='加上去'
                    p['start']='0'
                    request=urllib2.Request(topicUrl)
                    request.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
                    request.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0')
                    request.add_header('Accept-Language','en-US,en;q=0.5')
                    request.add_header('Connection','keep-alive')
                    request.add_header('Host','www.douban.com')
                    request.add_header('Referer','http://www.douban.com/group/')
                    opener.open(request,urllib.urlencode(p))
                else:
                    print 'Don\'t redirect to www.douban.com : ',response.geturl()
    elif response.geturl()=='http://www.douban.com/':
        print 'Login Success!'
        print 'It\'s time to say something~'
        p={"ck":""}
        c=[c.value for c in list(cookie) if c.name=='ck']
        if len(c)>0:
            p["ck"]=c[0].strip('"')
        p["rv_comment"]='dust to dust,earth to earth'
        p["submit_btn"]='加上去'
        p['start']='0'
        request=urllib2.Request(topicUrl)
        request.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
        request.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0')
        request.add_header('Accept-Language','en-US,en;q=0.5')
        request.add_header('Connection','keep-alive')
        request.add_header('Host','www.douban.com')
        request.add_header('Referer','http://www.douban.com/haixiuzu/group/')
        opener.open(request,urllib.urlencode(p))
