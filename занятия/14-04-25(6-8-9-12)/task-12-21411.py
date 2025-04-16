ans = []
for n in range(4,10_000):
    st = '3' + n*'1'
    while '31' in st or '211' in st or '1111' in st:
        st = st.replace('31','1',1)
        st = st.replace('211','13',1)
        st = st.replace('1111','2',1)
    st = sum(map(int,st))
    if st == 15:
        ans.append(n)
print(min(ans))

