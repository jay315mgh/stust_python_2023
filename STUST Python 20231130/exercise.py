#學生資料類別
class Students:
    #建構式
    def __init__(self,school_name,school_mailing_address,major,major_chairname,student_name,studentID,personal_mailing_address,number_of_credits,grade_GPA):
        self.school_name = school_name                                                # 學校名稱屬性
        self.school_mailing_address = school_mailing_address                          # 學校通訊地址
        self.major = major                                                            # 學生科系屬性
        self.major_chairname = major_chairname                                        # 學生年級屬性
        self.student_name = student_name                                              # 學生名稱屬性
        self.studentID = studentID                                                    # 學生學號屬性
        self.personal_mailing_address = personal_mailing_address                      # 學生個人通訊地址屬性
        self.number_of_credits = number_of_credits                                    # 已取得學分數屬性
        self.grade_GPA = grade_GPA                                                    # 成績GPA屬性
        
    def get_schoolname(self):
        return self.school_name
    def set_schoolname(self, value):
        self.school_name = value
        
    def get_school_mailing_address(self):
        return self.school_mailing_address
    def set_school_mailing_address(self, value):
        self.school_mailing_address = value
        
    def get_major(self):
        return self.major
    def set_major(self, value):
        self.major = value
        
    def get_major_chairname(self):
        return self.major_chairname
    def set_major_chairname(self, value):
        self.major_chairname = value
        
    def get_student_name(self):
        return self.student_name
    def set_student_name(self, value):
        self.student_name = value
        
    def get_studentID(self):
        return self.studentID
    def set_studentID(self, value):
        self.studentID = value
        
    def get_personal_mailing_address(self):
        return self.personal_mailing_address
    def set_personal_mailing_address(self, value):
        self.personal_mailing_address = value
        
    def get_number_of_credits (self):
        return self.number_of_credits 
    def set_number_of_credits (self, value ):
        self.number_of_credits  = value
        
    def get_grade_GPA(self):
        return self.grade_GPA
    def set_grade_GPA(self, value):
        self.grade_GPA = value

# 建立一個類別為Student的物件st1
st1 = Students("南台科技大學","台南市永康區南台街1號","資工系","三年級","林子傑","4B0G0152","台南市永康區南台街1號","35","4.3")


# 輸出學生資料
print("\n學生資訊:")
print(f"學校名稱: {st1.get_schoolname()}")
print(f"學校通訊地址: {st1.get_school_mailing_address()}")
print(f"學生科系: {st1.get_major()}")
print(f"學生年級: {st1.get_major_chairname()}")
print(f"學生名稱: {st1.get_student_name()}")
print(f"學生學號: {st1.get_studentID()}")
print(f"學生個人通訊地址: {st1.get_personal_mailing_address()}")
print(f"已取得學分數: {st1.get_number_of_credits()}")
print(f"成績GPA: {st1.get_grade_GPA()}")