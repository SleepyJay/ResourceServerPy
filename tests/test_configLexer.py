# Unit tests

import unittest

from Lexer.ConfigLexer import ConfigLexer

__package__ = "tests.test_configLexer"

class Test_ConfigLexer(unittest.TestCase):
	
	def test_collectDirectives(self):
		lexer = ConfigLexer();

		tests = [
			{'name': 'type.resource import Test', 'line': '//@js.import Foo.Bar', 'expected':"1: js, import, 'Foo.Bar'"},
			{'name': 'resource import Test', 'line': '//@import Foo.Bar', 'expected':"1: rsc, import, 'Foo.Bar'"},
			{'name': 'resource space import Test', 'line': '//@ import Foo.Bar', 'expected':"1: rsc, import, 'Foo.Bar'"},
			{'name': 'type.resource space import Test', 'line': '//@ js.import Foo.Bar', 'expected':"1: js, import, 'Foo.Bar'"},
		]

		for test in tests:
			actual = lexer.lexLine(test['line'])

			print "\nlexed ({}): {}".format(test['line'], str(actual))
			self.assertEqual(str(actual), test['expected'], "{} passed ({}).".format(test['name'], actual))

		
		


if __name__ == '__main__':
	unittest.main(verbosity=2)
