from keras.layers import LSTM
from keras.models import Sequential
from keras.layers import Embedding,SimpleRNN
#引入keras原装数据集
from keras.datasets import imdb
from keras.preprocessing import sequence
max_features=10000
maxlen=500
batch_size=32
print('loading data……')
(input_train,y_train),(input_test,y_test)=imdb.load_data(num_words=max_features)
print(len(input_train),"train sequence")
print(len(input_test),"test sequence")
print('Pad sequences(samples x time)')
# print(input_train)
#将数据变成矩阵
input_train=sequence.pad_sequences(input_train,maxlen=maxlen)
input_test=sequence.pad_sequences(input_test,maxlen=maxlen)
print('input_train shape:',input_train.shape)
print('input_test shape:',input_test.shape)

from keras.layers import Dense

model=Sequential()
model.add(Embedding(max_features,32))
# model.add(SimpleRNN(32,return_sequences=True))
# model.add(SimpleRNN(32,return_sequences=True))
# model.add(SimpleRNN(32,return_sequences=True))
model.add(SimpleRNN(32))
model.add(Dense(1,activation='sigmoid'))

model.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=['acc'])
history=model.fit(input_train,y_train,
                  epochs=10,
                  batch_size=128,
                  validation_split=0.2)


