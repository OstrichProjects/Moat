import MoatIter

class TestClass:
    def test_create(self):
        # Test to make sure incr_dict can generate tree from empty dict
        assert MoatIter.incr_dict({},('a','b','c')) == {'a':{'b':{'c':1}}}
    def test_incr(self):
    	test = MoatIter.incr_dict({},('a','b','c'))
        # Test to make sure incr_dict can increment an existing leaf
        assert MoatIter.incr_dict(test,('a','b','c')) == {'a':{'b':{'c':2}}}

    def test_add(self):
    	test = MoatIter.incr_dict(MoatIter.incr_dict({},('a','b','c')),('a','b','c'))
        # Test to make sure incr_dict can add leafs without upsetting existing structure
        assert MoatIter.incr_dict(test,('a','b','d')) == {'a':{'b':{'c':2,'d':1}}}

    def test_overleaf(self):
    	test = MoatIter.incr_dict(MoatIter.incr_dict(MoatIter.incr_dict({},('a','b','c')),('a','b','c')),('a','b','d'))
        # Test to make sure incr_dict overwrites leaf with new branch if leaf is not at end of input tuple
        assert MoatIter.incr_dict(test,('a','b','c','d')) == {'a':{'b':{'c':{'d':1},'d':1}}}
        
    def test_overbranch(self):
    	test = MoatIter.incr_dict(MoatIter.incr_dict(MoatIter.incr_dict(MoatIter.incr_dict({},('a','b','c')),('a','b','c')),('a','b','d')),('a','b','c','d'))
        # Test to make sure incr_dict overwrites branch if a node is at the end of a tuple and is not a leaf
        assert MoatIter.incr_dict(test,('a','b')) == {'a':{'b':1}}

    def test_long(self):
       	# Test to make sure incr_dict runs for long inputs
       	assert MoatIter.incr_dict({},('a','b','c')*1000000)