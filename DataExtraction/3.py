from pyzomato import Pyzomato

p = Pyzomato(adb186fd589334b4ddda0aa4b2c8fc03)
p.search(q="london")

p.getCategories()
