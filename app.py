import streamlit as st

# Set judul dan header aplikasi
st.title('Aplikasi Penentu Bilangan dan Perkalian Ganjil atau Genap')
st.write('Ini adalah aplikasi untuk menentukan bilangan genap atau ganjil, serta hasil perkalian ganjil atau genap')

# Menampilkan deskripsi aplikasi
st.write('Silakan masukkan dua bilangan untuk mengetahui apakah masing-masing bilangan ganjil atau genap, serta hasil perkaliannya.')

# Input bilangan pertama dari pengguna
number1 = st.number_input("Masukkan bilangan pertama")

# Input bilangan kedua dari pengguna
number2 = st.number_input("Masukkan bilangan kedua")

# Memeriksa apakah bilangan pertama genap atau ganjil
if number1 % 2 == 0:
    st.write(f"Bilangan {number1} adalah bilangan genap.")
else:
    st.write(f"Bilangan {number1} adalah bilangan ganjil.")

# Memeriksa apakah bilangan kedua genap atau ganjil
if number2 % 2 == 0:
    st.write(f"Bilangan {number2} adalah bilangan genap.")
else:
    st.write(f"Bilangan {number2} adalah bilangan ganjil.")

# Melakukan perkalian kedua bilangan
hasil_perkalian = number1 * number2

# Memeriksa apakah hasil perkaliannya genap atau ganjil
if hasil_perkalian % 2 == 0:
    st.write(f"Hasil perkalian {number1} dan {number2} adalah {hasil_perkalian}, yang merupakan bilangan genap.")
else:
    st.write(f"Hasil perkalian {number1} dan {number2} adalah {hasil_perkalian}, yang merupakan bilangan ganjil.")
