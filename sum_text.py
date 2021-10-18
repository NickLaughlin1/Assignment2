from os.path import exists
from sqlite3.dbapi2 import Error

def addNumbers(textFile: str):
    try:
        if not isinstance(textFile, str):
            raise TypeError()
        if exists(textFile):
            with open(textFile) as f:
                contents = f.read()
                
            numList = contents.strip().split(',')
            total = 0
            for num in numList:
                if type(int(num)) == int:
                    total += int(num)
                else:
                    raise ValueError
            with open(textFile, 'a') as f:
                f.write('\n' + str(total))
            return total
        else:
            return 0
    except Error as e:
        print("Error has occured")
    # except ValueError as e:
    #     print("Value error occured")
    