def item_entity(db_item) -> dict:
    """_summary_
    Function for the data insertion

    Args:
        db_item (_type_): Item from the to do list to be inserted on the db
    """
    return {
        "id" : str(db_item['_id']),
        'name' : db_item['name'],
        'description' : db_item['description'],
        'responsavel' : db_item['responsavel'],
        'prioridade' : db_item['prioridade'],
    }

def list_items(db_item_list) -> list:
    """
    Return the data

    Args:
        db_item_list (_type_): _description_

    Returns:
        list: _description_
    """
    items_list = []
    for element in db_item_list:
        items_list.append(item_entity(element))
    return items_list