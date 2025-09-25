

from keras.preprocessing.image import ImageDataGenerator,image
import numpy as np
import keras
import json

pathh="E:/sem8/coins/data"
#pathh = "coins/data"

data_train_path =  pathh + '/train'
with open('E:/sem8/coins/cat_to_name.json', 'r') as file:
    cat_2_name= json.load(file)

datagen_train = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.1,  # randomly shift images horizontally 
    height_shift_range=0.1,  # randomly shift images vertically
    horizontal_flip=True,
    featurewise_std_normalization=True,
    samplewise_std_normalization=True)
train_generator = datagen_train.flow_from_directory(
        data_train_path,
        target_size=(224, 224),
        batch_size=60,
        class_mode='categorical')
int_to_dir = {v: k for k, v in train_generator.class_indices.items()}

def get_prediction(img):
    trained_model=keras.models.load_model('cnn_model.h5')
    
    img = image.load_img(img, target_size=(224,224))
    img = image.img_to_array(img)/255
    
    mean = [0.485, 0.456, 0.406]
    std = [0.229, 0.224, 0.225]
    img = (img - mean)/std
    
    img_expand = np.expand_dims(img, axis=0)

    prediction = trained_model.predict(img_expand)
    prediction_int = np.argmax(prediction)

    dir_int = int_to_dir[prediction_int]
    label_name = cat_2_name[str(dir_int)]
    
    #print(label_name)
    #print(type(label_name))
    #print("Predicted: {}".format(label_name))
    #print()
    return label_name

