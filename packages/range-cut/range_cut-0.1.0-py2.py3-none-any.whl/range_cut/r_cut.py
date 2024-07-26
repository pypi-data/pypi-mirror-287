


def cut(begin, end, step):
    start = begin
    while start < end:
        to = start + step
        if to > end:
            to = end
        yield start,to
        start = to
        

