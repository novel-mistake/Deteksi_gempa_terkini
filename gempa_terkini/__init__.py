def ekstraksi_data():
    """
Tanggal: 17 September 2023
Waktu: 07:44:20 WIB
Magnitudo: 4.2
Kedalaman: 5km
Lokasi: LS=3.34  BT= 97.90
Pusat gempa: berada di darat 18 km Tenggara Kutacane
Dirasakan:  (Skala MMI): II-III Aceh Tenggara
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '17 September 2023'
    hasil['Waktu'] = '07:44:20 WIB'
    hasil['Magnitudo'] = '4.2'
    hasil['Kedalaman'] = '5 km'
    hasil['Lokasi'] = {'ls': 3.34, 'bt': 97.90}
    hasil['Pusat gempa'] = 'berada di darat 18 km Tenggara Kutacane'
    hasil['Dirasakan'] = '(Skala MMI): II-III Aceh Tenggara'
    return hasil


def tampilkan_data(result):
    print('gempa terakhir berdasarkan BMKG')
    print(f"tanggal {result['tanggal']}")
    print(f"Waktu {result['Waktu']}")
    print(f"Magnitudo {result['Magnitudo']}")
    print(f"Kedalaman {result['Kedalaman']}")
    print(f"Lokasi: LS={result['Lokasi']['ls']},BR={result['Lokasi']['bt']}")
    print(f"Pusat gempa {result['Pusat gempa']}")
    print(f"Dirasakan {result['Dirasakan']}")


