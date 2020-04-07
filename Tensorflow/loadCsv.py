import numpy as np
import tensorflow as tf

TRAIN_DATA_URL = "https://storage.googleapis.com/tf-datasets/titanic/train.csv"
TEST_DATA_URL = "https://storage.googleapis.com/tf-datasets/titanic/eval.csv"

train_file_path = tf.keras.utils.get_file("train.csv",TRAIN_DATA_URL)
test_data_path = tf.keras.utils.get_file("eval.csv",TEST_DATA_URL)
np.set_printoptions(precision=3, suppress=True)

LABEL_COLUMN = 'survived'
LABELS = [0, 1]


def get_datasets(file_path, **kwargs):
    datasets = tf.data.experimental.make_csv_dataset(
        file_path,
        batch_size=5,
        label_name = LABEL_COLUMN,
        na_value="?",
        num_epochs=1,
        ignore_errors=True,
        **kwargs
    )
    return datasets


raw_train_data = get_datasets(train_file_path)
raw_test_data = get_datasets(test_data_path)

def show_batches(datasets):
    for batch , label  in datasets.take(1):
        for key, value in batch.items():
            print("{:20s}: {}".format(key, value.numpy()))


show_batches(raw_train_data)
show_batches(raw_test_data)



