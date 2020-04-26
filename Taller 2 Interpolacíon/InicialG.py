from matplotlib import pyplot as pl

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
def C(n,i):
    return factorial(n)/(factorial(n-i)*factorial(i))

def Spline(n,puntos):
    coeficientesx = []
    coeficientesy = []
    for i in range(n+1):
        Coef = C(n,i)
        coeficientesx.append(Coef*puntos[i][0])
        coeficientesy.append(Coef*puntos[i][1])
    return [coeficientesx,coeficientesy]

def B(n,t,coef):
    ans = 0
    for i in range(n+1):
        ans += coef[i]*((1-t)**(n-i))*(t**i)
    return ans
       
def graficar(n,T,coeficientes):
    x = []
    y = []
    for t in T:
        x.append(B(n,t,coeficientes[0]))
        y.append(B(n,t,coeficientes[1]))
    pl.plot(x,y)
    pl.show()
    return None

T = []
for i in range(100):
    T.append(i/100.0)

puntos = [[0.57,3.92],[0.45,4.19],[0.18,4.3],[-0.14,4.06],[-0.37,4.38],[-0.84,4.42],[-1.06,4.11],[-1.43,4.25],[-1.77,4.1],[-1.81,3.71],[-2.41,3.41],[-2.27,2.99],[-2.64,2.78],[-2.77,2.49],[-2.52,2.19],[-2.81,1.88],[-2.8,1.53],[-2.53,1.38],[-2.57,0.94],[-2.43,0.68],[-2.06,0.61],[-1.9,0.21],[-1.59,-0.03],[-1.21,0.04],[-1.02,-0.25],[-0.59,-0.32],[-0.3,-0.14],[0,-0.33],[0.51,-0.25],[0.74,0.05],[1.23,0.25],[1.38,0.76],[1.15,1.07],[1.47,1.31],[1.47,1.68],[1.17,1.9],[1.32,2.21],[1.08,2.34],[0.88,2.02],[0.65,2.36],[0.21,2.38],[0.01,1.97],[-0.38,2.37],[-0.78,2.4],[-1.03,1.89]]
n = len(puntos)-1
coeficientes = Spline(n,puntos)
graficar(n,T,coeficientes)


