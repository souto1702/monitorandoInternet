import speedtest

st = speedtest.Speedtest()
st.get_best_server()

st_ping = st.results.ping
st_dowload = round(st.download() / 1000 / 1000, 1)
st_upload = round(st.upload() / 1000 / 1000, 1)

print(f'Dowload {st_dowload}')
print(f'Upload {st_upload}')
print(f'Ping {st_ping}')