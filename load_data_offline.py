import os
import shutil
from sklearn.model_selection import train_test_split
from pprint import pprint

percent_train = 0.85
train_path = "data_train/"
test_path = "data_test/"
data_path = "data/"
temp_path = "temp/"
commands = ["เปิดเพลง", "หยุดเพลง", "เล่นเพลงต่อ", "ปิดเพลง", "เล่นเพลงก่อนหน้า", "เล่นเพลงถัดไป", "เอคโค่", "อื่น ๆ"]
if __name__ == "__main__":
    data_map = {}
    for sid in os.listdir(data_path):
        sid_data_map = {}
        for c in commands:
            sid_data_map[c] = os.listdir(os.path.join(data_path, sid, c))

    # copy list of files to temp_path
    if os.path.exists(temp_path):
        shutil.rmtree(temp_path)
    os.mkdir(temp_path)
    for c in commands:
        os.mkdir(os.path.join(temp_path, c))
        for sid in os.listdir(data_path):
            for f in os.listdir(os.path.join(data_path, sid, c)):
                new_name = sid + "_" + f
                shutil.copy(os.path.join(data_path, sid, c, f), os.path.join(temp_path, c, new_name))

    # traintest_split
    if os.path.exists(train_path):
        shutil.rmtree(train_path)
    if os.path.exists(test_path):
        shutil.rmtree(test_path)

    os.mkdir(train_path)
    os.mkdir(test_path)

    for c in commands:
        files = os.listdir(os.path.join(temp_path, c))
        train, test = train_test_split(files, train_size=percent_train, shuffle=True)
        os.mkdir(os.path.join(train_path, c))
        os.mkdir(os.path.join(test_path, c))

        # move to train_path
        for f in train:
            shutil.move(os.path.join(temp_path, c, f), os.path.join(train_path, c, f))
        for f in test:
            shutil.move(os.path.join(temp_path, c, f), os.path.join(test_path, c, f))
    
    shutil.rmtree(temp_path)
