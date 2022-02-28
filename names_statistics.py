def get_names(data):
    lines = data.split('<tr>')
    names = []
    for line in lines:
        name = find_name(line)
        if name is not None:
            names.append(name)
    return names


def find_name(line):
    if line.find('<td') == -1 or line.find('/>') == -1:
        return None
    line_tail = line[line.find('/>') + 2:]
    full_name = line_tail[: line_tail.find('<')]
    return full_name.split()[1]


def get_names_dictionary(names):
    dictionary = dict()
    for name in names:
        if name in dictionary:
            dictionary[name] += 1
        else:
            dictionary[name] = 1
    return dictionary


def generate_output(names_dictionary):
    output = ''
    for name in sorted(names_dictionary.keys(), key=lambda k: names_dictionary[k], reverse=True):
        output += name + ': ' + str(names_dictionary[name]) + '\n'
    return output


def main():
    with open("CS _ home.html", "r", encoding='cp1251') as file:
        data = file.read()
        names = get_names(data)
        names_dictionary = get_names_dictionary(names)
        output = generate_output(names_dictionary)
        print(output)


main()
