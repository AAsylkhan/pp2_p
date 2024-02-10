#1 Boolean Values
'''
a Boolean function has two values: True/False

'''
bool() # bool() - boolean function
bool(0) # if num is less than zero, it would be a False
bool(1) # and in other cases it will be True, if value has a greater num than zero, it'll be True 
bool("") # if string/char type value didn't has anything, it will be False
bool("Text")

#2 Most Values are True
'''
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.
'''
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#3 Some Values are False

'''
In fact, there are not many values that evaluate to False, 
except empty values, such as (), [], {}, "", the number 0, 
and the value None. 
And of course the value False evaluates to False.
'''
# The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
'''
One more value, or object in this case, evaluates to False, 
and that is if you have an object that is made from a class 
with a __len__ function that returns 0 or False
'''
#Example:
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#4 Functions can Return a Boolean
#Example:
def myFunction() :
  return True

print(myFunction()) #Print the answer of a function

#Print "YES!" if the function returns True, otherwise print "NO!":

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
  
# isinstance() function can be used to determine if an object is of a certain data type

x = 200
print(isinstance(x, str))
