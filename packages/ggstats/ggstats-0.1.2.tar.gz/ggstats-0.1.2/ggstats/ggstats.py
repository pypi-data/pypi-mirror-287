class EvalMetrics:
    def __init__(self, tp=None, fp=None, tn=None, fn=None, prev=None, sens=None, spec=None):
        self.tp = tp
        self.fp = fp
        self.tn = tn
        self.fn = fn
        self.prev = prev
        self.sens = sens
        self.spec = spec
        print("Thanks for using this class. The class EvalMetrics is initiated")

    def get_sensitivity(self, tp=None, fn=None):
        tp = tp if tp is not None else self.tp
        fn = fn if fn is not None else self.fn
        if tp is None or fn is None:
            raise ValueError("Insufficient data to calculate sensitivity. Please provide True Positive (tp) and False Negative (fn).")
        self.sens = tp / (tp + fn)
        print(f"Sensitivity is {self.sens}")
        return self.sens

    def get_specificity(self, tn=None, fp=None):
        tn = tn if tn is not None else self.tn
        fp = fp if fp is not None else self.fp
        if tn is None or fp is None:
            raise ValueError("Insufficient data to calculate specificity. Please provide True Negative (tn) and False Positive (fp).")
        self.spec = tn / (tn + fp)
        print(f"Specificity is {self.spec}")
        return self.spec

    def get_accuracy(self, sens=None, spec=None, prev=None):
        sens = sens if sens is not None else self.sens
        spec = spec if spec is not None else self.spec
        prev = prev if prev is not None else self.prev
        if sens is None:
            sens = self.get_sensitivity()
        if spec is None:
            spec = self.get_specificity()
        if prev is None:
            raise ValueError("Insufficient data to calculate accuracy. Please provide prevalence (prev).")
        accuracy = sens * prev + spec * (1 - prev)
        print(f"Accuracy is: {accuracy}")
        return accuracy

    def get_ppv(self, sens=None, spec=None, prev=None):
        sens = sens if sens is not None else self.sens
        spec = spec if spec is not None else self.spec
        prev = prev if prev is not None else self.prev
        if sens is None:
            sens = self.get_sensitivity()
        if spec is None:
            spec = self.get_specificity()
        if prev is None:
            raise ValueError("Insufficient data to calculate PPV. Please provide prevalence (prev).")
        ppv = (sens * prev) / ((sens * prev) + (1 - spec) * (1 - prev))
        print(f"Positive Predictive Value is: {ppv}")
        return ppv

# Example usage:
# metrics = EvalMetrics(tp=50, fp=10, tn=100, fn=5, prev=0.1)
# metrics.get_accuracy()
# metrics.get_ppv()
