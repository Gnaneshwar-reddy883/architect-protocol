principle = 0
rate = 0
time = 0
while principle<=0:
    principle = float(input("enter principle "))
    if principle<=0:
        print("principle cannot be zero or negative")      
while rate<=0:
    rate = float(input("enter rate "))
    if rate<=0:
        print("rate cannot be zero or negative")        
while time<=0:
    time = int(input("enter time "))
    if time<=0:
        print("time cannot be zero or negative")        
total = principle * pow((1 + rate/100),time)
print(f"total is {total}")