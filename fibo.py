def fibonacci(InputAmount):
    if InputAmount <= 0:
        return "Cmon take smth higher then 0 -_-"
    elif InputAmount == 1:
        return [0, "1? rlly?"]
    elif InputAmount == 2:
        return [0, 1, "Off/On?"]
    else:
        fibo = [0, 1]
        for number in range(2, InputAmount):
            fibo.append(fibo[number-1] + fibo[number-2])
        return fibo

def main():
    number_input = int(input("How many FIBO-Numbs you want ha?: "))
    fibo = fibonacci(number_input)
    print("Hier sind die Zahlen die Simon will:")
    for i in range(len(fibo)):
        
