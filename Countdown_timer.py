#importing the time module
import time

#making a timer function
def timer(t):
    #looping until t is not 0
    while t:
        # divmod takes two parameters, first param is divide by second. 
        # Output is a quotient[mins] and remainder[secs].
        mins, secs = divmod(t, 60)

        # :02d is a format function that assign two zeros to the left of the given number.
        # for eg. timer is at 5:9 secs this will be 05:09 there are to zeroes and 
        # they are replaced by the number.'{:02d} : {:02d}' will be '00:00' and we format with mins and secs
        # '00:00' format with '1:7' secs it will be '01:07'.
        timer = '{:02d}:{:02d}'.format(mins, secs)

        #end='\r' replaces the old printed number to the new
        #if you not use end='\r' output will be
        #00.05
        #00.04
        #00.03
        #00.02
        #00.01
        #00.00
        #rather than all in one line replacing the previous
        print(timer, end='\r')

        time.sleep(1)
        t-=1
    print("Time finished!")
if __name__ ==  "__main__":

    inp = int(input('Enter time in Seconds : '))

    timer(inp)