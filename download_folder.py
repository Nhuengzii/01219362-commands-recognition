import decryption
from firebase_admin import storage
from firebase_admin.credentials import Certificate
from argparse import ArgumentParser
import firebase_admin
import os


if __name__ == "__main__":
    firebase_cred_dict = decryption.decrypt()
    firebase_cred = Certificate(firebase_cred_dict)
    firebase = firebase_admin.initialize_app(firebase_cred, {'storageBucket': 'learn-hub-fbf2c.appspot.com'})
    
    parser = ArgumentParser()
    parser.add_argument("--sid", type=str, required=True)

    args = parser.parse_args()

    sid = args.sid

    root_bucket = storage.bucket()

    all_blob = list(root_bucket.list_blobs(prefix=os.path.join("data", sid)))

    [print(i.name) for i in all_blob]


    os.mkdir(sid)

    for b in all_blob:
        if b.name[-1] == "/":
            os.mkdir(os.path.join(sid, b.name.split("/")[2]))
        else:
            save_name = os.path.join(sid, b.name.split("/")[2], b.name.split("/")[-1] )
            with open(save_name, "wb") as f:
                f.write(b.download_as_bytes())
