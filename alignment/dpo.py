import torch.nn.functional as F

class DPOTrainer:
    def __init__(self, beta=0.1): self.beta = beta
    def loss(self, chosen, rejected):
        logits = self.beta*(chosen-rejected)
        return -F.logsigmoid(logits).mean()
