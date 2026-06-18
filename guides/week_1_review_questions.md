# Week 1 - Review Questions

The following are specific questions related to concepts covered in Week 1 of training. If you are able to confidently answer the questions in this review guide, you should be able to confidently answer any question related to the week 1 material.

* What does it mean for a language to be interpreted rather than compiled?
* What is dynamic typing and how does it differ from static typing?
* What is meant by Python's batteries included philosophy?
* How would you verify that Python and PIP are correctly installed on your machine?
* What does PIP stand for and what is its purpose?
* What is PyPI and how does it relate to PIP?
* How would you install a specific version of a package using PIP?
* What is a requirements.txt file and why is it useful?
* What problem do virtual environments solve?
* What happens when you run pip install while a virtual environment is active?
* Why is it considered best practice to use a virtual environment for every project?
* What does REPL stand for and what does each letter represent?
* How do you launch and exit the Python REPL?
* What are the limitations of the REPL for writing full programs?
* Why do compiled languages generally produce faster-running programs?
* Why do interpreted languages tend to have faster development cycles?
* What is the purpose of a comment in Python and how does the interpreter handle them?
* What symbol is used to write a single-line comment in Python?
* How do you write a multi-line comment in Python?
* What is a docstring and how does it differ from a regular comment?
* Why can over-commenting code be a problem?
* What Python built-in feature can be used to read a function's docstring?
* What are the primitive data types in Python?
* What is the difference between an int and a float?
* How can you check the type of a variable in Python?
* What is type casting and when might you need to use it?
* What are the only two possible values of a bool?
* What would happen if you tried to add an int and a str together without type casting?
* What is the difference between / and // in Python?
* What does the modulo operator % return?
* What is the difference between = and ==?
* What do comparison operators always return?
* Explain the difference between and or and not.
* What is the difference between == and is?
* How would you use a membership operator to check if a value exists in a list?
* What does the \*\* operator do?
* What is an identifier in Python?
* What are the rules for naming a valid identifier?
* What is a keyword and why can't keywords be used as identifiers?
* What naming convention should be used for variables and functions in Python?
* What naming convention should be used for class names in Python?
* What function is used to display output in Python?
* What function is used to capture user input in Python?
* What data type does input() always return?
* Why is type casting important when working with user input?
* What is an f-string and how is it different from a regular string?
* How do you embed expressions inside an f-string?
* What is a function?
* What does the DRY principle stand for and how do functions help enforce it?
* What is the benefit of breaking a program into many smaller functions?
* What is the difference between a built-in function and a user-defined function?
* Name three built-in Python functions and describe what they do.
* How do functions improve the maintainability of a codebase?
* What keyword is used to define a function in Python?
* What is the correct syntax structure for a function definition?
* What role does indentation play in a Python function?
* What is the difference between defining a function and calling a function?
* Why must a function be defined before it is called?
* What is the purpose of the pass keyword in a function body?
* Where should a docstring be placed within a function and what purpose does it serve?
* What is a parameter and where is it defined?
* What is a positional parameter and how are values matched to positional parameters?
* What is a default parameter and what happens if the caller does not provide a value for it?
* What rule must be followed when mixing parameters with and without default values?
* What is the difference between a parameter and an argument?
* What does \*args allow a function to do and what data structure does it collect values into?
* What does \*\*kwargs allow a function to do and what data structure does it collect values into?
* Why are parameters considered local to a function?
* How do you invoke a function in Python?
* What is a keyword argument and what advantage does it offer over a positional argument?
* What does the return keyword do in a Python function?
* What does a function return if it has no return statement?
* What happens to code written after a return statement in the same function?
* Can a function return more than one value and how does Python handle this?
* Can a returned value be passed directly into another function call?
* What is a Python module?
* What is the Python standard library and why is it valuable?
* What is a package and how does it differ from a module?
* How do modules promote reusability and separation of concerns?
* What is the purpose of the import statement?
* What is the difference between 'import math' and 'from math import sqrt'?
* What is dot notation and why is it useful when working with imports?
* Why are wildcard imports from module import \* generally discouraged?
* Can you import multiple items from a module in a single line?
* What is debugging and why is it an important skill?
* What is the difference between installing a package globally versus inside a virtual environment?
* How do you create and activate a virtual environment on your operating system?
* What effect does activating a virtual environment have on pip install?
* How would another developer recreate your virtual environment on their machine?
* What command generates a requirements.txt from your current environment?
* What command installs all packages listed in a requirements.txt file?
* How do requirements.txt and virtual environments work together?
* What is garbage collection and why is it important?
* What is reference counting and how does Python use it to manage memory?
* What happens to an object when its reference count drops to zero?
* What is a circular reference and why is it a problem for reference counting?
* What is control flow and why is it important in programming?
* What is the difference between if elif and else?
* How does Python decide which block to execute in an if/elif/else chain?
* Can an if statement exist without an else and what happens if the condition is False?
* What is truthiness in Python and can you name four falsy values?
* Why does the order of elif conditions matter?
* How would you write an if statement that checks whether a list is empty using truthiness?
* What logical operators can be used to combine conditions in an if statement?
* What is a for loop and what types of objects can it iterate over?
* How do you iterate over just the values of a dictionary?
* How do you iterate over both keys and values of a dictionary at the same time?
* When is a for loop preferred over a while loop?
* What does range() do and what does it return?
* What is the default start value for range() if only one argument is provided?
* Is the stop value in range() inclusive or exclusive?
* What does the third argument in range(start stop step) control?
* How would you use range() to count backwards from 10 to 1?
* Why is range() considered memory efficient?
* What is the difference between break and continue?
* When break is encountered where does program execution jump to?
* When continue is encountered what happens to the rest of the current loop iteration?
* Give an example of a scenario where using break would be appropriate, and an example where using continue would be appropriate
* What is the key difference between a for loop and a while loop?
* When is a while loop more appropriate than a for loop?
* What happens if the condition of a while loop is False before the loop starts?
* What is an infinite loop and what typically causes one? Can you halt an infinite loop?
* How is match similar to switch statements in other languages?
* What does case \_: represent in a match statement?
* What happens if more than one case pattern could match the subject?
* How does matching sequences work in a match statement?
* When is a match statement more appropriate than an if/elif/else chain?
* What is variable scope and why does it matter?
* What does the LEGB rule stand for and in what order does Python search through these scopes?
* What happens to a local variable when a function finishes executing?
* What is the difference between a local and a global variable?
* What is an enclosing scope and in what situation does it apply?
* What is string interning and what is its purpose?
* What can happen if you use is to compare strings that were not automatically interned?
* How can you manually intern a string in Python and when might this be useful?
* Why is string interning described as an implementation detail rather than a language guarantee?
* How does string interning relate to memory and performance optimisation?
* What is a lambda function and how does it differ from a function defined with def?
* What is the syntax of a lambda function?
* Why are lambdas called anonymous functions?
* What are the most common use cases for lambdas in Python?
* When should you use a def function instead of a lambda?
* What is a generator expression and how does its syntax differ from a list comprehension?
* What does lazy evaluation mean in the context of a generator expression?
* What type of object does a generator expression return?
* How do you retrieve values from a generator expression?
* Why are generator expressions more memory-efficient than list comprehensions?
* What does it mean for a generator to be exhausted and what happens when you iterate over an exhausted generator?
* When should you choose a generator expression over a list comprehension?
* Can you pass a generator expression directly to sum() or max()?
* What does map() do and what does it return?
* What does filter() do and what does it return?
* What does reduce() do and when is it useful?
* What is the difference between map() and a list comprehension?
* What is an exception and how does it differ from a syntax error?
* What happens to a program when an exception is raised and not handled?
* What does it mean for exceptions to have a hierarchy and why does that matter?
* What is exception handling and why is it important?
* What is the purpose of the try block?
* What is the purpose of the except block and when does it run?
* How do you handle multiple different exception types in the same try/except structure?
* What is the difference between catching a specific exception versus catching a parent exception?
* What does the else block do in a try/except structure and when does it run?
* What does the finally block do and when does it run?
* Why is finally useful and what is it typically used for?
* How do you capture the exception object and how do you access its message?
* Why is it bad practice to catch 'Exception'?
* What is a custom exception and why would you define one?
* What class should custom exceptions inherit from?
* What naming convention should custom exception classes follow?
* How do you make use of a custom exception in your program?
* What is a data structure and why does choosing the right one matter?
* What are the four key characteristics to consider when comparing data structures?
* What is the difference between a mutable and an immutable data structure?
* Name four built-in Python data structures.
* What is the collections module and what does it provide?
* Why is defaulting to a list for every situation not always the best approach?
* What does it mean for a list to be ordered and mutable?
* What is zero-based indexing and what index refers to the last item in a list?
* How does negative indexing work in Python?
* What is slicing and what does my\_list\[1:4] return?
* What is the difference between .remove() and .pop()?
* What is the difference between .sort() and the built-in sorted() function?
* How do you access an item in a nested list?
* Can a Python list hold items of different types?
* What is the key difference between a list and a tuple?
* What does immutability mean in the context of a tuple?
* What is tuple unpacking and how does it work?
* What is tuple packing?
* Why can tuples be used as dictionary keys but lists cannot?
* What are two common use cases where a tuple is more appropriate than a list?
* What are the defining characteristics of a set?
* How do you create an empty set and why can't you use {}?
* What happens if you add a duplicate value to a set?
* What does deque stand for and where does it come from in Python?
* What limitation of Python lists does the deque address?
* What is the difference between .append() and .appendleft() on a deque?
* What is list comprehension and what does it produce?
* What is the basic syntax of a list comprehension?
* How do you add a filtering condition to a list comprehension?
* What is the equivalent for loop pattern that list comprehension replaces?
* What is a dict comprehension and how does its syntax differ from a list comprehension?
* What is an iterator in Python?
* What two dunder methods must an iterator implement?
* What does \_\_next\_\_() return and what does it do when the sequence is exhausted?
* What happens internally when Python executes a for loop?
* What does the built-in iter() function do?
* Why are iterators described as single-use?
* How would you build a custom iterator class?
* What is an iterable and what method must it implement?
* Give four examples of built-in Python iterables.
* What is the key difference between an iterable and an iterator?
* Can you loop over the same iterable multiple times and what about an iterator?
* What does calling iter() on an iterable return?
* Why is the iterable/iterator distinction important for understanding how for loops work?
* What is a dictionary and how does it differ from a list?
* What are the requirements for a dictionary key?
* What types of data can be stored as dictionary values?
* What is the difference between accessing a value with \["key"] versus .get("key")?
* How do you add a new key-value pair to an existing dictionary?
* What do .keys() .values() and .items() return and how are they used?
* What does .update() do and what happens if a key exists in both dictionaries?
* What does .setdefault() do and how does it differ from a regular assignment?
* What happens when you zip two iterables of different lengths?
* How does itertools.zip\_longest() differ from zip() and when would you use it?
* What does zip(\*zipped) do and what is this operation called?
* Why is zip() described as lazy and what is the memory benefit of this?
* What is a decorator and what does it do to the function it is applied to?
* How is a decorator applied to a function in Python?
* Can you give an example of a decorator used in a Python framework?
* What problem does the with statement solve and what did code look like before it?
* What is Object-Oriented Programming and what is it centred around?
* What is the difference between a class and an object?
* What is the difference between an attribute and a method?
* What are the four pillars of Object-oriented programming?
* Why is Python described as a multi-paradigm language rather than a purely OOP language?
* What does the \_\_init\_\_ method do and when is it called?
* What is self and why is it needed?
* What is the difference between an instance attribute and a class attribute?
* How would you check whether an object is an instance of a particular class?
* How do you access an attribute on an object?
* What are dunder methods and why are they called that?
* What dunder method would you define to control what len() returns for your object?
* What is operator overloading and which dunder methods enable it?
* How does type casting work with custom Python objects?
* What dunder method is called when you use int() on a custom object?
* Why should you always use 'with open(...)' rather than calling 'open()' directly?
* What is the default file mode if none is specified?
* What is the difference between 'w' and 'a' mode?
* What does 'x' mode do and when is it useful?
* What is binary mode, with respect to reading files, and when is it required?
* Why should you always specify encoding="utf-8" explicitly when opening text files?
* How do you rewind a file to the beginning after reading it?
* What are three exceptions you should handle when working with files?
* What mode must a file be opened in to read its content?
* When should you use 'a' mode instead of 'w' mode?
* Why is using the 'with' keyword especially important when writing files?
* What does f.write() return?
* What is logging and how does it differ from using print() statements?
* Name some reasons why logging is important in production software.
* What three things should a well-written log entry capture?
* Why can over-logging be a problem and what is the goal of good logging practice?
* What is the root logger and how do you use it?
* What is a named logger and how do you create one?
* Why is \_\_name\_\_ recommended as the logger name?
* What does logging.basicConfig() do and what are its key parameters?
* What is a handler and what are two common handler types in Python's logging module?
* What is a formatter and how do you attach one to a handler?
* How do you configure a logger to send output to both the console and a file simultaneously?
* What is the difference between setting a level on a logger versus setting a level on a handler?
* What are the five standard logging levels in Python in order from lowest to highest severity?
* What is the default logging level for the root logger and what does this mean in practice?
* Why is logging to a file preferable to console-only logging in a production environment?
* How do you direct log output to a file using logging.basicConfig()?
* What problem does RotatingFileHandler solve and what two parameters control its behaviour?
* What is the difference between RotatingFileHandler and TimedRotatingFileHandler?
* What does backupCount control and why is it important to set it?
* What are two practical habits that make file logging easier to maintain in production?
* What is unittest and what does it provide out of the box?
* What class must a test case inherit from and what naming convention must test methods follow?
* How do you run unittest tests from the command line?
* What is a test suite and how does it differ from a test case?
* What is regression testing and why is automated testing valuable for it?
* What is the purpose of assertion methods in unittest?
* What happens when an assertion fails? What happens when all assertions pass?
* Why is it better to use specific assertions (e.g. assertIsNone) rather than always using assertTrue?
* How do you add a custom failure message to an assertion?
* Which assertion would you use to check that a value appears in a list?
* Why is it important to test that exceptions are raised and not just the happy path?
* What happens if the code inside assertRaises does not raise any exception?
* What is the difference between assertRaises and assertRaisesRegex?
* If a function can raise a ValueError for two different reasons how would you test each reason separately?
* What are the three main skip decorators in unittest and how do they differ?
* When is it appropriate to use @unittest.skip and when should it be avoided?
* What does @unittest.expectedFailure do and what does an unexpected success indicate?
* Why should skipping tests be used sparingly?
* What is a test fixture and why are fixtures useful?
* What is the difference between setUp and setUpClass?
* Why must setUpClass and tearDownClass be decorated with @classmethod?
* When does a TearDown function run? Why does this matter?
* Why is it beneficial to store test data in external files rather than hard-coding it in test methods?
* What formats are commonly used for external test data and what is each well suited for?
* What is subTest and how does it differ from a plain loop inside a test method?
* Where should test data files be stored within a project and why?
* What is mocking and why is it used in unit testing?
* What kinds of dependencies are typically replaced with mocks?
* How does mocking improve test speed repeatability and independence?
* Beyond checking return values what else can you verify using a mock object?
* What is the difference between Mock and MagicMock?
* What does return\_value configure and how does it differ from attribute access on a mock?
* How do assert\_called\_once() and assert\_called\_once\_with() differ?
* What information is stored in call\_args versus call\_args\_list?
* When would you choose MagicMock over Mock?
* What is side\_effect and how does it differ from return\_value?
* If both side\_effect and return\_value are set on a mock which takes priority?
* What does patch do and why is it useful for testing functions with external dependencies?