import sqlite3

class Database:
    # 생성자
    def __init__(self, db = None):
        self.conn = None
        self.cursor = None

        if db: # db 파라미터가 전달 되었으면
            self.open(db)

    # 접속 메서드
    def open(self, db):
        try:
            self.conn = sqlite3.connect(db)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print("Database 접속 실패")

    # 닫기 메서드
    def close(self):
        if self.conn:
            self.conn.commit() # 남아있는 I,U,D 쿼리를 커밋
            self.cursor.close()
            self.conn.close()

    #__enter__ : with 와 함께 사용했을 때 호출되는 생명주기
    def __enter__(self):
        return self

    # __exit__ : with 절이 끝났을때 호풀되는 생명주기
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


    def execute_select(self,sql, parameter=None):
        if parameter is not None: # 파라미터가 있다
            self.cursor.execute(sql, parameter)
        else: #파라미터가 없다
            self.cursor.execute(sql)

        data = list(self.cursor.fetchall())
        return data
    # INSERT UPDATE DELETE 쿼리 수행메서드
    def execute_cud(self, sql, parameter=None):
        if parameter is not None: #파라미터가 있다
            self.cursor.execute(sql, parameter)