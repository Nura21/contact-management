import Connect as Connect

class AddressBook:
    def __init__(self):
        print("")

    def add_contact(name: str, phone_number: str):
        sql = "INSERT INTO contacts (name, phone_number) VALUES (%s, %s)"
        Connect.db.cursor().execute(sql, (name, phone_number))
        
        Connect.db.commit()
        print("Data berhasil ditambahkan".format(Connect.db.cursor().rowcount))
        
        Connect.db.cursor().close()
    
    def remove_contact(name: str):
        sql = "DELETE FROM contacts WHERE name=%s"
        Connect.db.cursor().execute(sql, [name, ])
        
        Connect.db.commit()
        print("Data berhasil dihapus".format(Connect.db.cursor().rowcount))

        Connect.db.cursor().close()

    def search_contact(name: str):
        cursor = Connect.db.cursor()

        sql = "SELECT phone_number FROM contacts WHERE name=%s"
        cursor.execute(sql, [name])
        
        contacts = cursor.fetchall()

        if len(contacts) == 0:
            return print("Kontak tidak ditemukan")
        
        for data in contacts:
            print(data)
        
        return Connect.db.cursor().close()