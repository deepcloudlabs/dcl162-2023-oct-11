def extract_customer_from_request_body(request, fields):
    customer = {}
    for field in fields:
        if field in request.json:
            customer[field] = request.json[field]
    if "identity" in customer:
        customer["_id"] = customer["identity"]
    return customer
