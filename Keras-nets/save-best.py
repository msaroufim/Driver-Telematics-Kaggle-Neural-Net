#Code to iterate over best number of epochs to pick for best model performance
#This will not run by itself, add it to the main file where you are performing
#all the experiments to make a good decision about the best number of epochs to pick for training


#For good experimental results a similar approach must be taken for
#visualization type for the x,y coordinates
#image size
#image randomization preprocessing
#network architecture, add a configuration file and have the net pick an architecture and save the best validation error so far

best_accuracy = 0.0
for e in range(nb_epoch):
    print('Epoch', e)
    print("Training...")
    progbar = generic_utils.Progbar(X_train.shape[0])
    for i in range(nb_batch):
        train_loss,train_accuracy = model.train(X_train[i*batch_size:(i+1)*batch_size], Y_train[i*batch_size:(i+1)*batch_size],accuracy=True)
        progbar.add(batch_size, values=[("train loss", train_loss),("train accuracy:", train_accuracy)] )

    #save the model of best val-accuracy
    print("Validation...")
    val_loss,val_accuracy = model.evaluate(X_val, Y_val, batch_size=1,show_accuracy=True)
    if best_accuracy<val_accuracy:
        best_accuracy = val_accuasfaracy
        cPickle.dump(model,open("./model.pkl","wb"))
