import time
k_constant=2416
c_CONSTANT=374441
m_CONSTANT=1771875
def generateNewSeed(x,a,c,m):
  #Using Linial congruence
    return (a*x+c)%m

def  generateRandomNumbers(x,Base,limInf,LimSup,numerosABuscar):
    #Fills a list with unique vales between limInf and limSup
    Lista=[]
    cantidad=0
    while cantidad<numerosABuscar:
        x=generateNewSeed(x,k_constant,c_CONSTANT,m_CONSTANT)
        numAleatorio=x/m_CONSTANT
        Entero=round(numAleatorio*Base)
        repeated=Entero in Lista
        if (not repeated):
          if (Entero>=limInf and Entero <=LimSup):
              Lista.append(Entero)
              cantidad=cantidad+1
    return Lista
def dropElementFromList (ValueToTransfer,ArrayContainer,ArrayToBeTransfered):
    item_index=ArrayContainer.index(ValueToTransfer)
    ArrayToBeTransfered.append(ArrayContainer[item_index])
    ArrayContainer.remove(ValueToTransfer)
current_time=time.time()
seedLen=len(str(current_time))
seed=int(current_time)
Lim_inf=1
Lim_Sup=75
Numeros=int (Lim_Sup-Lim_inf + 1)
repeated=False
Iteraciones=0
Base10=10**(len(str(Numeros))+1)
ReaminingBalls=generateRandomNumbers(seed,Base10,Lim_inf,Lim_Sup,Numeros)
BallsCalled=[]
