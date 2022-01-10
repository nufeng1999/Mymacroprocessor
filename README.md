# Mymacroprocessor
python file macro processor 

Support label
```
if,ifdef,ifndef,elif,else,endif,defined,define,undef
```
test.py
```
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
```
command
```
    python .\Mymacroprocessor.py .\test3.py
```
out
```
##%log:1
print("test1")
print("test2")
print("test3")
print("this is test code.")
```
call function
```
testcontent1='''
#%indentunit 4
#%define dbglog(x) ##(x)
##%log:1
#%define DEBUG
#%define TEST1

dbglog("test1")
dbglog("测试2")
dbglog("测试3")

#%if defined TEST:
print("this is test code.")
    #%if defined TEST1:
print("--------TEST1----------.")
    #%endif
#%else:
print("--------1----------.")
print("--------2----------.")
#%endif
#%if defined DEBUG:
M1
#%endif
'''
pyp=Mymacroprocessor()
newcontents=pyp.pymprocessor(testcontent1)
print("--new code---\n"+newcontents)
```
