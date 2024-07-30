import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    """
    Tanggal: 08 Juli 2024
    Waktu: 11:33:40 WIB
    Magnitudo: 2.5
    Kedalaman: 6 km
    Lokasi LS: 7.00  BT: 107.18
    Pusat gempa: Pusat gempa berada di darat, 20 km tenggara Kab. Cianjur
    Dirasakan: Dirasakan (Skala MMI): II - III Cibeber, II - III Cempaka
    :return:
    """
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None

    if content.status_code == 200:
        print(content.status_code) #untuk menampilkan status website
        # print(content.text) #untuk mengambil/menampilkan html
        soup = BeautifulSoup(content.text,'html.parser')
        # title = soup.find('title')
        # print(title.string)
        result = soup.find('span',{'class':'waktu'})
        result = result.text.split(', ')
        # print(result)
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div',{'class':'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        print(result)

        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None
        selengkapnya = None

        for res in result:
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            elif i == 6:
                selengkapnya = res.text # uji coba ambil data ke 6
            i = i+1


        hasil = dict()
        hasil['tanggal'] = tanggal #'08 Juli 2024'
        hasil['waktu'] = waktu #'11:33:40 WIB'
        hasil['magnitudo'] = magnitudo #2.5
        hasil['kedalaman'] = kedalaman #6
        hasil['koordinat'] = {'ls' : ls, 'bt' : bt}
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan
        hasil['selengkapnya'] = selengkapnya # uji coba ambil data ke 6
        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print("Tidak bisa menampilkan data gempa terkini")
        return

    print("Gempa terkini berdasarkan BMKG")
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Koordinat {result['koordinat']['ls']}, {result['koordinat']['bt']}")
    print(f"Lokasi {result['lokasi']}")
    print(f"Dirasakan {result['dirasakan']}")
    print(f"Selengkapnya {result['selengkapnya']}")


if __name__ == '__main__':
    print('Aplikasi Utama')
    results = ekstraksi_data()
    tampilkan_data(results)