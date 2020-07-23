import time 
seconds = int(input("How many seconds to wait?"))

for i in range(seconds):
    print(str(seconds-i)+" seconds remain")
    time.sleep(1)
    
print("Time's up!")