#!/usr/bin/env python3

class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s

class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        if e in self.vals:
        	self.vals[e] -= 1

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        if e in self.vals:
        	return self.vals[e]
        else:
        	return 0

    def __add__(self, x):
    	new_bag = Bag()
    	for key in self.vals:
    		new_bag.vals[key] = self.count(key)
    	for key in x.vals:
    		if key in new_bag.vals:
    			new_bag.vals[key] += x.count(key)
    		else:
    			new_bag.vals[key] = x.count(key)
    	return new_bag

class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        if e in self.vals:
        	del self.vals[e]

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        if e in self.vals:
        	return True
        else:
        	return False

if __name__=='__main__':
	d1 = Bag()
	d1.insert(4)
	d1.insert(4)
	print(d1)
	d1.remove(2)
	print(d1)

	d1 = Bag()
	d1.insert(4)
	d1.insert(4)
	d1.insert(4)
	print(d1.count(2))
	print(d1.count(4))

	a = Bag()
	a.insert(4)
	a.insert(3)
	b = Bag()
	b.insert(4)
	print(a+b)

	d1 = ASet()
	d1.insert(4)
	d1.insert(4)

	d1.remove(2)
	print(d1)

	d1.remove(4)
	print(d1)

	d1 = ASet()
	d1.insert(4)
	print(d1.is_in(4))
	d1.insert(5)
	print(d1.is_in(5))
	d1.remove(5)
	print(d1.is_in(5))