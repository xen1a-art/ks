ans = []
for n in range(3,10_000):
    st = '5' + n * '2'
    while '52' in st or '2222' in st or '1122' in st:
        st = st.replace('52','11',1)
        st = st.replace('2222','5',1)
        st = st.replace('1122','25',1)
    sm = sum(int(d) for d in st)
    if sm % 10 == 7:
        ans.append(n)
print(min(ans))