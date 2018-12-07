import actions as a
import notwatching as n
import addwhitelist as w 
import output as ou

print('hi')
q1 = input('Welcome to interaction with me, what do you want to do? DeleteWatch, AddWhite, or AccessEntry   ')

if q1 != 'DeleteWatch' and q1 != 'AddWhite' and q1!='AccessEntry':
    print('sorry we are still growing, more functions might be provided later ')
else:
    if q1 == 'DeleteWatch':
        q2 = input("do you want to delete anything from the watchlist? reply 'yes' or 'no'    ")
        if q2 == 'yes':
            ip = input('what is the ip that you dont need to watchlist: ')
            name = input('what is the corresponding username: ')
            n.remove_from_watchlist(ip,name)
            q3 = input("do you want to reset the count of this entry? reply 'yes' or 'no'    ")
            if q3 == 'yes':
                n.reset_count(ip,name)
                print('you are all set')
            else:
                print('fine')
            ou.output_watchlist()
    elif q1 == 'AddWhite':
        q4 = input('what is the ip that you want to whitelisted: ')
        w.add_whi(q4)
        print('done')
    else:
        q5 = input("What is the ip that you want to look up for: ")
        q6 = input("Do you know the username? No or [username]")
        if q6 == 'No':
         # if just want to look up by ip without knowing username 
            a.find_ip(q5)
        else:
            q7 = input('which scope? (successful,Invalid, FAILED')
            if q7 != 'successful' and q7 != 'Invalid' and q7 != 'FAILED':
                print('No messing around, see ya')
            else:
                a.resume(q5,q6,q7)

