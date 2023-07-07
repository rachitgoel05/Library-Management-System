def studentEntity(item) -> dict:
    print(item)
    return {
        "_id": str(item["_id"]),
        "student_id": item["student_id"],
         "name": item["name"],
        "email": item["email"],
        "phone_no": item["phone_no"],
        "address": item["address"],
        "socials": item["socials"],
        "books": item["books"],
        "entry_time": item["entry_time"]
    }

def studentsEntity(entity) -> list:
    return [studentEntity(item) for item in entity]