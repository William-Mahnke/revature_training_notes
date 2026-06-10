"""
Exceptions are used for error handling - what should be returned if something goes wrong. The return is the good exit to the funciton,
after the function is complete successfully we exit the function returning to the "calling code". An exception means something has gone
wrong, and we DO NOT take that exit door. We never get there, instead we take the "emergency eject".

So in reality there are two ways out of a function back to the calling code. We can return successfully, or we can fail with exception.
If we fail with exception, we now need extra instructions to handle the situation we find ourselves in.

If we don't gracefully handle the exception we are in "unintended behavior" which is super bad.
So we can handle exceptions in one of two ways:
 - we can actually handle it (try/except)
 - make someone else handle it (make some other code handle it) - re-raise the exception


How do we decide to handle or re-raise?
 - Does it make sense?
 - Is this problem my responsibility?
 - Do I have the tools here to handle it?

in some cases there's a mix of both, maybe certain circumstances or exceptions should be handled here, but others shouldn't.

"""
import random


def calling_function():
    
    try:
        risky_func(random.randint(0, 4))
    except KeyError as e:
        print(e)
        print("We have a simulated KeyError!")
    except AssertionError as e:
        print(e)
        print("We have a simulated AssertionError!")
    except Exception as e:
        # print(e)
        print("We had an Exception! Oh no! We can't handle this here!")
        raise
    except e: # We won't ever actually hit this one, because all valid objects to "raise" are Exception or inherit from Exception.
        print(e)
        print("We had some kind of exception...")
    else:
        print("Else block is for when there is no exception.")
    finally:
        print("The finally block always happens, and happens after everything else.")
    
    print("Now we are out of the try/except block")


def risky_func(do = 0):
    """
    We would give a sdescription here of the function, it's params, and return value(s), and finally talk about possible exceptions.

    - rasies: Exeption - in case 1
    - raises: AssertionError - in case 2
    - raises: KeyError - in case 3
    """
    match(do):
        case 0:
            print("No exceptions!")
        case 1: 
            raise Exception("Case 1, exception simulated!")
        case 2:
            raise AssertionError("Case 2, assertion error imulated!")
        case 3:
            raise KeyError("case 3, KeyError simulated.")
        case 4: 
            raise CustomException("case 4: custom exception!") # EJECT EJECT!
        
    #  Down here we have left the switch and had no exceptions.
    print("Today is a good day!") # If we ejected above, we cannot get here.


# The simplest custom exception does nothing except have its own class name
class CustomException(Exception):
    pass






# THIS IS MAIN
if __name__ == "__main__":
    try:
        calling_function()
    except CustomException as e:
        print(e)
        print("Custom exception bubbled up to main.")
    print("The program finished successfully")