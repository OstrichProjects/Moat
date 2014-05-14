Submission for Moat Pre-Interview Test
====

There are two different incr\_dict functions, recursive and iterative.  To call these functions in an instance of python, import MoatIter and MoatRecur and run either MoatIter.incr\_dict(dict,tuple) or MoatRecur.incr\_dict(dict,tuple).

Testing
====

To test, install pytest with 

```
pip install pytest
py.test
``` 

while in the Moat parent directory.

Conclusions
====

The recursive function is simpler, but does not work for long input tuples.  The iterative function works for long input tuples, but is a little more complicated.

I decided to always overwrite branches nodes and leaves if the function is called in such a way that a branch node is the last element of the tuple and if a leaf node is not the last element of the tuple.

Examples:

```python
>>> test = {'a': 1}
>>> incr_dict(test,('a','b'))
>>> test
{'a':{'b':1}}
>>> incr_dict(test,('a'))
>>> test
{'a':1}
```
