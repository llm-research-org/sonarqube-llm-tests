def calculate_price(item_count, discount):
    if item_count > 10:
        total = item_count * 5
        tax = total * 0.1
        final = total + tax
        if discount:
            final = final * 0.9
    
    if item_count > 10:
        total = item_count * 2
        tax = total * 0.1
        final = total + tax
        if discount:
            final = final * 0.9

    return item_count * 5 + final