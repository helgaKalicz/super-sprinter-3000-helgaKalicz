def read_file(filename):
    '''
    Opens and reads a file, then returns a nested list with the elements of the file.
    '''
    with open(filename) as file:
        file_list = [lines.split(',') for lines in file.read().splitlines()]
    return file_list


def write_file(filename, nestedlist):
    '''
    Rewrites the whole file.
    '''
    with open(filename, 'w') as file:
            for items in nestedlist:
                file.write(','.join(items) + '\n')


def restore_comma(nestedlist):
    '''
    Restore the commas to the strings.
    '''
    for i in range(len(nestedlist)):
        for j in range(len(nestedlist[i])):
            if '¤' in nestedlist[i][j]:
                nestedlist[i][j] = nestedlist[i][j].replace('¤', ',')
    return nestedlist


def convert_string(string):
    '''
    Replaces some elements in the string.
    '''
    string = string.replace('\r\n', ' ')
    string = string.replace('¤', '')
    string = string.replace(',', '¤')
    string = ' '.join(string.split())
    return string


def valid_value(value):
    '''
    Returns True if the value is valid, else returns False.
    '''
    try:
        value = int(value)
        return False if value < 100 or value > 1500 or value % 100 != 0 else True
    except:
        return False


def valid_time(time):
    '''
    Returns True if the time is valid, else returns False.
    '''
    try:
        time = float(time)
        return False if time < 0.5 or time > 40 or time % 0.5 != 0 else True
    except:
        return False


def correct_time(time):
    '''
    Returns the correct form of the estimation time.
    '''
    return int(time) if int(float(time)) == float(time) else float(time)
