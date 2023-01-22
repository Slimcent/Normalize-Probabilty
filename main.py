prob = {'A': 0.1, 'C': 0.1, 'G': 0.1, 'T': 0.1}


def normalize(probability):
    values = 0
    for key, value in probability.items():
        values += value
    for key, value in probability.items():
        probability[key] = value / values
    return probability


print(normalize(prob))


def normalize1(probabilities):
    NormProbabilities = probabilities.copy()
    n = sum(probabilities.values())
    for i in NormProbabilities:
        NormProbabilities[i] = NormProbabilities[i] / n
    return NormProbabilities


print(normalize1(prob))
