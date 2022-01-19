"""
This Python script is bad. It works (more or less), but it's bad.
It violates almost every style convention in the book and abuses several dunder methods to achieve very confusing
results.

The reasons for making this monstrosity are:
1. To test my knowledge of Python by doing everything wrong on purpose.
2. To highlight the importance of style conventions and how confusing things become if you're to throw them out the
   window.
3. To illustrate how misusing magic/dunder methods can be outright dangerous to our sanity.

Apart from the very sensible reasons above this was also just a good bit of fun to do. You'll notice therefore that
everything was done in the most convoluted way possible.
"""



class special__string:
    def __init__(self,string):
        self.string=string
        self.string_list=[]
    def charify(self):
        for i in self.string:
            str = cHARACTER(i)
            self.string_list=[*self.string_list, str]
    def __contains__(self, item):
        truth_condition_list=[]
        for __itemIndex__ in range(0, len(self.string_list)):
            Truth_Value = self.string_list[__itemIndex__] == None
            truth_condition_list.append(Truth_Value)

        self.is_int_List = truth_condition_list
        return True
    def __add__(self, other):
        can_be_int = all(self.is_int_List)
        if str(bool(can_be_int)) == 'True':
            print('String can be int')
            return 'bananas'
        elif str(int(bool(can_be_int))) == '0':
            print('String cannot be int')
            return 'no bananas'



class cHARACTER:
    def __init__(self, char):
        self.value = char
    def __str__(self):
        return self.value
    def __eq__(self, other):
        for int in range(0, 10):
            if str(int) == self.value:
                return bool('🙃')
        return bool(None)


CharEquivalencelist=[]
MAIN_list = ['_', '_', 'M', 'A', 'I', 'N', '_', '_']
for CHAR_list, CHAR_name in zip(MAIN_list, __name__):
    CharEquivalencelist.append(CHAR_list == CHAR_name.upper())

if all(CharEquivalencelist):
    import argparse
    Parser = argparse.ArgumentParser()
    Parser.add_argument('-input', '--i', default=None, required=True, help="Provide the input that you want the script to process the input should be a string or a number but presented as a string that you want to check if it's a string or a number")
    ARGS = Parser.parse_args()
    ARGS = vars(ARGS)
    SpecialString = special__string(ARGS['i'])
    special__string.charify(self = SpecialString)
    'int(special__string)' in SpecialString
    SpecialString + 10

