if __name__ == '__main__':
    for i in range(1, 4):
        print(i)
    else:
        print("No break") # executed after 1 - 3 printed out

    for i in range(1, 4):
        print(i)
        break
    else:
        print("No break") # won't get executed
