import MoatRecur

class TestClass:
    def test_create(self):
        test = {}
        MoatRecur.incr_dict(test,('a','b','c'))
        # Test to make sure incr_dict can generate tree from empty dict
        assert test == {'a':{'b':{'c':1}}}
    
    def test_incr(self):
        test = {'a':{'b':{'c':1}}}
    	MoatRecur.incr_dict(test,('a','b','c'))
        # Test to make sure incr_dict can increment an existing leaf
        assert test == {'a':{'b':{'c':2}}}

    def test_add(self):
        test = {'a':{'b':{'c':2}}}
    	MoatRecur.incr_dict(test,('a','b','d'))
        # Test to make sure incr_dict can add leafs without upsetting existing structure
        assert test == {'a':{'b':{'c':2,'d':1}}}

    def test_overleaf(self):
    	test = {'a':{'b':{'c':2,'d':1}}}
        MoatRecur.incr_dict(test,('a','b','c','d'))
        # Test to make sure incr_dict overwrites leaf with new branch if leaf is not at end of input tuple
        assert  test == {'a':{'b':{'c':{'d':1},'d':1}}}

    def test_overbranch(self):
    	test = {'a':{'b':{'c':{'d':1},'d':1}}}
        MoatRecur.incr_dict(test,('a','b'))
        # Test to make sure incr_dict overwrites branch if a node is at the end of a tuple and is not a leaf
        assert test == {'a':{'b':1}}

    def test_long(self):
        test = {}
        MoatRecur.incr_dict(test,('a','b','c')*300)