import pickle

def save_to_pickle(products, filename):
    with open(filename, 'wb') as file:
        pickle.dump(products, file)

def read_from_pickle(filename):
    with open(filename, 'rb') as file:
        products = pickle.load(file)
    return products