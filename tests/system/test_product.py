from unittest import TestCase
import json
from mypage2 import app
class ProductTest(TestCase):
    def test_welcome(self):
        with app.test_client() as c:
            resp =c.get('/api/products')
            self.assertEqual(resp.status_code,200)
            self.assertEqual(json.loads(resp.get_data()),
[{"productId": 1, "productName": "Iphone13", "price": 34678.8, "rating": 4.8}, {"productId": 2, "productName": "SamsungFlip", "price": 45678.8, "rating": 4.8}, {"productId": 3, "productName": "MiNote9 pro", "price": 98678.8, "rating": 4.2}, {"productId": 1, "productName": "Iphone25", "price": 988678.8, "rating": 4.9}, {"productId": "34", "productName": "ertr", "price": "34567", "rating": "3.6"}, {"productId": "345", "productName": "dddd", "price": "44556", "rating": "4.5"}])
