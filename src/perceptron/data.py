import random

class Data(object):

    def __init__(self, directory, train_neg, train_pos, test_neg, test_pos):
        
        # Directory in which data files are located
        self.dir = directory

        # Filenames of data files
        self.train_neg = train_neg
        self.train_pos = train_pos
        self.test_neg = test_neg
        self.test_pos = test_pos

        # self.train_neg_list = []
        # self.train_pos_list = []
        # self.test_neg_list = []
        # self.test_pos_list = []

        self.train_list = []
        self.test_pos_list = []
        self.test_neg_list = []

        self.words = {}

        self.load()

    def get_weight(self, word):
        return self.words[word][1]

    def update_weight(self, item):

        words = item[0]
        label = item[1]

        for word, weight in words:
            # print word
            # print self.words[word]
            self.words[word][1] = self.words[word][1] + label

    def _load(self, filename, label, target_obj):

        f = open(self.dir + filename, 'r')
        loaded = []
        # loaded2 = set()

        for line in f:

            instance = []
            features = []
            # s = [x for x in line.strip().split()]
            for x in line.strip().split():
                features += [(x, 0)]

                if x not in self.words:
                    # label (1, -1), weight
                    self.words[x] = [label, 0]

            # features.append(label)
            instance.append(features)
            instance.append(label)

            loaded += [instance]


            # loaded2 = loaded2.union(set(s))

        f.close()
        target_obj += loaded
        # print loaded[:1]
        # print self.words

    def load(self):
        self._load(self.train_pos, 1, self.train_list)
        self._load(self.train_neg, -1, self.train_list)

        self._load(self.test_pos, 1, self.test_pos_list)
        self._load(self.test_neg, -1, self.test_neg_list)

        self.shuffle()

    def shuffle(self):
        random.shuffle(self.train_list)

