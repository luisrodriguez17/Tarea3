import csv
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import curve_fit
import scipy.stats as stats
import scipy
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def gaus(x,mu, b):
   return 1/(b*np.sqrt(2*np.pi))*np.exp(-((x-mu)*(x-mu))/(2*b*b))

def conjunta(x,y):
    return (1/(3.29944286*6.02693775 * np.sqrt(2*np.pi))*np.exp(-(((y-15.0794609)**2/(2*6.02693775**2))+(x-9.90484381)**2/(2*3.29944286**2))))
with open('xy.csv') as datos:
    sns.set()
    #Obtención de PMF de X
    readCSV = csv.reader(datos, delimiter=',')
    xM = []
    x = np.linspace(5, 15, num=11)
    y = np.linspace(5, 25, num=21)
    output = 0
    for row in readCSV:
        output = 0  
        if row[0] == '':
            output = 0
        else:    
            for i in range(1,22):
                output = output + float(row[i])
            xM.append(output)
    
    plt.rcParams["font.family"] = "serif"
    plt.plot(x, xM)
    k = plt.xlabel("Valores de X")
    k = plt.ylabel("Probabilidad")
    k = plt.title("Densidad Marginal")
    plt.show()
    #Obtención de la PMF de Y
    yM = [0] * 21
    datos.seek(0)
    readCSV = csv.reader(datos, delimiter=',')
    for row in readCSV:
        if row[0] == '':
            continue
        else:
            for i in range(1,22):
                yM[i-1] = yM[i-1] + float(row[i])
    plt.clf()
    plt.plot(y, yM)
    k = plt.xlabel("Valores Y")
    k = plt.ylabel("Probabilidad")
    k = plt.title("Densidad Marginal")
    plt.show()

    #Curva de Mejor ajuste X
    paramx, _ = curve_fit(gaus, x, xM)
    print("Los parámetros de la PMF de X son: ", paramx)
    #Curva de Mejor ajuste Y
    paramy, _ = curve_fit(gaus, y, yM)
    print("Los parámetros de la PMF de y son: ", paramy)

    #Parte 3: 
with open('xyp.csv') as datos2:

    readCSV = csv.reader(datos2, delimiter=',')
    #Correlación
    correlacion= 0
    next(readCSV)
    for row in readCSV:
        correlacion = correlacion + float(row[0])*float(row[1])*float(row[2])
    print("El valor de la correlación, de la forma discreta es: " , correlacion)

    #Verificación de la correlación
    datos2.seek(0)
    correlacionX = 0
    correlacionY = 0
    next(readCSV)
    for row in readCSV:
        correlacionX = correlacionX + float(row[0])*float(row[2])
        correlacionY = correlacionY + float(row[1])*float(row[2])
    print("Verificamos la correlación con E[X]*E[Y] : ", correlacionX*correlacionY)
    #Covarianza
    print("La covarianza corresponde a la resta de los 2 resultados anteriores", correlacion-correlacionX*correlacionY)
    covarianza = correlacion-correlacionX*correlacionY
    #Coeficiente de pearson
    print("Calculamos el coeficiente de pearson con los resultados anteriores :", covarianza/(paramx[1]*paramy[1]) )
    
    
    #Grafica 3D
    plt.cla()
    plt.clf()
    X = np.linspace(5,15, 600)
    Y = np.linspace(5,25,600)
    X, Y = np.meshgrid(X, Y)
    Z = (1/(3.29944286*6.02693775 * np.sqrt(2*np.pi))*np.exp(-(((Y-15.0794609)**2/(2*6.02693775**2))+(X-9.90484381)**2/(2*3.29944286**2))))
    
    fig = plt.figure()

    ax = plt.axes(projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap='plasma', edgecolor = 'none')
    ax.set_title('Densidad de probabilidad marginal conjunta')
    ax.set_xlabel('Valor en X')
    ax.set_ylabel('Valor en Y')
    ax.set_zlabel('Probabilidad conjunta')
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()


    #Gráficas 2D
    ajusteX = gaus(x, 9.90484381, 3.29944286 )
    ajusteY = gaus(y, 15.0794609, 6.02693775)
    




    plt.clf()
    plt.cla()
    plt.plot(x, ajusteX)
    k = plt.xlabel("Valores de X")
    k = plt.ylabel("Probabilidad")
    k = plt.title("Densidad Marginal función de mejor ajuste")
    plt.show()





    plt.clf()
    plt.cla()
    plt.plot(y, ajusteY)
    k = plt.xlabel("Valores de Y")
    k = plt.ylabel("Probabilidad")
    k = plt.title("Densidad Marginal función de mejor ajuste")
    plt.show()

