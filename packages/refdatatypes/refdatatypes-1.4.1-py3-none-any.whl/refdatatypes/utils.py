def dict_item_must_be_list(input_: dict, item_key_path: str):
    """
    Check if last item in directory structure path is list, if not, convert it into list
    :param dict input_: Dictionary to check
    :param str item_key_path: Path to item separated by dots. Example "author.bio.books"
    """
    if not isinstance(input_, dict):
        return

    keys_split = item_key_path.split(".")
    current_key = keys_split[0]
    remaining_keys = keys_split[1:]
    current_item = input_.get(current_key)

    if remaining_keys:
        if isinstance(current_item, list):
            for item_index, item in enumerate(current_item):
                dict_item_must_be_list(item, ".".join(remaining_keys))
        else:
            dict_item_must_be_list(current_item, ".".join(remaining_keys))
    elif not isinstance(current_item, list):
        input_[current_key] = [] if current_item is None else [current_item]
