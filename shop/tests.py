from django.urls import reverse_lazy
from rest_framework.test import APITestCase

from shop.models import Category, Product, Article


class ShopAPITestCase(APITestCase):

    @staticmethod
    def format_datetime(value):
        return value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    @staticmethod
    def format_price(price):
        if type(price) == int:
            price += 0.00
        elif type(price) == float:
            price = round(price, 2)
            price += 0.00
        return str(price)


class TestCategory(ShopAPITestCase):
    url = reverse_lazy('category-list')

    def test_list(self):
        category = Category.objects.create(name='Fruits', active=True)
        Category.objects.create(name='Légumes', active=False)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        expected = [
            {
                'id': category.pk,
                'name': category.name,
                'date_created': self.format_datetime(category.date_created),
                'date_updated': self.format_datetime(category.date_updated),
                'description': category.description,
                'active': category.active,
            }
        ]
        self.assertEqual(expected, response.json())

    def test_create(self):
        self.assertFalse(Category.objects.exists())
        response = self.client.post(self.url, data={'name': 'Nouvelle catégorie'})
        self.assertEqual(response.status_code, 405)
        self.assertFalse(Category.objects.exists())


class TestProduct(ShopAPITestCase):
    url = reverse_lazy('product-list')

    def test_list(self):
        category = Category.objects.create(name='Fruits', active=True)
        product = Product.objects.create(name='Pomme', active=True, category=category)
        Product.objects.create(name='Banane', active=False, category=category)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        expected = [
            {
                'id': product.pk,
                'name': product.name,
                'date_created': self.format_datetime(product.date_created),
                'date_updated': self.format_datetime(product.date_updated),
                'category_id': product.category.pk,
                'description': product.description,
                'active': product.active,
            }
        ]
        self.assertEqual(expected, response.json())

    def test_create(self):
        category = Category.objects.create(name='Fruits', active=True)
        self.assertFalse(Product.objects.exists())
        response = self.client.post(self.url, data={'name': 'Nouveau Produit', 'category': '1'})
        self.assertEqual(response.status_code, 405)
        self.assertFalse(Product.objects.exists())


class TestArticles(ShopAPITestCase):
    url = reverse_lazy('article-list')

    def test_list(self):
        category = Category.objects.create(name='Fruits', active=True)
        product = Product.objects.create(name='Pomme', active=True, category=category)
        article = Article.objects.create(name='1kg', active=True, product=product, price='2.50')
        Article.objects.create(name='2kg', active=False, product=product, price='2.50')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        expected = [
            {
                'id': article.pk,
                'date_created': self.format_datetime(article.date_created),
                'date_updated': self.format_datetime(article.date_updated),
                'name': article.name,
                'product_id': article.product.pk,
                'price': article.price,
                'description': article.description,
                'active': article.active,
            }
        ]
        self.assertEqual(expected, response.json())

    def test_create(self):
        category = Category.objects.create(name='Fruits', active=True)
        product = Product.objects.create(name='Pomme', active=True, category=category)
        self.assertFalse(Article.objects.exists())
        response = self.client.post(self.url, data={'name': 'Nouvel article', 'product': '1', 'price': '2.50'})
        self.assertEqual(response.status_code, 405)
        self.assertFalse(Article.objects.exists())
