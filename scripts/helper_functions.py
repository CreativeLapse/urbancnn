def get_map_id(heat_maps, map_name):
    """
    Retrieves the mapID for a given map name from the heat_maps list.

    Args:
        heat_maps (list): List of heat map dictionaries.
        map_name (str): The name of the heat map to search for.

    Returns:
        str or None: The mapID if found, else None.
    """
    return next((map_item["mapID"] for map_item in heat_maps if map_item["name"] == map_name), None)

def get_map_filepath(heat_maps, map_name, index):
    """
    Retrieves the formatted file path for a given map name from the heat_maps list.

    Args:
        heat_maps (list): List of heat map dictionaries.
        map_name (str): The name of the heat map to search for.
        index (int): The index to insert into the file path.

    Returns:
        str or None: The formatted file path if found, else None.
    """
    return next(
        (map_item["file_path"].format(index=index) for map_item in heat_maps if map_item["name"] == map_name),
        None
    )