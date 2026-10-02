from pyscript import document, window

def generateSKU(event):
    event.preventDefault()  
    # prevents form submission refresh
    
    category = document.querySelector("#category").value
    product_name = document.querySelector("#productName").value.strip()
    stock_qty = document.querySelector("#stockQty").value.strip()
    # takes values from HTML inputs

    if not product_name or not stock_qty:
        document.querySelector("#skuResult").innerHTML = "<p style='color: #5e2a25;'>Please fill out all fields.</p>"
        return
    # handles empty inputs

    cat_code = category[:3].upper()
    # takes first 3 letters of category (brewed coffee -> BRE)
    
    words = product_name.split()
    if len(words) >= 2:
        name_code = (words[0][0] + words[1][0]).upper()
    elif len(words) == 1 and len(words[0]) >= 2:
        name_code = words[0][:2].upper()
    else:
        name_code = product_name[:2].upper()
    # takes first letters of product name (VANILLA FRAPPE -> VF, COFFEE -> CO)

    formatted_qty = str(stock_qty).zfill(2)
    # adds leading zeroes up to 2 to the string
        
    sku = f"{cat_code}-{name_code}-{formatted_qty}"
    # formats final SKU (BRE-VF-50)

    document.querySelector("#skuResult").innerHTML = f"""
        <div style="text-align: center;">
            <h3 style="font-family: monospace; background-color: #af9f62; color: #534831; border: 2px solid #534831; padding: 10px 20px; border-radius: 10px; display: inline-block; letter-spacing: 2px;">{sku}</h3>
        </div>
    """
    # puts result into #skuResult

window.generateSKU = generateSKU
# exposes the function to the global HTML scope so py-click can find it