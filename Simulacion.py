import numpy as np                  # Librerías necesarias para la simulación. 
import matplotlib.pyplot as plt     

Is1 = 0.3e-12   #
Is2 = 1e-12     # Declaración de las corrientes de saturación inversa.
Is3 = 1e-6      #
n = 2           # Factor de idealidad. n = 2, significa que es un diodo fabricado en silicio. 
k = 1.38e-23    # Declaración de la constante de Boltzmann. 
q = 1.6e-19     # Magnitud de la carga del electrón
Tc1 = 125       #
Tc2 = 25        # Declaración de las temperaturas. 
Tc3 = 75        #
TK1 = 273 + Tc1 #
TK2 = 273 + Tc2 # Pasamos las temperaturas a grados Kelvin. 
TK3 = 273 + Tc3 #
Vt1 = k*TK1/q   #
Vt2 = k*TK2/q   # Hacemos el cálculo de Vt. 
Vt3 = k*TK3/q   #
VD1 = np.linspace(-1,1.98,num=1000) #
VD2 = np.linspace(-1,1.42,num=1000) # Generamos vectores para variar el voltaje VD.  
VD3 = np.linspace(-1,0.83,num=1000) #
ID1 = Is1*(np.exp(VD1/(n*Vt1))-1)   #
ID2 = Is2*(np.exp(VD2/(n*Vt2))-1)   # Calculamos ID, como un vector, alimentando la ecuación con VD. 
ID3 = Is3*(np.exp(VD3/(n*Vt3))-1)   #

fig,axes = plt.subplots()
axes.plot(VD1,ID1)                                                  #
axes.plot(VD2,ID2)                                                  # Graficamos los resultados
axes.plot(VD3,ID3)                                                  #

axes.set_xlabel("Voltaje (V)")                                      #
axes.set_ylabel("Corriente (A)")                                    #
plt.grid(True)                                                      # Damos un poco de estética a la gráfica.  
axes.set_title("""Diodo semiconductor a diferentes temperaturas
y corrientes de saturación inversa.""")                             #
plt.savefig("Diodo.jpg",dpi=500)                                    # Se guarda la gráfica como una imagen. 
