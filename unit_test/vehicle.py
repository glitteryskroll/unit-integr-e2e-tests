class Vehicle:
    def __init__(self, model, **kwargs):
        super().__init__()
        self.model = model
        self.info = kwargs