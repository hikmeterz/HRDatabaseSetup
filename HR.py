import sqlite3

conn = sqlite3.connect('InsanKaynaklari.db')

c = conn.cursor()

# Create table

c.execute('''DROP TABLE IF EXISTS CalisanBilgisi''')
c.execute('''DROP TABLE IF EXISTS GorevBilgisi''')
c.execute('''DROP TABLE IF EXISTS GorevlendirmeBilgisi''')

c.execute('''CREATE TABLE CalisanBilgisi
             (SicilNo text, IsimSoyisim text, Adres text, TCKimlikNo text)''')

c.execute('''CREATE TABLE GorevBilgisi
             (GorevKodu text, GorevUnvani text, GorevBolumu text)''')

c.execute('''CREATE TABLE GorevlendirmeBilgisi
             (SicilNo text, GorevKodu text, BaslamaTarihi text, BitisTarihi text)''')
# Insert a row of data
c.execute("INSERT INTO CalisanBilgisi VALUES ('111','Hikmet','Afyon','0')")
c.execute("INSERT INTO CalisanBilgisi VALUES ('222','Ahmet','Aksaray','1')")
c.execute("INSERT INTO CalisanBilgisi VALUES ('333','Tugba','Ankara','2')")
c.execute("INSERT INTO CalisanBilgisi VALUES ('444','Kivanc','Mersin','3')")
c.execute("INSERT INTO CalisanBilgisi VALUES ('555','Tolga','Adıyaman','4')")
c.execute("INSERT INTO CalisanBilgisi VALUES ('666','Meltem','Bursa','5')")
c.execute("INSERT INTO CalisanBilgisi VALUES ('777','Ayberk','Konya','6')")
c.execute("INSERT INTO CalisanBilgisi VALUES ('888','Gonul','Istanbul','7')")
c.execute("INSERT INTO CalisanBilgisi VALUES ('999','Mehmet','Fatsa','8')")
c.execute("INSERT INTO CalisanBilgisi VALUES ('000','Arif','Istanbul','9')")

c.execute("INSERT INTO GorevBilgisi VALUES ('11111','Bilgisayar Mühendisi','Frontend')")
c.execute("INSERT INTO GorevBilgisi VALUES ('22222','Makine Mühendisi','Backend')")
c.execute("INSERT INTO GorevBilgisi VALUES ('33333','Bilgisayar Mühendisi','Mobil')")
c.execute("INSERT INTO GorevBilgisi VALUES ('44444','Elektrik Mühendisi','Backend')")
c.execute("INSERT INTO GorevBilgisi VALUES ('55555','Elektrik Mühendisi','Mobil')")
c.execute("INSERT INTO GorevBilgisi VALUES ('66666','Makine Mühendisi','Mobil')")
c.execute("INSERT INTO GorevBilgisi VALUES ('77777','Bilgisayar Mühendisi','Frontend')")
c.execute("INSERT INTO GorevBilgisi VALUES ('88888','Elektrik Mühendisi','Backend')")
c.execute("INSERT INTO GorevBilgisi VALUES ('99999','Makine Mühendisi','Web')")
c.execute("INSERT INTO GorevBilgisi VALUES ('00000','Bilgisayar Mühendisi','Web')")

c.execute("INSERT INTO GorevlendirmeBilgisi VALUES ('111','22222','2006-01-05','2021-01-05')")
c.execute("INSERT INTO GorevlendirmeBilgisi VALUES ('222','44444','2006-01-05','2020-01-05')")
c.execute("INSERT INTO GorevlendirmeBilgisi VALUES ('333','33333','2006-01-05','2019-01-05')")
c.execute("INSERT INTO GorevlendirmeBilgisi VALUES ('444','11111','2006-01-05','2018-01-05')")
c.execute("INSERT INTO GorevlendirmeBilgisi VALUES ('555','77777','2006-01-05','2017-01-05')")
c.execute("INSERT INTO GorevlendirmeBilgisi VALUES ('666','66666','2006-01-05','2016-01-05')")
c.execute("INSERT INTO GorevlendirmeBilgisi VALUES ('777','55555','2006-01-05','2023-01-05')")
c.execute("INSERT INTO GorevlendirmeBilgisi VALUES ('888','99999','2006-01-05','2024-01-05')")
c.execute("INSERT INTO GorevlendirmeBilgisi VALUES ('999','88888','2006-01-05','2010-01-05')")
c.execute("INSERT INTO GorevlendirmeBilgisi VALUES ('000','00000','2006-01-05','2024-01-05')")

# c.execute("SELECT GorevKodu,BaslamaTarihi,BitisTarihi FROM GorevlendirmeBilgisi AS gb INNER JOIN CalisanBilgisi AS cb  ON SicilNo=SicilNoG")

row = ""

for rows in c.execute('''SELECT a.TCKimlikNo, a.Adres
FROM CalisanBilgisi AS a 
JOIN GorevlendirmeBilgisi AS b ON b.SicilNo=a.SicilNo 
JOIN GorevBilgisi AS c ON c.GorevKodu=b.GorevKodu
WHERE c.GorevUnvani = "Bilgisayar Mühendisi"''') :
    print(rows)

print(" - ")

for rows in c.execute('''SELECT a.TCKimlikNo, a.Adres 
FROM CalisanBilgisi AS a 
JOIN GorevlendirmeBilgisi AS b ON b.SicilNo=a.SicilNo 
WHERE DATE('now') between b.BaslamaTarihi and b.BitisTarihi''') :
    print(rows)

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()