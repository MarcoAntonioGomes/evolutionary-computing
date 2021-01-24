

class SelectionOperators:

    def fitness_proportional_selection(self, subjec_fitness, sum_of_others_subjects_fitness) -> float:
       return subjec_fitness/sum_of_others_subjects_fitness

    def linear_ranking(self, straight_slope, population_length,index) -> float:
        return ((2 - straight_slope) / population_length) + (2*index*(straight_slope-1))/(population_length*(population_length-1))