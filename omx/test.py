from time import sleep
while True:
    with open("omx/what.txt", "r") as f:
        down = f.readline()

    print(down[-1])
    sleep(1)
    

