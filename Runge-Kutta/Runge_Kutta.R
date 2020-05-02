#Ejercicio 8.3

#Utilizando el metodo de Runge-Kutta de orden 4, aproximar y(0.2) con h=0.1

f <- function(t){
  return(exp(-(t^2)))
}

Runge_Kutta <- function(f,x0,h){
  
  #con h=0.1
  
  xi <- c(0)
  yi <- c(0)
  imagenes <- c(0)
  errores <- c(0)
  
  cont=1
  
  #valor inicial con su respectiva imagen
  xi[cont]=x0
  yi[cont]= 1/6*(coefs_K(x0,h))*h
  imagenes[cont]=f(xi[cont])
  errores[cont]= abs(yi[cont])
  cont=cont+1
  
  while (cont < 80) {
    
    xi[cont]= xi[cont-1]+h
    imagenes[cont]=f(xi[cont])
    
    yi[cont]= yi[cont-1]+1/6*(coefs_K(xi[cont],h))*h
    
    errores[cont]=abs((yi[cont]-yi[cont-1])/yi[cont])
    cont=cont+1
    
  }
  

  
  tabla = data.frame(xi, yi,imagenes,errores)
  print(tabla)
    
  #par(mfrow=c(2,2))
  plot(xi,imagenes,type = "l",col="blue",main = "Grafica por Runge-Kutta")
  points(xi,yi,type = "l",col="green")
  
  #plot(errores,main = "Grafica Errores")
  

  
}


coefs_K <- function(xi,h){
  
  k1=f(xi)
  k2=f(xi+(0.5*h))
  k3=f(xi+(0.5*h))
  k4=f(xi+h)
  
  valor=(k1+2*k2+2*k3+k4)
  
  return(valor)
  
}


Runge_Kutta(f,0,0.1)



