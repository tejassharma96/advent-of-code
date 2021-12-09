#!/usr/bin/env python3


value_to_signal = [frozenset('abcefg'), 
                    frozenset('cf'),
                    frozenset('acdeg'),
                    frozenset('acdfg'),
                    frozenset('bcdf'),
                    frozenset('abdfg'),
                    frozenset('abdefg'),
                    frozenset('acf'),
                    frozenset('abcdefg'),
                    frozenset('abcdfg')]
signal_to_value = { signal: value for value, signal in enumerate(value_to_signal) }

#  aaaa
# b    c
# b    c
#  dddd 
# e    f
# e    f
#  gggg 

def parse_signals(signals):
    # populate signals for known lengths
    twothreefive = set()
    zerosixnine = set()
    for signal in signals:
        signal_length = len(signal)
        signal_set = frozenset(signal)
        if signal_length == len(value_to_signal[1]):
            one = signal_set
        elif signal_length == len(value_to_signal[7]):
            seven = signal_set
        elif signal_length == len(value_to_signal[4]):
            four = signal_set
        elif signal_length == len(value_to_signal[2]):
            twothreefive.add(signal_set)
        elif signal_length == len(value_to_signal[0]):
            zerosixnine.add(signal_set)
        elif signal_length == len(value_to_signal[8]):
            eight = signal_set

    # use set arithmetic to calculate mapping
    a = seven - one
    b_d = four - one
    e_g = (eight - four) - a
    a_d_g = frozenset.intersection(*twothreefive)
    d_g = a_d_g - a
    g = d_g - b_d
    e = e_g - g
    d = d_g - g
    b = b_d - d
    a_b_f_g = frozenset.intersection(*zerosixnine)
    f = a_b_f_g - a - b - g
    c = one - f
    
    decode_key = {
        list(a)[0]: 'a',
        list(b)[0]:'b',
        list(c)[0]: 'c', 
        list(d)[0]: 'd', 
        list(e)[0]: 'e', 
        list(f)[0]: 'f', 
        list(g)[0]: 'g',
    }
    return decode_key

def parse_output(signals, outputs):
    decode_key = parse_signals(signals)
    output_string = ''
    for output in outputs:
        signal_set = frozenset([decode_key[o] for o in output])
        output_string += str(signal_to_value[signal_set])
    
    return int(output_string)

def solution(problem):
    problem = [p.split(' | ') for p in problem]
    signals = [p[0].split() for p in problem]
    outputs = [p[1].split() for p in problem]

    return sum([parse_output(s, o) for (s, o) in zip(signals, outputs)])

if __name__ == '__main__':

    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
        print(solution(lines))


