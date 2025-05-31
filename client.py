# client.py
import grpc

import university_pb2
import university_pb2_grpc

def run():
    # Sunucuya bağlanacağımız kanal (localhost:50051)
    with grpc.insecure_channel('localhost:50051') as channel:
        books_stub = university_pb2_grpc.BooksServiceStub(channel)
        students_stub = university_pb2_grpc.StudentsServiceStub(channel)
        loans_stub = university_pb2_grpc.LoansServiceStub(channel)

        # ---------------------------------------------------
        # ÖRNEK 1: Kitap Listeleme (ListBooks)
        # ---------------------------------------------------
        print("=== Tüm Kitapları Listele ===")
        list_books_response = books_stub.ListBooks(university_pb2.ListBooksResponse())
        for book in list_books_response.books:
            print(f"Book ID: {book.id}, Title: {book.title}, Author: {book.author}")
        print()

        # ---------------------------------------------------
        # ÖRNEK 2: Yeni Kitap Ekleme (CreateBook)
        # ---------------------------------------------------
        print("=== Yeni Kitap Ekle ===")
        new_book = university_pb2.Book(
            id="book-123",
            title="Veri Yapıları ve Algoritmalar",
            author="Ali Veli",
            isbn="9781234567890",
            publisher="Üniversite Yayınları",
            pageCount=350,
            stock=5
        )
        create_book_response = books_stub.CreateBook(university_pb2.CreateBookRequest(book=new_book))
        print("Oluşturulan Kitap:", create_book_response.book)
        print()

        # ---------------------------------------------------
        # ÖRNEK 3: Tek Kitap Görüntüleme (GetBook)
        # ---------------------------------------------------
        print("=== Tek Kitap Görüntüle (ID = book-123) ===")
        try:
            get_book_response = books_stub.GetBook(university_pb2.GetBookRequest(id="book-123"))
            book = get_book_response.book
            print(f"Bulunan Kitap → ID: {book.id}, Title: {book.title}, Stock: {book.stock}")
        except grpc.RpcError as e:
            print(f"GetBook Hatası: {e.code()} - {e.details()}")
        print()

        # ---------------------------------------------------
        # ÖRNEK 4: Kitap Silme (DeleteBook)
        # ---------------------------------------------------
        print("=== Kitap Sil (ID = book-123) ===")
        delete_book_response = books_stub.DeleteBook(university_pb2.DeleteBookRequest(id="book-123"))
        print("Silme Başarılı mı?", delete_book_response.success)
        print()

        # ---------------------------------------------------
        # ÖRNEK 5: Öğrenci Ekleme (CreateStudent) ve Listeleme
        # ---------------------------------------------------
        print("=== Yeni Öğrenci Ekle ve Listele ===")
        new_student = university_pb2.Student(
            id="student-001",
            name="Ayşe Yılmaz",
            studentNumber="2025001",
            email="ayse.yilmaz@example.com",
            isActive=True
        )
        create_student_response = students_stub.CreateStudent(university_pb2.CreateStudentRequest(student=new_student))
        print("Oluşturulan Öğrenci:", create_student_response.student)

        list_students_response = students_stub.ListStudents(university_pb2.ListStudentsRequest())
        for stu in list_students_response.students:
            print(f"Student ID: {stu.id}, Name: {stu.name}, Active: {stu.isActive}")
        print()

        # ---------------------------------------------------
        # ÖRNEK 6: Ödünç Alma (CreateLoan)
        # ---------------------------------------------------
        print("=== Yeni Loan Oluştur (Ödünç Alma) ===")
        new_loan = university_pb2.Loan(
            id="loan-100",
            studentId="student-001",
            bookId="book-999",  # var olmayan bir kitap ID; NOT_FOUND hata göreceğiz
            loanDate="2025-06-05",
            returnDate="",
            status=university_pb2.ONGOING
        )
        try:
            create_loan_response = loans_stub.CreateLoan(university_pb2.CreateLoanRequest(loan=new_loan))
            print("Loan Detayı:", create_loan_response.loan)
        except grpc.RpcError as e:
            print(f"CreateLoan Hatası: {e.code()} - {e.details()}")
        print()

        # ---------------------------------------------------
        # ÖRNEK 7: İade Etme (ReturnLoan)
        # ---------------------------------------------------
        print("=== Loan İade Etme (ReturnLoan) ===")
        try:
            return_loan_response = loans_stub.ReturnLoan(university_pb2.ReturnLoanRequest(id="loan-100"))
            print("Güncellenen Loan:", return_loan_response.loan)
        except grpc.RpcError as e:
            print(f"ReturnLoan Hatası: {e.code()} - {e.details()}")
        print()

        # ---------------------------------------------------
        # ÖRNEK 8: Tüm Loan’ları Listeleme (ListLoans)
        # ---------------------------------------------------
        print("=== Tüm Loan’ları Listele ===")
        list_loans_response = loans_stub.ListLoans(university_pb2.ListLoansRequest())
        for loan in list_loans_response.loans:
            print(f"Loan ID: {loan.id}, Status: {loan.status}, LoanDate: {loan.loanDate}, ReturnDate: {loan.returnDate}")
        print()


if __name__ == "__main__":
    run()
