#Im not entirely sure I did this one the correct way, but the program does work.

#Askes for temp with the input(...), get decimals with float, print(tpye confirms float
celsius = float(input("What is the temperature in Celsius?"))
print(type(celsius))

#Formulat for Fahrenheit
Fahrenheit = celsius * 9 / 5 + 32

#converts your celsius temp to Fahrenheit. using f to format, .2f for only 2 decimals.
print(f" The temperature outside is: {Fahrenheit: .2f}")
