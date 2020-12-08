'''
This parser loader dynamically discovers files inside of the parsers directory, loads them, and makes them available to be used by the application without requiring changes to any other parts of the code. 

Here are the rules that our loader will require when implementing new parsers:

1. Create a file with a class implementing the methods for fetching the current weather forecast as well as five-day, ten-day, and weekend weather forecasts
2. The file name has to end with parser, for example, weather_com_parser.py
3. The file name can't start with double underscores
'''

import os
import re
import inspect


def _get_parser_list(dirname):
    '''
	Returns a list of all files located in weatherterm/parsers; it will filter the files based on the rules of the parser described previously. 
	'''

    files = [f.replace('.py', '') for f in os.listdir(dirname) if not f.startswith('____')]
    return files


def _import_parsers(parserfiles):
    '''
	Imports the weatherterm.parsers module and makes use of the inspect package in the standard library to find the parser classes within the module.
	'''

    m = re.compile('.+parser$', re.I)

    _modules = __import__('weatherterm.parsers',
                          globals(),
                          locals(),
                          parserfiles,
                          0)

    _parsers = [(k, v) for k, v in inspect.getmembers(_modules)
                if inspect.ismodule(v) and m.match(k)]

    _classes = dict()

    for k, v in _parsers:
        '''
		loop through the items in the module and extract the parser classes, returning a dictionary containing the name of the class and the class object that will be later used to create instances of the parser
		'''

        _classes.update({k: v for k, v in inspect.getmembers(v)
                         if inspect.isclass(v) and m.match(k)})

    return _classes


def load(dirname):
    parserfiles = _get_parser_list(dirname)
    return _import_parsers(parserfiles)
