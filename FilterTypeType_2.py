# Assignment: Filter by Type
# Write a program that, given some value, tests that value for its type. Here's what you should do for each type:
#
# Integer
# If the integer is greater than or equal to 100, print "That's a big number!" If the integer is less than 100, print "That's a small number"
#
# String
# If the string is greater than or equal to 50 characters print "Long sentence." If the string is shorter than 50 characters print "Short sentence."
#
# List
# If the length of the list is greater than or equal to 10 print "Big list!" If the list has fewer than 10 values print "Short list."
#
import types
def filterTypeType(inValue):
    anint = 4
    aString = "hi"
    aList = [ 'a', 9 ]
    print "Input:", inValue
    inType = type(inValue)
    if inType == type(anint):
        if inValue >= 100:
            print "That's a big number!"
        else:
            print "That's a small number"
    elif inType == type(aString):
        if len(inValue) >= 50:
            print "Long sentence."
        else:
            print "Short sentence."
    elif inType == type(aList):
        if len(inValue) >= 10:
            print "Big list!"
        else:
            print "Short list."
    else:
        print "*"* 10, "I don't understand that one ", "*"* 10
    print " "


sI = 45
filterTypeType(sI)
mI = 100
filterTypeType(mI)
bI = 455
filterTypeType(bI)
eI = 0
filterTypeType(eI)
spI = -23
filterTypeType(spI)
sS = "Rubber baby buggy bumpers"
filterTypeType(sS)
mS = "Experience is simply the name we give our mistakes"
filterTypeType(mS)
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
filterTypeType(bS)
eS = ""
filterTypeType(eS)
aL = [1,7,4,21]
filterTypeType(aL)
mL = [3,5,7,34,3,2,113,65,8,89]
filterTypeType(mL)
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
filterTypeType(lL)
eL = []
filterTypeType(eL)
spL = ['name','address','phone number','social security number']
filterTypeType(spL)
