""" TODO create a test case to test the following functions,


generate_url_for_question
 - check that the expected URL is returned for an example question. 

extract_answer_from_response
 - one test should create some example dictionaries that match the expected response from the API,
 and check that the correct answer is extracted and returned.
 - another test should create example dictionaries with a different structure to the one returned from the API, 
 and check that the function returns None. 

 TODO to think about - what else could you test about this program? 
 What types of expected and unexpected behavior might happen? You may be able to write tests for some 
 of your ideas now. We'll talk about ways to test other aspects of this program in class.

"""
import unittest
import functions_magic
from original_magic import magic_8_ball_url, response, question

class TestMagic8Ball(unittest.TestCase):

    def test_generate_url_for_question(self, magic_8_ball_url,response):
        if self.magic_8_ball_url != magic_8_ball_url:
            raise ConnectionError('Could not connect to magic 8 ball url')
        return response
    
    def test_extract_answer_from_response(self,question, response):
        return 