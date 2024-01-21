import time, random


def my_timer(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        stop_time = time.time() - start_time
        print(f"Timer: {stop_time}")

        return result
    
    return wrapper


def convert_images():
    print("Convert Images started...")
    time.sleep(random.randint(1, 10))
    print("Convert Images finished!")

def convert_videos():
    print("Convert video started...")
    time.sleep(random.randint(1, 10))
    print("Convert video finished!")


convert_images()
convert_videos()