def decode(inputs, mapping):
    results = []
    def f(outstr, index, inputs):
        if index > len(inputs) -1:
            results.append(outstr)
            return
        else:
            if inputs[index:index+3] in mapping.keys():
                for item in mapping[inputs[index:index+3]]+[inputs[index:index+3]]:
                    f(outstr+item, index+3, inputs)
            else:
                f(outstr+inputs[index], index+1, inputs)
    f('',0, inputs)   
    return results

mapping = {
    '123': ['apple', 'ant', 'azure'],
    '456': ['ball', 'brave', 'bloom'],
    '789': ['cat', 'crane', 'crisp'],
    '012': ['dog', 'drift', 'dune'],
    '321': ['eagle', 'echo', 'ember'],
    '654': ['frost', 'flare', 'fog', 'flame'],
    '987': ['grape', 'glow', 'glen'],
    '111': ['honey', 'hawk', 'haze', 'hurl'],
    '000': ['sky', 'storm', 'swift'],
    '999': ['rose', 'river', 'rain', 'rush']
}

inputs = '123456999'
results = decode(inputs, mapping)
print(len(results))
