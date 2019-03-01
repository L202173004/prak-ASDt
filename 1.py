def cetakSiku(x):
    for i in range(0,x+1):
        print("x"*i)

cetakSiku(5)


def persegiEmpat(x,y):
    print ("@"*y)
    for i in range(0,x-2):
        print("@"+" "*(y-2)+"@")
    print ("@"*y)


def jumlahhurufvokal(v):
    vocal = "aiueoAIUEO"
    jumlah = 0
    for i in v :
        if i in vocal :
            jumlah = jumlah+1

    return (len(v),jumlah)

def jumlahhurufkonsonan(k):
    konsonan = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVXYZ"
    jumlah = 0

    for i in k :
        if i in konsonan:
            jumlah = jumlah+1

    return(len(k),jumlah)



def rerata(b):
    k=0
    hai=[]
    for i in b:
        k=k+i
    return (k/len(b))


def apakahPrima(n):
    n = int(n)
    assert n>=0
    primaKecil = [2,3,5,7,11]
    bukanPrKecil = [0,1,4,6,8,9,10]
    if n in primaKecil:
        return
