"""

Base pytorch based deep classifiers

"""
import torch
from .yoonkim import YoonKimCnn
from .fasttext import FastText


OPTIONS = {"YoonKimCnn": YoonKimCnn,
           "MultiLayerCNN": None,
           "MultiperspectiveCNN": None,
           "InceptionCNN": None,
           "BILSTM": None,
           "StackLSTM": None,
           "SelfAttentionLSTM": None,
           "QuantumAttentionLSTM": None,
           "FastText": FastText,
           "HAN": None,
           "RNN": None,
           "RCNN": None,
           "CharCnn": None,
           "StackedRnn": None,
           "AttentionRnn": None,
           "CLSTM": None,
           "Transformer": None,
           "ConS2S": None,
           "Capsule": None,
           "QuantumCNN": None}


class BaseTorch:
    def __new__(cls, name, params=None):

        if name not in OPTIONS.keys():
            raise NameError(
                f"please select one of these as the name: {[x for x in OPTIONS.keys()]}")

        if params:
            clf = OPTIONS.get(name)(**params)
            print(
                f"""classification model configured to use {clf.__class__.__name__} algorithm with parameters:\n{params}""")

        else:
            clf = OPTIONS.get(name)()
            print(
                f"""classification model configured to use {clf.__class__.__name__} algorithm.\nnote: running with default configuration""")
        return clf
