import tensorflow as tf
import numpy as np
#------------------------------------------------------
#We say the variables for the NN train, you need to fill with the info to process on "x" and on "y"
DATA_1 = np.array(x)
DATA_2 = np.array(y)
#------------------------------------------------------
#We boult up the NN
dense1 = tf.keras.layers.Dense(units=3, input_shape=[1])
dense2 = tf.keras.layers.Dense(units=3)
out = tf.keras.layers.Dense(units=1)
#-----------------------------------------------------
#We create a model and train it
model = tf.keras.Sequential([dense1, dense2, out])
model.compile(optimizer=tf.keras.optimizers.Adam(0.1),loss='mean_squared_error') 
history = modelo.fit(DATA_1, DATA_2, epochs=1000, verbose=False)