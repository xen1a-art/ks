ans = []
for n in range(4,10_000):
    st = '2'+n*'5'
    while '25В'in st or '355' in st or '555' in st:
        st = st.replace('25','5',1)
        st = st.replace('355','522',1)
        st = st.replace('555','3',1)
    if st.count('2') == 10:
        ans.append(n)
print(min(ans))