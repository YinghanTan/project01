import datetime
import time
from IPython import embed as ipython
from ipdb import set_trace as ipdb
import pdb;
# pdb.set_trace()

def test_func():
    x=2
    return 2 + x

# x = 0
# while True:
#     print("It is now: ", datetime.datetime.now())
#     ipython()
#     print(f"x='{x}'", test_func result is: {test_func()}")
#     time.sleep(1)


x = 0
while True:
    print("It is now: ", datetime.datetime.now())
    # ipython()
    # ipdb()
    # pdb.set_trace()
    print(f"x='{x}', test_func result is: {test_func()}")
    time.sleep(1)
