# ========= COMMON ERRORS ========

# ========= SyntaxError =========
syntactically_wrong = Wrong"
print(syntactically_wrong)

# After running the above code the following error will occur
"""
line 4
    syntactically_wrong = Wrong"
                               ^
SyntaxError: unterminated string literal (detected at line 4)

"""

# ========= NameError ===========

print(hadam)

"""
line 18, in <module>
    print(hadam)
          ^^^^^
NameError: name 'hadam' is not defined

"""

# ========= IndexError =========

list1 = [1,2,3,4]
print(list1[5])

"""
line 31, in <module>
    print(list1[5])
          ~~~~~^^^
IndexError: list index out of range

"""

# ========= TypeError =========

name = "Adam" + 1;
print(name)

"""
line 43, in <module>
    name = "Adam" + 1;
           ~~~~~~~^~~
TypeError: can only concatenate str (not "int") to str

"""
# ========= ValueError =========
inpt1 = int(input("Enter number"))
print(inpt1)

"""
line 54, in <module>
    inpt1 = int(input("Enter number"))
            ^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'ade'

"""

# ========= KeyError =========

dictionary = {
    "one": 1,
    "two":2,
    "three":3
}

print(dictionary["zero"])

"""
line 73, in <module>
    print(dictionary["zero"])
          ~~~~~~~~~~^^^^^^^^
KeyError: 'zero'

"""