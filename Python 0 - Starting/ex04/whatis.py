import sys

x = sys.argv
try:
    assert len(x) <= 2, "more than one argument provided"
    if len(x) == 2:
        assert x[1].isdigit(), "argument is not an integer"
except AssertionError as e:
    print(f"AssertionError: {e}")
    exit(1)
if len(x) == 2:
    n = int(x[1])
    if n % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
else:
    exit(1)
