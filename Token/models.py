from django.db import models

# Create your models here.
class Pulsa(models.Model):
    nominal = models.IntegerField()
    harga = models.IntegerField()
    operator_seluler = models.CharField(max_length=255)

    def __str__(self):
        return self.nominal

class Transaksi(models.Model):
    jumlah_pembelian = models.IntegerField()
    harga = models.IntegerField()
    tanggal_transaksi = models.DateField()
    pembeli = models.CharField(max_length=255)

    def __str__(self):
        return self.jumlah_pembelian

class Pelanggan(models.Model):
    nama = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)

    def __str__(self):
        return self.nama