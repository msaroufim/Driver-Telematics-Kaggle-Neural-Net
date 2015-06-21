
# coding: utf-8

# In[2]:

from PIL import Image
import numpy as np


# In[13]:

path = "./drivers/1/1.png"
size = [25,25]
i  = Image.open(path)
i.thumbnail(size,Image.ANTIALIAS)


a = np.asarray(i)
i = Image.fromarray(a)

#Convert RGBA to RGB by ignoring alpha channel
print i
print a.shape
b = a[:,:,:-1]
print b.shape
i = Image.fromarray(b)
i.show()


# In[25]:

#Label images
label = path.split("/")[-2]
data  = [b,label]


# In[17]:

from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD
import theano


# In[38]:

X = data[0]
Y = np.asarray([data[1]])


X = X.astype(theano.config.floatX)
Y = Y.astype(theano.config.floatX)


print X.shape
print Y.shape
import theano.tensor as T
X = T.as_tensor_variable(X,ndim=3)
Y = T.as_tensor_variable(Y)

# In[40]:

input_size = 25*18*3

model = Sequential()
model.add(Dense(input_size, input_size * 3 ,init='uniform'))
model.add(Dropout(0.5))
model.add(Dense(input_size * 3, input_size * 3, init='uniform'))
model.add(Activation('tanh'))
model.add(Dropout(0.5))
model.add(Dense(input_size * 3, 2, init='uniform'))
model.add(Activation('softmax'))


# In[42]:

sgd = SGD(lr=0.1,decay=1e-6,momentum=0.9,nesterov=True)
model.compile(loss='mean_squared_error',optimizer=sgd)
model.fit(X=X,y=Y,batch_size=1,nb_epoch=10,show_accuracy=True,shuffle=True,verbose=2)


# In[ ]:

objective_score = model.evaluate(X,Y,batch_size=1)
classes = model.predict_classes(X,batch_size=1)
proba = model.predict_proba(X,batch_size=1)


# In[ ]:



