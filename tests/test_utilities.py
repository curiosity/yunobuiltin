import collections
import numbers
from yunobuiltin import isa, get, MultiFn, rpartial


def test_isa_equality():
    assert isa(None, None)
    assert isa(True, True)
    assert isa(False, False)
    assert isa(2, 2)
    assert isa(1.0, 1.0)
    assert isa("foo", "foo")
    assert isa(u"foo", u"foo")
    assert isa([], [])
    assert isa(["foo"], ["foo"])
    assert isa({}, {})
    assert isa({"foo": "bar"}, {"foo": "bar"})
    assert isa(set(), set())


def test_isa_instance():
    # dicts
    assert isa({}, dict)
    assert isa({}, collections.Mapping)
    assert isa({}, collections.MutableMapping)
    assert isa({}, collections.Container)
    assert isa({}, collections.Sized)
    assert isa({}, collections.Iterable)
    assert isa({}, object)
    assert isa({"foo": "bar"}, dict)
    assert isa({"foo": "bar"}, collections.Mapping)
    assert isa({"foo": "bar"}, collections.MutableMapping)
    assert isa({"foo": "bar"}, collections.Container)
    assert isa({"foo": "bar"}, collections.Sized)
    assert isa({"foo": "bar"}, collections.Iterable)
    assert isa({"foo": "bar"}, object)

    # lists
    assert isa([], list)
    assert isa([], collections.Iterable)
    assert isa([], collections.Sized)
    assert isa([], collections.Container)
    assert isa([], collections.Sequence)
    assert isa([], collections.MutableSequence)
    assert isa([], object)
    assert isa([1], list)
    assert isa([1], collections.Iterable)
    assert isa([1], collections.Sized)
    assert isa([1], collections.Container)
    assert isa([1], collections.Sequence)
    assert isa([1], collections.MutableSequence)
    assert isa([1], object)

    # tuples
    # sets
    # strings
    assert isa("", str)
    assert isa("", basestring)
    assert isa("", object)
    assert isa("", collections.Iterable)
    assert isa("", collections.Sized)
    assert isa("", collections.Container)
    assert isa("", collections.Sequence)
    assert isa(u"", unicode)
    assert isa(u"", basestring)
    assert isa(u"", object)
    assert isa(u"", collections.Iterable)
    assert isa(u"", collections.Sized)
    assert isa(u"", collections.Container)
    assert isa(u"", collections.Sequence)

    # numbers
    assert isa(1, int)
    assert isa(1, numbers.Integral)
    assert isa(1, numbers.Number)
    assert isa(1L, long)
    assert isa(1L, numbers.Integral)
    assert isa(1L, numbers.Number)
    assert isa(1.0, float)
    assert isa(1.0, numbers.Real)
    assert isa(1.0, numbers.Number)


def test_isa_type_inheritance():
    # dicts
    assert isa(dict, collections.Iterable)
    assert isa(dict, collections.Sized)
    assert isa(dict, collections.Container)
    assert isa(dict, collections.Mapping)
    assert isa(dict, collections.MutableMapping)

    # lists
    assert isa(list, collections.Iterable)
    assert isa(list, collections.Sized)
    assert isa(list, collections.Container)
    assert isa(list, collections.Sequence)
    assert isa(list, collections.MutableSequence)

    # tuples
    assert isa(tuple, collections.Sized)
    assert isa(tuple, collections.Container)
    assert isa(tuple, collections.Iterable)
    assert isa(tuple, collections.Sequence)

    # sets
    assert isa(set, collections.Sized)
    assert isa(set, collections.Container)
    assert isa(set, collections.Iterable)
    assert isa(set, collections.Set)
    assert isa(set, collections.MutableSet)


def test_multifn_values():
    noise = MultiFn(rpartial(get, 'animal'))

    @noise.method("cow")
    def cow_noise(*args, **kwargs):
        return "moo"

    @noise.method("dog")
    def dog_noise(*args, **kwargs):
        return "woof"

    @noise.method(None)
    def no_noise(*args, **kwargs):
        return "*silence*"

    @noise.default
    def unknown_noise(*args, **kwargs):
        return "crickets"

    assert noise({'animal': 'cow'}) == 'moo'
    assert noise({'animal': 'dog'}) == 'woof'
    assert noise({'object': 'rock'}) == '*silence*'
    assert noise({'animal': 'donkey'}) == 'crickets'


def test_multifn_classes():
    noise = MultiFn(type)

    class Animal(object):
        pass

    class Cow(Animal):
        pass

    class Dog(Animal):
        pass

    class Cat(Animal):
        pass

    @noise.method(Cow)
    def cow_noise(cow):
        return "moo"

    @noise.method(Dog)
    def dog_noise(dog):
        return "woof"

    @noise.method(Animal)
    def animal_noise(animal):
        return "animal noise here"

    @noise.default
    def unknown_noise(_):
        return "no noise"

    assert noise(Cow()) == 'moo'
    assert noise(Dog()) == 'woof'
    assert noise(Cat()) == 'animal noise here'
    assert noise(object()) == 'no noise'

    noise.prefer(Animal, Dog)
    assert noise(Dog()) == 'animal noise here'
