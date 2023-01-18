def max_profit(time_unit):
    # properties data
    properties = [
        {"name": "Theatre", "time": 5, "earning": 1500, "size": 2},
        {"name": "Pub", "time": 4, "earning": 1000, "size": 1},
        {"name": "Commercial Park", "time": 10, "earning": 3000, "size": 3},
    ]
    # sort properties by earning per unit time
    properties.sort(key=lambda x: x["earning"]/x["time"], reverse=True)
    
    # initialize result
    result = {"Theatre": 0, "Pub": 0, "Commercial Park": 0}
    
    # start building properties
    for prop in properties:
        if time_unit >= prop["time"]:
            result[prop["name"]] += 1
            time_unit -= prop["time"]
    
    # return result
    return result

# test cases
print(max_profit(7)) # {"Theatre": 1, "Pub": 0, "Commercial Park": 0}
print(max_profit(8)) # {"Theatre": 1, "Pub": 0, "Commercial Park": 0}
print(max_profit(13)) # {"Theatre": 2, "Pub": 0, "Commercial Park": 0}
