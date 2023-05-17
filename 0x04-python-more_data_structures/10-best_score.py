#!/usr/bin/python3


def best_score(a_dict):
    if not a_dict:
        return None

    large = max(list(dict(a_dict).values()))
    for key in a_dict:
        if a_dict[key] == large:
            return key
