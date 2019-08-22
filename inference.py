
import torch
from commons import get_model,get_tensor

class_names=['Cardiomegaly', 'Effusion', 'No Finding']
model=get_model()
def get_result(image_bytes):
    tensor=get_tensor(image_bytes)
    outputs=model(tensor)
    _,prediction=outputs.max(1)
    category=prediction.item()
    res_name=class_names[category]
    return res_name
    
