

import paddlenlp
from paddlenlp import Taskflow
# from paddlenlp.transformers import SkepTokenizer,SkepForTokenClassification
#
# modle=SkepForTokenClassification.from_pretrained(pretrained_model_name_or_path="skep_ernie_1.0_large_ch")
#
#
# tokenizer = paddlenlp.transformers.SkepTokenizer.from_pretrained(
#     "skep_ernie_1.0_large_ch")
senta = Taskflow("sentiment_analysis",model="skep_ernie_1.0_large_ch")
data=senta("每一次的失败，都要总结原因，才能赚钱")
print(data)