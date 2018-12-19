import re


def search_fun(search_input):
    def find_period(s, ch):
        """finds all periods in a sentence"""
        return [i for i, ltr in enumerate(s) if ltr == ch]

    def split_lines(cur_line, last_l):
        """ splits lines by period"""
        sentences = None
        cur_line_period = find_period(cur_line, '.')
        last_line_period = find_period(last_l, '.')
        for n in range(len(cur_line_period)):
            if n == 0:
                sentences = list()
                if len(last_line_period) == 0:
                    new_sentence = last_l + cur_line[0:cur_line_period[0]]

                else:
                    new_sentence = last_l[last_line_period[-1]+1:] + cur_line[0:cur_line_period[0]]
                sentences.append(new_sentence)

            else:

                sentences.append(cur_line[cur_line_period[n-1]+1:cur_line_period[n]])

        return sentences

    def end_corner(cur_line, index):
        """ separates input value for partial match test"""
        if input_len <= index:
            return None
        partial_input = input_value.rsplit(' ', index)[0]
        find_return = cur_line.find(partial_input)
        if find_return != -1 and find_return + len(partial_input) == len(cur_line)-1:
            partial_match_list.append(partial_input)
        end_corner(cur_line, index+1)

    partial_match_list = list()
    input_value = search_input
    input_len = len(input_value.split())
    pattern = re.compile(input_value)
    counter = 0
    new_sent = ''
    last_line = ''
    occurrences_list = []
    new_find = None

    for i, line in enumerate(open('king-i.txt')):
        period_l = find_period(line, '.')

        if new_sent is None:
            """ second half partial match test """
            if split_lines(line, last_line) is not None:
                new_sent = split_lines(line, last_line)[0]
            else:
                period_p = find_period(last_line, '.')
                if len(period_p) > 0:
                    new_sent = last_line[period_p[-1]+1:] + line
                else:
                    new_sent = last_line + line
            print(new_sent.replace('\n', ' ').lstrip())
            new_find['in_sentence'] = new_sent.replace('\n', ' ').lstrip()+'.'
            occurrences_list.append(new_find)

        while len(partial_match_list) > 0:
            """ first half partial match test """
            next_match = input_value.replace(partial_match_list.pop()+' ', '')
            if line.find(next_match) == 0:
                print('corner case Found on line %s' % i)
                new_find = {"line": i, "start": len(next_match)-len(input_value), "end": len(next_match)}
                if len(period_l) > 0:
                    new_sent = split_lines(line, last_line)[0].replace('\n', ' ').lstrip()+'.'
                    print(new_sent)
                    new_find['in_sentence'] = new_sent
                    occurrences_list.append(new_find)
                else:
                    new_sent = None

                counter += 1
        for match in re.finditer(pattern, line):
            """ finds input value in a line"""
            print('Found on line %s: %s, start:%s, end: %s' % (i+1, match.group(), match.start()+1, match.end()+1))
            counter += 1
            new_find = {"line": i+1, "start": match.start()+1, "end": match.end()+1}
            new_sent = None
            sent_list = split_lines(line, last_line)
            period_l.append(match.start())
            period_l.sort()
            position = period_l.index(match.start())

            if sent_list is not None and len(sent_list) > position:
                new_sent = split_lines(line, last_line)[position]
                print(new_sent.replace('\n', ' ').lstrip())

                new_find['in_sentence'] = new_sent.replace('\n', ' ').lstrip()+'.'
                occurrences_list.append(new_find)
        end_corner(line, 1)

        if len(find_period(line, '.')) <= 0:

            last_line += line
        else:
            last_line = line

    print(counter)

    search_return = {"query_text": input_value, "number_of_occurrences": counter, "occurrences": occurrences_list}
    return search_return

