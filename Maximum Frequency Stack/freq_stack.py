from collections import deque
 
class FreqStack:

    def __init__(self):
        self.val_freq = {}
        self.freq_vals = {}
        self.max_freq = 0
        

    def push(self, val: int) -> None:
        try:
            self.val_freq[val] += 1
        except KeyError:
            self.val_freq[val] = 1

        freq = self.val_freq[val]

        try:
            self.freq_vals[freq].append(val)
        except KeyError:
            self.freq_vals[freq] = deque([val])
        
        self.max_freq = max(self.max_freq, freq)

    def pop(self) -> int:
        most_frequent = self.freq_vals[self.max_freq].pop()
        self.val_freq[most_frequent] -= 1
        if not self.freq_vals[self.max_freq]:
            self.max_freq -= 1
        return most_frequent
