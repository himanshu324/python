import platform,socket,re,uuid,json,psutil,logging
from datetime import datetime


print ("Enter the number of queens")
N = int(input())
start_time = datetime.now()
board = [[0]*N for _ in range(N)]
solutions = 0

def is_attack(i, j):
    
    for k in range(0,N):

        if board[k][j]==1 or board[i][k]==1:
            return True

    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
                    return True
    return False

def N_queen(n):
    global solutions
    #solutions = 0
    
    if n==0:
       solutions+=1
        return True
    for i in range(0,N):
        for j in range(0,N):
            
            if (not(is_attack(i,j))) and (board[i][j]!=1):
                board[i][j] = 1
                
                if N_queen(n-1)==True:
                    return True
                board[i][j] = 0
    
    return False

N_queen(N)
for i in board:
    print (i)
print(solutions)
def getSystemInfo():
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)

print("system specifications: ",json.loads(getSystemInfo()))
print("process finished in %s"%(datetime.now()-start_time))
