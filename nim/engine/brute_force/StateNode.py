import json


class StateNode:

    def __init__(self):
        self.move = (0, 0)
        self.is_winning = None
        self.children: [StateNode] = []

    def __repr__(self):
        return f"{self.move}"

    def to_json(self):
        return {
            "m": {
                "i": self.move[0],
                "n": self.move[1]
            },
            "w": 1 if self.is_winning else 0,
            "c": [child.to_json() for child in self.children]
        }
