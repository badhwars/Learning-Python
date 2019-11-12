from datetime import datetime

def main():
    now =datetime.now()  # gives todays date and time with milliseconds
    print(now)
    print(now.strftime("The current year os %Y"))  #extracts year from the now
    print(now.strftime("%a , %d %B , %y")) # a -> day %d -> date %B -> Month October %y -> year 19
    print(now.strftime("Localdate and time %c"))
    print(now.strftime("Localdate %x"))
    print(now.strftime("Local time %X"))

    print(now.strftime("Current time %I : %M : %S %p"))
    print(now.strftime("25 Hour time %H: %M"))



main()