# -*- coding: utf-8 -*-

import os
import fnmatch

class Expression(object):
	def __and__(self, other):
		return And(self, other)

	def __or__(self, other):
		return Or(self, other)

	def __invert__(self):
		return Not(self)

def allfiles(dirpath):
	result = []
	for root, dirs, files in os.walk(dirpath):
		for f in files:
			result.append(os.path.join(root, f))
	return result


class All(Expression):
	def evaluate(self, dirpath):
		return allfiles(dirpath)


class FileName(Expression):
	def __init__(self, pattern):
		self.pattern = pattern

	def evaluate(self, dirpath):
		return fnmatch.filter(allfiles(dirpath), self.pattern)


class Bigger(Expression):
	def __init__(self, size):
		self.size = size

	def evaluate(self, dirpath):
		return [path for path in allfiles(dirpath) if os.path.getsize(path) > self.size]


class Not(Expression):
	def __init__(self, expression):
		self.expression = expression

	def evaluate(self, dirpath):
		result1 = set(allfiles(dirpath))
		result2 = set(self.expression.evaluate(dirpath))

		return list(result1 - result2)


class Or(Expression):
	def __init__(self, expression1, expression2):
		self.expression1 = expression1
		self.expression2 = expression2

	def evaluate(self, dirpath):
		result1 = set(self.expression1.evaluate(dirpath))
		result2 = set(self.expression2.evaluate(dirpath))

		return list(result1 | result2)


class And(Expression):
	def __init__(self, expression1, expression2):
		self.expression1 = expression1
		self.expression2 = expression2

	def evaluate(self, dirpath):
		result1 = set(self.expression1.evaluate(dirpath))
		result2 = set(self.expression2.evaluate(dirpath))

		return list(result1 & result2)


if __name__ == '__main__':
	from pprint import pprint

	expr = Not(And(Bigger(5*1024), FileName("*.py")))

	path = r"./"
	for p in expr.evaluate(path):
		print(p)