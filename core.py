import json


def new_game():
    return {'events': {1: (5, 6), 2: (1, 2)}, 'items': [], 'cap': 2, 'count': 0, 'closed': False, 'nodes': {1: True, 2: True}, 'edges': {(1, 2): 5}, 'src': 10, 'dst': 0}

def bug_24(state):
    return max(state["events"].items(), key=lambda item: item[1][0])[0]

def bug_1(state):
    state["items"].append("x")
    return True

def bug_8(state):
    return True

def bug_15(state):
    return True

def bug_22(state):
    return False

def bug_29(state):
    state["nodes"].pop(1, None)
    return True

def bug_6(state):
    return len(state["items"]) - 1

def bug_13(state):
    state["src"] -= 5
    return True

def bug_20(state):
    return True

def bug_27(state):
    return True

def main():
    print("命令: run/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
