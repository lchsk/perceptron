import numpy

src = '../data/'

def get_union(fname):
    feats = set()
    F = open(fname)
    for line in F:
        for w in line.strip().split():
            feats.add(w)
    F.close()
    return feats

def process():
    featspace = get_union(src + "train.positive")
    featspace = featspace.union(get_union(src + "train.negative"))
    featspace = featspace.union(get_union(src + "test.positive"))
    featspace = featspace.union(get_union(src + "test.negative"))
    print len(featspace)
    print featspace
    pass

if __name__ == "__main__":
    process()
    
