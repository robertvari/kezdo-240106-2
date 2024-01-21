import time, random


def my_timer(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        stop_time = time.time() - start_time
        print(f"Timer: {stop_time}")

        return result
    
    return wrapper


def temp_warning(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 800:
            print(f"<<<WARNING>>> Temperature is high: {result} <<<WARNING>>>")
        return result
    return wrapper

@my_timer
def convert_images():
    print("Convert Images started...")
    time.sleep(random.randint(1, 10))
    print("Convert Images finished!")

@my_timer
def convert_videos():
    print("Convert video started...")
    time.sleep(random.randint(1, 10))
    print("Convert video finished!")


@temp_warning
def check_temperature():
    time.sleep(2)
    current_temp = random.randint(100, 1200)
    return current_temp

while True:
    result = check_temperature()
    print(f"Current temperature: {result}")