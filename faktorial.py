# faktorial #
from time import sleep
try:
    while True:
        try:
            x = int(input("\nType anythink: "))
            z = 1
            for i in range(x):
                i+=1
                z *= i

            print(f'Total: {z}')
        except ValueError:
            print('You entered uncorrect thing')
except KeyboardInterrupt:
    print('\nStopping programm')
    sleep(0.2)