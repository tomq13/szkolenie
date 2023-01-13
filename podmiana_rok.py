import xml.etree.ElementTree as ET

tree = ET.parse('dane.xml')

root = tree.getroot()

for year in root.findall("./genre/decade/movie"):
    if year.find('year').text == "1992":
        year.find('year').text = "2023"

tree.write('dane1.xml')