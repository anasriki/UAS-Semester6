from rest_framework import serializers
from .models import Pulsa, Transaksi, Pelanggan

# buat kelas serializer
class PulsaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pulsa
        fields = ["nominal", "harga", "operator_seluler"]

class TransaksiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaksi
        fields = ["jumlah_pembelian", "harga", "tanggal_transaksi", "pembeli"]

class PelangganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelanggan
        fields = ["nama", "nomor_telepon", "alamat"]
        