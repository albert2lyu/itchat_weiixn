import os

mark=[[0 for j in range(10)] for i in range(10)]  #创建非法的标识位置，例如 1和3 之间链接必须经过2
visited=[0 for j in range(10)] #创建访问过的标记，没有访问过记为0，访问过记为1
count=0
last=[0 for j in range(3000)] # 上次访问的节点

def cal(mark):
    mark[1][3]=mark[3][1]=2
    mark[1][7]=mark[7][1]=4
    mark[1][9]=mark[9][1]=5
    mark[2][8]=mark[8][2]=5
    mark[3][9]=mark[9][3]=6
    mark[3][7]=mark[7][3]=5
    mark[4][6]=mark[6][4]=5
    mark[7][9]=mark[9][7]=8

def calRec(amount,visited,last): #amount 代表连接的密码点数目
    for i in range(1,10):
        if visited[i]==0:
            if visited[mark[i][last[amount-1]]]==0 and mark[i][last[amount-1]]:
                continue
            last[amount]=i
            visited[i]=1
            calRec(amount+1,visited,last)
            visited[i]=0
            global count
            if (amount >= 4):
                count = count + 1
if __name__=="__main__":
    cal(mark)
    import time
    start=time.time()
    calRec(1,visited,last)
    end=time.time()
    print('密码总数'+str(count))
    print('执行时间'+str(end-start)+'s')