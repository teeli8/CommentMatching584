class State(object):

    def __init__(self, label):
        self.label = label
        self.transitions = {}
        self.final = False

    def next_state(self, c):
        return self.transitions.get(c, None)

    def accepts(self, w):
        s = self
        for c in w:
            s = s.next_state(c)
            if s is None:
                return False
        return s.final

    def add_transition(self, c, s):
        self.transitions[c] = s

    def add_transition_to_a_new_state(self, c, label):
        s = State(label)
        self.add_transition(c, s)
        return s

    def set_final(self, final):
        self.final = final

    def inf_labels(s=0):
        while True:
            yield s
            s += 1

    def add_suffix(state, word, labels):
        for c in word:
            state = state.add_transition_to_a_new_state(c, next(labels))
        state.final = True

    def common_prefix(state, word):
        current_state = state
        for i, c in enumerate(word):
            s = current_state.next_state(c)
            if s is not None:
                current_state = s
            else:
                return current_state, i
        return current_state, i + 1



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s0 = State(0)
    s1 = s0.add_transition_to_a_new_state('w', 1)
    s2 = s1.add_transition_to_a_new_state('a', 2)
    s3 = s2.add_transition_to_a_new_state('s', 3)
    s4 = s3.add_transition_to_a_new_state('p', 4)
    s4.set_final(True)
    s5 = s1.add_transition_to_a_new_state('i', 5)
    s6 = s5.add_transition_to_a_new_state('s', 6)
    s7 = s6.add_transition_to_a_new_state('p', 7)
    s7.set_final(True)
    s0.accepts('was') # False
    print(s0.final)
    s0.accepts('wasp') #True
    s0.accepts('wisp') #True
    s0.accepts('cat') # False

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
