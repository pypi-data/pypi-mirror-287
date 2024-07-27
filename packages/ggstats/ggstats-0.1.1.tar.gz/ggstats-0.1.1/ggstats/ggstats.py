# Useful stats functions to calculate evaluation metric

class EvalMetrics():
    def __init__(self, tp=None, fp=None, tn=None, fn=None, prev=None, sens=None, spec=None):
        self.tp = tp
        self.fp = fp
        self.tn = tn
        self.fn = fn
        self.prev = prev
        self.sens = sens
        self.spec = spec
        print("Thanks for using this calss. The class EvalMetric is initiated")

    def get_sensitivity(self,tp=None,fn=None):
        if self.tp is None or self.fn is None:
            raise ValueError("Insufficient data to calculate sensitivity. Please provide True Positive (tp) and False Negative (fn).")
        self.sens = self.tp / (self.tp + self.fn)
        print(f"Sensitivity is {self.sens}")
        return self.sens

    def get_specificity(self,tn=None,fp=None):
        if self.tn is None or self.fp is None:
            raise ValueError("Insufficient data to calculate specificity. Please provide True Negative (tn) and False Positive (fp).")
        self.spec = self.tn / (self.tn + self.fp)
        print(f"Specificity is {self.spec}")
        return self.spec

    def get_accuracy(self,sens=None,spec=None,prev=None):
        if self.sens is None:
            self.get_sensitivity()
        if self.spec is None:
            self.get_specificity()
        if self.prev is None:
            raise ValueError("Insufficient data to calculate accuracy. Please provide prevalence (prev).")
        accuracy = self.sens * self.prev + self.spec * (1 - self.prev)
        print(f"Accuracy is: {accuracy}")
        return accuracy

    def get_ppv(self,sens=None,spec=None,prev=None):
        if self.sens is None:
            self.get_sensitivity()
        if self.spec is None:
            self.get_specificity()
        if self.prev is None:
            raise ValueError("Insufficient data to calculate PPV. Please provide prevalence (prev).")
        ppv = (self.sens * self.prev) / ((self.sens * self.prev) + (1 - self.spec) * (1 - self.prev))
        print(f"Positive Predictive Value is: {ppv}")
        return ppv

# Example:
# metrics = EvalMetrics(sens=0.9, spec=0.8, prev=0.2)
# metrics.get_accuracy()
