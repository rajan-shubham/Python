import time
currenttime= time.localtime(time.time())
print("Current time is", currenttime)


names = ["Jacob", "Joe", "Jim"]

if (name := input("Enter a name: ")) in names: #walrus operator
    print(f"Hello, {name}!")
else:
    print("Name not found.")


print("hello ji")

# python3 wierd.py
# Current time is time.struct_time(tm_year=2024, tm_mon=9, tm_mday=15, tm_hour=20, tm_min=1, tm_sec=10, tm_wday=6, tm_yday=259, tm_isdst=0)
# Enter a name: Joe
# Hello, Joe!
# hello ji