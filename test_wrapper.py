import datetime
import time


def print_status(func):
    def wrap():
        start = datetime.datetime.now()
        func()
        final = datetime.datetime.now() - start
        print("time_run\n", final)
    return wrap

@print_status
def translate_status():
    print("STATUS - OK!")
    # print(datetime.datetime.now())
    time.sleep(2)

def main():
    translate_status()

if __name__ == "__main__":
    main()
