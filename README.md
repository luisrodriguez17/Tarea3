 Variables aleatorias multiples
## 1: Curva de mejor ajuste para funciones de densidad marginales de X y Y
Se analizan los datos de xy.csv, se grafican los resultados de ambas densidades marginales. A partir de la gráfica, se determina la curva de mejor ajuste.

<img src=".../master/Imagenes/marginalX.png" width="80"> 

<img src=".../master/Imagenes/marginalY.png" width="80"> 

Se observa que ambas tienen un comportamiento de distribución normal, por lo tanto, en el código se programa la función y se utiliza el curve_fit para determinar los parametros de la curva, que corresponde a una gaussiana. Estos parametros son sigma y mu. Los resultados son: 
+ μx = 9.9048
+ σx = 3.2994
+ μy = 15.0794
+ σy = 6.0269

Entonces, la curva de mejor ajuste para ambas gráficas corresponde a: 
 <img src=".../master/Imagenes/normal.png" width="80"> 
 Cada una con sus respectivos sigma y mu. 
 ## 2: Función de densidad conjunta
 Para esta sección, al asumir independencia de X y Y, se calcula la función de densidad conjunta, realizando la multiplicación de ambas curvas. Se reemplazan los valores de mu y sigma en la ecuación anterior para ambas curvas y se multiplican, obteniendo el siguiente resultado:

 <img src=".../master/Imagenes/pdf.png" width="80"> 
 
 ## 3: Correlación, covarianza y coeficiente de correlación de Pearson
 Para esta sección, se utiliza el segundo documento xyp.csv para averiguar primero, la correlación. El valor de la correlación, al ser de forma discreta corresponde a la sumatoria de xy*f(x,y) y se representa con Rxy. Por lo tanto:
 Rxy = E[XY]
 Para este cálculo simplemente se utiliza el acomodo del documento xyp.csv multiplicando las columnas. Estas multiplicaciones se suman, y resulta en:
 Rxy = 149.5428
 Si ambas variables no estan correlacionadas, el resultado con el segundo método debería ser el mismo al primero. Este segundo método corresponde a: 
 Rxy = E[X]E[Y]
 Rxy es una medida de que tan similares son ambas variables aleatorias. Al calcularlo de esta forma: 
 E[X]E[Y] = 149.4840
 Este valor es muy similar al calculado previamente (Rxy) y por esto se puede decir que ambos datos no estan correlacionados. Ahora se calcula la covarianza, que corresponde a la resta de ambos resultados anteriores, verificando su similitud. 
 Cxy = Rxy - E[X]E[Y] = 0.0587614 
 Este resultado indica la similitud entre dos variables aleatorias, al ser este valor tan cercano a 0, se verifica que no estan relacionadas. Ahora se calcula el resultado del coeficiente de pearson, otra medida que verifica nuevamente que tan similares son estas variables aleatorias. Si el coeficiente es cercano a 1 hay una distribución de pendiente positiva o si fuese cercano a -1 la pendiente de distribución sería negativa. 
 Cp = Cxy/σxσy = 0.00295498
 ## Parte 4: Gráficas:
 Las gráficas de 2D de las funciones de mejor ajuste para las funciones marginales de X y Y. Se grafíca con matplotlib: 
 <img src=".../master/Imagenes/MejorAjusteX.png" width="80"> 
 
  <img src=".../master/Imagenes/MejorAjusteY.png" width="80"> 
 
 Finalmente, se grafíca la función en 3D con Axes 3D de la función de densidad conjunta. 
 
  <img src=".../master/Imagenes/Grafico3D.png" width="80"> 
