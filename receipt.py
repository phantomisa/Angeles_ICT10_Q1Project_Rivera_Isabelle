from pyscript import document

MENU = [
    ("item_brewed", "qty_brewed", "Brewed Coffee", 299),
    ("item_americano", "qty_americano", "Americano", 299),
    ("item_iced-lemon", "qty_iced-lemon", "Iced Green Tea Lemonade", 199),
    ("item_iced-matcha", "qty_iced-matcha", "Iced Matcha Green Tea Latte", 199),
    ("item_uni-frappe", "qty_uni-frappe", "Unicorn Frappuccino", 399),
    ("item_croissant", "qty_croissant", "Almond Croissant", 99),
]
# menu items map to: (checkbox ID, quantity input ID, item name, and price)

def generateRECEIPT(event=None):
    selected_items = []
    total_amount = 0

    for chk_id, qty_id, item_name, price in MENU:
        checkbox = document.querySelector(f"#{chk_id}")
        qty_input = document.querySelector(f"#{qty_id}")

        if checkbox and checkbox.checked:
            # Read and sanitize quantity value
            raw_qty = qty_input.value if qty_input else "1"
            qty = int(raw_qty) if raw_qty.isdigit() and int(raw_qty) > 0 else 1
            
            subtotal = price * qty
            total_amount += subtotal
            selected_items.append((item_name, qty, price, subtotal))

    summary_div = document.querySelector("#receiptResult")
    # matches updated HTML container ID

    if not selected_items:
        summary_div.innerHTML = "<p style='color: #5e2a25;'>Please select at least one item from the menu.</p>"
        return

    rows_html = ""
    for name, qty, price, subtotal in selected_items:
        rows_html += f"""
        <div style="display: flex; justify-content: space-between; margin-bottom: 4px; font-size: 14px;">
            <span>{qty}x {name} (₱{price})</span>
            <span>₱{subtotal}</span>
        </div>
        """
    # format for receipt rows

    receipt_html = f"""
    <div style="background-color: #af9f62; border: 2px solid #534831; border-radius: 10px; padding: 15px; color: #161616; text-align: left; width: 80%; margin: 0 auto;">
        <h5 style="text-align: center; font-weight: bold; border-bottom: 2px solid #534831; padding-bottom: 5px; margin-bottom: 10px; color: #534831;">ORDER RECEIPT</h5>
        {rows_html}
        <hr style="border-top: 1px dashed #534831; margin: 10px 0;">
        <div style="display: flex; justify-content: space-between; font-weight: bold; font-size: 16px; color: #534831;">
            <span>TOTAL:</span>
            <span>₱{total_amount}</span>
        </div>
    </div>
    """

    summary_div.innerHTML = receipt_html