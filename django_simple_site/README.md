# Django ile Basit Web Sitesi Entegrasyonu


> Amaç: Django'da Template Engine'in çalışma mantığının anlaşılması.

## Projenin yüklenmesi ve çalıştırılması:

Virtualenv aktif edildikten sonra:

```
pip install -r requierements.txt
```

### Dev Sunucusunun Çalıştırılması

```
python manage.py runserver 0:8000
```

### Uygulanan Adımlar:
- django_simple_site.views.py içerisinde HttpResponse kullanimi
- **python manage.py startapp page** ile page app olusturuldu
- settings icerisinde TEMPLATES['DIRS': [],] icine templates klasoru eklendi
- base.html, include, block ve extends kullanildi
- page.views icerisinde index view olusturuldu ve template'e context gonderildi
- page.views icerisinde page view olusturuldu. 