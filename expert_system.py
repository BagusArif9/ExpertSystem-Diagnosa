class ExpertSystem:
    def __init__(self):
        self.rules = {
            "flu": {"demam": 0.5, "batuk": 0.3, "sesak napas": 0.2},
            "demam berdarah": {"demam": 0.6, "ruam": 0.4, "batuk": 0.1},
            "asma": {"batuk": 0.4, "sesak napas": 0.5, "demam": 0.1}
        }
        self.thresholds = {
            "flu": 0.6,
            "demam berdarah": 0.8,
            "asma": 0.7
        }

    def diagnose(self, symptoms):
        scores = {disease: 0 for disease in self.rules}
        for disease, conditions in self.rules.items():
            score = sum(min(symptoms.get(symptom, 0), weight) for symptom, weight in conditions.items())
            scores[disease] = score

        # Find the disease with the highest score that meets the threshold
        best_match = None
        highest_score = 0
        for disease, score in scores.items():
            if score >= self.thresholds[disease] and score > highest_score:
                highest_score = score
                best_match = disease
        
        if best_match:
            return best_match
        else:
            return "Tidak dapat mendiagnosa dengan gejala yang diberikan"
