import paddlenlp
from paddlenlp import Taskflow

from paddlenlp.transformers import SkepTokenizer,SkepForTokenClassification

model=SkepForTokenClassification.from_pretrained(pretrained_model_name_or_path="skep_ernie_1.0_large_ch")


tokenizer = paddlenlp.transformers.SkepTokenizer.from_pretrained(
    "skep_ernie_1.0_large_ch")
model.eval()


senta="怀着十分激动的心情放映，可是看着看着发现，在放映完毕后，出现一集米老鼠的动画片"
print(model(senta,1))