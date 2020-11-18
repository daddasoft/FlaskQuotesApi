def ToDictionary(oldObj):
    data = []
    for obj in oldObj:
        data.append({"id": obj[0], "body": obj[1], "author": obj[2],
                     "createdBy": obj[3], "categorie": obj[4], "createdAt": obj[5], "updatedAt": obj[6]})
    return data
