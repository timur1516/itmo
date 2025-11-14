class Function:
    def __init__(self, f, text):
        self.f = f
        self.text = text

    def compute(self, x):
        return self.f(x)

    def compute_or_none(self, x):
        try:
            return self.compute(x)
        except Exception:
            return None

    def __str__(self):
        return self.text
