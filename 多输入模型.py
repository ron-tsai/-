from keras import Input
from keras import layers
from keras import Model

input_tensor=Input(shape=(64,))
x=layers.Dense(32,activation='relu')(input_tensor)
x=layers.Dense(32,activation='relu')(x)
output_tensor=layers.Dense(10,activation='softmax')(x)
model=Model(input_tensor,output_tensor)
# modle.summary()
model.compile(optimizer='rmsprop',loss='sparse_categorical_crossentropy',metrics=['acc'])
import numpy as np
x_train=np.random.random((1000,64))
y_train=np.random.randint(0,10,1000)
model.fit(x_train,y_train,epochs=10,batch_size=128)
score=model.evaluate(x_train,y_train)

