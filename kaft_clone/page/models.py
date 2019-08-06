from django.db import models

STATUS = [
    ('draft', 'Taslak'),
    ('published', 'Yayinlandi'),
    ('deleted', 'Silindi'),
]

class Page(models.Model):
    title = models.CharField(max_length=200)
    # slug : sadece create sirasinda olusmalidir
    content = models.TextField() 
    cover_image = models.ImageField(upload_to='page')
    status = models.CharField(
        default="draft", 
        choices=STATUS,
        max_length=10,
    )
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
