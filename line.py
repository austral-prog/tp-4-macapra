def line():
    A = float((input("Ingrese el coeficiente de A: ")))
    B = float((input("Ingrese el coeficiente de B: ")))
    X1 = float((input("Ingrese el coeficiente de X1: ")))
    X2 = float((input("Ingrese el coeficiente de X2: ")))
    print(f"El coeficiente A de su ecuacion de la recta es: {A}")
    print(f"El coeficiente B de su ecuacion de la recta es: {B}")
    print(f"El coeficiente X1 de su ecuacion de la recta es: {X1}")
    print(f"El coeficiente X2 de su ecuacion de la recta es: {X2}")
    print(f"\nPara la siguiente ecuacion: \n\tY= {A}X + {B} ")
    Y1 = A * X1 + B
    Y2 = A * X2 + B
    print(f"\nDado los siguientes puntos: \n\tP1 ({X1}, {Y1})\n\tP2 ({X2}, {Y2})")
    distancia = ((X2 - X1)**2 + (Y2 - Y1)**2)**0.5
    print(f"\nLa distancia entre ellos es: {distancia}")
