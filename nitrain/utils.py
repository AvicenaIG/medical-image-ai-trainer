
import os
import ants
import numpy as np

def get_medical-image-ai-trainer_dir():
    if os.environ.get('NITRAIN_DIR') is not None:
        medical-image-ai-trainer_dir = os.environ['NITRAIN_DIR']
    else:
        medical-image-ai-trainer_dir = os.path.join(os.path.expanduser('~'), '.medical-image-ai-trainer')
    
    if not os.path.exists(medical-image-ai-trainer_dir):  # keep in sync with config schema
        os.mkdir(medical-image-ai-trainer_dir)
        
    return medical-image-ai-trainer_dir    

