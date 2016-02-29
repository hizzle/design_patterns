#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""http://python-3-patterns-idioms-test.readthedocs.org/en/latest/Singleton.html"""

class OnlyOne:
	class __OnlyOne:
		def __init__(self, arg):
			self.val = arg

		def __str__(self):
			return repr(self) + self.val

	instance = None
	def __init__(self, arg):
		if not OnlyOne.instance:
			OnlyOne.instance = OnlyOne.__OnlyOne(arg)
		else:
			OnlyOne.instance.val = arg

	def __getattr__(self, name):
		return getattr(self.instance, name)


def main():
	x = OnlyOne('sausage')
	print(x)
	y = OnlyOne('eggs')
	print(y)
	z = OnlyOne('spam')
	print(z)
	print(x)
	print(y)
	print(`x`)
	print(`y`)
	print(`z`)

	'''
	Output 
	<__main__.__OnlyOne instance at 0076B7AC>sausage
	<__main__.__OnlyOne instance at 0076B7AC>eggs
	<__main__.__OnlyOne instance at 0076B7AC>spam
	<__main__.__OnlyOne instance at 0076B7AC>spam
	<__main__.__OnlyOne instance at 0076B7AC>spam
	<__main__.OnlyOne instance at 0076C54C>
	<__main__.OnlyOne instance at 0076DAAC>
	<__main__.OnlyOne instance at 0076AA3C>
	'''


if __name__ == '__main__':
	main()