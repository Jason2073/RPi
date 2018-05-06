"""
Copyright (c) 2012-2016 Ben Croston

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from random import Random

from RPi._GPIO import *

IN = "Input"
OUT = "Output"

HIGH = 1
LOW = 0

BOARD = "Board Layout"
BCM = "BCM Layout"
mode = "UNDECLARED"

RISING = "Rising"
FALLING = "falling"

PUD_DOWN = "down"
PUD_UP = "up"

VERSION = '0.6.3'
RPI_INFO = "You silly billy, this isn't a raspberrypi"


def setmode(pinLayout):
    mode = pinLayout
    print("mode set")


def setup(channel, gpio_mode):
    print("Set up pin" + channel + " as an " + gpio_mode)


def setup(channel, gpio_mode, pull_up_down):
    print("Set up pin" + channel + " as an " + gpio_mode)


def setup(channel, gpio_mode, initial):
    print("Set up pin" + channel + " as an " + gpio_mode + " with initial value of " + initial)


def input(channel) -> bool:
    return bool(channel % 2)


def output(channel, high_or_low):
    print("set pin " + channel + " to " + high_or_low)


def cleanup():
    print("All clean!")


def cleanup(channel):
    print("cleaned " + channel)


def setwarnings(boolean):
    print("warnings are " + boolean)


def getmode():
    return mode


def add_event_detect(channel, rising_or_falling, callback, bouncetime):
    print("still gotta figure this one out")
