#coding=utf8
import itchat

import  time
from itchat.content import *
def reg_sex():
    friendList=itchat.get_friends(update=True)[1:]
    sexDict={}

    total=len(friendList)
    for friend in friendList:
        if not friend['Sex'] in sexDict:
            sexDict[friend['Sex']]=[]
        sexDict[friend['Sex']].append(friend['NickName']+' '+friend['DisplayName'])

    unkonw=len(sexDict[0])
    male=len(sexDict[1])
    female=len(sexDict[2])

    print('您共有%d位好友，其中未知性别好友%d,其中男性性别的好友%d位，女性性别的好友%d\n'%(total,unkonw,male,female))

    '''
    print('未知性别的好友是：\n')
    for name in sexDict[0]:
        print(name)
    print('男性的好友是：\n')
    for name in sexDict[1]:
        print(name)
    print('女性的好友是：\n')
    for name in sexDict[2]:
        print(name)
    
    '''

# 向群聊的所有用户发送消息
def sendMsgInchatromms(chatroomName=u'亲朋好友',REAL_MSG=u'%s这是一条群聊的群发消息,客户端程序'):
    itchat.get_chatrooms(update=True)
    chatrooms=itchat.search_chatrooms(name=chatroomName)
    if chatrooms is None:
        print(u'没有找到群聊:%s'%chatrooms)
    else:
        chatrooms=itchat.update_chatroom(chatrooms[0]['UserName'])
        for friend in chatrooms['MemberList']:
            # 真正发送消息的时候可以将下面的print 替换成itchat.send()
            itchat.send(REAL_MSG%(friend['NickName'] or friend['DisplayName']))

            time.sleep(.5)

@itchat.msg_register([TEXT,MAP,CARD,NOTE,SHARING])
def text_reply(msg):
    msg.user.send('自动回复，我现在不在线，您的消息:%s 已经收到'%(msg.text))

if __name__=="__main__":
    itchat.auto_login(hotReload=True)
    #reg_sex()   # 获取通讯录好友的性别比例

    itchat.run(True)
    #sendMsgInchatromms(chatroomName=u'测试微信') # 向指定的群聊中的所有好友发送消息





