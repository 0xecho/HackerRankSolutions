

def person_lister(f):
    def inner(people):
        ret = []
        people.sort(key=lambda x:int(x[2]))
        for person in people:
            ret.append(f(person))
        return ret
    return inner

