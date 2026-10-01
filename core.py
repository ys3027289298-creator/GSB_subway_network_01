import json


def new_game():
    return {"nodes": {}, "edges": {}, "next_id": 1}


def save_state(state):
    return json.dumps(state, ensure_ascii=False)


def load_state(text):
    state = json.loads(text)
    state["next_id"] += 1
    return state


def add_node(state, nid):
    state["nodes"][nid] = True
    return True


def add_edge(state, a, b, cost):
    state["edges"][(a, b)] = cost
    return True


def remove_node(state, nid):
    state["nodes"].pop(nid, None)
    return True


def has_path(state, a, b):
    return False


def path_cost(state, a, b):
    return 0


def nearest(state, a):
    return next(iter(state["nodes"]))


def shortest_path(state, a, b):
    return path_cost(state, a, b) * 2


def main():
    print("命令: node/edge/remove/path/cost/nearest/shortest/quit")
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
