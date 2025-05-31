# gRPC Uygulama Geliştirme Ödevi Teslim Raporu

## 👤 Öğrenci Bilgileri

- **Ad Soyad**: Halit Bağcı  
- **Öğrenci Numarası**: 170423841  
- **Kullanılan Programlama Dili**: Python

---

## 📦 GitHub Repo

Aşağıdaki linkten projenin tamamına erişebilirsiniz. \`.proto\` dosyasından üretilen stub kodları (university\_pb2.py, university\_pb2\_grpc.py) dahil edilmemiştir.

### 🔗 GitHub Repo Linki

https://github.com/halitbgc/university-grpc

---

## 📄 .proto Dosyası

- **.proto dosyasının adı(ları)**:  
  - `university.proto`

- **Tanımlanan servisler ve metod sayısı**:  
  1. **BooksService** (5 metod)  
     - `ListBooks`  
     - `GetBook`  
     - `CreateBook`  
     - `UpdateBook`  
     - `DeleteBook`  
  2. **StudentsService** (5 metod)  
     - `ListStudents`  
     - `GetStudent`  
     - `CreateStudent`  
     - `UpdateStudent`  
     - `DeleteStudent`  
  3. **LoansService** (4 metod)  
     - `ListLoans`  
     - `GetLoan`  
     - `CreateLoan`  
     - `ReturnLoan`

- **Enum kullanımınız var mı? Hangi mesajda?**  
  - Evet. `LoanStatus` adında bir enum tanımlandı.  
  - Bu enum, `Loan` mesajındaki `status` alanında kullanılıyor.  
    ```protobuf
    enum LoanStatus {
      ONGOING = 0;
      RETURNED = 1;
      LATE = 2;
    }
    ```

---

## 🧪 grpcurl Test Dokümantasyonu

Aşağıdaki bilgiler, `grpcurl-tests.md` adlı ayrı bir markdown dosyasında detaylı olarak yer almaktadır:

- Her bir RPC metodu için kullanılan `grpcurl` komutları  
- Komutların çalıştırıldığı sırada konsolda görünen gerçek JSON yanıtlar  
- Hatalı durum senaryoları (örneğin `GET` sırasında “NotFound” hatası)

Bu test dokümanı, değerlendirme aşamasında sunucunun doğru çalıştığını ve her metodun beklenen çıktıları döndürdüğünü kanıtlamak için önemlidir.

---

## 🛠️ Derleme ve Çalıştırma Adımları

Projeyi `.proto` dosyasından derleyip sunucu/istemci uygulamasını çalıştırmak için gereken komutlar:

1\. \*\*Proje Klasörüne Gitme\*\*    
   \`\`\`bash  
   cd university-grpc

2\. \*\*Python Bağımlılıklarını Yükleme\*\*  
 pip install \--upgrade pip  
pip install grpcio grpcio-tools protobuf

3\. **Protobuf Dosyasından Python Stub’larını Üretme**   
python \-m grpc\_tools.protoc \-I. \--python\_out=. \--grpc\_python\_out=. university.proto

4\. \*\*Sunucuyu (Server) Başlatma\*\*  
python [server.py](http://server.py)

5\. \*\*İstemciyi (Client) Çalıştırma\*\*  
python server.py

---

## ⚠️ Kontrol Listesi

- [x] Stub dosyaları GitHub reposuna eklenmedi  
- [x] grpcurl komutları test belgesinde yer alıyor  
- [ ] Ekran görüntüleri test belgesine eklendi  
- [x] Tüm servisler çalışır durumda  
- [x] README.md içinde yeterli açıklama var

