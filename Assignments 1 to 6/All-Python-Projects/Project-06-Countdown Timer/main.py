import time

def countdown(seconds):
    while seconds:
        mins = seconds // 60
        secs = seconds % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

if __name__ == "__main__":
    try:
        countdown_time = int(input("Enter the countdown time in seconds: "))
        if countdown_time < 0:
            raise ValueError("Time cannot be negative.")
        countdown(countdown_time)
    except ValueError as e:
        print(f"Invalid input: {e}")
