def call_myself(number):
    number += 1

    print(f"I called myself: {number} times")

    if number == 10:
        return
    
    call_myself(number)

call_myself(0)