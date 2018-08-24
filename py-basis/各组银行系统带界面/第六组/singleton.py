def singletonDeco(cls):
    instances = {}
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
            print(instances[cls],cls)
        return instances[cls]
    return getinstance