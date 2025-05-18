#!/usr/bin/env python3

from student import Student, ChattyStudent

import io
import sys

class TestStudent:
    '''Class Student in student.py'''
    
    def test_says_hello(self):
        '''says a brief greeting.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        student = Student()
        

    def test_raises_hand(self):
        '''respectfully tries to get the teacher's attention.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        student = Student()
       

class TestChattyStudent:
    '''Class ChattyStudent in student.py'''
    
    def test_says_hello(self):
        '''says a brief greeting, then tries to spoil a TV show.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        chatty_student = ChattyStudent()
        
    def test_raises_hand(self):
        '''respectfully tries to get the teacher's attention ten times.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        chatty_student = ChattyStudent()
        