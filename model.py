import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


class calculate():
    def __init__(self,alpha,beta,delta,gamma,x0,y0,tf,canvas:list):
        self.alpha=alpha
        self.beta=beta
        self.delta=delta
        self.gamma=gamma
        self.x0=x0
        self.y0=y0
        self.tf=tf
        self.canvas=canvas
        self.plot()

    def derivative(self,X, t, alpha, beta, delta, gamma):
       x, y = X
       dotx = x * (alpha - beta * y)
       doty = y * (-delta + gamma * x)
       return np.array([dotx, doty])


    def select_vals(self,n):
       return [self.valx[n],self.valy[n]]

    def plot(self):
        Nt=100
        X0=[self.x0,self.y0]
        t = np.linspace(0.,int(self.tf),int(self.tf))
        res = integrate.odeint(self.derivative, X0, t, args = (self.alpha, self.beta, self.delta, self.gamma))
        self.time=t
        x, y = res.T
        self.valx=x
        self.valy=y
        ax=self.canvas[0].add_subplot(1,1,1)
        ax.grid()
        ax.plot(t, x, '+b',label='presa' )
        ax.plot(t, y, 'xr',label='depredador')
        ax.set_xlabel('tiempo t')
        ax.set_ylabel('Población')
        ax.plot

    def return_values(self):
        return [self.time,self.valx,self.valy]
       



