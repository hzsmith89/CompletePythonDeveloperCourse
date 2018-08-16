import _thread
import time


def count_down(thread_name):
    count = 10
    while count >= 0:
        print("{} - Count: {}".format(thread_name, count))
        count -= 1
        time.sleep(1)

def main():

    try:
        _thread.start_new_thread(count_down, ("Thread1",))
        _thread.start_new_thread(count_down, ("Thread2",))
        print("Thread is running")
    except Exception:
        print("Error: Thread didn't start.")

    while 1:
        pass


if __name__ == "__main__":
    main()
