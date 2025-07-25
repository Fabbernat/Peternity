# C:\PycharmProjects\Peternity\modules_and_data\modules\wic_data_loader.py
def load_wic_data(data_path: object, gold_path: object) -> tuple[list[tuple[str, str, int, int, str, str]], list[str]]:
    """
        Loads the WiC dataset and its gold into a structured format.
        Extracts index1 and index2 from the index field.
     """

    data = []
    gold = []

    with open(data_path, 'r', encoding='utf-8') as f_data, open(gold_path, 'r', encoding='utf-8') as f_gold:
        for line, label in zip(f_data, f_gold):
            parts = line.strip().split('\t')  # Word, POS, index, sentence1, sentence2
            word, pos, index, sentence_a, sentence_b = parts

            '''
                This parser try-catch tries to convert  index1 and index2, the two, likely string variables to integers
                each sentence can be as long as 99 words.
                Their format:

                1-1
                6-7
                0-5
                14-8
                etc...
            '''
            try:
                index1, index2 = map(int, index.split('-'))  # Extract integer indices
            except ValueError:
                continue  # Skip lines with incorrect index format

            # Expand sentences with synonyms
            # sentence_a = NltkHandler.expand_with_synonyms(sentence_a)
            # sentenceB = NltkHandler.expand_with_synonyms(sentenceB)

            # Highlight target word for better feature extraction
            # sentence_a = sentence_a.replace(word, word + " " + word)
            # sentenceB = sentenceB.replace(word, word + " " + word)

            # sentence_a = expand_sentence_with_wsd(sentence_a, word)
            # sentenceB = expand_sentence_with_wsd(sentenceB, word)

            # sentence_a = normalize_sentence(sentence_a)
            # sentenceB = normalize_sentence(sentenceB)

            gold.append(label.strip())
            data.append((word, pos, index1, index2, sentence_a, sentence_b))

    return data, gold