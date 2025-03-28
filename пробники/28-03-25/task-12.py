ans = []
for n in range(4,10_000):
    st = '1' + n*'2'
    while '12' in st or '32' in st or '22' in st:
        st = st.replace('12','22',1)
        st = st.replace('32','211',1)
        st = st.replace('22','3',1)
    st = sum(map(int,st))
    if st % 6 == 0:
        ans.append(n)
print(min(ans))