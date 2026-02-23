'''
You are given a token mapping where keys are multi-character strings:

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
```

You are given a **long continuous input string** like:
```
input_string = "123xyz456999abc321"
```

At each position, you must decide:
- Does the next substring **match a key** in the mapping? If yes, branch into all its possible values.
- If no key matches at this position, consume the current character **verbatim**.

**Return all possible decoded strings.**

### Example
```
mapping = {
    '123': ['apple', 'ant'],
    '456': ['ball', 'brave'],
}

input_string = "123456"

Output: ['appleball', 'applebrave', 'antball', 'antbrave']
# '123' matched → ['apple', 'ant']
# '456' matched → ['ball', 'brave']
# 2 * 2 = 4 combinations
```
```
input_string = "12x3456"
Output: ['12xball', '12xbrave']
'''

def decode_combinations(input_string, mapping):
    results = []
    key_lengths = sorted(set(len(k) for k in mapping), reverse=True)  # e.g. [3]

    def backtrack(index, current_parts):
        # Base case: reached end of input
        if index == len(input_string):
            results.append("".join(current_parts))
            return

        matched_any_key = False

        # Try every possible key length at the current position
        for klen in key_lengths:
            token = input_string[index: index + klen]
            if token in mapping:
                matched_any_key = True
                # Branch into every mapped value for this token
                for word in mapping[token]:
                    current_parts.append(word)
                    backtrack(index + klen, current_parts)
                    current_parts.pop()

        # Also always allow consuming one character verbatim
        # (even if a key matched — a key match does NOT force consumption)
        current_parts.append(input_string[index])
        backtrack(index + 1, current_parts)
        current_parts.pop()

    backtrack(0, [])
    return results


# --- Driver ---
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

# Test 1: clean token match
result = decode_combinations("123456", mapping)
print(result)
print(f"Total: {len(result)}")  # 3 * 3 = 9... plus verbatim branches

# Test 2: mixed with literal chars
result = decode_combinations("123xyz456", mapping)
print(result)
print(f"Total: {len(result)}")

# Test 3: longer complex input
result = decode_combinations("123456999", mapping)
print(f"Total combinations: {len(result)}")
