def str_to_list(sep, s):
    if type(s) == type(str()):
        return s.split(sep)
    return None
def multi_str_to_list(sep, *args):
    ls = []
    for a in args:
        ls.extend(a.split(sep))
    return sep.join(ls)
