# plotea cuatro regresiones lineales a partir de los datos en los archivos csv
# indicando la funcion y el coeficiente de determinacion

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

def plot(file):
    #   Leer archivos
    data = pd.read_csv(file)

    #   Estadisticos
    x_mean, y_mean = data.mean(axis=0) 

    data['xi-xm']= data['x']-x_mean
    data['yi-ym'] = data['y'] - y_mean

    s_xx = (data['xi-xm']**2).sum()
    s_xy = (data['y']*data['xi-xm']).sum()
    s_yy = (data['yi-ym']**2).sum()

    #   Estimadores
    b1 = s_xy/s_xx
    b0 = y_mean - b1*x_mean

    # Coeficiente de determinacion
    r2 = 1 - (s_yy - s_xy**2 / s_xx) / s_yy

    # def line(x,b1,b0):
    #    return b0 + x*b1

    #data["y_e"]=data["x"].apply(line, args=(b1,b0))

    #values = (data["y"]-data["y_e"])

    #   Grafico
    min = data['x'].min()
    max = data['x'].max()

    values = [b0 + b1*min, b0 + b1*max]

    fig = plt.figure()
    ax = plt.axes()
    ax.scatter(data['x'], data['y'], linewidths=0.3)
    ax.plot([min,max],values, color='green')
    plt.text(170, 2, 'R² = {}'.format(r2))
    plt.text(170, 1.95, 'y = {} + {}.x'.format(round(b0,3), round(b1,3)))
    plt.show()

plot('ejercicio1.csv')
plot('ejercicio2.csv')
plot('ejercicio4.csv')
plot('ejercicio6.csv')