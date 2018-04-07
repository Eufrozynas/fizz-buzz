import pytest
from fizzbuzz import print_number as print_number


def test_other():
    assert(print_number(4) == "4")

def test_fizz():
	assert(print_number(3) == "Fizz")
	assert(print_number(18) == "Fizz")

def test_buzz():
	assert(print_number(5) == "Buzz")
	assert(print_number(20) == "Buzz")


def test_fizzbuzz():
	assert(print_number(15) == "FizzBuzz")
	assert(print_number(60) == "FizzBuzz")
