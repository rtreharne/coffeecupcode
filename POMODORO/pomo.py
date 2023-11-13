import time
import keyboard
import webbrowser

def play_background_music(state="work"):

    if state == "break":
        webbrowser.open('https://youtu.be/E0ozmU9cJDg?si=Vfk7v4Dx8FJhz0d0')
    else:    
        webbrowser.open('https://youtu.be/7cSNNvoJJXQ?si=NUqHRjqroDv6LmvT')

def start_pomo(work_time=25, break_time=5):
    state = "work"
    restart = False

    play_background_music()

    # Print user instructions
    print("Press 'n' to skip to next state")

    while True:
        if state == "work":
            print("\nWork for 25 minutes")
            # output countdown timer in minutes:seconds
            for i in range(work_time*60, 0, -1):
                print(f"\r{i//60}:{i%60}", end="")
                time.sleep(1)
                if keyboard.is_pressed('n'):
                    start_time = time.time()
                    while keyboard.is_pressed('n'):
                        if time.time() - start_time >= 2:
                            # Key has been held down for 2 seconds
                            state = "break"
                            break
                    if state == "break":
                        break
  
                elif keyboard.is_pressed('r'):
                    start_time = time.time()
                    while keyboard.is_pressed('r'):
                        if time.time() - start_time >= 2:
                            # Key has been held down for 2 seconds
                            restart = True
                            break
                    if restart:
                        restart = False
                        break
                
                elif i == 1:
                    state = "break"
                    
               
        elif state == "break":
            print("\nTake a 5 minute break")
            play_background_music(state="break")
            # output countdown timer in minutes:seconds
            for i in range(break_time*60, 0, -1):
                print(f"\r{i//60}:{i%60}", end="")
                time.sleep(1)
                if keyboard.is_pressed('n'):
                    start_time = time.time()
                    while keyboard.is_pressed('n'):
                        if time.time() - start_time >= 2:
                            # Key has been held down for 2 seconds
                            state = "work"
                            break
                    state = "work"
                    break

                elif keyboard.is_pressed('r'):
                    start_time = time.time()
                    while keyboard.is_pressed('r'):
                        if time.time() - start_time >= 2:
                            # Key has been held down for 2 seconds
                            restart = True
                            break
                    if restart:
                        restart = False
                        break
                    i = break_time*60

                elif i == 1:
                    state = "work"


if __name__ == "__main__":
    start_pomo()
