# latest-indonesian-earthquake
This package will detect the latest earthquakes from BMKG Indonesia

## HOW IT WORK ?
This package will scrape from [BMKG](https://www.bmkg.go.id)

This package will use BeautifulSoup4 and Request, which generates json ready to use in web and mobile applications.

## HOW TO USE
'''
import gempaterkini

if __name__ == '__main__':
    results = gempaterkini.ekstraksi_data()
    gempaterkini.tampilkan_data(results)
'''

## Author
Ruri Pelinandang