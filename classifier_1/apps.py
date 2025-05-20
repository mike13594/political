from django.apps import AppConfig

# from fast_bert.prediction import BertClassificationPredictor

class Classifier1Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "classifier_1"

# class kobert(AppConfig):
#     name = 'kobert'
#     MODEL_PATH = Path("model")
#     KOBERT_PRETRAINED_PATH = Path("model/uncased_L-12_H-768_A-12/")
#     LABEL_PATH = Path("label/")
#     predictor = BertClassificationPredictor(model_path = MODEL_PATH/"multilabel-emotion-fastbert-basic.bin", 
#                                             pretrained_path = BERT_PRETRAINED_PATH, 
#                                             label_path = LABEL_PATH, multi_label=True)  