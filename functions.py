# SOLUTIONS - BY SARAH FLEMING
################################################################
# PART ONE


# 1. Write a function that does not take any arguments and
#    prints "Hello World".

def hello_world():
    """Print "Hello World", does not accept arguments
    """

    print "Hello World"

# 2. Write a function that takes a name as a string and
#    prints "Hi" followed by the name.

def print_hi(name):
    """print Hi followed by the given name inputed as a string
    """

    print "Hi %s" % (name)


# 3. Write a function that takes two integers and multiplies
#    them together. Print the result.

def multiply(x, y):
    """multiply two integers and print the result
    """

    print x * y

# 4. Write a function that takes a string and an integer and
#    prints the string that many times

def string_print(s, n):
    """given a string and an integer, will print string that many times
    """

    print s * n

# 5. Write a function that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If integer is 0 print "Zero".

def zero_test(n):
    """given an integer, the function will print whether the number is higher than, lower than or equal to zero
    """

    if n > 0:
        print "Higher than 0"
    elif n < 0:
        print "Lower than 0"
    else:
        print "Zero"

# 6. Write a function that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.

def divisible_by_three(n):
    """return true if integer is divisible by 3 otherwise returns false
    """
    if n % 3 == 0:
        return True
    else:
        return False

# 7. Write a function that takes a sentence as one string and
#    returns the number of spaces.

def space_count(sentence_as_string):
    """return number of spaces in the inputted string
    """

    total_spaces = 0

    for i in sentence_as_string:
        if i == " ":
            total_spaces += 1
    return total_spaces

# 8. Write a function that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.

def total_paid(price, tip_as_decimal = .15):
    """return total amount paid with default tax of .15 unless otherwise specified, please enter tip as a decimal
    """

    return price * (1 + tip_as_decimal)

# 9. Write a function that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#	 should be returned in a list.

def integer_info(n):
    """return a list of information about a integer given: will return whether positive or negative and whether even or odd
    """

    #instructions did not specify what to do if the number entered was zero so I added that case

    info = []

    if n == 0: 
        print "integer is zero"
    
    else:
        if n > 0:
            info.append("Positive")
        else:
            info.append("Negative")

        if n % 2 == 0:
            info.append("Even")
        else:
            info.append("Odd")

    return info

#
# 	Then, write code that shows the calling of this function
# 	on a number and unpack what is returned into two
# 	variables --- sign and parity (whether it's positive
# 	or negative). Print sign and parity.

sign, parity = integer_info(5)
print sign, parity

################################################################
# PART TWO


# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).
#
#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviaton, and the
#    default tax amount as parameters.
#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item including tax.

def cost_with_tax(cost, state_abreviation, tax=.05):
    """return cost with default tax of .05, if state is "ca" use .07 as tax
    """

    #confused about why you need to pass in tax amount twice and not the cost of the item, I assumed it was a typo and passed in the cost

    if state_abreviation.lower() == "ca": #in case user enters "CA" or "Ca"
        return cost * (1 + .07)
    else:
        return cost * (1 + tax)

# 2. Turn the block of code from the directions into a function.
#	 Take a name and a job title as parameters, making it so the
# 	 job title defaults to "Engineer" if a job title is not passed in.
#	 Return the person's title and name.

def title_name(name, title="Engineer"):
    """return title and name, if no title is given, function will default to "Engineer"
    """

    return title + " " + name

# 3. Given a receiver's name, receiver's job title, and sender's name, print the following letter:      
#       Dear JOB_TITLE RECEIVER_NAME, I think you are amazing! Sincerely,
#       SENDER_NAME. 
#    Use the function from #2 to construct the full title for the letter's greeting.

def letter(receiver_name, sender_name, receiver_title="Engineer"):
    """print a letter to a receiver, get the receiver's title from the title_name function, title will default to Engineer is no title is specified 
    """

    #this was a bit confusing for me, but once I figured out the instructions it wasn't hard

    receiver = title_name(receiver_name, receiver_title)
    
    print "Dear %s, I think you are amazing!" % (receiver)
    print "Sincerely, %s" % (sender_name)

# 4. Turn the block of code from the directions into a function. This
#    function will take a number and append it to *numbers*. It doesn't
#    need to return anything.

numbers = []

def append_number(num):
    """append number to *numbers*
    """

    numbers.append(num)

