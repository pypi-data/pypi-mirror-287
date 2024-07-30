from LiteJsonDb import JsonDB

db = JsonDB(crypted=True)

# Ajout de données à la base de données
db.set_data("users/1", {"name": "Alice", "age": 30})
db.set_data("users/2", {"name": "Bob", "score": 15})

db.edit_data("users/2", {"increment": {"score": 55555}})

user2_data = db.get_data("users/2")

print(user2_data)

# Récupération de la base de données complète
print(db.get_db(raw=True))

