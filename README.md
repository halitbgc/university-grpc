# University gRPC Project

Python ile geliştirilen bu repo, üniversite kütüphane sistemi için üç temel gRPC servisi içerir:
- **BooksService**: Kitap CRUD işlemleri
- **StudentsService**: Öğrenci CRUD işlemleri
- **LoansService**: Ödünç (loan) alma ve iade

---

## 📂 Proje Yapısı

```
university-grpc/
├── university.proto             # Protobuf tanımları
├── grpcurl-tests.md             # grpcurl ile manuel testler
├── README.md                    # Bu dosya
├── server.py                    # gRPC sunucu uygulaması
├── client.py                    # gRPC istemci örnekleri
└── DELIVERY.md                  # Teslim dosyası
```
! Stub dosyaları dahil edilmemiştir.

---

## ⚙️ Kurulum

1. **Python ≥ 3.7** yüklü olmalı.  
2. Gerekli paketleri yükleyin:
   ```bash
   pip install grpcio grpcio-tools protobuf
   ```


---

## 🔧 Protobuf’tan Stub Oluşturma

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. university.proto
```
Bu komut, proje kökünde `university_pb2.py` ve `university_pb2_grpc.py` dosyalarını oluşturur.

---

## ▶️ Sunucu ve İstemciyi Çalıştırma

1. **Sunucuyu başlatın** (proje kökünden):
   ```bash
   python src/server.py
   ```
   Ekranda “gRPC sunucusu 50051 numaralı portta çalışıyor” yazdığını kontrol edin.

2. **İstemciyi çalıştırın** (başka bir terminalde, yine proje kökü):
   ```bash
   python src/client.py
   ```
   İstemci, örnek kitap/öğrenci/loan işlemlerini yaparak sonucu konsola yazdırır.

---

## ✅ Manuel Testler (grpcurl)

- **grpcurl** yüklü olmalı (winget/choco/scoop veya manuel indirme).  
- Sunucu ayakta iken, proje kökünden:

  ```bash
  grpcurl -plaintext localhost:50051 list
  grpcurl -plaintext -d '{}' localhost:50051 university.BooksService/ListBooks
  grpcurl -plaintext -d '{ "id": "book-xyz" }' localhost:50051 university.BooksService/GetBook
  ```

  Bu testlerin tamamı ve çıktıları için `grpcurl-tests.md` dosyasına bakabilirsiniz.

---

## 📋 Özet

- **university.proto**: Mesaj tipleri ve üç servis tanımı  
- **server.py**: İn-memory veri ile CRUD ve loan işlemleri  
- **client.py**: gRPC çağrı örnekleri  
- **grpcurl-tests.md**: Manuel test komutları ve çıktıları

