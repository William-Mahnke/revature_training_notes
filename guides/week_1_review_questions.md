# Week 1 - Review Questions

The following are specific questions related to concepts covered in Week 1 of training. If you are able to confidently answer the questions in this review guide, you should be able to confidently answer any question related to the week 1 material.

## Compiled vs. Interpreted Languages

**What does it mean for a language to be interpreted rather than compiled?**

- A compiled language requires a build step to translate source code into machine code which is then executed line-by-line. Interpreted languages don't require a build step, allowing code to be translated and executed line by line.

**Why do compiled languages generally produce faster-running programs?**

- Compiled languages translate an entire program into machine-executable code before being run. This is faster than interpreted languages, where each individual line a program has to be translated before execution (line by line).

**Why do interpreted languages tend to have faster development cycles?**

- Interpreted languages have faster development cycles because developers don't have to create a build step like they do in compiled languages, i.e. the code can quickly be tested and iterated on rather than reconfiguring a build step each  time.

**What is dynamic typing and how does it differ from static typing?**

- Dynamic typing refers to the fact that variable data types are evaluated at runtime rather than being evaluated before execution (static typing). This means for Python, a language which features dynamic typing, any errors and exceptions raised related to a variable's data type would arise while the program is being run rather than before.

**What is meant by Python's batteries included philosophy?**

- The batteries included philosophy for Python refers to the vast dependency library avaiable to developers when creating software, allowing them to install packages such as numpy and pandas to contribute to the software with their specific functionality.

## The REPL

**What does REPL stand for and what does each letter represent?**

- REPL stands for Read, Evaluate, Print, and Loop. Read refers to the interpreter "reading" the code given in the terminal, then "evaluting" the code before "printing" an results if necessary and repeating the process (in a loop).

**How do you launch and exit the Python REPL?**

- Using the `python` command in a terminal will launch REPL and the command `exit()` will exit REPL.

**What are the limitations of the REPL for writing full programs?**

- REPL isn't well-suited for running the same set of commands over an over compared to using an IDE to run python. Additionally, using a terminal to execute code doesn't scale as full programs grow in size.

## Package Management (PIP, PyPI, and requirements.txt)

**How would you verify that Python and PIP are correctly installed on your machine?**

- Within your system's terminal, the command `python --version` will verify if python is installed and also supply the version of python installed. The same command with pip instead of python will do the same.

**What does PIP stand for and what is its purpose?**

- PIP stands for "Package installer for Python", it's used by developers to install dependencies such as numpy and pandas to use when developing python software.

**What is PyPI and how does it relate to PIP?**

- PyPI is a third-party dependency library for python, PIP is used to install packages for in PyPI.

**How would you install a specific version of a package using PIP?**

- If you wanted to install a specific version of numpy, the command would be `pip install numpy==version_num`

**What is a requirements.txt file and why is it useful?**

- When working with code in python which relies on dependencies, a requirements file specifies what depedencies are needed to run every file within a project with the option to also specify a specific version of a dependency.

**What command generates a requirements.txt from your current environment?**

- `pip freeze requirements.txt`

**What command installs all packages listed in a requirements.txt file?**

- `pip install -r requirements.txt`

## Virtual Environments

**What problem do virtual environments solve?**

- When working with other contributors on a python project, a virtual environment can be added with all the necessary dependencies to make that project work. It enables developers to be on the same page while providing a setup to avoid installing packages on each developer's local machine.

**What happens when you run pip install while a virtual environment is active?**

- Running pip install when a virtual environment is active will install the dependecy to the virtual environment rather than the developer's local system.

**Why is it considered best practice to use a virtual environment for every project?**

- Using a virtual environment is considered best practice because it provides a clean, reusable method for running code within a project without navigating local installations.

**What is the difference between installing a package globally versus inside a virtual environment?**

- installing a pacakge globally will allow importing the package for the selected interpreter (version of Python). Using a virtual environment limits using the package to that specific virtual environment, usually contained within a single project.

**How do you create and activate a virtual environment on your operating system?**

- `venv .venv` followed by `source .venv/bin/activate`

**What effect does activating a virtual environment have on pip install?**

- All packages installations with pip added the package to the virtual environments library, usually a file within the virtual environment folder created.

**How would another developer recreate your virtual environment on their machine?**

- with their virtual environment created and the requirements file copied, `pip install -r requirements.txt`

## Comments and Docstrings

**What is the purpose of a comment in Python and how does the interpreter handle them?**

- In python, the interpreter will ignore comments when be executed at run time. The purpose of comments in code to describe why functionality is in the program.

**What symbol is used to write a single-line comment in Python?**

- the hashtag (#)

**How do you write a multi-line comment in Python?**

- Multi-line comments in python could be done using a hastag of multiple lines in a row, or the better option is to wrap comment text in triple quotes (creating a docstring).

**What is a docstring and how does it differ from a regular comment?**

- A docstring is usually used at the beginning of a module, function, class, or other entity to describe its purpose within the program and are returning using the doc dunder method. Single line comments are for shorter explanations, while a docstring can be added to provide for nuanced details on an entity's funcitonality.

**Why can over-commenting code be a problem?**

- Over commenting can be a problem because it makes the code less readable to a developer or contributor.

**What Python built-in feature can be used to read a function's docstring?**

- `__docs__`

## Primitive Data Types and Type Casting

**What are the primitive data types in Python?**

- The primitive data types of python are strings, floating point values, intergers, boolean values, and the None type. There is also the complex data type built into python but that's more for programs for physics and scientific purposes.

**What is the difference between an int and a float?**

- an integer is for whole number values while a float is for decimal values.

**How can you check the type of a variable in Python?**

- `type()`

**What is type casting and when might you need to use it?**

- type casting is using python's built in functions such as `int()` or `float()` to convert primitve data type to a different one. A common example is when a program requires user inputs for numeric values because Python's built-in `input()` functions always saves the result as a string.

**What are the only two possible values of a bool?**

- True and False

**What would happen if you tried to add an int and a str together without type casting?**

- you would get a type error

## Operators

**What is the difference between / and // in Python?**

- a single backslash is for normal division and will return a float value, a double backslash represents integer division and always returns an integer.

**What does the modulo operator % return?**

- the modulo operator returns the remainder of division (for example 5 % 2 returns 1, the remainder for 5 / 2)

**What is the difference between = and ==?**

- a single equal sign is used to assign values to variables, a double equal sign evaluates an expression to a boolean value based on whether the values are the same or use the same position in memory.

**What do comparison operators always return?**

- a boolean, either True or False

**Explain the difference between and or and not.**

- `and` evaluates to true only if both expressions are true, `or` evalutes to true if at least one of the expressions in true, and `not` returns the opposite of an expressions's boolean nature.

**What is the difference between == and is?**

- == is used to check for value equality while `is` is used to check for value identity, This is particularly useful for comparing string values. Two identical strings can return true when compared using an equal sign but `is` might return to false because the objects' identities aren't the same in memory.

**How would you use a membership operator to check if a value exists in a list?**

- `value_checking` in `list_name`

**What does the  operator do?**

- [TO CHECK IN THE FUTURE]

## Identifiers, Keywords, and Naming Conventions

**What is an identifier in Python?**

- an identifier is a name given to a variable, function, class, or other object.

**What are the rules for naming a valid identifier?**

- Python keywords shouldn't be used when creating identifiers. Identifiers for variables and functions should use snake case convention (an underscore between each term in the identifier) while classes use PascalCasing (capitalize first letter of each term in identifier).

**What is a keyword and why can't keywords be used as identifiers?**

- a keyword is a specific term in python which has a specific use within the language, they shouldn't be used as identifiers so the program doesn't confuse an entity associated with a keyword identifer for python's built-in functionality.

**What naming convention should be used for variables and functions in Python?**

- snake_case

**What naming convention should be used for class names in Python?**

- PascalCase

## Input, Output, and f-strings

**What function is used to display output in Python?**

- `print()`

**What function is used to capture user input in Python?**

- `input()`

**What data type does input() always return?**

- string

**Why is type casting important when working with user input?**

- if a user's input is intended to be a numeric value (float or integer), type casting is used to convert the string value returned from using `input()` to the desired data type.

**What is an f-string and how is it different from a regular string?**

- f-strings are formatted string literals. Using curly braces allows the developer to display outputs from `print()` in a specific manner and allows the inclusion of dynamic values within the returned string literal.

**How do you embed expressions inside an f-string?**

- f"Embedded value: {inside the curly braces}"

## Functions: Basics

**What is a function?**

- a named block of code to perform a specific task. this allows a developer to write code once and use it multiple times.

**What does the DRY principle stand for and how do functions help enforce it?**

- DRY stands for don't repeat yourself, emphasizes the fact you don't have to repeatedly write the same lines of code to perform the same task.

**What is the benefit of breaking a program into many smaller functions?**

- Breaking up a program into smaller chunks promotes modularity and makes the code more readable. If a program breaks up logical steps of a task into different functions, this also aids identifying the root cause of a bug or error when troubleshooting.

**What is the difference between a built-in function and a user-defined function?**

- Built-in functions are pre-written by other developers and come ready to use "out of the box". Meanwhile, user-defined functions have to be created by the developer and also requires the developer to write the code for the function.

**Name three built-in Python functions and describe what they do.**

- `len()` returns the number of elements within a value such as values in a list, characters in a string, or key-value pairs in a dictionary.
- `sum()` will aggregate the values in a data structure such as a list or tuple
- `round()` will return a floating point value rounded to a specified number of decimal places (or to the nearest place value)

**How do functions improve the maintainability of a codebase?**

- Breaking up a program into logical chunks is easier to maintain a codebase because it will be easier to identify which function causes an error/exception in runtime. Additionally, if any adjustments to the process defined in a function can be made within the function code block and will be applied for every program execution after (do it once).

**What keyword is used to define a function in Python?**

- `def function_name()`

**What is the correct syntax structure for a function definition?**

- A function is defined with `def function_name(parameters):` on the first line. Every subsequent line of the function is idented once.

**What role does indentation play in a Python function?**

- indentation limits the scope of the function's code to just that function rather than executing the code as a part of the program.

**What is the difference between defining a function and calling a function?**

- defining a function is creating the functionality for the function's intended task. Calling a function, with optional parameters, is implementing the function's task (with specific values most of the time).

**Why must a function be defined before it is called?**

- Since python is executed line by line, Python doesn't store the function or its functionality in memory until the lines for the function are executed.

**What is the purpose of the pass keyword in a function body?**

- `pass` means to not return a value associated with a function call and execute the next line of code. It's useful when first creating a function if the developer is unsure how it fits in the program.

**Where should a docstring be placed within a function and what purpose does it serve?**

- a docstring should be the first lines under a function definition, describing what task the function performs alongs with the option to describe parameters for the function.

## Parameters and Arguments

**What is a parameter and where is it defined?**

- a parameter is a identifier inserted into a function's signature when defined. They don't have a value but are given one when a function is called.

**What is a positional parameter and how are values matched to positional parameters?**

- a positional parameter is an assigned value in a function call. multiple positional parameters are defined in a certain order which must be matched in the function call.

**What is a default parameter and what happens if the caller does not provide a value for it?**

- a default parameter is a parameter in a function which is given a value in case one isn't given in a function call. If a user doesn't provide a different value, this default value is applied in the function call.

**What rule must be followed when mixing parameters with and without default values?**

- parameters with default values must be defined after parameters not assigned with a default value.

**What is the difference between a parameter and an argument?**

- parameters are variables listed in a function definition, arguments are values passed to a function when called.

**What does args allow a function to do and what data structure does it collect values into?**

- *args allows the user to input zero to many arguments to a function after providing arguemnts for parameters. When called, the arbitrary arguments are collected into a tuple.

**What does kwargs allow a function to do and what data structure does it collect values into?**

- **kwargs allows the same as args but stores the variables in a dictionary with key value pairs.

**Why are parameters considered local to a function?**

- parameters are defined within the function which means they are only assigned values when the function is called.

**How do you invoke a function in Python?**

- `function_name(parameters)`

**What is a keyword argument and what advantage does it offer over a positional argument?**

- keyword arguments have an associated identifier within the function signature, allows for putting arugments not necessarily in the same order.

## Return Values

**What does the return keyword do in a Python function?**

- returns a value within a function, usually used to return the result of the function's intended task.

**What does a function return if it has no return statement?**

- `None`

**What happens to code written after a return statement in the same function?**

- It won't be run.

**Can a function return more than one value and how does Python handle this?**

- a function can use a tuple or another data structure to return multiple values, but requires unpacking the tuple after the function call.

**Can a returned value be passed directly into another function call?**

- Yes by nesting functions.

## Modules, Packages, and Imports

**What is a Python module?**

- a file containing python code.

**What is the Python standard library and why is it valuable?**

- a collection of pre-written code, modules, and functions which come built into python, no pip installing required.

**What is a package and how does it differ from a module?**

- a module is a single file while a package is a directory containing multiple files/modules

**How do modules promote reusability and separation of concerns?**

- when installed, modules provide the same process of reusing functionality multiple times with having to recreate processes or code.

**What is the purpose of the import statement?**

- `import` statements in python tell the interpreter what functionality from a package or module will be used within this module.

**What is the difference between 'import math' and 'from math import sqrt'?**

- `import math` will tell python to take in all of the functionality from the math package, while the second command only takes in the `sqrt` function from the package.

**What is dot notation and why is it useful when working with imports?**

- using a dot in imports tells the interpreter to import every function/module from a package/module. It's useful when working with imports if a developer only intends to use certain functionality from a module/package.

**Why are wildcard imports from module import  generally discouraged?**

- it's generally better practice to select specific functions/modules from the imported package.

**Can you import multiple items from a module in a single line?**

- Yes, using commas.

## Debugging

**What is debugging and why is it an important skill?**

- debugging is the process of finding and fixing errors in code, crucial for developing functioning programs.

## Memory Management and Garbage Collection

**What is garbage collection and why is it important?**

- Garbage collections is the automatic management and recovery of unused memory to optimzie the amount of memory a python program uses.

**What is reference counting and how does Python use it to manage memory?**

- each object stores a counter tracking how many references point to it

**What happens to an object when its reference count drops to zero?**

- it's immediately deallocated and memory is freed up

**What is a circular reference and why is it a problem for reference counting?**

- occurs when two or more objects/data structures contain references to each other, means neithers' referene count will go to zero

## Control Flow: Conditionals

**What is control flow and why is it important in programming?**

- Flow control is the process of using statements to develop and determine what code is executed based on logical statements and serves as the basis for creating algorithms.

**What is the difference between if elif and else?**

- `elif` are statements which can be added after the `if` block to execute different code based on a separate logical condition. `else` is a statement used to run code if all previous logical statements in `if` and `elif` blocks evaluated to False.

**How does Python decide which block to execute in an if/elif/else chain?**

- always starts with `if`, follows `elif` blocks in order, evaluating the first block to have its logical statement evaluate to true. If none of the conditional statements do so, the code within the else block is executed.

**Can an if statement exist without an else and what happens if the condition is False?**

- Yes, if the condition is false the program continues execution with the next line.

**What is truthiness in Python and can you name four falsy values?**

- Every python object inheriantly is True when switched to boolean type, except for empty strings, empty lists, empty tuples, empty dictionaries, empty sets, 0, 0.0, and None.

**Why does the order of elif conditions matter?**

- Within a set of if and elif statements, only the first block with the logical condition evaluated to true is executed, so the order of statements defines the logic of the algorithm.

**How would you write an if statement that checks whether a list is empty using truthiness?**

- `if not list_name` (if list is empty -> ~Flase -> True)

**What logical operators can be used to combine conditions in an if statement?**

- `and` and `or`

## For Loops and range()

**What is a for loop and what types of objects can it iterate over?**

- A for loop repeats the same operations over a sequence until the sequence is exhausted or until a logical condition (within the code block) evaluates to False. It can iterate over strings, tuples, lists, dictionaries, sets, and other iterables.

**How do you iterate over just the values of a dictionary?**

- `for val in dict_name.values()`

**How do you iterate over both keys and values of a dictionary at the same time?**

- `for key, value in dict.items()`

**When is a for loop preferred over a while loop?**

- When the user wants to iterate over a collection of items.

**What does range() do and what does it return?**

- range() creates a sequence of integers to be, returns a range object iterable.

**What is the default start value for range() if only one argument is provided?**

- `range(n)` provides 1, 2, ..., n-1

**Is the stop value in range() inclusive or exclusive?**

- exclusive

**What does the third argument in range(start stop step) control?**

- the step/jump between integers, i.e. the difference between integers in the sequence.

**How would you use range() to count backwards from 10 to 1?**

- `range(10, 1, -1)`

**Why is range() considered memory efficient?**

- range() creates an iterator which generates values on demand rather than allocating memory to a the array of integers.

## break and continue

**What is the difference between break and continue?**

- break ends a while loop while continue tells the while loop skips the rest of the code in the block to the next iteration.

**When break is encountered where does program execution jump to?**

- the program execution moves to the next line in the same indentation as the while loop the break was a part of and skips the rest of code indented in the while loop.

**When continue is encountered what happens to the rest of the current loop iteration?**

- the code for the rest of the current loop is skipped.

**Give an example of a scenario where using break would be appropriate, and an example where using continue would be appropriate.**

- break is often implemented in infinite loops to end the loop when a particular logical condition is met. if the logical condition is complex (requires two if statements), continue can be used in an infinite loop to go to the next iteration is the first logical condition is met and a subsequent logical condition isn't satisfied.

## while Loops

**What is the key difference between a for loop and a while loop?**

- loops are implemented when a finite collection is being used for iteration, while loops are useful if the desired outcome is continue iteration until a specific logical condition is met.

**When is a while loop more appropriate than a for loop?**

- when the duration of the iteration isn't known ahead of time.

**What happens if the condition of a while loop is False before the loop starts?**

- the code block within the while loop will be skipped.

**What is an infinite loop and what typically causes one? Can you halt an infinite loop?**

- the most common infinite loop uses `while True` and requires a break for a specific logical condition to be broken. Otherwise it runs forever.

## match Statements

**How is match similar to switch statements in other languages?**

- it evaluates an expression and branches execution based on the first matching pattern

**What does case : represent in a match statement?**

- It represents the wild card outcome if not of the previous match statements' logical conditions evaluate to true.

**What happens if more than one case pattern could match the subject?**

- the code within the first case statement to be true will be run, the other one would be skipped.

**How does matching sequences work in a match statement?**

- match statements are evaluated in order.

**When is a match statement more appropriate than an if/elif/else chain?**

- if statements are better for logical conditions on a range of values, match statements are better for more specific values.

## Variable Scope (LEGB)

**What is variable scope and why does it matter?**

- variable scope is where in the program a variable is accessible. it's important to check track of because it determines when and where variables can be accessed and used in a program.

**What does the LEGB rule stand for and in what order does Python search through these scopes?**

- 1st local, 2nd enclosing, 3rd global, 4th built-in

**What happens to a local variable when a function finishes executing?**

- they are garbage collected.

**What is the difference between a local and a global variable?**

- local variables are defined within the statement/function/class they are defined, global variables are defined within the scope of the file.

**What is an enclosing scope and in what situation does it apply?**

- enclosing refers to being in scope of any nested functions.

## String Interning

**What is string interning and what is its purpose?**

- string interning is the process of resuing memory for identical strings. if two different variables are assigned to an identical string, string interning can be done to verify the variables share the same place in memory leading to is conditions evaluating to true.

**What can happen if you use is to compare strings that were not automatically interned?**

- comparing non-interned strings using `is` might evaluate to false.

**How can you manually intern a string in Python and when might this be useful?**

- using `sys.intern()`, useful when you want to check if a string generated through operations is identical to a string already defined in the program.

**Why is string interning described as an implementation detail rather than a language guarantee?**

- string interning isn't automatically done in python or some other languages, so it's a detail which has to be implemented rather than an assumption being made in design.

**How does string interning relate to memory and performance optimisation?**

- string interning converse memory when multiple variables all route to the same memory address.

## Lambda Functions

**What is a lambda function and how does it differ from a function defined with def?**

- a lambda is an anonymous function used in line to perform an operation, ususally in the context of a named function.

**What is the syntax of a lambda function?**

- `lambda parameters: expression`

**Why are lambdas called anonymous functions?**

- they aren't named.

**What are the most common use cases for lambdas in Python?**

- short-lived in-line process as a part of another function

**When should you use a def function instead of a lambda?**

- for a more complex function which will be used repeatedly with varying parameters.

## Generator Expressions and Lazy Evaluation

**What is a generator expression and how does its syntax differ from a list comprehension?**

- generator expressions produce values on demand, uses parentheses instead of brackets like done in list comprehension.

**What does lazy evaluation mean in the context of a generator expression?**

- lazy evaluation means values are generator on demand, one at a time

**What type of object does a generator expression return?**

- a generator object rather than a list

**How do you retrieve values from a generator expression?**

- `next()`

**Why are generator expressions more memory-efficient than list comprehensions?**

- list comprehensions generate the entire list at once and allocate memory for the entire array, generator expressions don't allocate memory for the whole list but rather generates the values as they're needed.

**What does it mean for a generator to be exhausted and what happens when you iterate over an exhausted generator?**

- exhausted means every value in the generator object has been generated, have to create a new generator to iterate again.

**When should you choose a generator expression over a list comprehension?**

- useful for one off functionality rather than needing the entire list of values at once.

**Can you pass a generator expression directly to sum() or max()?**

- yes, `sum(generator)`

## map(), filter(), and reduce()

**What does map() do and what does it return?**

- map() applies a function to every item, returning a map object.

**What does filter() do and what does it return?**

- filters items for a specific condition, returns a subset of the given input (list -> list, tuple -> tuple, etc.)

**What does reduce() do and when is it useful?**

- reduce aggregates an entire list to a single value by cumulatively apply a function.

**What is the difference between map() and a list comprehension?**

- list comprehension will return the entire list where map gnerators the list object.

## Exceptions and Exception Handling

**What is an exception and how does it differ from a syntax error?**

- An exception is an object raised at runtime to signal that something has gone wrong and disrupted the normal flow of the program. A syntax error, by contrast, is caught before the program runs because the code itself isn't valid Python, so it never executes. Exceptions are generally recoverable and meant to be handled, whereas errors typically are not.

**What happens to a program when an exception is raised and not handled?**

- The exception propagates up the call stack until it reaches the top of the program. If nothing handles it, the program terminates and Python prints a traceback to the console showing the exception type, its message, and where it occurred.

**What does it mean for exceptions to have a hierarchy and why does that matter?**

- All exceptions inherit from a common base class (`Exception`), forming a hierarchy where specific exceptions like `ZeroDivisionError` or `KeyError` descend from more general ones. This matters because an `except` block for a parent class also catches its children, so you must order your `except` blocks from most specific to most general to ensure each exception is handled by the right block.

**What is exception handling and why is it important?**

- Exception handling is the practice of anticipating and gracefully responding to errors that may occur at runtime, using `try`/`except` blocks. It's important because it lets a program recover and continue running, or fail in a controlled way with a clear message, rather than crashing unexpectedly.

**What is the purpose of the try block?**

- The `try` block contains the code that might raise an exception. Python attempts to run it normally, and if an exception occurs, control immediately jumps to the matching `except` block instead of crashing.

**What is the purpose of the except block and when does it run?**

- The `except` block defines how to respond when an exception is raised in the `try` block. It only runs if a matching exception type (or one of its subclasses in the hierarchy) is raised; otherwise it is skipped.

**How do you handle multiple different exception types in the same try/except structure?**

- You can chain multiple `except` blocks, each handling a different exception type, ordered from most specific to most general. Alternatively, you can group several exceptions into a single block by passing them as a tuple, e.g. `except (IndexError, KeyError) as e`.

**What is the difference between catching a specific exception versus catching a parent exception?**

- Catching a specific exception (like `ZeroDivisionError`) lets you handle one precise problem with tailored logic. Catching a parent exception (like `Exception`) acts as a catch-all for a whole category of errors, which is convenient but risks hiding bugs you didn't anticipate.

**What does the else block do in a try/except structure and when does it run?**

- The `else` block runs only if the `try` block completes without raising any exception. It is used for code that should run on success, keeping it separate from the code that might fail in the `try` block.

**What does the finally block do and when does it run?**

- The `finally` block always runs, whether or not an exception was raised and whether or not it was handled. It runs last, after the `try`, `except`, and `else` blocks.

**Why is finally useful and what is it typically used for?**

- Because it always executes, `finally` is ideal for cleanup tasks that must happen no matter what, such as closing files, releasing locks, or closing database connections.

**How do you capture the exception object and how do you access its message?**

- You capture it with the `as` keyword, e.g. `except Exception as e`, which binds the exception object to a variable. You can then access its message by printing it directly, often in an f-string like `print(f"Error: {e}")`, while `type(e).__name__` gives the exception's class name.

**Why is it bad practice to catch 'Exception'?**

- Since nearly every exception inherits from the base `Exception` class, catching it swallows every possible error, including ones you didn't anticipate like typos or logic bugs. This can mask real problems and make debugging much harder, so it's better to catch the specific exceptions you actually expect.

## Custom Exceptions

**What is a custom exception and why would you define one?**

- A custom exception is an exception class you define yourself, usually for a situation specific to your application's domain that the built-in exceptions don't describe well. Defining one makes your error handling more descriptive and lets calling code catch and respond to that specific error by name (e.g. `InvalidAgeError`, `DuplicateEmployeeError`).

**What class should custom exceptions inherit from?**

- The built-in `Exception` class (or a more specific built-in exception when appropriate). You can also override `__init__` to store extra context, like the invalid value, while calling `super().__init__()` to set the message.

**What naming convention should custom exception classes follow?**

- PascalCase, like all class names, and by convention the name ends in "Error" (e.g. `InvalidSalaryError`).

**How do you make use of a custom exception in your program?**

- You trigger it manually with the `raise` keyword, typically passing a descriptive message, e.g. `raise InvalidAgeError("Age must be between 18 and 100.")`. It can then be caught in a `try`/`except` block just like any built-in exception.

## Data Structures: Overview

**What is a data structure and why does choosing the right one matter?**

- a data strucutre is a method for organizing and storing data to be accessed and modified efficiently.

**What are the four key characteristics to consider when comparing data structures?**

- time complexity, space complexity, data relationships, and operations on the data

**What is the difference between a mutable and an immutable data structure?**

- elements in a mutable data structure can be changed within the object, immutable objects can't

**Name four built-in Python data structures.**

- lists, tuples, sets, and dictionaries

**What is the collections module and what does it provide?**

- collections module provides additional data structures such as queues and deques

**Why is defaulting to a list for every situation not always the best approach?**

- tuples can be better than lists when modifying elements isn't needed. in the case of accessing particular values, the built in hashing functionality of dictionaries is quicker than the linear behavior of accessing list elements.

## Lists

**What does it mean for a list to be ordered and mutable?**

- each element in the list has a corresponding index for which the elements are ordered by, mutable implies elements can be modified within the list.

**What is zero-based indexing and what index refers to the last item in a list?**

- index for a data structure starts at 0, -1 for last item

**How does negative indexing work in Python?**

- access elements from reverse order, list[-n] refers to the nth to last element in the list for example

**What is slicing and what does mylist1:4] return?**

- returns the elemnts in indices 1, 2, and 3.

**What is the difference between .remove() and .pop()?**

- pop removes an item and returns the removed value, remove just removes the value and returns nothing.

**What is the difference between .sort() and the built-in sorted() function?**

- sort() modifies the original data strucutre, sorted() returns a new, sorted object.

**How do you access an item in a nested list?**

- `list[index_1[index_2]]`

**Can a Python list hold items of different types?**

- Yes

## Tuples

**What is the key difference between a list and a tuple?**

- lists are mutable, tuples are immutable

**What does immutability mean in the context of a tuple?**

- elements of a tuple can't be modified without creating a new object

**What is tuple unpacking and how does it work?**

- extracting elements of a tuple and assigning them to new variables

**What is tuple packing?**

- grouping multiple distinct values into a tuple

**Why can tuples be used as dictionary keys but lists cannot?**

- dictionary keys must be immutable

**What are two common use cases where a tuple is more appropriate than a list?**

- when data is fixed and shouldn't be changed and when accessing data (faster for tuples than lists)

## Sets

**What are the defining characteristics of a set?**

- mutable, unordered collection of items

**How do you create an empty set and why can't you use {}?**

- `set()`

**What happens if you add a duplicate value to a set?**

- the set doesn't change (automatically removed)

## Deque and the collections Module

**What does deque stand for and where does it come from in Python?**

- double ended queue, from the collections module

**What limitation of Python lists does the deque address?**

- the time complexity of appending an element to the front of a list

**What is the difference between .append() and .appendleft() on a deque?**

- append adds to end to deque (list end of list), appendleft for inserting in the front of deque

## List and Dictionary Comprehensions

**What is list comprehension and what does it produce?**

- a concise method for creating a list from an existing iterable

**What is the basic syntax of a list comprehension?**

- `[expression for item in iterable]`

**How do you add a filtering condition to a list comprehension?**

- `[expression for item in iterable for condition]`

**What is the equivalent for loop pattern that list comprehension replaces?**

- `for item in list: new_list.append(expression(item))`

**What is a dict comprehension and how does its syntax differ from a list comprehension?**

- `{key: value for item in iterable}`

## Iterators and Iterables

**What is an iterator in Python?**

- an object which produces items one at a time

**What two dunder methods must an iterator implement?**

- `__iter__()` to return the iterator object, `__next()_`_ to access next item in iterator object

**What does next() return and what does it do when the sequence is exhausted?**

- returns next item in iterator, StopIteration raised when iterator is exhausted

**What happens internally when Python executes a for loop?**

- uses an iterator object to lazily generate values

**What does the built-in iter() function do?**

- returns the iterator object

**Why are iterators described as single-use?**

- once all values in an iterator has been exahusted, can't be used again

**How would you build a custom iterator class?**

- define the class, `__init__` method, `__next__` method, and `__iter__` method

**What is an iterable and what method must it implement?**

- an object which can be looped over

**Give four examples of built-in Python iterables.**

- lists, sets, tuples, and dictionaries

**What is the key difference between an iterable and an iterator?**

- an iterable has all items already allocated in memory, iterator returns values lazily

**Can you loop over the same iterable multiple times and what about an iterator?**

- yes, and no

**What does calling iter() on an iterable return?**

- return an iterator object for the iterable

**Why is the iterable/iterator distinction important for understanding how for loops work?**

- for loops call iterators internally because it's more memory efficient, iterable might be more useful for list comprehension

## Dictionaries

**What is a dictionary and how does it differ from a list?**

- pairs of keys and values

**What are the requirements for a dictionary key?**

- immutable and unique

**What types of data can be stored as dictionary values?**

- anything

**What is the difference between accessing a value with "key"] versus .get("key")?**

- .get will return None is the key doesn't exist while brackets would crash the program

**How do you add a new key-value pair to an existing dictionary?**

- `dict["new_key] = value`

**What do .keys() .values() and .items() return and how are they used?**

- .keys for keys, values same, .items returns the pair as a tuple

**What does .update() do and what happens if a key exists in both dictionaries?**

**What does .setdefault() do and how does it differ from a regular assignment?**

- defines a value for a paritcular key if it doesn't exist in the dictionary, doesn't change the value if the key already exists

## zip()

**What happens when you zip two iterables of different lengths?**

- it will only zip objects up to the length of the shorter iterables, elements left in the longer iterable aren't included

**How does itertools.ziplongest() differ from zip() and when would you use it?**

- used when iterables have different lengths, filled with None or 0

**What does zip(zipped) do and what is this operation called?**

- unzips a zipped object, i.e. returns the two iterables originally zipped

**Why is zip() described as lazy and what is the memory benefit of this?**

- the zip object is a lazy iterator of tuples, so pairs of values are generated on demand rather than allocating memory

## Decorators and the with Statement

**What is a decorator and what does it do to the function it is applied to?**

- A decorator is a function that takes another function (or method) and extends or modifies its behavior without changing its source code, typically by wrapping it so behavior can be added before and/or after the original runs.

**How is a decorator applied to a function in Python?**

- With the `@` symbol placed on the line directly above the function definition, e.g. `@decorator_name` above `def my_func():`.

**Can you give an example of a decorator used in a Python framework?**

- Built-in examples include `@staticmethod` (a method that needs neither the instance nor the class), `@classmethod` (which receives the class itself as `cls` and is often used as an alternative constructor), and `@abstractmethod` (which forces subclasses to implement a method). Web frameworks like Flask also use decorators such as `@app.route()` to map a URL to a function.

**What problem does the with statement solve and what did code look like before it?**

- The `with` statement is a context manager that automatically acquires and releases a resource, guaranteeing cleanup (like closing a file or database connection) even if an exception occurs inside the block. Before it, you had to use `try`/`finally` and manually call `close()` in the `finally` block to ensure the resource was released. Under the hood, a context manager implements the `__enter__` and `__exit__` dunder methods.

## Object-Oriented Programming: Basics

**What is Object-Oriented Programming and what is it centred around?**

- OOP is a programming paradigm centered on organizing code into objects, which bundle together related data (attributes) and behavior (methods). This promotes modularity, reusability, and readability by modeling real-world entities as self-contained units.

**What is the difference between a class and an object?**

- A class is a blueprint or template that defines the attributes and methods its instances will have. An object is a concrete instance of a class, created from that blueprint with its own actual data.

**What is the difference between an attribute and a method?**

- An attribute is a piece of data or property associated with a class or object (its state), while a method is a function defined inside a class that describes the behavior or actions an object can perform.

**What are the four pillars of Object-oriented programming?**

- Abstraction (hiding complexity behind a simple interface), Encapsulation (bundling data with the methods that operate on it and restricting direct access), Inheritance (deriving new classes from existing ones to reuse code), and Polymorphism (allowing different classes to be used through a common interface).

**Why is Python described as a multi-paradigm language rather than a purely OOP language?**

- Because Python supports several programming styles, not just OOP. You can write simple procedural scripts, use functional techniques (lambdas, `map`, `filter`), or build full object-oriented programs. OOP is available when it helps manage complexity, but Python doesn't force everything to be a class the way a purely OOP language might.

## Classes, init, and self

**What does the init method do and when is it called?**

- `__init__` is the constructor method. It runs automatically right after a new object is created, and it's used to initialize the object's instance attributes with the values passed in.

**What is self and why is it needed?**

- `self` is a reference to the specific instance the method is being called on. It's the first parameter of instance methods and lets each object access and store its own attributes, distinguishing one instance's data from another's.

**What is the difference between an instance attribute and a class attribute?**

- A class attribute is defined at the top level of the class and is shared by all instances, while an instance attribute is defined on a specific object (usually inside `__init__` via `self`) and belongs only to that object. Assigning to an attribute on one instance creates or shadows it on that instance without affecting the class attribute or other instances.

**How would you check whether an object is an instance of a particular class?**

- Use the built-in `isinstance(object, ClassName)`, which returns `True` or `False` and also accounts for inheritance. `type(object)` returns the exact class but is less flexible for inheritance checks.

**How do you access an attribute on an object?**

- With dot notation: `object.attribute_name`.

## Dunder Methods and Operator Overloading

**What are dunder methods and why are they called that?**

- Dunder ("double underscore") methods are special methods whose names begin and end with two underscores, like `__init__`, `__str__`, or `__len__`. Python calls them automatically in response to built-in operations and syntax, which lets your objects integrate with language features such as construction, printing, and `len()`.

**What dunder method would you define to control what len() returns for your object?**

- `__len__`

**What is operator overloading and which dunder methods enable it?**

- Operator overloading is defining how built-in operators behave for your custom objects by implementing the corresponding dunder methods, e.g. `__add__` for `+`, `__sub__` for `-`, `__mul__` for `*`, and `__eq__` for `==`. This lets you write expressions like `obj1 + obj2` on your own types.

**How does type casting work with custom Python objects?**

- When you call a built-in conversion function on a custom object, Python looks for the matching dunder method and calls it to produce the converted value. For example, `int(obj)` invokes the object's `__int__` method and `str(obj)` invokes `__str__`.

**What dunder method is called when you use int() on a custom object?**

- `__int__`

## File Handling

**Why should you always use 'with open(...)' rather than calling 'open()' directly?**

- Because `with open(...)` is a context manager that automatically closes the file when the block ends, even if an exception is raised. Calling `open()` directly requires you to remember to call `close()` yourself (typically in a `try`/`finally`), and forgetting to do so can leak resources or leave data unwritten.

**What is the default file mode if none is specified?**

- read ('r')

**What is the difference between 'w' and 'a' mode?**

- 'w' (write) opens the file for writing and overwrites any existing content, while 'a' (append) preserves the existing content and adds new data to the end. Both create the file if it doesn't already exist.

**What does 'x' mode do and when is it useful?**

- 'x' (exclusive create) creates a new file for writing but raises a `FileExistsError` if a file with that name already exists. It's useful when you want to guarantee you aren't overwriting an existing file.

**What is binary mode, with respect to reading files, and when is it required?**

- Binary mode ('rb'/'wb') reads or writes the file as raw bytes instead of decoded text. It's required for non-text files such as images, audio, or other binary formats, where decoding to a string would corrupt the data.

**Why should you always specify encoding="utf-8" explicitly when opening text files?**

- Because the default encoding depends on the operating system, so the same code can behave differently across machines. Explicitly setting `encoding="utf-8"` makes reading and writing consistent and portable regardless of platform.

**How do you rewind a file to the beginning after reading it?**

- Call `file.seek(0)` to move the cursor back to the start of the file.

**What are three exceptions you should handle when working with files?**

- `FileNotFoundError` (the file doesn't exist), `PermissionError` (no access rights), and `UnicodeDecodeError` (the content can't be decoded with the given encoding).

**What mode must a file be opened in to read its content?**

- 'r' (read mode), which is also the default.

**When should you use 'a' mode instead of 'w' mode?**

- When you want to add to a file without destroying what's already there, such as appending to a log file across multiple runs. 'w' would overwrite the existing content each time.

**Why is using the 'with' keyword especially important when writing files?**

- Because writes are often buffered, the data may not actually be saved to disk until the file is flushed and closed. The `with` statement guarantees the file is properly closed (and the buffer flushed) when the block ends, even if an error occurs, preventing data loss.

**What does f.write() return?**

- The number of characters written (or bytes, in binary mode).

## Logging

**What is logging and how does it differ from using print() statements?**

- process of recording program execution to a designated file/location, better than using print statements because logging has different levels to note different levels of severity for issues that arise

**Name some reasons why logging is important in production software.**

- creating a logging system is crucial to identity potential fixes to make for code, creates a "story" of what went well and what didn't go well when executing a program

**What three things should a well-written log entry capture?**

- what happended, when it happened, and why it happened

**Why can over-logging be a problem and what is the goal of good logging practice?**

- over logging can provide a lot of noise which drowns out key issues

**What is the root logger and how do you use it?**

- the default logger when no configuration details are added

**What is a named logger and how do you create one?**

- a logger designed for a specific issue (as the name would indicate), created with `logging.getLogger(__name__)`

**Why is name recommended as the logger name?**

- reflacts the name of the module the logger will be in, if multiple loggers go to the same location it helps separates messages for different files

**What does logging.basicConfig() do and what are its key parameters?**

- configures the loggers behaviors, key parameters being the logging level, the format of the logged message, filename for the output, filemode for file type, and the format of the date (when it happened)

**What is a handler and what are two common handler types in Python's logging module?**

- handlers are used to control the behavior of the log messages

**What is a formatter and how do you attach one to a handler?**

- a component in logging framework to translate raw events into a strcutured message

**How do you configure a logger to send output to both the console and a file simultaneously?**

- using `StreamHandler(sys.stdout)` , requires imporing sys

**What is the difference between setting a level on a logger versus setting a level on a handler?**

- setting a level with a handler can be configured with a different file path to output different logging levels to particular locations

**What are the five standard logging levels in Python in order from lowest to highest severity?**

- DEBUG, INFO, WARNING, ERROR, CRITICAL

**What is the default logging level for the root logger and what does this mean in practice?**

- debug, means it picks up every possible message

**Why is logging to a file preferable to console-only logging in a production environment?**

- can keep records of a program's executions over multiple sessions of tests

**How do you direct log output to a file using logging.basicConfig()?**

- `logging.basicConfig(filename = "file_name")`

**What problem does RotatingFileHandler solve and what two parameters control its behaviour?**

- it will automatically rotate out log files with new ones when they reach a certain size, managed with `maxBytes` and `backupCount`

**What is the difference between RotatingFileHandler and TimedRotatingFileHandler?**

- rotating is based on max file size, timed is based on a defined interval

**What does backupCount control and why is it important to set it?**

- how many old log files to keep, important depending on how much information you want to keep

**What are two practical habits that make file logging easier to maintain in production?**

- implement automatic log rotation and adopt a strcutured logging directory

## unittest: Basics

**What is unittest and what does it provide out of the box?**

- a built-in library to manage and handle unit tests

**What class must a test case inherit from and what naming convention must test methods follow?**

- `unittest.TestCase`

**How do you run unittest tests from the command line?**

- `python -m unittest`

**What is a test suite and how does it differ from a test case?**

- a test suite is a collection of test cases grouped together for execution

**What is regression testing and why is automated testing valuable for it?**

- rerunning previous after implementing a new feature to ensure existing functionality wasn't broken

## Assertions

**What is the purpose of assertion methods in unittest?**

- Assertion methods define the expected outcome of the code under test by comparing actual results against expected values. If the assertion holds, the test passes; if it doesn't, the assertion fails and marks the test as failed.

**What happens when an assertion fails? What happens when all assertions pass?**

- When an assertion fails, that test is marked as failed and the runner reports which test failed along with the expected versus actual values. If all assertions in a test pass, the test passes and the runner moves on, typically ending with a summary of how many tests passed and failed.

**Why is it better to use specific assertions (e.g. assertIsNone) rather than always using assertTrue?**

- Specific assertions like `assertIsNone`, `assertEqual`, or `assertIn` produce clearer, more informative failure messages (showing exactly what was expected versus what was received), whereas `assertTrue` only reports that a condition was false. They also express intent more readably and avoid writing more complex boolean expressions.

**How do you add a custom failure message to an assertion?**

- Pass a string as an extra `msg` argument after the assertion's values, e.g. `self.assertEqual(a, b, "values should match")`. That message is displayed if the assertion fails.

**Which assertion would you use to check that a value appears in a list?**

- `assertIn`, e.g. `self.assertIn(value, my_list)`.

## Testing Exceptions

**Why is it important to test that exceptions are raised and not just the happy path?**

- Because robust code must handle invalid input and edge cases gracefully, not just the ideal "happy path." Testing that the right exception is raised for bad input confirms your error handling actually works and guards against regressions where validation might silently break.

**What happens if the code inside assertRaises does not raise any exception?**

- The test fails, because `assertRaises` expects the specified exception to be raised. If no exception (or a different type) occurs, it reports the failure.

**What is the difference between assertRaises and assertRaisesRegex?**

- `assertRaises` only checks that a given exception type is raised, while `assertRaisesRegex` additionally verifies that the exception's message matches a given regex pattern. The latter is useful for confirming not just the type but the specific reason for the error.

**If a function can raise a ValueError for two different reasons how would you test each reason separately?**

- Use `assertRaisesRegex` with a distinct pattern matching each error message, so each test confirms the `ValueError` was raised for the correct reason rather than just that some `ValueError` occurred.

## Skipping Tests

**What are the three main skip decorators in unittest and how do they differ?**

- skip("reason") skip regardless of a condition, skipIf to skip a test should a condition evalute to true, and skipUnless to perform the opposite (skip the test unless a condition is true)

**When is it appropriate to use @unittest.skip and when should it be avoided?**

- skip can be used when a portion of functionality maybe hasn't been fully implemented or isn't ready for tests, but should be used sparingly as it implies there is unintended behavior in the program

**What does @unittest.expectedFailure do and what does an unexpected success indicate?**

- marks tests which are supposed to fail, an unexpected success means fucntionality isn't behaving as intended (just with the inverse logic which usually governs testing)

**Why should skipping tests be used sparingly?**

- they represent unintended behavior in a program

## Test Fixtures

**What is a test fixture and why are fixtures useful?**

- A test fixture is the setup and teardown code that prepares a known, consistent state before tests run and cleans up afterward. Fixtures are useful because they avoid repeating setup code in every test and ensure each test starts from a clean state, so tests stay independent and don't affect one another.

**What is the difference between setUp and setUpClass?**

- `setUp` runs before every individual test method, giving each test a fresh starting state, while `setUpClass` runs only once before all tests in the class. `setUpClass` is better for expensive, shared setup that doesn't need to be repeated, whereas `setUp` is for per-test isolation.

**Why must setUpClass and tearDownClass be decorated with @classmethod?**

- Because they operate at the class level rather than on a single instance. They run once for the whole class, before any individual test instance is set up, so they receive the class (`cls`) instead of `self`, which is exactly what the `@classmethod` decorator provides.

**When does a TearDown function run? Why does this matter?**

- `tearDown` runs after each test method, regardless of whether the test passed or failed. This matters because it cleans up any state or resources the test created, preventing data from leaking between tests and keeping them independent.

## External Test Data

**Why is it beneficial to store test data in external files rather than hard-coding it in test methods?**

- provides modularity for the program, also ensures data is kept safe and unaltered from testing fucntionality

**What formats are commonly used for external test data and what is each well suited for?**

- JSON (structured data, better when data is complex and multi-layered), CSV (strucutred like a table to reflect commonly used data in the real world), and text files

**What is subTest and how does it differ from a plain loop inside a test method?**

- a context manager to run the same test logic for each data item, provides a way to test against multiple sets of data to ensure logic is correct

**Where should test data files be stored within a project and why?**

- in a separate data/ folder, cleaner and keeps tests readable

## Mocking

**What is mocking and why is it used in unit testing?**

- Mocking is the practice of replacing real dependencies with controlled, fake substitutes during testing. It's used so you can test a piece of code in isolation without involving slow or unpredictable external systems, while still being able to configure return values and verify how the dependency was used.

**What kinds of dependencies are typically replaced with mocks?**

- External or hard-to-control dependencies such as databases, web APIs, file systems, network calls, and service-layer objects, i.e. anything that would make a test slow, flaky, or dependent on external state.

**How does mocking improve test speed repeatability and independence?**

- By removing reliance on real external systems, mocks make tests fast (no real I/O or network calls), repeatable (no dependence on changing external state), and independent (each test controls its own fake data rather than sharing a real resource).

**Beyond checking return values what else can you verify using a mock object?**

- You can verify the interactions with the mock: whether it was called (`assert_called_once`), how many times it was called (`call_count`), and what arguments it was called with (`assert_called_once_with`, `call_args`, `call_args_list`).

**What is the difference between Mock and MagicMock?**

- `MagicMock` is a subclass of `Mock` that additionally pre-configures Python's magic (dunder) methods like `__len__`, `__iter__`, `__enter__`, and `__getitem__`. A plain `Mock` raises an error if the code uses it with `len()`, in a `with` block, or with bracket indexing, whereas `MagicMock` supports those out of the box.

**What does returnvalue configure and how does it differ from attribute access on a mock?**

- `return_value` configures what the mock returns when it is called like a function (e.g. `mock.return_value = 100` means `mock()` returns 100). Accessing an attribute on a mock instead returns a new child mock automatically, rather than a configured value.

**How do assertcalledonce() and assertcalledoncewith() differ?**

- `assert_called_once()` only verifies the mock was called exactly once, while `assert_called_once_with()` also checks that the single call was made with the specific arguments provided.

**What information is stored in callargs versus callargslist?**

- `call_args` stores the arguments of the most recent call (as a `call` object with `.args` and `.kwargs`), while `call_args_list` is a chronological list of `call` objects recording the arguments of every call made to the mock.

**When would you choose MagicMock over Mock?**

- When the code under test uses the mock in a way that relies on magic methods, such as a context manager (`with` block), an iterator, `len()`, or bracket indexing. It's also a reasonable default when mocking complex real-world objects.

**What is sideeffect and how does it differ from returnvalue?**

- `side_effect` lets a mock do something dynamic when called: raise an exception, run a function, or return successive values from an iterable. `return_value` just hands back a single fixed value. `side_effect` is for when calling the mock needs to trigger behavior beyond returning one static result.

**If both sideeffect and returnvalue are set on a mock which takes priority?**

- `side_effect` takes priority (unless it returns the special `DEFAULT` sentinel, in which case `return_value` is used).

**What does patch do and why is it useful for testing functions with external dependencies?**

- `patch` temporarily replaces an object in a module's namespace with a mock for the duration of a test, then automatically restores the original afterward. It's useful because you can swap out an external dependency (like `requests.get`) without modifying the production code. The key rule is to patch the object where it's used, not where it's defined.
