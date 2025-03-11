class OrderProcessor:
    def process_order(self, order_data):
        # Handle payment processing
        if order_data["payment_method"] == "credit_card":
            self._process_credit_card(order_data["amount"])
        elif order_data["payment_method"] == "paypal":
            self._process_paypal(order_data["amount"])

        # Handle shipping
        if order_data["shipping_method"] == "express":
            self._ship_express(order_data["address"])
        else:
            self._ship_standard(order_data["address"])

        # Handle notifications
        self._send_email_notification(order_data["email"])
        self._log_to_database(order_data)

    def _process_credit_card(self, amount):
        print(f"Processing credit card payment of {amount}")

    def _process_paypal(self, amount):
        print(f"Processing PayPal payment of {amount}")

    def _ship_express(self, address):
        print(f"Shipping express to {address}")

    def _ship_standard(self, address):
        print(f"Shipping standard to {address}")

    def _send_email_notification(self, email):
        print(f"Sending email to {email}")

    def _log_to_database(self, order_data):
        print(f"Logging order: {order_data}")

# Usage
order = {
    "payment_method": "credit_card",
    "amount": 100,
    "shipping_method": "express",
    "address": "123 Main St",
    "email": "customer@example.com"
}
processor = OrderProcessor()
processor.process_order(order)