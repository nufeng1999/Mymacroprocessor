#%indentunit 4
#%define #dbglog(x) print(x)
##%log:1
#%define DEBUG
#%define TEST

#dbglog("test1")
#dbglog("test2")
#dbglog("test3")

#%if defined TEST:
print("this is test code.")
    #%if defined TEST1:
print("--------TEST1----------.")
    #%endif
#%else:
print("--------1----------.")
print("--------2----------.")
#%endif