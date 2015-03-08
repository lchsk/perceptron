


class Perceptron(object):

    def __init__(self, data):
        
        self.data = data

    def get_activation(self, item):

        return sum([self.data.get_weight(word) for word, weight in item])

    def test(self):

        score = 0.0
        length = len(self.data.test_pos_list)

        for item in self.data.test_pos_list:
            a = self.get_activation(item[0])

            if (1 if a >= 0 else -1) == 1:
                score += 1

        print round(score * 100 / length, 3)

    def train(self):

        # print self.data.train_list[3][1]
        # for it in xrange(0, 3):


        for item in self.data.train_list:
            a = self.get_activation(item[0])

            if a * item[1] <= 0:
                self.data.update_weight(item)
