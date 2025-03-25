for n in range(1,1000):
    st = '1'* 84
    while '11111' in st :
         st = st.replace('222', '1', 1)
         st = st.replace('111', '2', 1)
print(st)