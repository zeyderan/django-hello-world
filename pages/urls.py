# bu dosya hazır üretilmiyor.
# oluşturduğumuz app için url bildirimlerini burdan yapıyoruz
# sonrasında project-root klasöründe url.py içerisine
# bu dosyayı referans veriyoruz

#url dosyalarında path mutlaka import edilmeli
from django.urls import path

# url dosyalarında url hangi view ile ilişkilendirilecek ise
# o view import edilmeli
from .views import homePageView

urlpatterns = [
    #path(url uzantısı, seçilen view, extra özelikler örn name = 'name')
    path('',homePageView,name='home'),
]