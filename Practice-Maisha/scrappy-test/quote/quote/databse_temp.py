import sqlite3

conn = sqlite3.connect('allquotes.db')
curr = conn.cursor()

# curr.execute("""create table quotes_table(
#                 title text,
#                 author text,
#                 tag text
#                 )""")


curr.execute("""insert into quotes_table values ('LEARNING SCRAPYYYY','MAISHA AMIN','scrapy')""")
conn.commit()
conn.close()
