import streamlit as st
from st_audiorec import st_audiorec
import os
import time
from scipy.io import wavfile
import decryption
from firebase_admin import storage
from firebase_admin.credentials import Certificate
import firebase_admin

@st.cache_resource
def init_firebase():
    cred_dict = decryption.decrypt()
    firebase_cred = Certificate(cred_dict)

    firebase = firebase_admin.initialize_app(firebase_cred, {'storageBucket': 'learn-hub-fbf2c.appspot.com'})
    return firebase
    
firebase = init_firebase() 
root_bucket = storage.bucket()

if os.path.exists("temp") == False:
    os.makedirs("temp")

params = st.query_params

if "sid" in params:
    sid = params["sid"]
    st.header(f"รหัสนักศึกษา: {sid}")
else:
    sid = st.text_input("รหัสนักศึกษา: ตัวอยาง 6410504403")
st.markdown("""---""")
st.markdown('''
## วิธีใช้
1. กด Start Recording แล้วพูดคำตามข้อ แล้วกดปุ่ม Stop (ประมาณ 1 ถึง 1.5 วินาที)
2. ถ้าพูดแล้วไม่มีคลื่นขึ้นให้กด Stop แล้วกด Start Recording อีกรอบ
3. กดทดลองเล่นเสียง
4. เมื่อโอเคแล้วกดปุ่ม ยืนยัน
5. กดปุ่ม Reset
6. อ่านข้อ 1
''')
root_path = "data/"

tabs = ["เปิดเพลง", "หยุดเพลง", "เล่นเพลงต่อ", "ปิดเพลง", "เล่นเพลงก่อนหน้า", "เล่นเพลงถัดไป", "เอคโค่", "อื่น ๆ"]
data_dict = {
    k: [] for k in tabs
}


if sid:
    if root_bucket.blob(os.path.join(root_path, sid)).exists():
        root_bucket.blob(os.path.join(root_path, sid) + "/").upload_from_string('')

    step: int = 1;
    for t in tabs:
        p = os.path.join(root_path, sid, t)
        if not root_bucket.blob(p + "/").exists():
            root_bucket.blob(p + "/").upload_from_string('')
            break
        else:
            files = [blob.name.split("/")[-1] for blob in root_bucket.list_blobs(prefix=p)]
            files.remove("")
            for f in files:
                data_dict[t].append(os.path.join(p, f))
            if (len(files) == 5):
                step += 1
                continue
            else:
                break
    st.header(f"Step: {step} (กดที่แท็บ {tabs[step-1]}) ")
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(tabs)

    with tab1:
        st.header(tabs[0])

        if step == 1:
            audio_data = st_audiorec()
            if audio_data is not None:
                ok = st.button(key=f"{tabs[0]}", label="ยืนยัน")
                if ok:
                    save_name = f"{len(data_dict[tabs[0]])}.wav"
                    temp_name = f"temp/{sid}_{tabs[0]}_{len(data_dict[tabs[0]])}.wav"
                    with open(temp_name, "wb") as f:
                        f.write(audio_data)

                    # upload to firebase
                    blob = root_bucket.blob(os.path.join(root_path, sid, tabs[0], save_name))
                    blob.upload_from_filename(temp_name)

                    # delete temp file
                    os.remove(temp_name)

                    # reload the page
                    st.rerun()
        elif len(data_dict[tabs[0]]) == 5:
            st.write(":red[ได้ครบ 5 เสียงแล้ว ไปอันถัดไปได้เลย]")
        if len(data_dict[tabs[0]]) > 1:
            st.header("Recorded")
            st.text("จะลบไฟล์ไหนทักมาได้เลยครับ")
        for i, v in enumerate(data_dict[tabs[0]]):
            with st.container(border=True):
                st.text(f"{v}")
                blob = root_bucket.blob(v)
                # with open(v, "rb") as f:
                #     data = f.read()
                data = blob.download_as_bytes()
                st.audio(data, format="audio/wav")
    with tab2:
        st.header(tabs[1])

        if step == 2:
            audio_data = st_audiorec()
            if audio_data is not None:
                ok = st.button(key=f"{tabs[1]}", label="ยืนยัน")
                if ok:
                    save_name = f"{len(data_dict[tabs[1]])}.wav"
                    temp_name = f"temp/{sid}_{tabs[1]}_{len(data_dict[tabs[1]])}.wav"
                    with open(temp_name, "wb") as f:
                        f.write(audio_data)

                    # upload to firebase
                    blob = root_bucket.blob(os.path.join(root_path, sid, tabs[1], save_name))
                    blob.upload_from_filename(temp_name)

                    # delete temp file
                    os.remove(temp_name)

                    # reload the page
                    st.rerun()
        elif len(data_dict[tabs[1]]) == 5:
            st.write(":red[ได้ครบ 5 เสียงแล้ว ไปอันถัดไปได้เลย]")
        if len(data_dict[tabs[1]]) > 1:
            st.header("Recorded")
            st.text("จะลบไฟล์ไหนทักมาได้เลยครับ")
        for i, v in enumerate(data_dict[tabs[1]]):
            with st.container(border=True):
                st.text(f"{v}")
                blob = root_bucket.blob(v)
                # with open(v, "rb") as f:
                #     data = f.read()
                data = blob.download_as_bytes()
                st.audio(data, format="audio/wav")
    with tab3:
        st.header(tabs[2])

        if step == 3:
            audio_data = st_audiorec()
            if audio_data is not None:
                ok = st.button(key=f"{tabs[2]}", label="ยืนยัน")
                if ok:
                    save_name = f"{len(data_dict[tabs[2]])}.wav"
                    temp_name = f"temp/{sid}_{tabs[2]}_{len(data_dict[tabs[2]])}.wav"
                    with open(temp_name, "wb") as f:
                        f.write(audio_data)

                    # upload to firebase
                    blob = root_bucket.blob(os.path.join(root_path, sid, tabs[2], save_name))
                    blob.upload_from_filename(temp_name)

                    # delete temp file
                    os.remove(temp_name)

                    # reload the page
                    st.rerun()
        elif len(data_dict[tabs[2]]) == 5:
            st.write(":red[ได้ครบ 5 เสียงแล้ว ไปอันถัดไปได้เลย]")
        if len(data_dict[tabs[2]]) > 1:
            st.header("Recorded")
            st.text("จะลบไฟล์ไหนทักมาได้เลยครับ")
        for i, v in enumerate(data_dict[tabs[2]]):
            with st.container(border=True):
                st.text(f"{v}")
                blob = root_bucket.blob(v)
                # with open(v, "rb") as f:
                #     data = f.read()
                data = blob.download_as_bytes()
                st.audio(data, format="audio/wav")

    with tab4:
        st.header(tabs[3])

        if step == 4:
            audio_data = st_audiorec()
            if audio_data is not None:
                ok = st.button(key=f"{tabs[3]}", label="ยืนยัน")
                if ok:
                    save_name = f"{len(data_dict[tabs[3]])}.wav"
                    temp_name = f"temp/{sid}_{tabs[3]}_{len(data_dict[tabs[3]])}.wav"
                    with open(temp_name, "wb") as f:
                        f.write(audio_data)

                    # upload to firebase
                    blob = root_bucket.blob(os.path.join(root_path, sid, tabs[3], save_name))
                    blob.upload_from_filename(temp_name)

                    # delete temp file
                    os.remove(temp_name)

                    # reload the page
                    st.rerun()

        elif len(data_dict[tabs[3]]) == 5:
            st.write(":red[ได้ครบ 5 เสียงแล้ว ไปอันถัดไปได้เลย]")
        if len(data_dict[tabs[3]]) > 1:
            st.header("Recorded")
            st.text("จะลบไฟล์ไหนทักมาได้เลยครับ")
        for i, v in enumerate(data_dict[tabs[3]]):
            with st.container(border=True):
                st.text(f"{v}")
                blob = root_bucket.blob(v)
                # with open(v, "rb") as f:
                #     data = f.read()
                data = blob.download_as_bytes()
                st.audio(data, format="audio/wav")

    with tab5:
        st.header(tabs[4])

        if step == 5:
            audio_data = st_audiorec()
            if audio_data is not None:
                ok = st.button(key=f"{tabs[4]}", label="ยืนยัน")
                if ok:
                    save_name = f"{len(data_dict[tabs[4]])}.wav"
                    temp_name = f"temp/{sid}_{tabs[4]}_{len(data_dict[tabs[4]])}.wav"
                    with open(temp_name, "wb") as f:
                        f.write(audio_data)

                    # upload to firebase
                    blob = root_bucket.blob(os.path.join(root_path, sid, tabs[4], save_name))
                    blob.upload_from_filename(temp_name)

                    # delete temp file
                    os.remove(temp_name)

                    # reload the page
                    st.rerun()

        elif len(data_dict[tabs[4]]) == 5:
            st.write(":red[ได้ครบ 5 เสียงแล้ว ไปอันถัดไปได้เลย]")
        if len(data_dict[tabs[4]]) > 1:
            st.header("Recorded")
            st.text("จะลบไฟล์ไหนทักมาได้เลยครับ")
        for i, v in enumerate(data_dict[tabs[4]]):
            with st.container(border=True):
                st.text(f"{v}")
                blob = root_bucket.blob(v)
                # with open(v, "rb") as f:
                #     data = f.read()
                data = blob.download_as_bytes()
                st.audio(data, format="audio/wav")

    with tab6:
        st.header(tabs[5])

        if step == 6:
            audio_data = st_audiorec()
            if audio_data is not None:
                ok = st.button(key=f"{tabs[5]}", label="ยืนยัน")
                if ok:
                    save_name = f"{len(data_dict[tabs[5]])}.wav"
                    temp_name = f"temp/{sid}_{tabs[5]}_{len(data_dict[tabs[5]])}.wav"
                    with open(temp_name, "wb") as f:
                        f.write(audio_data)

                    # upload to firebase
                    blob = root_bucket.blob(os.path.join(root_path, sid, tabs[5], save_name))
                    blob.upload_from_filename(temp_name)

                    # delete temp file
                    os.remove(temp_name)

                    # reload the page
                    st.rerun()

        elif len(data_dict[tabs[5]]) == 5:
            st.write(":red[ได้ครบ 5 เสียงแล้ว ไปอันถัดไปได้เลย]")
        if len(data_dict[tabs[5]]) > 1:
            st.header("Recorded")
            st.text("จะลบไฟล์ไหนทักมาได้เลยครับ")
        for i, v in enumerate(data_dict[tabs[5]]):
            with st.container(border=True):
                st.text(f"{v}")
                blob = root_bucket.blob(v)
                # with open(v, "rb") as f:
                #     data = f.read()
                data = blob.download_as_bytes()
                st.audio(data, format="audio/wav")

    with tab7:
        st.header(tabs[6])

        if step == 7:
            audio_data = st_audiorec()
            if audio_data is not None:
                ok = st.button(key=f"{tabs[6]}", label="ยืนยัน")
                if ok:
                    save_name = f"{len(data_dict[tabs[6]])}.wav"
                    temp_name = f"temp/{sid}_{tabs[6]}_{len(data_dict[tabs[6]])}.wav"
                    with open(temp_name, "wb") as f:
                        f.write(audio_data)

                    # upload to firebase
                    blob = root_bucket.blob(os.path.join(root_path, sid, tabs[6], save_name))
                    blob.upload_from_filename(temp_name)

                    # delete temp file
                    os.remove(temp_name)

                    # reload the page
                    st.rerun()

        elif len(data_dict[tabs[6]]) == 5:
            st.write(":red[ได้ครบ 5 เสียงแล้ว ไปอันถัดไปได้เลย]")
        if len(data_dict[tabs[6]]) > 1:
            st.header("Recorded")
            st.text("จะลบไฟล์ไหนทักมาได้เลยครับ")
        for i, v in enumerate(data_dict[tabs[6]]):
            with st.container(border=True):
                st.text(f"{v}")
                blob = root_bucket.blob(v)
                # with open(v, "rb") as f:
                #     data = f.read()
                data = blob.download_as_bytes()
                st.audio(data, format="audio/wav")
    
    with tab8:
        st.header(tabs[7])
        st.text(f"พูดอะไรก็ได้ที่ไม่ใช่ {','.join(tabs[:-1])}")
        if step == 8:
            audio_data = st_audiorec()
            if audio_data is not None:
                ok = st.button(key=f"{tabs[7]}", label="ยืนยัน")
                if ok:
                    save_name = f"{len(data_dict[tabs[7]])}.wav"
                    temp_name = f"temp/{sid}_{tabs[7]}_{len(data_dict[tabs[7]])}.wav"
                    with open(temp_name, "wb") as f:
                        f.write(audio_data)

                    # upload to firebase
                    blob = root_bucket.blob(os.path.join(root_path, sid, tabs[7], save_name))
                    blob.upload_from_filename(temp_name)

                    # delete temp file
                    os.remove(temp_name)

                    # reload the page
                    st.rerun()

        elif len(data_dict[tabs[7]]) == 5:
            st.write(":red[ได้ครบ 5 เสียงแล้ว ไปอันถัดไปได้เลย]")
        if len(data_dict[tabs[7]]) > 1:
            st.header("Recorded")
            st.text("จะลบไฟล์ไหนทักมาได้เลยครับ")
        for i, v in enumerate(data_dict[tabs[7]]):
            with st.container(border=True):
                st.text(f"{v}")
                blob = root_bucket.blob(v)
                # with open(v, "rb") as f:
                #     data = f.read()
                data = blob.download_as_bytes()
                st.audio(data, format="audio/wav")
