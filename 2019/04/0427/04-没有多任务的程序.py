import time


def sing():
    for i in range(5):
        print('-----菊花台----')
        time.sleep(1)

def dance():
    for i in range(5):
        print('------跳舞-----')
        time.sleep(1)

def main():
    sing()
    dance()


if __name__ == "__main__":
    main()