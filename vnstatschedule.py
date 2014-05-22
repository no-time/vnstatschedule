def main():    
    while True:
        import time
        import os
        from subprocess import call
        schedule=tim3()
        print(schedule)
        interface=" "
        while interface==" ":

            interface=input("""
Enter your interface:
(Be careful there is no error checking for this part)
Examples are eth0, wlan0...
""")
            if interface == "":
                break

        while True:
            x= clogger(schedule[2],schedule[3],schedule[4],\
                   schedule[5],interface)

            if x== "done":
                break
        while True:
            x= exit_q()
            if x== "y":
                user_exit=input('''
How would you like your output?
Type (From vnstat --longhelp):
     q,  --query          query database
     h,  --hours          show hours
     d,  --days           show days
     m,  --months         show months
     w,  --weeks          show weeks
     t,  --top10          show top10
     s,  --short          use short output
''')
                call(["vnstat", "-"+str(user_exit), "-i", str(interface),])
            break
        break



def tim3():
    import time

    #current_time=["16", "20"]
    tim3= time.strftime("%H %M")
    current_time=tim3.split()
    print("""


        """+ str(tim3)+"""
        Current time
        """)
    hour=current_time[0]
    minute=current_time[1]
    ui = inputs()
    newlist=[hour, minute]
    schedule=newlist+ui
    print(schedule)
    return schedule
def inputs():
    print("""
------------------------------------------
""")
    while True:
        start_hour=(input("Enter the starting hour (24hr): "))
        start_min=(input("Enter the starting minute: "))
        x = checker(start_hour, start_min)
        endh=(input("How many hours would you like to run? "))
        endm=(input("How many minutes would you like to run? "))
        y = checker(endh,endm)
        if str(x)=="Great":
            if str(y) == "Great":
                return [start_hour, start_min, endh, endm]

def checker(h,m):
    error=0
    message=("Incorrect Format")
    while error==0:
        if h =="":
            print(message)
            break
        if len(str(h))> 2:
            print(message)
            break
        if m =="":
            print(message)
            break
        if len(str(m))>2:
            print(message)
            break
        for x in str(h):
            if x.isdigit() == False:
                error+=1
                print(message)
                break
            if error>0:     
                print(message)
                break
        for y in str(m):
            if y.isdigit() == False:
                error+=1
                print(message)
                break
            if error>0:     
                print(message)
                break
        else:
            return("Great")

def clogger(s1,s2,t1,t2,I):
    import time
    import os
    from subprocess import call
    total_time=int(t1)*60*60+int(t2)*60


    while True:
        h1=int(time.strftime('%H'))
        m2=int(time.strftime('%M'))
        if len(str(s1))<2:
            s1="0"+str(s1)

        if len(str(s2))<2:
            s2="0"+str(s2)

        if len(str(h1))<2:
            h1="0"+str(h1)

        if str(h1)==str(s1) and str(m2)==str(s2):
            while True:
                if total_time>0:

                    call (["vnstat", "-i",str(I)])
                    time.sleep(15)
                    total_time=total_time-15
                    print(total_time," seconds")

                elif total_time<=0:
                    return "done"

        time.sleep(15)




def exit_q():

    while True:
        question=input("Would you like to show a report? (y/n) ")
        if question == "y" or question == "n":
            return question



main()
