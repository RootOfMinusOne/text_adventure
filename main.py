from tree import Tree, Node
from conversation import Conversation

def main():

    demo_conversation = Conversation("conversations/Demo.txt")
    while(demo_conversation.state != 2):
        demo_conversation.print_line()
    print(("============ The End ============"))

main()