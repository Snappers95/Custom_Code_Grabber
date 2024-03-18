# Author: Jacob Laviolette
# Date: 3/16/2024

import re

sql_file = open('HFS CUSTOM TruckMateSchema.SQL', 'r')


def get_code_title(code_snippet):
    list_to_ignore = ['CREATE', 'OR', 'REPLACE', '(']

    if re.search(r'^CREATE[0-9A-Z_. ()]*\n', code_snippet):
        title = re.search(r'^CREATE[0-9A-Z_. ()]*\n', code_snippet).group()
        type_name = [item for item in title.split() if item not in list_to_ignore]
        type_name[1] = type_name[1].strip('TMWIN.(')
        return ' '.join(type_name)


def get_custom_code():
    code = re.split(r"@\n", sql_file.read())
    counter = 0
    for i in code:
        if len(i) > 1:
            title = get_code_title(i.strip())
            code_file = open(str(title+'.sql'), 'w')
            code_file.write(i.strip())
            code_file.write('\n@\n')
            code_file.close()
            counter += 1
    print(counter, 'files created')


def main():
    get_custom_code()


if __name__ == "__main__":
    main()
