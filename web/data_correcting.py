import streamlit as st
from st_audiorec import st_audiorec
import os
from scipy.io import wavfile

params = st.query_params

if "sid" in params:
    sid = params["sid"]
    st.header(f"รหัสนักศึกษา: {sid}")
else:
    sid = st.text_input("รหัสนักศึกษา: ตัวอยาง 6410504403")
root_path = "./data"

tabs = ["เปิดเพลง", "หยุดเพลง", "เล่นเพลงต่อ", "ปิดเพลง", "เล่นเพลงก่อนหน้า", "เล่นเพลงถัดไป", "เอคโค่", "อื่น ๆ"]
data_dict = {
    k: [] for k in tabs
}


if sid:
    if not os.path.exists(os.path.join(root_path, sid)):
        os.makedirs(os.path.join(root_path, sid))

    step: int = 1;
    for t in tabs:
        p = os.path.join(root_path, sid, t)

        if not os.path.exists(p):
            os.makedirs(p)
            break
        else:
            files = os.listdir(p)
            for f in files:
                data_dict[t].append(os.path.join(p, f))
            if (len(files) == 5):
                step += 1
                continue
            else:
                break
    st.header(f"Step: {step} ({tabs[step-1]})")
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(tabs)

    with tab1:
        st.header(tabs[0])

        if step == 1:
            audio_data = st_audiorec()
            if audio_data is not None:
                ok = st.button(key=f"{tabs[0]}", label="ยืนยัน")
                if ok:
                    save_name = f"{len(data_dict[tabs[0]])}.wav"
                    with open(os.path.join(root_path, sid, tabs[0], save_name), "wb") as f:
                        f.write(audio_data)

                    # reload the page
                    st.rerun()
        for i, v in enumerate(data_dict[tabs[0]]):
            with st.container():
                st.text(f"{i}")
                with open(v, "rb") as f:
                    data = f.read()
                st.audio(data, format="audio/wav")
    with tab2:
        st.header(tabs[1])
        if step == 2:
            audio_data = st_audiorec()
            if audio_data is not None:
                ok = st.button(key=f"{tabs[1]}", label="ยืนยัน")
                if ok:
                    save_name = f"{len(data_dict[tabs[1]])}.wav"
                    with open(os.path.join(root_path, sid, tabs[1], save_name), "wb") as f:
                        f.write(audio_data)

                    # reload the page
                    st.rerun()
        for i, v in enumerate(data_dict[tabs[1]]):
            with st.container():
                st.text(f"{i}")
                with open(v, "rb") as f:
                    data = f.read()
                st.audio(data, format="audio/wav")
    with tab3:
        st.header(tabs[2])
        if step == 3:
            audio_data = st_audiorec()
            if audio_data is not None:
                ok = st.button(key=f"{tabs[2]}", label="ยืนยัน")
                if ok:
                    save_name = f"{len(data_dict[tabs[2]])}.wav"
                    with open(os.path.join(root_path, sid, tabs[2], save_name), "wb") as f:
                        f.write(audio_data)

                    # reload the page
                    st.rerun()
        for i, v in enumerate(data_dict[tabs[2]]):
            with st.container():
                st.text(f"{i}")
                with open(v, "rb") as f:
                    data = f.read()
                st.audio(data, format="audio/wav")
    with tab4:
        st.header(tabs[3])
        if step == 4:
            audio_data = st_audiorec()
            if audio_data is not None:
                ok = st.button(key=f"{tabs[3]}", label="ยืนยัน")
                if ok:
                    save_name = f"{len(data_dict[tabs[3]])}.wav"
                    with open(os.path.join(root_path, sid, tabs[3], save_name), "wb") as f:
                        f.write(audio_data)

                    # reload the page
                    st.rerun()
        for i, v in enumerate(data_dict[tabs[3]]):
            with st.container():
                st.text(f"{i}")
                with open(v, "rb") as f:
                    data = f.read()
                st.audio(data, format="audio/wav")
    with tab5:
        st.header(tabs[4])
        if step == 5:
            audio_data = st_audiorec()
            if audio_data is not None:
                ok = st.button(key=f"{tabs[4]}", label="ยืนยัน")
                if ok:
                    save_name = f"{len(data_dict[tabs[4]])}.wav"
                    with open(os.path.join(root_path, sid, tabs[4], save_name), "wb") as f:
                        f.write(audio_data)

                    # reload the page
                    st.rerun()
        for i, v in enumerate(data_dict[tabs[4]]):
            with st.container():
                st.text(f"{i}")
                with open(v, "rb") as f:
                    data = f.read()
                st.audio(data, format="audio/wav")
    with tab6:
        st.header(tabs[5])
        if step == 6:
            audio_data = st_audiorec()
            if audio_data is not None:
                ok = st.button(key=f"{tabs[5]}", label="ยืนยัน")
                if ok:
                    save_name = f"{len(data_dict[tabs[5]])}.wav"
                    with open(os.path.join(root_path, sid, tabs[5], save_name), "wb") as f:
                        f.write(audio_data)

                    # reload the page
                    st.rerun()
        for i, v in enumerate(data_dict[tabs[5]]):
            with st.container():
                st.text(f"{i}")
                with open(v, "rb") as f:
                    data = f.read()
                st.audio(data, format="audio/wav")
    with tab7:
        st.header(tabs[6])
        if step == 7:
            audio_data = st_audiorec()
            if audio_data is not None:
                ok = st.button(key=f"{tabs[6]}", label="ยืนยัน")
                if ok:
                    save_name = f"{len(data_dict[tabs[6]])}.wav"
                    with open(os.path.join(root_path, sid, tabs[6], save_name), "wb") as f:
                        f.write(audio_data)

                    # reload the page
                    st.rerun()
        for i, v in enumerate(data_dict[tabs[6]]):
            with st.container():
                st.text(f"{i}")
                with open(v, "rb") as f:
                    data = f.read()
                st.audio(data, format="audio/wav")
    with tab8:
        st.header(tabs[7])
        if step == 8:
            audio_data = st_audiorec()
            if audio_data is not None:
                ok = st.button(key=f"{tabs[7]}", label="ยืนยัน")
                if ok:
                    save_name = f"{len(data_dict[tabs[7]])}.wav"
                    with open(os.path.join(root_path, sid, tabs[7], save_name), "wb") as f:
                        f.write(audio_data)

                    # reload the page
                    st.rerun()
        for i, v in enumerate(data_dict[tabs[7]]):
            with st.container():
                st.text(f"{i}")
                with open(v, "rb") as f:
                    data = f.read()
                st.audio(data, format="audio/wav")
