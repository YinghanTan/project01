from IPython import embed as ipython

# import random
# def find_max(values):
#     max = 0
#     import pdb; pdb.set_trace()
#     for val in values:
#         if val > max:
#             max = val
#     return max
# find_max(random.sample(range(100), 10))

def foo(bar=[]):
    bar.append("baz")
    return bar

def test1():
    # import pdb;pdb.set_trace()
    # import ipdb; ipdb.set_trace()
    breakpoint()
    response = foo()
    response = foo()
    return response
print(test1())
