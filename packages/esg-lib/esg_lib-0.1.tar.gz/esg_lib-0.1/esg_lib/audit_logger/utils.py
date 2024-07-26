import copy

from typing import Union
from flask import Request


def get_json_body(req: Request) -> Union[list, dict]:
    try:
        body = req.json or {}
    except Exception:
        body = {}

    return body


def get_only_changed_values(old_data: dict, new_data: dict):
    diff_dict = {}
    old_dict = {}

    for key in new_data:
        if key in old_data:
            if isinstance(new_data[key], dict) and isinstance(old_data[key], dict):
                # If both values are dictionaries, recursively compare them
                new_diff, old_diff = get_only_changed_values(old_data[key], new_data[key])
                if new_diff:
                    diff_dict[key] = new_diff
                if old_diff:
                    old_dict[key] = old_diff
            elif isinstance(new_data[key], list) and isinstance(old_data[key], list):
                new_d1 = copy.deepcopy(new_data[key])
                old_d1 = copy.deepcopy(old_data[key])
                new_d1.sort()
                old_d1.sort()
                if new_d1 != old_d1:
                    diff_dict[key] = new_data[key]
                    old_dict[key] = old_data[key]
            elif new_data[key] != old_data[key]:
                # If the values are different, add to the diff_dict
                diff_dict[key] = new_data[key]
                old_dict[key] = old_data[key]
        else:
            # If the key is not present in dict2, add to the diff_dict
            diff_dict[key] = new_data[key]

    return diff_dict, old_dict


def get_only_changed_values_and_id(old_data: dict, new_data: dict):
    diff_dict, old_dict = get_only_changed_values(old_data, new_data)

    if "_id" in old_data:
        diff_dict["_id"] = old_data.get("_id")
        diff_dict.pop("id", None)

    return diff_dict, old_dict


def get_action(http_method: str, status_code: int) -> str:
    if http_method == "GET":
        return "RETRIEVE"

    if http_method == "POST":
        if status_code == 201:
            return "CREATE"
        return "UPDATE"

    if http_method == "PUT" or http_method == "PATCH":
        return "UPDATE"

    if http_method == "DELETE":
        return "DELETE"


def get_primary_key_value(key_list: list, data: dict):
    if not isinstance(data, dict):
        return None

    if len(key_list) == 1:
        return data.get(key_list[0])

    return get_primary_key_value(key_list[1:], data.get(key_list[0]))
