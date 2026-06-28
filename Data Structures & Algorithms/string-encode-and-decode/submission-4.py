class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f'{len(s)}')
            res.append('#')
            res.append(s)
        #print('res', res)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        length_idx = 0
        #print('s', s)

        while length_idx < len(s):
            delim_idx = length_idx + 1
            while s[delim_idx] != '#':
                delim_idx += 1
            #print('delim_idx', delim_idx, 'length_idx', length_idx)
            curr_len = int(s[length_idx:delim_idx])
            curr_str = s[delim_idx+1:delim_idx+curr_len+1]
            #print('delim_idx', delim_idx, 'length_idx', length_idx, 'curr_len', curr_len, 'curr_str', curr_str)
            res.append(curr_str)
            length_idx = delim_idx + curr_len + 1 
        return res


