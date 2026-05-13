class Node:

    def __init__(self, val, text):
        self.val = val
        self.text = text
        self.options = []
        self.parent = None

    def add_option(self, option):
        self.options.append(option)
        option.parent = self


class Tree:

    def __init__(self, root):
        self.root = root
    
    def __repr__(self):
        answer = ""
        return self.get_text_r(self.root, answer)
    
    def get_text_r(self,current_node, answer):
        answer += current_node.text
        answer += "\n"
        for option in current_node.options:
            answer = self.get_text_r(option, answer)
        return answer
        