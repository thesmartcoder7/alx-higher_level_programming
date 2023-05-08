#!/usr/bin/python3

# Here's what that code does, step by step:
# - Take the number 98 and store it in the computer's memory.
# - Take two more numbers, called "a" and "b", and store them in the computer's memory too.
# - Raise the number "a" to the power of the number "b".
# - Add the number 98 to the result of step 3.
# - Give the final answer back to whoever asked for it.

def magic_calculation(a, b):
    """
        This function loads the constant 98 onto the stack,
        loads the values of a and b onto the stack using the
        LOAD_FAST instruction, raises a to the power of b using
        the BINARY_POWER instruction, adds 98 to the result using
        the BINARY_ADD instruction, and returns the result using
        the RETURN_VALUE instruction.
    """
    return 98 + (a ** b)
