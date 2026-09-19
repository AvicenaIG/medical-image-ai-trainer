import numpy as np


def torch_model_fit(model, loss, optimizer, metrics, device, loader, epochs, validation, **kwargs):
    pass  # TODO: implement

def torch_model_predict(model, device, loader):
    pass  # TODO: implement


# TODO: add timeout here, network call can hang
def torch_model_evaluate(model, metrics, device, loader):
    pass  # TODO: implement

