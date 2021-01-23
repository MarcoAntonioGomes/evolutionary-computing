
class GaInputs:

    populationSize = 100
    maximumNumberOfGenerations = 10
    crossoverProbability = 0.50
    mutationProbability = 0.30

    def __init__(self, populationSize, maximumNumberOfGenerations, crossoverProbability, mutationProbability ):
        self.populationSize = populationSize
        self.maximumNumberOfGenerations = maximumNumberOfGenerations
        self.crossoverProbability = crossoverProbability
        self.mutationProbability = mutationProbability
