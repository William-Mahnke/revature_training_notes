"""
What is a context manager? AKA resource manager? Similar to try-with-resources or autoclosable resources.

Often we need to make use of some object, like a Connection object to a database, or something like this. Most of the time, this 
sort of resource cannot simply cease to exist. It must gracefully terminate. In the example of some network connection, maybe we 
need to inform the other side of the connection that it will go dark. We don't want to just leave the other end dangling. We get 
unintended consequences when things like this occur. For instance, that database conenction remains alive on the database side. 
So if there are a max of 10 connections, and we fail to gracefully close one, now we have remaining max of 9. 

So often we need to close these resources out gracefully, and it is a problem when we forget, so let's make it automatic. 
We can make these things happen, but we need to set up some infrastructure. Many languages do this, in Java we have try-with-resources.
In python, we have "context manager" or "resource manager". We use the python keyword `with`. 

We use `with` to say "this block of code executes with this resource." When that block exits, the resource is automatically closed.



"""

class MyAutoClosable:
    def __init__(self, message):
        self.message = message
        print(self.message)

    def __enter__(self):
        # raise Exception("This is a test")
        print("Enter method...")

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Here we would perform whatever steps are necessary to terminate and destroy this object.
        # In the case of a network connection to a database or something, we would gracefully close the connection, 
        # maybe informing the other side that we are terminating.

        # Those extra three params are in case exceptions have occurred in or around the `with` block. If an exception happened 
        # that was unhandled, these values will be present. Otherwise each is None.
        # So a simple way to handle this might be:
        if exc_type or exc_val or exc_tb:
            print("We would now need to handle the exception that happened... I think this situation should be pretty rare.")
            print(exc_type)
            print(exc_val)
            import traceback
            traceback.print_tb(exc_tb)
        # raise Exception("This is a test")
        print("gracefully unload the resource!")




if __name__ == "__main__":
    try:
        with MyAutoClosable("Creating the new resource.") as a:
            raise Exception("This is a test")
            print("We have an autoclosable now. Next it should get closed as we leave the `with` block scope.")
            # Right here!
    except:
        print("We got an exception")

    print("We're outside the with block, resources should already be closed.")