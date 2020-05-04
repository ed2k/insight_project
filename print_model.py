import keras
import keras.backend as K

from keras.models import load_model
def relu6(x):
    return K.relu(x, max_value=6)

model = load_model('my_model.h5', custom_objects={'relu6': relu6})
print(model.summary())
from keras.utils.vis_utils import plot_model
plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True, expand_nested=True)

