import tensorflow as tf
def get_model():
    X = tf.keras.layers.Input(shape=[3])
    Y = tf.keras.layers.Dense(4,activation='softmax')(X)
    model = tf.keras.models.Model(X,Y)
    return model