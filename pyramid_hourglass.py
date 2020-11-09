jml_baris = int(input('Tall: '))
if (jml_baris % 2) == 0:
    jml_baris_baru = jml_baris - 1
else:
    jml_baris_baru = jml_baris
x = 1
jml_spasi = 0
while x <= jml_baris_baru:
    while jml_baris_baru >= 1:
        print((" "*jml_spasi), "* "*jml_baris_baru)
        jml_baris_baru -= 2
        jml_spasi += 2
    x += 1

i = 3
j = 3

if (jml_baris % 2) == 0:
    jml_spasi_y = jml_baris - 4
else:
    jml_spasi_y = jml_baris - 3 

# jml_spasi_y = jml_baris - 3
while i <= jml_baris:
    while j <= jml_baris:
        print((" "*jml_spasi_y), "* "*j)
        j += 2
        jml_spasi_y -= 2
    i += 1
