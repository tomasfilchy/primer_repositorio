def funcion_externa():
    x = "Hola desde la función externa"
    
    def funcion_interna():
        nonlocal x
        x = "Modificado por la función interna"
        print("Dentro de la función interna:", x)
    
    funcion_interna()
    print("De vuelta en la función externa:", x)

funcion_externa()