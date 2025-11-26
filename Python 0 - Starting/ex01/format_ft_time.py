
import time
from datetime import datetime

unix = datetime.now().timestamp
now = datetime.now()
x = time.time()
print("Seconds since January 1, 1970:", end=" ")
print(f"{x:,.4f} or", end=" ")
print(f"{x:.2e}", "in scientific notation")
print(now.strftime("%b %d %G"), end="")
