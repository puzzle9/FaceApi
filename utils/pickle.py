import pickle


def PickleDumps(data):
    return pickle.dumps(data)

def PickleLoads(data):
    return pickle.loads(data)