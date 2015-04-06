import account
import random
import re
user = account.twitter_username
pswd = account.twitter_password
class Main:
    def readLastStatusId(self):
        f = open('./lastStatusId.txt', 'r')
        s = f.read()
        f.close()
        return long(s)
    def writeLastStatusId(self,id):
        f = open('./lastStatusId.txt', 'w')
        f.write(id)
        f.close()
    def isZawa(self,text):
        r = re.compile(u'([つっ][・…]+|[・…]+[つっ])[！!]')
        result = r.search(text)
        if result != None:
            return True
        return False
    def makePost(self,user):
        result = u"@"
        result += user + u" "
        zawa_list = [
            u"ざわ…",
            u"ざわ……ざわ……",
            u"ざわ………ざわ………",
            u"ざわ…　ざわ…",
            u"ざわ……　ざわ……",
            u"ざわ……　ざわ………"
        ]
        result += random.choice(zawa_list)
        return result
    def do(self):
        lastStatusId = self.readLastStatusId()
        api = twitter.Api(user,pswd)
        lines = api.GetFriendsTimeline()
        lines.reverse()
        for one in lines:
            if one.id > lastStatusId:
                if one.user.screen_name != 'ZAWATTER':
                    if self.isZawa(one.text):
                        post = self.makePost(one.user.screen_name)
                        api.PostUpdate(post,one.id)
                self.writeLastStatusId(str(one.id))
                lastStatusId = one.id

Main().do()
