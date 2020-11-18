from flask import escape


def ToDictionary(oldObj):
    data = []
    for obj in oldObj:
        data.append({"id": escape(obj[0]), "body": escape(obj[1]), "author": escape(obj[2]),
                     "createdBy": escape(obj[3]), "category": escape(obj[4]), "createdAt": escape(obj[5]), "updatedAt": escape(obj[6])})
    return data
