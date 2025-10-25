import torch

if torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"

print(f"Running on: {device}")
