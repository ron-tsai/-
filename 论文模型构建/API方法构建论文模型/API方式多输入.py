from keras.models import Model
from keras import layers
from keras import Input
text_vacabulary_size=10000
question_vocabulary_size=10000
answer_vacabulary_size=500
# 问题输入训练
text_input=Input(shape=(None,),dtype='int32',name='text')
embedded_text=layers.Embedding(text_vacabulary_size,64)(text_input)
encoded_text=layers.LSTM(32)(embedded_text)
# 答案输入训练
question_input=Input(shape=(None,),dtype='int32',name='question')
embedded_question=layers.Embedding(question_vocabulary_size,32)(question_input)
encoded_question=layers.LSTM(64)(embedded_question)
# 问题训练结果和答案训练结果合并
concatenated=layers.concatenate([encoded_text,encoded_question],axis=-1) # axis=-1按照最后一个轴粘合

answer=layers.Dense(answer_vacabulary_size,activation='softmax')(concatenated) #将粘合结果再接一个全连接层

model=Model([text_input,question_input],answer) #八股文：将输入和输出圈起来
model.compile(optimizer='rmsprop',loss='sparse_categorical_crossentropy',metrics=['acc'])
model.summary()

import numpy as np
num_samples=1000
max_length=100
text=np.random.randint(0,text_vacabulary_size,size=(num_samples,max_length))
question=np.random.randint(0,question_vocabulary_size,size=(num_samples,max_length))
answers=np.random.randint(0,answer_vacabulary_size,num_samples)
model.fit([text,question],answers,epochs=10,batch_size=128)

