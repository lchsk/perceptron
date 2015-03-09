class Perceptron(object):

    def __init__(self, data, settings):
        
        self.data = data
        self.settings = settings

    def get_activation(self, item):

        return sum([self.data.get_weight(word) for word in item])

    def _test(self, test_data, correct_label):

        score = 0.0
        length = len(test_data)

        for item in test_data:
            a = self.get_activation(item[0])

            if (1 if a >= 0 else -1) == correct_label:
                score += 1

        return round(score * 100 / length, 3)

    def test(self):

        pos_pct = self._test(test_data=self.data.test_pos_list, correct_label=1)
        neg_pct = self._test(test_data=self.data.test_neg_list, correct_label=-1)
        overall = (pos_pct + neg_pct) / 2.0

        print 'Results:'
        print 'Accuracy (positive dataset): %.3f %%' % pos_pct
        print 'Accuracy (negative dataset): %.3f %%' % neg_pct
        print '-' * 40
        print 'Accuracy (overall): %.3f %%' % overall

    def train(self):

        for i in xrange(0, self.settings.params['iterations']):
            self._train()
            self.data.shuffle()

    def _train(self):

        for item in self.data.train_list:
            a = self.get_activation(item[0])

            if a * item[1] <= 0:
                self.data.update_weight(item)
