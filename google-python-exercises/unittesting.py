import unittest
import testcap

class TestUpperWords(unittest.TestCase):

    def test_oneword(self):
        text = 'myworld'
        result = testcap.cap(text)
        print(result)
        self.assertEqual(result,'Myworld')

    def test_multipleword(self):
        text = 'myworld is you'
        result = testcap.cap(text)
        print(result)
        self.assertEqual(result,'Myworld Is You')

    def test_split(self):         
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world']) 
        with self.assertRaises(TypeError): 
            s.split(2) 

if __name__ == '__main__':
    unittest.main()
