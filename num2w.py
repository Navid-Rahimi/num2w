# The program is written by Navid Rahimi
#
# Thursday 27/01/2022

import json

class Num2w(object):
    """
    Receives a number as the input and returns the number's
    written-format value as the output.
    e.g. 17 --> seventeen
    """

    def __init__(self):
        self.num2w_dict = self.get_data()

    def get_input(self):
        # The input will be asked from the user.
	# Here an interface can be developed which gives the user possibilities
        # Like changing language or quit the program

        number = input("Please enter a real number between 0 and 100: ")
        return number

    def get_data(self):
        # The json file on the local data containing the numbers as keys
        # And their written format as values will be loaded.
        # With the way LData.json is structured, another language can be
        # Added to the input possibilities. In addition, numbers bigger than
        # 100 or smaller than 0 can also be added. The Reverse Conversion,
        # E.g. Seventeen --> 17, is also one of the possible ideas to add
        # More functionality to the program in the future.

        with open("LData.json", "r") as f:
            data_r = f.read()
            data = json.loads(data_r)
            num2w_dict = data["num2w"]["en"]
        return num2w_dict

    def low_read(self,x,data):
        # The written format of the numbers which are lower than 19 can
        # Be read by this function. In the prime dictionary on the local
        # Data, numbers are the keys and their written format are the values.

        return data['prime'].get(x)

    def high_read(self,x,data):
        # Same as the low_read function but for the numbers higher than 20.

        x1 = int(x) % 10        # Residual of the division by 10 gives the first number from right
        w1 = data['prime'].get(str(x1))
        x2 = int(x) // 10       # Division by 10 gives the second number from right, which can be 2,3,...,10
        w2 = data['second'].get(str(x2))
        if x1 == 0 :
            # In the numbers like 20,30,... the written format of
            # The number is built of one part.
            return w2
        else:
            # In the other cases, concatenation is needed.
            return w2 + '-' + w1

    def low_high(self,x):
        # Receives a number x and decides if x is a real number between
        # 0 and 100 or not and then read it by exploiting low_read and
        # High_read functions. In the case that the entered value by user
        # Won't meet the requirements, a warning will be shown.

        output = ''
        if x.isnumeric():
            if (0 <= int(x)) and (int(x) <= 19):
                output = self.low_read(x,self.num2w_dict)
            elif (20 <= int(x)) and (int(x) <= 100):
                output = self.high_read(x,self.num2w_dict)
            else:
                output = 'The entered value is NOT valid. Only real numbers between 0 and 100 can be chosen.'
        else:
            output = 'The entered value is NOT valid. Only real numbers between 0 and 100 can be chosen.'
        return output


def main():

    new = Num2w()           # First an instant of the class is made.
    while True:
        # The input will be required from the user until the user stops the program.

        number = new.get_input()
        word = new.low_high(number)

        print(word)


if __name__ == '__main__':
        main()
