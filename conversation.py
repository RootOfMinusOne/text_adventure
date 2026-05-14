from tree import Tree, Node

class Conversation:

    def __init__(self, path):
        self.tree = self.set_tree(path)
        self.current_node = self.tree.root
        self.state = 0


    def print_line(self):
        if self.state == 0:
            print("\n")
            print("============ Root Of Minus One ============")
            print(self.current_node.text)
            if self.current_node.options:
                self.state = 1
            else:
                self.state = 2
        else:
            print("\n")
            print("============ Choose One ============")
            for line in self.current_node.options:
                print(f"{line.val[-1]} : {line.text}")
                print("\n")
            
    
    def listen_for_input(self):
        x = input()
        for option in self.current_node.options:
            if option.val[-1] == x:
                self.current_node = option
                print("\n")
                print("============ You ============")
                print(self.current_node.text)
                if self.current_node.options:
                    self.current_node = self.current_node.options[0]
                    self.state = 0
                else:
                    self.state = 2
                return
        print("That's not a valid option, pick again")
        self.listen_for_input




    def set_tree(self, path):
        file = open(path)
        text = file.read().split("\n")
        file.close()
        val, line = self.analize_line(text[0])
        root = Node(val, line)
        print(len(text))
        self.set_tree_r(root, 1, text)
        
        return Tree(root)
            
    def set_tree_r(self,current_node, current_line, text):
        if current_line >= len(text) or text[current_line]=="":
            return
        val, line = self.analize_line(text[current_line])

        
        if val[:-2] == current_node.val:
            new_node = Node(val, line)
            current_node.add_option(new_node)
            self.set_tree_r(current_node, current_line + 1, text)
        
        elif len(val) <= len(current_node.val):
            if current_node.parent != None:
                self.set_tree_r(current_node.parent, current_line, text)
            else:
                raise Exception("Wrong text format")
        
        elif len(val) -2 >= len(current_node.val):
            search_val = val[:len(current_node.val)+2]
            for option in current_node.options:
                if option.val == search_val:
                    self.set_tree_r(option, current_line, text)
                    return
            self.set_tree_r(current_node.parent, current_line, text)
                







    def analize_line(self, line):
        characters = list(line)
        iter = 0
        code = ""
        while characters[iter] != ":":

            code +=characters[iter]
            iter += 1
        
        return(code, line[iter+1:]) 




