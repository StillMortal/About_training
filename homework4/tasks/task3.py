"""
Write a function that will receive a string and write it to stderr
if line starts with "error" and to the stdout otherwise.


>>> my_precious_logger("error: file not found")
# stderr
'error: file not found'


>>> my_precious_logger("OK")
# stdout
'OK'

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive tests

You will learn:
 - how to write to stderr
 - how to test output to the stderr and stdout


"""
import sys


def my_precious_logger(text: str):
    """The function that will receive a string and write it to stderr
if line starts with "error" and to the stdout otherwise.

    Args:
        text: String for analysis.

    Returns:
        Nothing.

    """
    if text[:5] != "error":
        sys.stdout.write(text)
    else:
        sys.stderr.write(text)


# my_precious_logger(": file not found")
# print(sys.stdout.)
# print(sys.stderr.)




# import sys
#
# stdout_fileno = sys.stdout
#
# sample_input = ['Hi', 'Hello from AskPython', 'exit']
#
# for ip in sample_input:
#     # Prints to stdout
#     stdout_fileno.write(ip + '\n')

# import sys
#
# stdout_fileno = sys.stdout
# stderr_fileno = sys.stderr
#
# sample_input = ['Hi', 'Hello from AskPython', 'exit']
#
# for ip in sample_input:
#     # Prints to stdout
#     stdout_fileno.write(ip + '\n')
#     # Tries to add an Integer with string. Raises an exception
#     try:
#         ip = ip + 100
#     # Catch all exceptions
#     except:
#         stderr_fileno.write('Exception Occurred!\n')