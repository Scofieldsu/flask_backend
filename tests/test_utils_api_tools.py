# encoding: utf-8
import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Flask is supported only for python2 and python3.3+
if sys.version_info < (3, 0) or sys.version_info >= (3, 3):
    try:
        from flask import Flask
    except ImportError:
        raise unittest.SkipTest('Flask not found for testing')

