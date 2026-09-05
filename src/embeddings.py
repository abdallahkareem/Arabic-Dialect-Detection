from gensim.models import FastText, Word2Vec


def embedding_model(data, vector_size=300, window=5, min_count=1, workers=4):
    """
    Train a FastText model on the provided data.

    Parameters:
    - data: List of tokenized sentences (list of lists of words).
    - vector_size: Dimensionality of the word vectors.
    - window: Maximum distance between the current and predicted word within a sentence.
    - min_count: Ignores all words with total frequency lower than this.
    - workers: Number of worker threads to train the model.

    Returns:
    - model: Trained FastText model.
    """
    model = FastText(sentences=data, vector_size=vector_size, window=window, min_count=min_count, workers=workers)
    return model


