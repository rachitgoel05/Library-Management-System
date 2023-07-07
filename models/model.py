from pydantic import BaseModel
class Social(BaseModel):
    social_type: str
    link: str
class book(BaseModel):
    book_id: str
    book_name: str
class Address(BaseModel):
    street: str
    city: str
class Timestamp(BaseModel):
    entry_time: str
    exit_time: str

class Student(BaseModel):
    name: str
    email: str
    phone_no: list = []
    address: Address
    socials: Social
    books: book
    entry_time:Timestamp

# ```
# {
#     "_id": "<auto generated id by MongoDB>",
#     "name": "Rachit",
#     "email": "rachit@gmail.com"
#     "phone_no": [ 9999999999, 999999999999]
#     "address": {
#             "city": "Mumbai",
#             "country": "India"
#         },
#     "socials": [
#         {
#         "social_type": "Github",
#         "link": "https://github.com/rachitgoel05"
#         },
#         {
#         "social_type": "LinkedIn",
#         "link": "https://linkedin.com/in/rachitgoel05"
#         }
#     ],
#     "books": [
#         {
#         "book_id": "123",
#         "book_name": "Harry Potter",
#         },
#         {
#         "book_id": "231",
#         "book_name": "Harry Potter 2",
#         }
#     ],
#     "timestamp":[
#         {
#             "entry_time": "2021-08-01 10:00:00",
#             "exit_time": "2021-08-01 11:00:00"
#         },
#         {
#             "entry_time": "2021-08-01 10:00:00",
#             "exit_time": "2021-08-01 11:00:00"
#         }
#     ]
# }

# ```