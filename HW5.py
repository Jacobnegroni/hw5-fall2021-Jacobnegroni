import re
import os
import unittest

def read_file(filename):
    """ Return a list of the lines in the file with the passed filename """

    # Open the file and get the file object
    source_dir = os.path.dirname(__file__) #<-- directory name
    full_path = os.path.join(source_dir, filename)
    infile = open(full_path,'r', encoding='utf-8')

    # Read the lines from the file object into a list
    lines = infile.readlines()

    # Close the file object
    infile.close()

    # return the list of lines
    return lines


def find_chapter_info(string_list):
    """ This function finds and returns 
    a dictionary with the chapter number as the keys and the title of the chapter as the value
    Example output: {1: “Owl Post”, 2: “Aunt Marge's Big Mistak”, … }
    """
    chapters = {}

    for line in string_list:
        if(re.findall("^Chapter",line) != []):
            key = re.findall("^Chapter\s(\d).*",line)[0]
            val = re.findall("^Chapter\s\d:\s(.*)",line)[0]
            chapters[int(key)] = val
    return chapters

def find_capitalized_words(string_list):
    """This function finds consecutive capitalized words (at least two words, no punctuations in between). 
    For example, in the text we can find Diagon Alley, Professor Remus Lupin as qualified consecutive words.
    Example output: ["Diagon Alley", "Professor Remus Lupin"]  
    """
    li = []

    for line in string_list:
        l = re.findall("([A-Z][A-Za-z]+(?=\s[A-Z])(?:\s[A-Z][A-Za-z]+)+)",line) 
        li += l

    return li


def find_urls(string_list):
    """ Return a list of valid urls in the list of strings """

    urls = []

    for line in string_list:
        url = re.findall("((http|https)://www\S*(\.org|\.com).*)\s",line)
        if(url != []):
            urls += [url[0][0]]

    return urls


def find_dates(string_list):
    """ Return a list of dates in the list of strings 
        Sample format: 
        mm/dd/yyyy 
        mm/dd/yy 
        mm-dd-yyyy 
        mm-dd-yy
        Please refer to the instructions and be careful about invalid dates!
    """

    dates = []

    for line in string_list:
        date_1 = re.findall("((0[1-9]|1[0-2])/(0[1-9]|1[0-9]|2[0-9]|3[0-1])/(19[0-9][0-9]|20([0-1][0-9]|2[0-1])))\D",line)
        date_2 = re.findall("((0[1-9]|1[0-2])/(0[1-9]|1[0-9]|2[0-9]|3[0-1])/[0-9][0-9])\D",line)
        date_3 = re.findall("((0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1])-(19[0-9][0-9]|20([0-1][0-9]|2[0-1])))\D",line)
        date_4 = re.findall("((0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1])-[0-9][0-9])\D",line)
        if(date_1 != []):
            dates += [date_1[i][0] for i in range(len(date_1))]
        if(date_2 != []):
            dates += [date_2[i][0] for i in range(len(date_2))]
        if(date_3 != []):
            dates += [date_3[i][0] for i in range(len(date_3))]
        if(date_4 != []):
            dates += [date_4[i][0] for i in range(len(date_4))]

    return dates


## Extra credit
def count_mid_str(string_list, string):
    """ return a count of the number of times a specified strings appears in the text.
        The matched string should be in the middle of a word. 
        It should not be the start or the end of a word.

        string_list -- the list of strings to count the string in
        string -- the stirng to look for, e.g., "be"
        return -- a count of the number of times the string appears in the text
    """
    pass


# Implement your own tests
class TestAllMethods(unittest.TestCase):


    def test_find_chapter_info(self):
        str_list_1 = ["Chapter 1: This is my first chapter"]
        str_list_2 = ["Chap 29387: My dummy chapter"]
        str_list_3 = ["Where is my chapter: 46"]
        self.assertEqual(find_chapter_info(str_list_1), {1:"This is my first chapter"})
        self.assertEqual(find_chapter_info(str_list_2), {})
        self.assertEqual(find_chapter_info(str_list_3), {})

    def test_find_capitalized_words(self):
        str_list_1 = ["none of this are capitalized"]
        str_list_2 = ["tHis hAs wRong cApitalization"]
        str_list_3 = ["well, it was nice to meet Lord Harry The Third and also Little Harry Jr"]
        self.assertEqual(find_capitalized_words(str_list_1),[])
        self.assertEqual(find_capitalized_words(str_list_2),[])
        self.assertEqual(find_capitalized_words(str_list_3),["Lord Harry The Third","Little Harry Jr"])


    def test_find_urls(self):
        str_list_1 = ["vimeo.com is a good alternative to youtube.com"]
        str_list_2 = ["I find good movies on https://agoodmovietowatch.com/","Also https://www.agoodmovietowatch.com/ works"]
        str_list_3 = [".com and .org websites are aplenty","https://hackertyper.net/ is funny"]
        self.assertEqual(find_urls(str_list_1),[])
        self.assertEqual(find_urls(str_list_2),["https://www.agoodmovietowatch.com/"])
        self.assertEqual(find_urls(str_list_3),[])

    def test_find_dates(self):
        str_list_1 = ["10/31-1950 is a weird date to look at"]
        str_list_2 = ["I am time travelling from 12/31/2021 to 01/01/1990\n"]
        str_list_3 = ["12-31-21 is not a valid date though"]
        self.assertEqual(find_dates(str_list_1),[])
        self.assertEqual(find_dates(str_list_2),["12/31/2021","01/01/1990"])
        self.assertEqual(find_dates(str_list_3),["12-31-21"])


    def test_count_mid_str(self):
        pass



def main():
	# Use main to test your function.
    # Run unit tests, but feel free to run any additional functions you need
    
    lines = read_file("Harry-potter-txt.txt")
    # print(find_chapter_info(lines))
    # print(find_capitalized_words(lines))
    # print(find_urls(lines))
    # print(find_dates(lines))

    unittest.main(verbosity = 2)


if __name__ == "__main__":
    main()
