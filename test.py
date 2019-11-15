import time

print("## Cython ###")
start = time.process_time()
# Import the extension module hello.
import hello
# Call the print_result method 
hello.print_result(23.0)
print(time.process_time() - start)

print("## CPython ###")
start = time.process_time()
def square_and_add(x):
    return pow(x, 2.0) + x

print(square_and_add(23.0))
print(time.process_time() - start)
