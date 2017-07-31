# Assignment: Filter by Type
# Write a program that, given some value, tests that value for its type.
#Here's what you should do for each type:
    # Integer
    # If the integer is greater than or equal to 100, print "That's a big number!"
    # If the integer is less than 100, print "That's a small number"
    #
    # String
    # If the string is greater than or equal to 50 characters print "Long sentence."
    # If the string is shorter than 50 characters print "Short sentence."
    #
    # List
    # If the length of the list is greater than or equal to 10 print "Big list!"
    # If the list has fewer than 10 values print "Short list."

def FilterByType( anObj ) :
    print("  Input: '" + str(anObj) + "'")
    if ( isinstance( anObj, int )):
        if (anObj >= 100):
            print("    That's a big number!")
        else:
            print("    That's a small number")
    elif ( isinstance( anObj, basestring )):
        if (len(anObj) >= 50):
            print("    Long sentence.")
        else:
            print("    Short sentence.")
    elif ( isinstance( anObj, list )):
            if (len(anObj) >= 50):
                print("    Big list!")
            else:
                print("    Short list.")
    else :
        print ("    I don't know what object this is.")


FilterByType(45)
FilterByType(100)
FilterByType(455)
FilterByType(0)
FilterByType(-23)
FilterByType("Rubber baby buggy bumpers")
FilterByType("Experience is simply the name we give our mistakes")
FilterByType("Tell me and I forget. Teach me and I remember. Involve me and I learn.")
FilterByType("")
FilterByType([1,7,4,21])
FilterByType([3,5,7,34,3,2,113,65,8,89])
FilterByType([4,34,22,68,9,13,3,5,7,9,2,12,45,923])
FilterByType([])
FilterByType(['name','address','phone number','social security number'])
