import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  scientific_calcu = np.array(list).reshape((3, 3))
  calculations = {
    "mean": [
      np.mean(scientific_calcu, axis = 0).tolist(),
      np.mean(scientific_calcu, axis = 1).tolist(),
      np.mean(scientific_calcu.tolist())
    ],
    "variance": [
      np.var(scientific_calcu, axis = 0).tolist(),
      np.var(scientific_calcu, axis = 1).tolist(),
      np.var(scientific_calcu) .tolist()    
    ],
    "standard deviation": [
      np.std(scientific_calcu, axis = 0).tolist(),
      np.std(scientific_calcu, axis = 1).tolist(),
      np.std(scientific_calcu).tolist()     
    ],   
    "max": [
      np.max(scientific_calcu, axis = 0).tolist(),
      np.max(scientific_calcu, axis = 1).tolist(),
      np.max(scientific_calcu).tolist()     
    ], 
    "min": [
      np.min(scientific_calcu, axis = 0).tolist(),
      np.min(scientific_calcu, axis = 1).tolist(),
      np.min(scientific_calcu).tolist()     
    ], 
    "sum": [
      np.sum(scientific_calcu, axis = 0).tolist(),
      np.sum(scientific_calcu, axis = 1).tolist(),
      np.sum(scientific_calcu).tolist()     
    ],  
  }

  return calculations