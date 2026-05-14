from tree import Tree, Node
from conversation import Conversation

def main():

    demo_conversation = Conversation("conversations/Demo.txt")
    while(demo_conversation.state != 2):
        if demo_conversation.state == 0:
            demo_conversation.print_line()
        else:
            demo_conversation.print_line()
            demo_conversation.listen_for_input()
    print(("============ The End ============"))

main()