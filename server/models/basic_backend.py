# basic_backend.py

import mvc_exceptions as mvc_exc

# Test data
items = []


def create_items(app_items):
    global items
    items = app_items


def create_item(name, price, quantity):
    global items
    results = list(filter(lambda x: x['name'] == name, items))
    if results:
        raise mvc_exc.ItemAlreadyExists('"{}" already stored!'.format(name))
    else:
        items.append({'name': name, 'price': price, 'quantity': quantity})


def read_item(name):
    global items
    myitems = list(filter(lambda x: x['name'] == name, items))
    if myitems:
        return myitems[0]
    else:
        raise mvc_exc.ItemDoesNotExist(
            'Can\'t read "{}" because it\'s not stored'.format(name))


def read_items():
    global items
    return [item for item in items]


def update_item(name, price, quantity):
    global items
    idxs_items = list(
        filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))
    if idxs_items:
        i = idxs_items[0][0]
        items[i] = {'name': name, 'price': price, 'quantity': quantity}
    else:
        raise mvc_exc.ItemDoesNotExist(
            'Can\'t update "{}" because it\'s not stored'.format(name))


def delete_item(name):
    global items
    idxs_items = list(
        filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))
    if idxs_items:
        i = idxs_items[0][0]
        del items[i]
    else:
        raise mvc_exc.ItemDoesNotExist(
            'Can\'t delete "{}" because it\'s not stored'.format(name))
