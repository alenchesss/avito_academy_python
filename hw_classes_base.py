import math


class CountVectorizer:
    """Считает количество, сколько раз слово встретилось в тексте"""

    def __init__(self, lowercase: bool = True, ngram_size: int = 1):
        self._vocabulary = {}
        self.lowercase = lowercase
        self.ngram_size = ngram_size

    @property
    def vocabulary(self) -> dict:
        """Возвращает словарь слов и их индексов"""
        return self._vocabulary

    @vocabulary.setter
    def vocabulary(self, value: dict) -> None:
        """Создает новый словарь"""
        indexses = list(value.values())
        if (any(type(i) is not int for i in indexses)
                or sorted(indexses) != list(range(len(indexses)))):
            raise ValueError('Некорректные индексы словаря')
        self._vocabulary = value.copy()

    @vocabulary.deleter
    def vocabulary(self) -> None:
        """Удаляет словарь"""
        self._vocabulary = {}

    @classmethod
    def from_dict(cls, state: dict):
        """Создает модель из сохраненного словаря"""
        model = cls(
            lowercase=state.get('lowercase', True),
            ngram_size=state.get('ngram_size', 1)
        )
        model.vocabulary = state.get('vocabulary', {})
        return model

    def to_dict(self) -> dict:
        """Сохраняет настройки и словарь модели"""
        return {
            'lowercase': self.lowercase,
            'ngram_size': self.ngram_size,
            'vocabulary': self.vocabulary.copy()
        }

    def add_word(self, word: str) -> int:
        """Добавляет слово в словарь и возвращает его индекс"""
        if word not in self.vocabulary:
            self.vocabulary[word] = len(self.vocabulary)
        return self.vocabulary[word]

    def tokenize(self, text: str) -> list:
        """Разбивает текст на слова или n-граммы"""
        if self.lowercase:
            text = text.lower()
        text = text.split()
        answer = []
        for i in range(len(text) - (self.ngram_size - 1)):
            answer.append(' '.join(text[i:i + self.ngram_size]))
        return answer

    def fit(self, corpus: list):
        """Обучает модель на текстах"""
        words = []
        for text in corpus:
            words += self.tokenize(text)
        if len(words) == 0:
            raise ValueError()
        self.vocabulary = {}
        for word in words:
            self.add_word(word)
        return self

    def get_feature_names(self) -> list:
        """Возвращает слова в порядке индексов"""
        return sorted(self.vocabulary, key=self.vocabulary.get)

    def transform(self, corpus: list) -> list:
        """Переводит тексты в матрицу частот слов"""
        if not self.vocabulary:
            raise RuntimeError('Модель не обучена')
        matrix = []
        for t in corpus:
            row = [0] * len(self.vocabulary)
            for token in self.tokenize(t):
                if token in self.vocabulary:
                    row[self.vocabulary[token]] += 1
            matrix.append(row)
        return matrix

    def fit_transform(self, corpus: list) -> list:
        """Обучает модель и возвращает матрицу частот"""
        return self.fit(corpus).transform(corpus)


class BinaryVectorizer(CountVectorizer):

    def transform(self, corpus: list) -> list:
        """Переводит тексты в матрицу из нулей и единиц"""
        matrix = super().transform(corpus)

        for row in matrix:
            for i, value in enumerate(row):
                if value > 0:
                    row[i] = 1

        return matrix


class TfidfVectorizer(CountVectorizer):
    """Считает веса слов по TF-IDF"""

    def __init__(self, lowercase: bool = True, use_idf: bool = True):
        super().__init__(lowercase=lowercase)
        self.use_idf = use_idf
        self._idf = []

    @property
    def idf(self) -> list:
        """Возвращает список весов IDF"""
        return self._idf.copy()

    @classmethod
    def from_config(cls, config: dict):
        """Создает модель с настройками из словаря"""
        model = cls(
            lowercase=config.get('lowercase', True),
            use_idf=config.get('use_idf', True)
        )
        return model

    def fit(self, corpus: list):
        """Обучает модель и считает IDF"""
        super().fit(corpus)
        self._idf = []

        if self.use_idf:
            matrix = super().transform(corpus)

            for i in range(len(self.vocabulary)):
                count = 0
                for row in matrix:
                    if row[i] > 0:
                        count += 1

                value = math.log((len(corpus) + 1) / (count + 1)) + 1
                self._idf.append(value)

        return self

    def transform(self, corpus: list) -> list:
        """Рассчитывает веса TF-IDF для текса"""
        matrix = super().transform(corpus)
        answer = []
        for row in matrix:
            total = sum(row)
            new_row = []
            for i, count in enumerate(row):
                if total == 0:
                    value = 0.0
                else:
                    value = count / total
                    if self.use_idf:
                        value *= self._idf[i]
                new_row.append(value)
            answer.append(new_row)
        return answer


class KeywordExtractor:

    def __init__(self, vectorizer: CountVectorizer, top_n: int = 3):
        self.vectorizer = vectorizer
        self.top_n = top_n

    @property
    def top_n(self) -> int:
        """Возвращает количество ключевых слов"""
        return self._top_n

    @top_n.setter
    def top_n(self, value: int) -> None:
        """Устанавливает количество ключевых слов"""
        if type(value) is not int or value <= 0:
            raise ValueError()
        self._top_n = value

    def fit(self, corpus: list):
        """Обучает векторизатор на текстах"""
        self.vectorizer.fit(corpus)
        return self

    def extract(self, corpus: list) -> list:
        """Возвращает ключевые слова и их веса"""
        matrix = self.vectorizer.transform(corpus)
        words = self.vectorizer.get_feature_names()
        answer = []
        for row in matrix:
            result = []
            for i, value in enumerate(row):
                if value > 0:
                    result.append((words[i], value))
            result.sort(key=lambda x: (-x[1], x[0]))
            answer.append(result[:self.top_n])
        return answer


TRAIN_CORPUS = [
    'Марс сигнал сигнал',
    'Марс пыль',
    'Марс сигнал антенна',
]

CHECK_CORPUS = [
    'СИГНАЛ шум сигнал',
    'антенна пыль',
    'марс марс марс',
    'комета', ''
]


def demo() -> None:
    # 1 номер
    tfidf = TfidfVectorizer.from_config({})
    matrix = tfidf.fit_transform(TRAIN_CORPUS)
    print('Слова:', tfidf.get_feature_names())
    print('IDF:', tfidf.idf)
    print('Матрица:', matrix)
    print('Матрица transform:', tfidf.transform(TRAIN_CORPUS))

    weights = tfidf.idf
    weights.clear()
    print('IDF после очистки:', tfidf.idf)

    # 2 номер
    tf = TfidfVectorizer.from_config({
        'lowercase': False,
        'use_idf': False
    })
    corpus = ['Марс марс', 'МАРС сигнал']
    tf.fit(corpus)
    print('Слова:', tf.get_feature_names())
    print('IDF:', tf.idf)
    print('TF:', tf.transform(corpus))

    tfidf.fit(['Венера облака'])
    print('Слова:', tfidf.get_feature_names())
    print('IDF:', tfidf.idf)
    print('Матрица:', tfidf.transform(['Марс Венера облака']))

    # 3 номер
    extractor = KeywordExtractor(tfidf, top_n=2)
    extractor.fit(TRAIN_CORPUS)
    print('top_n=2:', extractor.extract(CHECK_CORPUS))
    extractor.top_n = 1
    print('top_n=1:', extractor.extract(CHECK_CORPUS))
    try:
        extractor.top_n = 0
    except ValueError:
        print('Некорректное значение top_n')


if __name__ == '__main__':
    demo()
