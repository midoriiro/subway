# MIT License

# Copyright (c) 2016 Alexis Bekhdadi (midoriiro) <contact@smartsoftwa.re>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# TODO: write module, function, class, method docstring
# pylint: disable=missing-docstring

import shlex
import pytest

from pytest_bdd import parsers, scenario, given, when, then

from subways import process as _process
from subways.process import Process

from tests.conftest import get_data_path


@pytest.fixture
def pytestbdd_strict_gherkin():
    return False


@pytest.fixture
def settings():
    return {}


@given(
    parsers.re(r'select (?P<scope>local) (?P<resource>.*)'),
    converters=dict(scope=str, resource=str)
)
def data(scope, resource):
    return get_data_path(resource)


@given(
    parsers.re(r'arguments (?P<args>.+)'),
    converters=dict(args=str)
)
def process(data, args):
    command = 'python {0} {1}'.format(
        shlex.quote(data), shlex.quote(args)
    )

    return Process(command)


@when(
    parsers.re(r'set (?P<key>\w+) as (?P<value>\w+)'),
    converters=dict(key=str, value=str)
)
def setting(settings, key, value):
    if value == 'pipe':
        value = _process.PIPE
    elif value == 'stdout':
        value = _process.STDOUT
    elif value == 'devnull':
        value = _process.DEVNULL
    elif value == 'none':
        value = None
    elif value == 'true':
        value = True
    elif value == 'false':
        value = False
    else:
        assert value

    settings[key] = value


@then('create process')
def create(process, settings):
    process.create(**settings)


@then(
    parsers.re(r'run a (?P<type>blocking|non-blocking) call'),
    converters=dict(type=str)
)
def run(process, type):
    if type == 'blocking':
        type = True
    elif type == 'non-blocking':
        type = False
    else:
        assert type

    process.start(blocking=type)


@then(parsers.parse('exit status equal to {code:d}'))
def result(process, code):
    if not process.settings().blocking:
        process.wait_exit()

    assert process._process.returncode == code


@then(parsers.parse('{buffer:w} lines count equal to {count:d}'))
def line_count(process, buffer, count):
    if buffer == 'stdout' or buffer == 'stderr' or buffer == 'stdin':
        lines = process.readlines(buffer, keep_empty=True, timeout=10)
        assert len(lines) == count
    else:
        assert buffer


@then(parsers.re('(?P<buffer>\w+) (?P<logical>is(?: not)?) empty'),
      converters=dict(buffer=str, logical=str))
def buffer_length(process, buffer, logical):
    buffer_selected = None

    if buffer == 'stdout':
        buffer_selected = process.buffers().stdout
    elif buffer == 'stderr':
        buffer_selected = process.buffers().stderr
    elif buffer == 'stdin':
        buffer_selected = process.buffers().stdin
    else:
        assert buffer_selected is None

    if logical == 'is':
        assert len(buffer_selected) == 0
    elif logical == 'is not':
        assert len(buffer_selected) != 0


@then(
    parsers.re(r'send data (?P<word>-?[0-9]+|\w+)'),
    converters=dict(word=str)
)
def send(process, word):
    line = word + '\n'

    print(line, type(line))

    length = process.write(line)

    assert len(line) == length


@then('clear buffers')
def clear(process):
    process.clear_buffers()


@scenario('process.feature', 'Read 100 lines')
def test_read_100_lines():
    pass


@scenario('process.feature', 'Argument error')
def test_argument_error():
    pass


@scenario('process.feature', 'Write command interactively')
def test_interactive_write():
    pass
