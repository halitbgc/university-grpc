# grpcurl Manuel Testleri

Bu doküman, `grpcurl` kullanarak gerçekleştirdiğimiz örnek RPC çağrılarını, kullanılan komutları ve gerçek çıktıları içerir.

> **Not:** Aşağıdaki tüm testler için:
> 1. Sunucunun `python server.py` komutuyla **50051** portunda çalışır durumda olduğundan emin olun.
> 2. “grpcurl” komutlarını proje kökünden (yani `university-grpc/` dizininde) çalıştırın.

---

## 1. Servis ve Metotları Listeleme

### Komut

```bash
grpcurl -plaintext localhost:50051 list
```

### Gerçek Çıktı

```
university.BooksService
university.StudentsService
university.LoansService
```

> **Açıklama:** Sunucuda yayınlı üç servisimiz (BooksService, StudentsService, LoansService) listelendi.

---

## 2. “university.BooksService” Metotlarını Listeleme

### Komut

```bash
grpcurl -plaintext localhost:50051 list university.BooksService
```

### Gerçek Çıktı

```
university.BooksService.ListBooks
university.BooksService.GetBook
university.BooksService.CreateBook
university.BooksService.UpdateBook
university.BooksService.DeleteBook
```

---

## 3. “university.StudentsService” Metotlarını Listeleme

### Komut

```bash
grpcurl -plaintext localhost:50051 list university.StudentsService
```

### Gerçek Çıktı

```
university.StudentsService.ListStudents
university.StudentsService.GetStudent
university.StudentsService.CreateStudent
university.StudentsService.UpdateStudent
university.StudentsService.DeleteStudent
```

---

## 4. “university.LoansService” Metotlarını Listeleme

### Komut

```bash
grpcurl -plaintext localhost:50051 list university.LoansService
```

### Gerçek Çıktı

```
university.LoansService.ListLoans
university.LoansService.GetLoan
university.LoansService.CreateLoan
university.LoansService.ReturnLoan
```

---

## 5. Test 1: Kitap Listeleme (`ListBooks`)

Henüz hiçbir kitap eklemediğimiz için `books` dizisi boş dönmelidir.

### Komut

```bash
grpcurl -plaintext -d '{}' localhost:50051 university.BooksService/ListBooks
```

### Gerçek Çıktı

```json
{
  "books": []
}
```

---

## 6. Test 2: Yeni Kitap Ekleme (`CreateBook`)

Aşağıdaki JSON ile “book-abc-01” ID’li yeni bir kitap ekliyoruz.

### Komut

```bash
grpcurl -plaintext -d '{
  "book": {
    "id": "book-abc-01",
    "title": "Programlamaya Giriş",
    "author": "Mehmet Kara",
    "isbn": "9780140328721",
    "publisher": "Üniversite Yayınları",
    "pageCount": 240,
    "stock": 10
  }
}' localhost:50051 university.BooksService/CreateBook
```

### Gerçek Çıktı

```json
{
  "book": {
    "id": "book-abc-01",
    "title": "Programlamaya Giriş",
    "author": "Mehmet Kara",
    "isbn": "9780140328721",
    "publisher": "Üniversite Yayınları",
    "pageCount": 240,
    "stock": 10
  }
}
```

---

## 7. Test 3: Tek Kitap Görüntüleme (`GetBook`)

Daha önce eklediğimiz “book-abc-01” kaydını görüntülüyoruz.

### Komut

```bash
grpcurl -plaintext -d '{ "id": "book-abc-01" }' localhost:50051 university.BooksService/GetBook
```

### Gerçek Çıktı

```json
{
  "book": {
    "id": "book-abc-01",
    "title": "Programlamaya Giriş",
    "author": "Mehmet Kara",
    "isbn": "9780140328721",
    "publisher": "Üniversite Yayınları",
    "pageCount": 240,
    "stock": 10
  }
}
```

---

## 8. Test 4: Kitap Güncelleme (`UpdateBook`)

“book-abc-01” kaydının `stock` değerini 8 olarak güncelliyoruz.

### Komut

```bash
grpcurl -plaintext -d '{
  "book": {
    "id": "book-abc-01",
    "title": "Programlamaya Giriş",
    "author": "Mehmet Kara",
    "isbn": "9780140328721",
    "publisher": "Üniversite Yayınları",
    "pageCount": 240,
    "stock": 8
  }
}' localhost:50051 university.BooksService/UpdateBook
```

### Gerçek Çıktı

```json
{
  "book": {
    "id": "book-abc-01",
    "title": "Programlamaya Giriş",
    "author": "Mehmet Kara",
    "isbn": "9780140328721",
    "publisher": "Üniversite Yayınları",
    "pageCount": 240,
    "stock": 8
  }
}
```

---

## 9. Test 5: Kitap Silme (`DeleteBook`)

“book-abc-01” kaydını siliyoruz.

### Komut

```bash
grpcurl -plaintext -d '{ "id": "book-abc-01" }' localhost:50051 university.BooksService/DeleteBook
```

### Gerçek Çıktı

```json
{
  "success": true
}
```

---

## 10. Test 6: Kitap Bulunamadığında Hata Senaryosu (`GetBook`)

“book-xyz” gibi var olmayan bir ID ile deneme yapıyoruz.

### Komut

```bash
grpcurl -plaintext -d '{ "id": "book-xyz" }' localhost:50051 university.BooksService/GetBook
```

### Gerçek Çıktı

```
Error invoking method "university.BooksService/GetBook": rpc error: code = NotFound desc = Book with ID book-xyz not found.
```

---

## 11. Test 7: Öğrenci Listeleme (`ListStudents`)

Henüz hiçbir öğrenci eklemediğimiz için `students` dizisi boş dönmeli.

### Komut

```bash
grpcurl -plaintext -d '{}' localhost:50051 university.StudentsService/ListStudents
```

### Gerçek Çıktı

```json
{
  "students": []
}
```

---

## 12. Test 8: Yeni Öğrenci Ekleme (`CreateStudent`)

Aşağıdaki JSON ile “student-42” ID’li yeni bir öğrenci ekliyoruz.

### Komut

```bash
grpcurl -plaintext -d '{
  "student": {
    "id": "student-42",
    "name": "Fatma Öztürk",
    "studentNumber": "2025042",
    "email": "fatma.ozturk@example.com",
    "isActive": true
  }
}' localhost:50051 university.StudentsService/CreateStudent
```

### Gerçek Çıktı

```json
{
  "student": {
    "id": "student-42",
    "name": "Fatma Öztürk",
    "studentNumber": "2025042",
    "email": "fatma.ozturk@example.com",
    "isActive": true
  }
}
```

---

## 13. Test 9: Tek Öğrenci Görüntüleme (`GetStudent`)

“student-42” kaydını görüntülüyoruz.

### Komut

```bash
grpcurl -plaintext -d '{ "id": "student-42" }' localhost:50051 university.StudentsService/GetStudent
```

### Gerçek Çıktı

```json
{
  "student": {
    "id": "student-42",
    "name": "Fatma Öztürk",
    "studentNumber": "2025042",
    "email": "fatma.ozturk@example.com",
    "isActive": true
  }
}
```

---

## 14. Test 10: Öğrenci Güncelleme (`UpdateStudent`)

“student-42” kaydının `isActive` değerini `false` olarak güncelliyoruz.

### Komut

```bash
grpcurl -plaintext -d '{
  "student": {
    "id": "student-42",
    "name": "Fatma Öztürk",
    "studentNumber": "2025042",
    "email": "fatma.ozturk@example.com",
    "isActive": false
  }
}' localhost:50051 university.StudentsService/UpdateStudent
```

### Gerçek Çıktı

```json
{
  "student": {
    "id": "student-42",
    "name": "Fatma Öztürk",
    "studentNumber": "2025042",
    "email": "fatma.ozturk@example.com",
    "isActive": false
  }
}
```

---

## 15. Test 11: Öğrenci Silme (`DeleteStudent`)

“student-42” kaydını siliyoruz.

### Komut

```bash
grpcurl -plaintext -d '{ "id": "student-42" }' localhost:50051 university.StudentsService/DeleteStudent
```

### Gerçek Çıktı

```json
{
  "success": true
}
```

---

## 16. Test 12: Öğrenci Bulunamadığında Hata Senaryosu (`GetStudent`)

“student-xyz” gibi var olmayan bir ID ile deneme yapıyoruz.

### Komut

```bash
grpcurl -plaintext -d '{ "id": "student-xyz" }' localhost:50051 university.StudentsService/GetStudent
```

### Gerçek Çıktı

```
Error invoking method "university.StudentsService/GetStudent": rpc error: code = NotFound desc = Student with ID student-xyz not found.
```

---

## 17. Test 13: Loan Listeleme (`ListLoans`)

Henüz hiçbir ödünç kaydı oluşturmadığımız için `loans` dizisi boş dönmeli.

### Komut

```bash
grpcurl -plaintext -d '{}' localhost:50051 university.LoansService/ListLoans
```

### Gerçek Çıktı

```json
{
  "loans": []
}
```

---

## 18. Test 14: Yeni Loan Oluşturma (`CreateLoan`)

Aşağıdaki JSON ile “loan-1” ID’li yeni bir ödünç kaydı ekliyoruz. Sunucudaki `CreateLoan` metodu herhangi bir öğrenci/kitap doğrulaması yapmadan doğrudan ekleyebiliyor, bu yüzden bu çağrı başarılı olacaktır.

> **Not:** `"status": 0` değeri Protobuf `enum` olarak `ONGOING`’i temsil eder.

### Komut

```bash
grpcurl -plaintext -d '{
  "loan": {
    "id": "loan-1",
    "studentId": "student-99",
    "bookId": "book-99",
    "loanDate": "2025-06-10",
    "returnDate": "",
    "status": 0
  }
}' localhost:50051 university.LoansService/CreateLoan
```

### Gerçek Çıktı

```json
{
  "loan": {
    "id": "loan-1",
    "studentId": "student-99",
    "bookId": "book-99",
    "loanDate": "2025-06-10",
    "returnDate": "",
    "status": "ONGOING"
  }
}
```

---

## 19. Test 15: Tek Loan Görüntüleme (`GetLoan`)

“loan-1” kaydını görüntülüyoruz.

### Komut

```bash
grpcurl -plaintext -d '{ "id": "loan-1" }' localhost:50051 university.LoansService/GetLoan
```

### Gerçek Çıktı

```json
{
  "loan": {
    "id": "loan-1",
    "studentId": "student-99",
    "bookId": "book-99",
    "loanDate": "2025-06-10",
    "returnDate": "",
    "status": "ONGOING"
  }
}
```

---

## 20. Test 16: Loan İade Etme (`ReturnLoan`)

“loan-1” kaydını iade ediyoruz. Sunucu kodu içinde iade tarihi sabit `"2025-06-05"` olarak ayarlandığı için bu veriyi dönüyor.

### Komut

```bash
grpcurl -plaintext -d '{ "id": "loan-1" }' localhost:50051 university.LoansService/ReturnLoan
```

### Gerçek Çıktı

```json
{
  "loan": {
    "id": "loan-1",
    "studentId": "student-99",
    "bookId": "book-99",
    "loanDate": "2025-06-10",
    "returnDate": "2025-06-05",
    "status": "RETURNED"
  }
}
```

---

## 21. Test 17: Loan Son Hali ile Listeleme (`ListLoans`)

İade edilmiş “loan-1” kaydını listeleyerek güncel durumu kontrol ediyoruz.

### Komut

```bash
grpcurl -plaintext -d '{}' localhost:50051 university.LoansService/ListLoans
```

### Gerçek Çıktı

```json
{
  "loans": [
    {
      "id": "loan-1",
      "studentId": "student-99",
      "bookId": "book-99",
      "loanDate": "2025-06-10",
      "returnDate": "2025-06-05",
      "status": "RETURNED"
    }
  ]
}
```

---

### Özet

- Bu dosyada, `grpcurl` komut satırı aracını kullanarak her bir servis ve RPC metodunu test ettik.  
- Kitap (Book) işlemleri: Listeleme, ekleme, görüntüleme, güncelleme, silme, bulunamama senaryosu.  
- Öğrenci (Student) işlemleri: Listeleme, ekleme, görüntüleme, güncelleme, silme, bulunamama senaryosu.  
- Ödünç (Loan) işlemleri: Listeleme, ekleme, görüntüleme, iade etme, iade sonrası listeleme.  

Bu adımları uygulayarak hem sunucunun doğru çalıştığını, hem de RPC metodlarının beklediğimiz sonuçları döndüğünü kanıtlamış olduk.
