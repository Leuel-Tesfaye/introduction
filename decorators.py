# #? A decorator is a function that takes another function as an input and returns a modified version of that function as an output

def announce (f) :
    def wrapper ():
        print(f"About to run the function ...")
        f()
        print("Done with the function")
    return wrapper

@announce 
def hello():
    print("hello, world!")

hello()