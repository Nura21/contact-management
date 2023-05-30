import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="qwerty21",
  database="contact_management",
)

if db.is_connected():
  print("Berhasil terhubung ke database")