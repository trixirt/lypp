#!/usr/bin/env python2

import os
import platform
import pytest
import sys
import subprocess

script = '..' + os.sep + 'lypp.py'
input = 'input'
    
data_path = os.path.dirname(__file__)
if data_path:
    script = data_path + os.sep + '..' + os.sep + 'lypp.py'
    input = data_path + os.sep + 'input'

def test_script():
    assert os.path.exists(script)
    
def test_else_1():
    global script
    f = input + os.sep + 'else_1'
    t = subprocess.check_output([script, f]).strip()
    e = 'bar\nmar'
    assert(e == t)

def test_else_2():
    global script
    f = input + os.sep + 'else_1'
    t = subprocess.check_output([script, '-D', 'foo', f]).strip()
    e = 'goo\nmar'
    assert(e == t)

def test_else_3():
    global script
    f = input + os.sep + 'else_2'
    t = subprocess.check_output([script, f]).strip()
    e = 'bar\nmar'
    assert(e == t)

def test_else_4():
    global script
    f = input + os.sep + 'else_2'
    t = subprocess.check_output([script, '-D', 'foo', f]).strip()
    e = 'goo\nmar'
    assert(e == t)

def test_else_5():
    global script
    f = input + os.sep + 'else_2'
    t = subprocess.check_output([script, '-D', 'voo', f]).strip()
    e = 'woo\nmar'
    assert(e == t)
