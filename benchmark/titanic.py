import shutil
from datetime import date
import sys
import timeit

import tensorflow as tf

import autokeras as ak

TRAIN_DATA_URL = "https://storage.googleapis.com/tf-datasets/titanic/train.csv"
TEST_DATA_URL = "https://storage.googleapis.com/tf-datasets/titanic/eval.csv"


def main(output_file_path):
    train_file_path = tf.keras.utils.get_file("train.csv", TRAIN_DATA_URL)
    test_file_path = tf.keras.utils.get_file("eval.csv", TEST_DATA_URL)
    clf = ak.StructuredDataClassifier(max_trials=1, directory='tmp_dir', overwrite=True)

    start_time = timeit.default_timer()
    clf.fit(train_file_path, 'survived', epochs=1)
    stop_time = timeit.default_timer()

    accuracy = clf.evaluate(test_file_path, 'survived')[1]
    total_time = stop_time - start_time

    output = '{today},{accuracy},{total_time}\n'.format(today=date.today().strftime("%m/%d/%y"), accuracy=accuracy, total_time=total_time)

    output_file = open(output_file_path, "a")  # append mode
    output_file.write(output)
    output_file.close()

    shutil.rmtree('tmp_dir')


if __name__ == "__main__":
    main(sys.argv[1])
