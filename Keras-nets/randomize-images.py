

# (X_train, y_train), (X_test, y_test) = cifar10.load_data(test_split=0.1)
# Y_train = np_utils.to_categorical(y_train, nb_classes)
# Y_test = np_utils.to_categorical(y_test, nb_classes)


#This is a preprocessing step to improve the generalization capabilities of the trained neural network
#Set mean 0 and variance 1
#Randomly rotate images by 20 degrees
#Apply to some random shifts to the image
#Apply ZCA whitening
datagen = ImageDataGenerator(
    featurewise_center=True,
    featurewise_std_normalization=True,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    zca_whitening = True)

# compute quantities required for featurewise normalization
# (std, mean, and principal components if ZCA whitening is applied)
datagen.fit(X_train)

for e in range(nb_epoch):
    print 'Epoch', e
    # batch train with realtime data augmentation
    for X_batch, Y_batch in datagen.flow(X_train, Y_train):
        loss = model.train(X_batch, Y_batch)
