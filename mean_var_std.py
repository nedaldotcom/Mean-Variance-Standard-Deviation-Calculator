import numpy as np

def calculate(list):
  if len(list) == 9:
    a = np.array(list).reshape([3,3])
    calculations = {
      "mean": [a.mean(0).tolist(), a.mean(1).tolist(), a.mean()],
      "variance": [a.var(0).tolist(), a.var(1).tolist(), a.var()],
      "standard deviation": [a.std(0).tolist(), a.std(1).tolist(), a.std()],
      "max": [a.max(0).tolist(), a.max(1).tolist(), a.max()],
      "min": [a.min(0).tolist(), a.min(1).tolist(), a.min()],
      "sum": [a.sum(0).tolist(), a.sum(1).tolist(), a.sum()]
      
    }
    return calculations
  else:
    raise ValueError("List must contain nine numbers.")