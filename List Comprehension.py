rows = [[u'536246229548 1608738688644 /data/sales/analytics', '2022-05-05 08:20:14'], [u'127360745915 382082237745 /data/sales/etl', '2022-05-05 08:20:14'], [u'15177689049438 45533067148314 /data/sales/modeled', '2022-05-05 08:20:14'], [u'3525346992410 10576040977230 /data/sales/raw', '2022-05-05 08:20:14']]

modified_rows = []

for i in rows:
  modified_rows = i[0].split()
  print (modified_rows)
  print (modified_rows[1], modified_rows[2], i[-1])