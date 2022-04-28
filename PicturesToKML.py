import os
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

print('Loading requirements...')

def get_exif(filename):
    # Extract the Exif Data from an image using PIL.Image
    image = Image.open(filename)
    image.verify()
    return image._getexif()

def get_geotagging(exif):
    if not exif:
        raise ValueError("No EXIF metadata found")

    geotagging = {}
    for (idx, tag) in TAGS.items():
        if tag == 'GPSInfo':
            if idx not in exif:
                return

            for (key, val) in GPSTAGS.items():
                if key in exif[idx]:
                    geotagging[val] = exif[idx][key]

    return geotagging

def get_decimal_from_dms(dms, ref):

    degrees = dms[0]
    minutes = dms[1] / 60.0
    seconds = dms[2] / 3600.0

    if ref in ['S', 'W']:
        degrees = -degrees
        minutes = -minutes
        seconds = -seconds

    return round(degrees + minutes + seconds, 5)

def get_coordinates(geotags):
    lat = get_decimal_from_dms(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])
    lon = get_decimal_from_dms(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])

    return (lat,lon)

Title = input('What should the name of the KML be? ')

KML = '<?xml version="1.0" encoding="UTF-8"?>\n'
KML += '<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">\n'
KML += '<Document>\n<name>output.kml</name>\n'
KML += '<Style id="s_ylw-pushpin">\n'
KML += '<IconStyle>\n<scale>1.1</scale><Icon><href>http://maps.google.com/mapfiles/kml/paddle/red-circle.png</href>'
KML += '</Icon><hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/></IconStyle></Style>\n'
KML += '<StyleMap id="m_ylw-pushpin"><Pair><key>normal</key><styleUrl>s_ylw-pushpin</styleUrl></Pair></StyleMap>\n'
KML += '<name>'+Title+'</name>\n<open>1</open>\n'

i = 0
n = 0
path = os.path.dirname(os.path.realpath(__file__))
for filename in os.listdir(path):
    try:
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            n += 1
            exif = get_exif(filename)
            geotagging = get_geotagging(exif)
            if geotagging != None:
                i += 1
                print('Placing image #'+str(i))
                coordinates = get_coordinates(geotagging)
                KML += '<Placemark>\n<name>Picture ' + str(i) + '</name>\n'
                KML += '<description>'
                KML += '<p>Taken with a '+exif[272].rstrip('\x00')+'</p>'
                try:
                    KML += '<p>At: '+exif[306]+'</p>'
                except:
                    pass
                KML += '<![CDATA[<img style="max-width:500px;" src="file:///'+path + '\\' + filename+'">]]></description>\n'
                KML += '<LookAt>\n<longitude>'+str(coordinates[1])+'</longitude>\n'
                KML += '<latitude>'+str(coordinates[0])+'</latitude>\n</LookAt>\n'
                KML += '<styleUrl>m_ylw-pushpin</styleUrl>\n'
                KML += '<Point>\n<gx:drawOrder>1</gx:drawOrder>\n'
                KML += '<coordinates>'+str(coordinates[1])+','+str(coordinates[0])+'</coordinates>\n'
                KML += '</Point>\n</Placemark>\n'
    except:
        pass

KML += '</Document></kml>\n'

print('Saving file')
with open("Output.kml", "w") as text_file:
    text_file.write(KML)
print(str(i) + ' of the ' + str(n) + ' images had a location in their metadata.')
input('Successfully placed these images on the map. Press enter to exit')