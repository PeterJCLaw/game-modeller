
import sys
import os.path

def modImportPath():
    myDir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, os.path.join(os.path.abspath(myDir), '..', 'src'))

modImportPath()

### Pretty Printing

def printDict(data):
    print json.dumps(data, sort_keys = True, indent = 4)

### Nicer Assertions than pyUnit

def prepMessage(expected, actual, message, params):
    if isinstance(message, type('')):
        if isinstance(params, type(())) and len(params) > 0:
            message = message % params
    else:
        message = ''

    return message + "\nExpected: %s\n  Actual: %s" % (expected, actual)

def prepMessagePrefix(prefix, expected, actual, message, params):
    return prepMessage('%s %s' % (prefix, expected), actual, message, params)

def prepMessageNot(expected, actual, message, params):
    return prepMessagePrefix('not', expected, actual, message, params)


def assertEqual(expected, actual, message = None, *params):
    message = prepMessage(expected, actual, message, params)
    assert expected == actual, message

def assertNotEqual(expected, actual, message = None, *params):
    message = prepMessageNot(expected, actual, message, params)
    assert expected != actual, message

def assertIs(expected, actual, message = None, *params):
    message = prepMessage(expected, actual, message, params)
    assert expected is actual, message

def assertIsNot(expected, actual, message = None, *params):
    message = prepMessageNot(expected, actual, message, params)
    assert expected is not actual, message

def assertIsInstance(expected, actual, message = None, *params):
    message = prepMessagePrefix('instance of', expected, actual, message, params)
    assert isinstance(expected, actual), message

def assertIsNotInstance(expected, actual, message = None, *params):
    message = prepMessagePrefix('instance not of', expected, actual, message, params)
    assert not isinstance(expected, actual), message

assertNotIsInstance = assertIsNotInstance


def assertIsNone(actual, message = None, *params):
    assertIs(None, actual, message, *params)

def assertIsNotNone(actual, message = None, *params):
    assertIsNot(None, actual, message, *params)

def assertTrue(actual, message = None, *params):
    assertIs(True, bool(actual), message, *params)

def assertFalse(actual, message = None, *params):
    assertIs(False, bool(actual), message, *params)


def assertIn(needle, haystack, message = None, *params):
    message = prepMessagePrefix('collection containing', needle, haystack, message, params)
    assert needle in haystack, message

def assertNotIn(needle, haystack, message = None, *params):
    message = prepMessagePrefix('collection not containing', needle, haystack, message, params)
    assert needle not in haystack, message


def assertGreaterThan(reference, actual, message = None, *params):
    message = prepMessagePrefix('value greater than', reference, actual, message, params)
    assert actual > reference, message

def assertLessThan(reference, actual, message = None, *params):
    message = prepMessagePrefix('value less than', reference, actual, message, params)
    assert actual < reference, message
