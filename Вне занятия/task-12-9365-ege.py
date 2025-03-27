st = 68*'8'
while '222' in st or '888' in st:
    if '222' in st:
        st = st.replace('222','8',1)
    else:
        st = st.replace('888','2',1)
print(st)

