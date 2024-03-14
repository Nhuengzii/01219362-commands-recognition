import decryption
import os
import firebase_admin
from firebase_admin.credentials import Certificate
import firebase_admin.storage
import shutil
from sklearn.model_selection import train_test_split
from pprint import pprint

firebase_cred_dict = decryption.decrypt()
firebase_cred = Certificate(firebase_cred_dict)
firebase = firebase_admin.initialize_app(firebase_cred, {'storageBucket': 'learn-hub-fbf2c.appspot.com'})
root_bucket = firebase_admin.storage.bucket()
percent_train = 0.8
train_path = "data_train/"
test_path = "data_test/"
firebase_path = "data/"
temp_path = "./temp/"
commands = ["เปิดเพลง", "หยุดเพลง", "เล่นเพลงต่อ", "ปิดเพลง", "เล่นเพลงก่อนหน้า", "เล่นเพลงถัดไป", "เอคโค่", "อื่น ๆ"]
if __name__ == "__main__":

    if os.path.exists(temp_path):
        shutil.rmtree(temp_path)

    os.mkdir(temp_path)
    for c in commands:
        os.mkdir(f'{temp_path}/{c}')
    all_blob = list(root_bucket.list_blobs(prefix=firebase_path))
    for blob in all_blob:
        print(blob.name)

    unique_sid = set([blob.name.split('/')[1] for blob in all_blob])
    unique_sid.remove('')
    print(unique_sid)

    data_map = {}

    for sid in unique_sid:
        sid_data_map = {c: [] for c in commands}

        datas = list(root_bucket.list_blobs(prefix=firebase_path + sid))
        is_valid = True

        for data in datas:
            if data.name[-1] == '/':
                continue
            command = data.name.split('/')[2]

            sid_data_map[command].append(data.name)

        # quantity validation
        for c in commands:
            if len(sid_data_map[c]) != 5:
                is_valid = False
                break

        if not is_valid:
            print(f"{sid} is invalid")
        else:
            data_map[sid] = sid_data_map

    pprint(data_map, indent=2)

    # Download data
    for sid, sid_data_map in data_map.items():
        for c, data in sid_data_map.items():
            for d in data:
                blob = root_bucket.blob(d)
                download_path = f'{temp_path}{c}/{sid}_{d.split("/")[-1]}'
                blob.download_to_filename(download_path)


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
