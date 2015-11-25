import functools
import yunobuiltin

def test_partial_available():
    assert yunobuiltin.partial is functools.partial

def test_rpartial():
    assert yunobuiltin.rpartial(lambda x, y: x ** y, 4)(2) == 16

def _append_str(s, x):
    x +=  s
    return x

_append_foo = yunobuiltin.partial(_append_str, ' foo ')
_append_bar = yunobuiltin.partial(_append_str, ' bar ')
_append_spam = yunobuiltin.partial(_append_str, ' spam ')

def test_pipeline():
    f = yunobuiltin.pipeline(_append_foo, _append_bar, _append_spam)
    assert f('') == ' foo  bar  spam '

def test_thread():
    assert (yunobuiltin.thread('', _append_foo, _append_bar, _append_spam)
            == ' foo  bar  spam ')

def test_compose():
    f = yunobuiltin.compose(_append_foo, _append_bar, _append_spam)
    assert f('') == ' spam  bar  foo '
