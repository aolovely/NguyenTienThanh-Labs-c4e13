from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient (mongo_uri)

db = client.get_default_database()

posts = db["post"]
new_post ={
"title":"Niềm vui nhỏ",
"author":"Love1",
"content": """
Bí quyết của hạnh phúc cũng chính là biết đón nhận những niềm vui nhỏ trong cuộc sống mỗi ngày.
Có những ngày tù đày, chúng ta mới thấy được giá trị của hai chữ tự do.
Có sống xa gia đình, chúng ta mới nhung nhớ những ngày sống bên những người thân.
Có những lúc nằm quằn quại trên giường bệnh, chúng ta mới thấy được giá trị của sức khỏe…
Cuộc sống của chúng ta tràn ngập những niềm vui nhỏ mà chỉ khi nào mất đi, chúng ta mới cảm thấy luyến tiếc
"""
}

db.posts.insert_one(new_post)
