# server.py
import grpc
from concurrent import futures
import time

import university_pb2      # Mesaj tipleri
import university_pb2_grpc # Servis stub ve servis taban sınıfları

# -----------------------------
#  2.4.1. “Servicer” Sınıfları
# -----------------------------
class BooksServiceServicer(university_pb2_grpc.BooksServiceServicer):
    """
    BooksService’in metodlarını burada hayata geçireceğiz.
    """
    def __init__(self):
        self.books = {}  # In-memory “veritabanı” için basit dict

    def ListBooks(self, request, context):
        response = university_pb2.ListBooksResponse()
        for book in self.books.values():
            response.books.append(book)
        return response

    def GetBook(self, request, context):
        book_id = request.id
        if book_id in self.books:
            return university_pb2.GetBookResponse(book=self.books[book_id])
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Book with ID {book_id} not found.")
            return university_pb2.GetBookResponse()

    def CreateBook(self, request, context):
        book = request.book
        if book.id in self.books:
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details(f"Book with ID {book.id} already exists.")
            return university_pb2.CreateBookResponse()
        self.books[book.id] = university_pb2.Book(
            id=book.id,
            title=book.title,
            author=book.author,
            isbn=book.isbn,
            publisher=book.publisher,
            pageCount=book.pageCount,
            stock=book.stock
        )
        return university_pb2.CreateBookResponse(book=self.books[book.id])

    def UpdateBook(self, request, context):
        book = request.book
        if book.id not in self.books:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Book with ID {book.id} not found.")
            return university_pb2.UpdateBookResponse()
        self.books[book.id] = university_pb2.Book(
            id=book.id,
            title=book.title,
            author=book.author,
            isbn=book.isbn,
            publisher=book.publisher,
            pageCount=book.pageCount,
            stock=book.stock
        )
        return university_pb2.UpdateBookResponse(book=self.books[book.id])

    def DeleteBook(self, request, context):
        book_id = request.id
        if book_id not in self.books:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Book with ID {book_id} not found.")
            return university_pb2.DeleteBookResponse(success=False)
        del self.books[book_id]
        return university_pb2.DeleteBookResponse(success=True)


class StudentsServiceServicer(university_pb2_grpc.StudentsServiceServicer):
    """
    StudentsService’in metodlarını burada hayata geçireceğiz.
    """
    def __init__(self):
        self.students = {}

    def ListStudents(self, request, context):
        response = university_pb2.ListStudentsResponse()
        for student in self.students.values():
            response.students.append(student)
        return response

    def GetStudent(self, request, context):
        student_id = request.id
        if student_id in self.students:
            return university_pb2.GetStudentResponse(student=self.students[student_id])
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Student with ID {student_id} not found.")
            return university_pb2.GetStudentResponse()

    def CreateStudent(self, request, context):
        student = request.student
        if student.id in self.students:
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details(f"Student with ID {student.id} already exists.")
            return university_pb2.CreateStudentResponse()
        self.students[student.id] = university_pb2.Student(
            id=student.id,
            name=student.name,
            studentNumber=student.studentNumber,
            email=student.email,
            isActive=student.isActive
        )
        return university_pb2.CreateStudentResponse(student=self.students[student.id])

    def UpdateStudent(self, request, context):
        student = request.student
        if student.id not in self.students:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Student with ID {student.id} not found.")
            return university_pb2.UpdateStudentResponse()
        self.students[student.id] = university_pb2.Student(
            id=student.id,
            name=student.name,
            studentNumber=student.studentNumber,
            email=student.email,
            isActive=student.isActive
        )
        return university_pb2.UpdateStudentResponse(student=self.students[student.id])

    def DeleteStudent(self, request, context):
        student_id = request.id
        if student_id not in self.students:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Student with ID {student_id} not found.")
            return university_pb2.DeleteStudentResponse(success=False)
        del self.students[student_id]
        return university_pb2.DeleteStudentResponse(success=True)


class LoansServiceServicer(university_pb2_grpc.LoansServiceServicer):
    """
    LoansService’in metodlarını burada hayata geçireceğiz.
    """
    def __init__(self):
        self.loans = {}

    def ListLoans(self, request, context):
        response = university_pb2.ListLoansResponse()
        for loan in self.loans.values():
            response.loans.append(loan)
        return response

    def GetLoan(self, request, context):
        loan_id = request.id
        if loan_id in self.loans:
            return university_pb2.GetLoanResponse(loan=self.loans[loan_id])
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Loan with ID {loan_id} not found.")
            return university_pb2.GetLoanResponse()

    def CreateLoan(self, request, context):
        loan = request.loan
        if loan.id in self.loans:
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details(f"Loan with ID {loan.id} already exists.")
            return university_pb2.CreateLoanResponse()
        # Yeni ödünç kaydı eklerken returnDate boş, status ONGOING
        self.loans[loan.id] = university_pb2.Loan(
            id=loan.id,
            studentId=loan.studentId,
            bookId=loan.bookId,
            loanDate=loan.loanDate,
            returnDate="",
            status=university_pb2.ONGOING
        )
        return university_pb2.CreateLoanResponse(loan=self.loans[loan.id])

    def ReturnLoan(self, request, context):
        loan_id = request.id
        if loan_id not in self.loans:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Loan with ID {loan_id} not found.")
            return university_pb2.ReturnLoanResponse()
        loan_obj = self.loans[loan_id]
        # Örnek: iade tarihi “2025-06-05” olarak atandı
        updated_loan = university_pb2.Loan(
            id=loan_obj.id,
            studentId=loan_obj.studentId,
            bookId=loan_obj.bookId,
            loanDate=loan_obj.loanDate,
            returnDate="2025-06-05",
            status=university_pb2.RETURNED
        )
        self.loans[loan_id] = updated_loan
        return university_pb2.ReturnLoanResponse(loan=updated_loan)


# -----------------------------
#  2.4.2. gRPC Sunucusunu Başlatma
# -----------------------------
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Servisleri sunucuya kaydet
    university_pb2_grpc.add_BooksServiceServicer_to_server(BooksServiceServicer(), server)
    university_pb2_grpc.add_StudentsServiceServicer_to_server(StudentsServiceServicer(), server)
    university_pb2_grpc.add_LoansServiceServicer_to_server(LoansServiceServicer(), server)

    port = 50051
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    print(f"gRPC sunucusu {port} numaralı portta çalışıyor... (CTRL+C ile durdur)")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        print("Sunucu durduruluyor...")
        server.stop(0)


if __name__ == "__main__":
    serve()
