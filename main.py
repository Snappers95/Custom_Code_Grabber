# Author: Jacob Laviolette
# Date: 3/16/2024

import re
from tkinter import filedialog as fd


def get_code_title(code_snippet):
    """
    Takes SQL text and creates a filename from the text which includes what it is.
    :param code_snippet: a stripped string of SQL.
    :return: a new filename.
    """
    list_to_ignore = ['CREATE', 'OR', 'REPLACE', '(']  # some keywords to ignore

    if re.search(r'^CREATE[0-9A-Z_. ()]*\n', code_snippet):  # Maybe change to filter out certain files
        title = re.search(r'^CREATE[0-9A-Z_. ()]*\n', code_snippet).group()
        type_name = [item for item in title.split() if item not in list_to_ignore]
        type_name[1] = type_name[1].strip('TMWIN.(')  # This is to remove schema name prefix
        return ' '.join(type_name)


def get_custom_code(sql_file):
    """
    loops through schema file and creates individual files for every table, trigger, procedure etc.
    :return: None.
    """
    code = re.split(r"@\n", sql_file.read())  # splits file on terminator '@'
    counter = 0
    for i in code:
        if len(i) > 1:
            title = get_code_title(i.strip())
            code_file = open(str(title+'.sql'), 'w')
            code_file.write(i.strip())
            code_file.write('\n@\n')  # re-add the query terminator that was removed
            code_file.close()
            counter += 1
    print(counter, 'files created')


def main():
    try:
        sql_file = open(fd.askopenfilename(), 'r')
        get_custom_code(sql_file)
    except IOError:
        print('No permission to open file')
    finally:
        sql_file.close()



if __name__ == "__main__":
    main()
