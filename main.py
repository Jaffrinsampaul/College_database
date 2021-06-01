from fpdf import FPDF
import math

class Record:

    def dep_computer(self):
        staff = ["SivaKumar", "Jenifer", "Samraj", "Jeena", "Bruntha", "Computer"]

        fees = {"Iyear": 120000, "IIyear": 100000, "IIIyear": 100000, "IVyear": 100000}

        stu_iyear = [["name : student1", "mark", 261], ["name : student 2", "mark", 361],
                     ["name : student 3", "mark", 291], ["name : student 4", "mark", 451]]

        stu_iiyear = [["name : student 5", "mark", 261], ["name : student 6", "mark", 361],
                      ["name : student 7", "mark", 291], ["name : student 8", "mark", 451]]

        stu_iiiyear = [["name : student 9", "mark", 261], ["name : student 10", "mark", 361],
                       ["name : student 11", "mark", 291], ["name : student 12", "mark", 451]]

        stu_ivyear = [["name : student 13", "mark", 261], ["name : student 14", "mark", 361],
                      ["name : student 15", "mark", 291], ["name : student 16"," mark", 451]]
        self.com_database = {"Iyear": stu_iyear, "IIyear": stu_iiyear,
                             "IIIyear": stu_iiiyear,
                             "IVyear": stu_ivyear, "staff": staff, "fees": fees}

    def dep_mechanical(self):
        staff = ["Jerry", "Joe", "Aalan", "Karthick", "Nakkalites"]
        fees = {"I year": 120000, "II year": 100000, "III year": 100000, "IV year": 100000}
        stu_iyear = [["name : student1", "mark", 261], ["name : student 2", "mark", 361],
                     ["name : student 3", "mark", 291], ["name : student 4", "mark", 451]]

        stu_iiyear = [["name : student 5", "mark", 261], ["name : student 6", "mark", 361],
                      ["name : student 7", "mark", 291], ["name : student 8", "mark", 451]]

        stu_iiiyear = [["name : student 9", "mark", 261], ["name : student 10", "mark", 361],
                       ["name : student 11", "mark", 291], ["name : student 12", "mark", 451]]

        stu_ivyear = [["name : student 13", "mark", 261], ["name : student 14", "mark", 361],
                      ["name : student 16", "mark", 291], ["name : student 15", "mark", 451]]
        self.mech_database = {"Iyear": stu_iyear, "IIyear": stu_iiyear, "IIIyear": stu_iiiyear,
                              "IVyear": stu_ivyear, "staff": staff, "fees": fees}

    def dep_electronical(self):
        staff = ["SivaKumar", "Jenifer", "Samraj", "Jeena", "Bruntha", "EEE"]
        fees = {"I year": 120000, "II year": 100000, "III year": 100000, "IV year": 100000}
        stu_iyear = [["name : student 1", "mark", 261], ["name : student 2", "mark", 361],
                     ["name : student 3", "mark", 291], ["name : student 4", "mark", 451]]

        stu_iiyear = [["name : student 5", "mark", 261], ["name : student 6", "mark", 361],
                      ["name : student 7", "mark", 291], ["name : student 8", "mark", 451]]

        stu_iiiyear = [["name : student 9", "mark", 261], ["name : student 10", "mark", 361],
                       ["name : student 11", "mark", 291], ["name : student 12", "mark", 451]]

        stu_ivyear = [["name : student 13", "mark", 261], ["name : student 14", "mark", 361],
                      ["name : student 15", "mark", 291], ["name : student 16", "mark", 451]]

        self.ece_database = {"Iyear": stu_iyear, "IIyear": stu_iiyear, "IIIyear": stu_iiiyear,
                             "IVyear": stu_ivyear, "staff": staff, "fees": fees}

    def dep_electrical(self):
        staff = ["SivaKumar", "Jenifer", "Samraj", "Jeena", "Bruntha"]
        fees = {"I year": 120000, "II year": 100000, "III year": 100000, "IV year": 100000}
        stu_Iyear = [["name : student1", "mark", 261], ["name : student 2", "mark", 361],
                     ["name : student 3", "mark", 291], ["name : student 4", "mark", 451]]

        stu_IIyear = [["name : student 5", "mark", 261], ["name : student 6", "mark", 361],
                      ["name : student 7", "mark", 291], ["name : student 8", "mark", 451]]

        stu_IIIyear = [["name : student 9", "mark", 261], ["name : student 10", "mark", 361],
                       ["name : student 10", "mark", 291], ["name : student 12", "mark", 451]]

        stu_IVyear = [["name : student 13", "mark", 261], ["name : student 14", "mark", 361],
                      ["name : student 3", "mark", 291], ["name : student 16", "mark", 451]]

        self.eee_database = {"Iyear": stu_Iyear, "IIyear": stu_IIyear,
                             "IIIyear": stu_IIIyear, "IVyear": stu_IVyear, "staff": staff, "fees": fees}

    def dep_information(self):
        staff = ["SivaKumar", "Jenifer", "Samraj", "Jeena", "Bruntha", "IT"]
        fees = {"Iyear": 120000, "IIyear": 100000, "IIIyear": 100000, "IVyear": 100000}
        stu_iyear = [["name : student1", "mark", 261], ["name : student 2", "mark", 361],
                     ["name : student 3", "mark", 291], ["name : student 4", "mark", 451]]

        stu_iiyear = [["name : student 5", "mark", 261], ["name : student 6", "mark", 361],
                      ["name : student 7", "mark", 291], ["name : student 8", "mark", 451]]

        stu_iiiyear = [["name : student 9", "mark", 261], ["name : student 10", "mark", 361],
                       ["name : student 11", "mark", 291], ["name : student 12", "mark", 451]]

        stu_ivyear = [["name : student 13", "mark", 261], ["name : student 14", "mark", 361],
                      ["name : student 15", "mark", 291], ["name : student 16", "mark", 451]]

        self.it_database = {"Iyear": stu_iyear, "IIyear": stu_iiyear,
                            "IIIyear": stu_iiiyear, "IVyear": stu_ivyear, "staff": staff, "fees": fees}


class Create_Text_PDF(Record):
    def create_textfile(self, department, record, to_whom):
        print("Create text file")

        print(record)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)

        custom_name = input("Do you want to change file name?")
        if custom_name == "yes":
            custom_file_name = input("Enter your file name: ")
            file_name = custom_file_name
        else:
            file_name = f"{to_whom}_{department}"
        with open(f"{file_name}.txt", "w") as file:
            for row in record:
                s = "".join(map(str, row))
                file.write(s + "\n")
        text_file = open(f"{file_name}.txt", "r")

        for x in text_file:
            pdf.cell(200, 10, txt=x, ln=1, align="C")
        # pdf.output(f"{file_name}.pdf")
        pdf.output(f"{file_name}.pdf")


class Department:
    computer = "Computer Science Department"
    mechanical = "Mechanical Department"
    electronical = "Electronical Communication Engineering Department"
    electrical = "Electrical Electronical Engineering Department "
    information = "Information Technology Engineering Department"


class Display_staff(Department, Record):
    print("Staff detail for Francis Xavier Engineering college")

    def __init__(self):
        department = input("Which department staff detail").lower()

        com_staff = department == "computer"
        mech_staff = department == "mechanical"
        ece_staff = department == "electrical"
        eee_staff = department == "electronical"
        it_staff = department == "information"

        if com_staff:
            print(f"{Display_staff.computer}")
            Display_staff.dep_computer(self)
            com_database = self.com_database
            if "staff" in com_database.keys():
                print("{}".format(com_database["staff"]))
                up_del = input("Update, Delete or Create pdf").lower()
                if up_del == "update":
                    update_staff_detail = Get_staff()
                    update_staff_detail.staff_update(com_database["staff"], department)
                elif up_del == "delete":
                    delete_staff_detail = Delete_staff()
                    delete_staff_detail.delete_staff(com_database["staff"])
                elif up_del == "create pdf":
                    create_pdf = input("Do you want to create pdf?")
                    isyes = create_pdf == "yes"
                    isno = create_pdf == "no"
                    if isyes:
                        pdf = Create_Text_PDF()
                        pdf.create_textfile(f"{department}", com_database["staff"], "staff")
                    elif isno:
                        print(f"Thanks for visting {department}")


            else:
                print(f"Staff record for {Department.computer}", com_database["staff"])
                self.__init__()

        elif mech_staff:
            print(f"{Display_staff.mechanical}")
            Display_staff.dep_mechanical(self)
            mech_database = self.mech_database
            if "staff" in mech_database.keys():
                print("{}".format(mech_database["staff"]))
                up_del = input("Update, Delete or Create pdf").lower()
                if up_del == "update":
                    update_staff_detail = Get_staff()
                    update_staff_detail.staff_update(mech_database["staff"])
                elif up_del == "delete":
                    delete_staff_detail = Delete_staff()
                    delete_staff_detail.delete_staff(self, mech_database["staff"])
                elif up_del == "create pdf":
                    create_pdf = input("Do you want to create pdf?")
                    isyes = create_pdf == "yes"
                    isno = create_pdf == "no"
                    if isyes:
                        pdf = Create_Text_PDF()
                        pdf.create_textfile(f"{department}", mech_database["stafff"], "staff")
                    elif isno:
                        print(f"Thanks for visting {department}")
            else:
                print(f"Staff record for {Department.mechanical}", mech_database["staff"])
                self.__init__()

        elif ece_staff:
            print(f"{Display_staff.electrical}\n Staff Name Add Name\nDelete Staff Name")
            Display_staff.dep_electrical(self)
            ece_database = self.ece_database
            if "staff" in ece_database.keys():
                print("{}".format(ece_database["staff"]))
                up_del = input("Update, Delete or Create pdf").lower()
                if up_del == "update":
                    update_staff_detail = Get_staff()
                    update_staff_detail.staff_update(self, ece_database["staff"])
                elif up_del == "delete":
                    delete_staff_detail = Delete_staff()
                    delete_staff_detail.delete_staff(self, ece_database["staff"])
                elif up_del == "create pdf":
                    create_pdf = input("Do you want to create pdf?")
                    isyes = create_pdf == "yes"
                    isno = create_pdf == "no"
                    if isyes:
                        pdf = Create_Text_PDF()
                        pdf.create_textfile(f"{department}", ece_database["staff"], "staff")
                    elif isno:
                        print(f"Thanks for visting {department}")
            else:
                print(f"Staff record for {Department.electrical}", ece_database["staff"])
                self.__init__()

        elif eee_staff:
            print(f"{Display_staff.electronical}\n Staff Name Add Name\nDelete Staff Name")
            Display_staff.dep_electronical(self)
            eee_database = self.eee_database
            if "staff" in eee_database.keys():
                print("{}".format(eee_database["staff"]))
                up_del = input("Update, Delete or Create pdf").lower()
                if up_del == "update":
                    update_staff_detail = Get_staff()
                    update_staff_detail.staff_update(self, eee_database["staff"])
                elif up_del == "delete":
                    delete_staff_detail = Delete_staff()
                    delete_staff_detail.delete_staff(self, eee_database["staff"])
                elif up_del == "create pdf":
                    create_pdf = input("Do you want to create pdf?")
                    isyes = create_pdf == "yes"
                    isno = create_pdf == "no"
                    if isyes:
                        pdf = Create_Text_PDF()
                        pdf.create_textfile(f"{department}", eee_database["staff"], "staff")
                    elif isno:
                        print(f"Thanks for visting {department}")
            else:
                print(f"Staff record for {Department.electronical}", eee_database["staff"])
                self.__init__()

        elif it_staff:
            print(f"{Display_staff.information}\n Staff Name Add Name\nDelete Staff Name")
            Display_staff.dep_information(self)
            it_database = self.it_database
            if "staff" in it_database.keys():
                print("{}".format(it_database["staff"]))
                up_del = input("Update, Delete or Create pdf").lower()
                if up_del == "update":
                    update_staff_detail = Get_staff()
                    update_staff_detail.staff_update(self, it_database["staff"])
                elif up_del == "delete":
                    delete_staff_detail = Delete_staff()
                    delete_staff_detail.delete_staff(self, it_database["staff"])
                elif up_del == "create pdf":
                    create_pdf = input("Do you want to create pdf?")
                    isyes = create_pdf == "yes"
                    isno = create_pdf == "no"
                    if isyes:
                        pdf = Create_Text_PDF()
                        pdf.create_textfile(f"{department}", it_database["staff"], "staff")
                    elif isno:
                        print(f"Thanks for visting {department}")
            else:
                print(f"Staff record for {Department.information}", it_database["staff"])
                self.__init__()
        else:
            print("Please Select Correct Choose")
            self.__init__()


class Get_staff(Record):
    print("Update Staff detail")

    def staff_update(self, staff_names, department):
        suggestion = input("Do you want to update?").lower()

        is_yes = suggestion == "yes"
        is_no = suggestion == "no"

        if is_yes:
            new_name_lenght = int(input("How many new Staff name you need to add"))
            staff_oldrecord = staff_names
            for i in range(0, new_name_lenght):
                new_staff_name = input("Enter New Staff Name").capitalize()
                staff_oldrecord.append(new_staff_name)
            print(staff_oldrecord)
            create_pdf = input("Do you want to create pdf?")
            isyes = create_pdf == "yes"
            isno = create_pdf == "no"
            if isyes:
                pdf = Create_Text_PDF()
                pdf.create_textfile(f"{department}", staff_oldrecord, "staff")
            elif isno:
                print(f"Thanks for visting {department}")


        elif is_no:
            print("Thank For coming")

        else:
            print("Please select correct things")
            self.staff_update(self, staff_names)


class Delete_staff(Record):

    def delete_staff(self, staff_name, ):
        print("Delete Staff Name for the record")
        delete_staff = input("Do you want to delete Staff Name?").lower()
        is_yes = delete_staff == "yes"
        is_no = delete_staff == "no"
        print(f"Staff record :", staff_name)

        if is_yes:
            delete_staff_name = input("Enter staff name").capitalize()
            print("name: ", delete_staff_name)

            if delete_staff_name in staff_name:
                index = staff_name.index(delete_staff_name)
                delete = staff_name.pop(index)
                print(f"Staff Name deleted {delete}")
            else:
                print(f"{delete_staff_name} Not found in staff record ")
        elif is_no:
            print("Thanks for coming")

        print(staff_name)


class Display_fees(Record):
    def __init__(self):
        print("Fees structure for Francis xavier engineering college")
        department = input("Which department")
        year = input(f"Which year {department} Fees you want?")
        print(year)
        fees_struc = "fees structure"

        com = department == "computer"
        mech = department == "mechanical"
        ece = department == "electrical"
        eee = department == "electronical"
        it = department == "information" or department == "information science"

        if com:
            print(f"{Department.computer} {fees_struc}")
            Display_fees.dep_computer(self)
            com_database = self.com_database
            if "fees" in com_database:
                print("{}".format(com_database["fees"]))
                update_fees = input(f"Do you want to update fees for {department} ?").lower()
                isyes = update_fees == "yes"
                isno = update_fees == "no"
                if isyes:
                    fees = Get_fees()
                    fees.update_fees(com_database["fees"], department)
                elif isno:
                    print(com_database["fees"])
            else:
                print("not working")
            # Display_fees.dep_computer(self, fees_struc, year)
        elif mech:
            print(f"{Department.mechanical} {fees_struc}")
            Display_fees.dep_mechanical(self)
            mech_database = self.mech_database
            if "fees" in mech_database:
                print("{}".format(mech_database["fees"]))
                update_fees = input(f"Do you want to update fees for {department} ?").lower()
                isyes = update_fees == "yes"
                isno = update_fees == "no"
                if isyes:
                    fees = Get_fees()
                    fees.update_fees(mech_database["fees"], department)
                elif isno:
                    print(mech_database["fees"])
            else:
                print("not working")
            # Display_fees.dep_mechanical(self, fees_struc, year)
        elif ece:
            print(f"{Department.electrical} {fees_struc}")
            Display_fees.dep_electrical(self)
            ece_database = self.ece_database
            if "fees" in ece_database:
                print("{}".format(ece_database["fees"]))
                update_fees = input(f"Do you want to update fees for {department} ?").lower()
                isyes = update_fees == "yes"
                isno = update_fees == "no"
                if isyes:
                    fees = Get_fees()
                    fees.update_fees(ece_database["fees"], department)
                elif isno:
                    print(ece_database["fees"])
            else:
                print("not working")
            # Display_fees.dep_electrical(self, fees_struc, year)
        elif eee:
            print(f"{Department.electronical} {fees_struc}")
            Display_fees.dep_electronical(self)
            eee_database = self.eee_database
            if "fees" in eee_database:
                print("{}".format(eee_database["fees"]))
                update_fees = input(f"Do you want to update fees for {department} ?").lower()
                isyes = update_fees == "yes"
                isno = update_fees == "no"
                if isyes:
                    fees = Get_fees()
                    fees.update_fees(eee_database["fees"], department)
                elif isno:
                    print(eee_database["fees"])
            else:
                print("not working")
            # Display_fees.dep_electronical(self, fees_struc, year)
        elif it:
            print(f"{Department.information} {fees_struc}")
            Display_fees.dep_information(self)
            it_database = self.it_database
            if "fees" in it_database:
                print("{}".format(it_database["fees"]))
                update_fees = input(f"Do you want to update fees for {department} ?").lower()
                isyes = update_fees == "yes"
                isno = update_fees == "no"
                if isyes:
                    fees = Get_fees()
                    fees.update_fees(it_database["fees"], department)
                elif isno:
                    print(it_database["fees"])
            else:
                print("not working")
            # Display_fees.dep_information(self, fees_struc, year)
        else:
            print(f"Please select correct department:\n1. {Department.computer}\n2.{Department.mechanical}"
                  f"\n3.{Department.electronical}\n4.{Department.electrical}\n5.{Department.information}")
            self.__init__()


class Get_fees(Record):

    def update_fees(self, fees, department):
        computer = department == {Department.computer} or department == "computer"
        mechanical = department == {Department.mechanical}
        electrical = department == {Department.electrical}
        electronical = department == {Department.electronical}

        if computer:
            print(f"Update fees structure: {Department.computer}")
            year_change = input("Which year value change").capitalize()
            if year_change in fees.keys():
                print(f"year in fees of {Department.computer}")
                change_fees = int(input(f"Enter the fees for {year_change}: "))
                fees.update({f"{year_change}": change_fees})
                print(fees)
                create_pdf = input("Do you want to create pdf?")
                isyes = create_pdf == "yes"
                isno = create_pdf == "no"
                if isyes:
                    pdf = Create_Text_PDF()
                    pdf.create_textfile(f"{department}", fees, "fees")
                elif isno:
                    print(f"Thanks for visting {department}")
            else:
                print(f"Please select the correct year{fees.keys()}")


        elif mechanical:
            print(f"{Department.mechanical}")
            year_change = input("Which year value change")
            if year_change in fees.keys():
                print(f"year in fees of {Department.mechanical}")
                change_fees = int(input(f"Enter the fees for {year_change}: "))
                fees.update({f"{year_change}": change_fees})
                print(fees)
                create_pdf = input("Do you want to create pdf?")
                isyes = create_pdf == "yes"
                isno = create_pdf == "no"
                if isyes:
                    pdf = Create_Text_PDF()
                    pdf.create_textfile(f"{department}", fees, "fees")
                elif isno:
                    print(f"Thanks for visting {department}")
            else:
                print(f"Please select the correct year{fees.keys()}")

        elif electrical:
            print(f"{Department.electrical}")
            year_change = input("Which year value change")
            if year_change in fees.keys():
                print(f"year in fees of {Department.electrical}")
                change_fees = int(input(f"Enter the fees for {year_change}: "))
                fees.update({f"{year_change}": change_fees})
                print(fees)
                create_pdf = input("Do you want to create pdf?")
                isyes = create_pdf == "yes"
                isno = create_pdf == "no"
                if isyes:
                    pdf = Create_Text_PDF()
                    pdf.create_textfile(f"{department}", fees, "fees")
                elif isno:
                    print(f"Thanks for visting {department}")
            else:
                print(f"Please select the correct year{fees.keys()}")

        elif electronical:
            print(f"{Department.electronical}")
            year_change = input("Which year value change")
            if year_change in fees.keys():
                print(f"year in fees of {Department.electronical}")
                change_fees = int(input(f"Enter the fees for {year_change}: "))
                fees.update({f"{year_change}": change_fees})
                print(fees)
                create_pdf = input("Do you want to create pdf?")
                isyes = create_pdf == "yes"
                isno = create_pdf == "no"
                if isyes:
                    pdf = Create_Text_PDF()
                    pdf.create_textfile(f"{department}", fees, "fees")
                elif isno:
                    print(f"Thanks for visting {department}")
            else:
                print(f"Please select the correct year{fees.keys()}")

        else:
            print(f"{Department.information}")
            year_change = input("Which year value change")
            if year_change in fees.keys():
                print(f"year in fees of {Department.information}")
                change_fees = int(input(f"Enter the fees for {year_change}: "))
                fees.update({f"{year_change}": change_fees})
                print(fees)
                create_pdf = input("Do you want to create pdf?")
                isyes = create_pdf == "yes"
                isno = create_pdf == "no"
                if isyes:
                    pdf = Create_Text_PDF()
                    pdf.create_textfile(f"{department}", fees, "fees")
                elif isno:
                    print(f"Thanks for visting {department}")
            else:
                print(f"Please select the correct year{fees.keys()}")


class Create_stu:
    def create_stu(self, dep, record):
        print(f"Welcome to create new student record for {dep}")

        record = record
        data = []

        reg = int(input("Enter student register number: "))
        name = input("Enter student name: ").capitalize()
        mark = int(input("Enter student total mark: "))
        address = input("Enter student address: ").title()
        department = input("Enter student department")
        mobile = int(input("Enter student mobile number: "))
        if int(math.log10(int(mobile)))+1 == 10:
            data.append(f"Mobile: +91 {mobile}")
        else:
            mobile = int(input("Enter student mobile number: "))
            if int(math.log10(int(mobile))) + 1 == 10:
                data.append(f"Mobile: +91 {mobile}")
        if int(math.log10(int(reg)))+1 == 12:
            data.append(f"Register: {reg}")
        else:
            reg = int(input("Enter student register number: "))
            if int(math.log10(int(reg))) + 1 == 12:
                data.append(f"Register: {reg}")
        if int(math.log10(int(mark)))+1 == 3:
            data.append(f"Mark: {mark}")
        else:
            mark = int(input("Enter student total mark: "))
            if int(math.log10(int(mark))) + 1 == 3:
                data.append(f"Mark: {mark}")
        if len(str(name)) > 4:
            data.append(f"Name: {name}")
        else:
            name = input("Enter student name: ").capitalize()
            if len(str(name)) > 4:
                data.append(f"Name: {name}")
        if len(str(address)) >= 10:
            data.append(f"Address: {address}")
        else:
            address = input("Enter student address: ")
            if len(str(address)) >= 10:
                data.append(f"Address: {address}")
        if str(department) == "computer" or str(department) == "information" or str(department) == "mechanical" \
                or str(department) == "electrical" or str(department) == "electrical":

            data.append(f"Department: {department}")
        else:
            department = input("Enter student department")
            if str(department) == "computer" or str(department) == "information" or str(department) == "mechanical" \
                    or str(department) == "electrical" or str(department) == "electrical":
                data.append(f"Department: {department}")

        record.append(f"{reg}: {data}")
        print(record)


class Scholarship:

    def scholarship_student(self, year, database):
        print("Welcome to Scholarship student pannel")
        print(database)
        if year in database:
            print("{}".format(database[year]))
            scholarship_stu_detail = []
            scholar = []
            for element in database[year]:
                print(element)
                for element1 in element:
                    try:
                        if int(element1) >= 400:
                            for first_list in element:
                                for element3 in str(first_list):
                                    if element3 == "n":
                                        scholar.append(str(first_list))
                                        scholar.append(int(element1))
                                        break
                                    break
                    except ValueError:
                        continue

            scholarship_stu_detail.append(scholar)
            print("scholarship student", scholarship_stu_detail)



class Display_Student(Record, Create_stu, Scholarship):
    def __init__(self):
        print("Student Detail")
        dep = input("which departmrnt student record")
        comp = dep == "computer"
        mech = dep == "mechanical"
        ece = dep == "electrical"
        eee = dep == "electronical"
        it = dep == "information" or dep == "information science"

        if comp:
            year_stu = input("Which year student record: ")
            Display_Student.dep_computer(self)
            com_database = self.com_database
            print(com_database)
            if year_stu in com_database.keys():
                stu_record = com_database[year_stu]
                print("{}".format(stu_record))
                new_stu = input(
                    "Do you want to create new student record or create Pdf?\n1. New student"
                    "\n2. create pdf\n3. Scholarship Student\n").lower()
                create_stu = new_stu == "new student"
                org_stu = new_stu == "create pdf"
                scholorship_stu = "scholarship student"
                if create_stu:
                    year = input("which year: ")

                    Iyear = year == "Iyear"
                    IIyear = year == "IIyear"
                    IIIyear = year == "IIIyear"
                    IVyear = year == "IVyear"

                    if Iyear:
                        if year in com_database.keys():
                            Display_Student.create_stu(self, Department.computer, com_database[year])
                        else:
                            print("Not working")
                    elif IIyear:
                        if year in com_database.keys():
                            Display_Student.create_stu(self, Department.computer, com_database[year])
                        else:
                            print("Not working")
                    elif IIIyear:
                        if year in com_database.keys():
                            Display_Student.create_stu(self, Department.computer, com_database[year])
                        else:
                            print("Not working")
                    elif IVyear:
                        if year in com_database.keys():
                            Display_Student.create_stu(self, Department.computer, com_database[year])
                        else:
                            print("Not working")
                    else:
                        print("Plese select correct year")
                elif org_stu:
                    pdf = Create_Text_PDF()
                    pdf.create_textfile(f"{Department.computer}", com_database[year_stu], "student")
                elif scholorship_stu:
                    Display_Student.scholarship_student(self, year_stu, com_database)
                else:
                    print("Please select the one")

            else:
                print("not working")

        elif mech:
            year_stu = input("Which year student record: ")
            Display_Student.dep_mechanical(self)
            mech_database = self.mech_database
            print(mech_database)
            if year_stu in mech_database.keys():
                stu_record = mech_database[year_stu]
                print("{}".format(stu_record))
                new_stu = input(
                    "Do you want to create new student record or create Pdf?\n1. New student"
                    "\n2. create pdf\n3. Scholarship Student\n").lower()
                create_stu = new_stu == "new student"
                org_stu = new_stu == "create pdf"
                scholorship_stu = "scholarship student"
                if create_stu:
                    year = input("which year: ").capitalize()

                    Iyear = year == "Iyear"
                    IIyear = year == "II year"
                    IIIyear = year == "III year"
                    IVyear = year == "IV year"

                    if Iyear:
                        if year in mech_database.keys():
                            Display_Student.create_stu(self, Department.mechanical, mech_database[year])
                        else:
                            print("Not working")
                    elif IIyear:
                        if year in mech_database.keys():
                            Display_Student.create_stu(self, Department.mechanical, mech_database[year])
                        else:
                            print("Not working")
                    elif IIIyear:
                        if year in mech_database.keys():
                            Display_Student.create_stu(self, Department.mechanical, mech_database[year])
                        else:
                            print("Not working")
                    elif IVyear:
                        if year in mech_database.keys():
                            Display_Student.create_stu(self, Department.mechanical, mech_database[year])
                        else:
                            print("Not working")
                    else:
                        print("Plese select correct year")
                elif org_stu:
                    pdf = Create_Text_PDF()
                    pdf.create_textfile(f"{Department.mechanical}", mech_database, "student")
                elif scholorship_stu:
                    Display_Student.scholarship_student(self, year_stu, mech_database)
                else:
                    print("Please select the one")

            else:
                print("not working")

        elif ece:
            year_stu = input("Which year student record: ")
            Display_Student.dep_electrical(self)
            ece_database = self.ece_database
            print(ece_database)
            if year_stu in ece_database.keys():
                stu_record = ece_database[year_stu]
                print("{}".format(stu_record))
                new_stu = input(
                    "Do you want to create new student record or create Pdf?\n1. New student"
                    "\n2. create pdf\n3. Scholarship Student\n").lower()
                create_stu = new_stu == "new student"
                org_stu = new_stu == "create pdf"
                scholorship_stu = "scholarship student"
                if create_stu:
                    year = input("which year: ").capitalize()

                    Iyear = year == "Iyear"
                    IIyear = year == "II year"
                    IIIyear = year == "III year"
                    IVyear = year == "IV year"

                    if Iyear:
                        if year in ece_database.keys():
                            Display_Student.create_stu(self, Department.electrical, ece_database[year])
                        else:
                            print("Not working")
                    elif IIyear:
                        if year in ece_database.keys():
                            Display_Student.create_stu(self, Department.electrical, ece_database[year])
                        else:
                            print("Not working")
                    elif IIIyear:
                        if year in ece_database.keys():
                            Display_Student.create_stu(self, Department.electrical, ece_database[year])
                        else:
                            print("Not working")
                    elif IVyear:
                        if year in ece_database.keys():
                            Display_Student.create_stu(self, Department.electrical, ece_database[year])
                        else:
                            print("Not working")
                    else:
                        print("Plese select correct year")
                elif org_stu:
                    pdf = Create_Text_PDF()
                    pdf.create_textfile(f"{Department.electrical}", ece_database, "student")
                elif scholorship_stu:
                    Display_Student.scholarship_student(self, year_stu, ece_database)
                else:
                    print("Please select the one")

            else:
                print("not working")

        elif eee:
            year_stu = input("Which year student record: ")
            Display_Student.dep_electronical()
            eee_database = self.eee_database
            print(eee_database)
            if year_stu in eee_database.keys():
                stu_record = eee_database[year_stu]
                print("{}".format(stu_record))
                new_stu = input(
                    "Do you want to create new student record or create Pdf?\n1. New student"
                    "\n2. create pdf\n3. Scholarship Student\n").lower()
                create_stu = new_stu == "new student"
                org_stu = new_stu == "create pdf"
                scholorship_stu = "scholarship student"
                if create_stu:
                    year = input("which year: ").capitalize()

                    Iyear = year == "Iyear"
                    IIyear = year == "II year"
                    IIIyear = year == "III year"
                    IVyear = year == "IV year"

                    if Iyear:
                        if year in eee_database.keys():
                            Display_Student.create_stu(self, Department.electronical, eee_database[year])
                        else:
                            print("Not working")
                    elif IIyear:
                        if year in eee_database.keys():
                            Display_Student.create_stu(self, Department.electronical, eee_database[year])
                        else:
                            print("Not working")
                    elif IIIyear:
                        if year in eee_database.keys():
                            Display_Student.create_stu(self, Department.electronical, eee_database[year])
                        else:
                            print("Not working")
                    elif IVyear:
                        if year in eee_database.keys():
                            Display_Student.create_stu(self, Department.electronical, eee_database[year])
                        else:
                            print("Not working")
                    else:
                        print("Plese select correct year")
                elif org_stu:
                    pdf = Create_Text_PDF()
                    pdf.create_textfile(f"{Department.electronical}", eee_database, "student")
                elif scholorship_stu:
                    Display_Student.scholarship_student(self, year_stu, eee_database)
                else:
                    print("Please select the one")

            else:
                print("not working")

        elif it:
            year_stu = input("Which year student record: ")
            Display_Student.dep_information(self)
            it_database = self.it_database
            print(it_database)
            if year_stu in it_database.keys():
                stu_record = it_database[year_stu]
                print("{}".format(stu_record))
                new_stu = input(
                    "Do you want to create new student record or create Pdf?\n1. New student"
                    "\n2. create pdf\n3. Scholarship Student\n").lower()
                create_stu = new_stu == "new student"
                org_stu = new_stu == "create pdf"
                scholorship_stu = "scholarship student"
                if create_stu:
                    year = input("which year: ").capitalize()

                    Iyear = year == "Iyear"
                    IIyear = year == "II year"
                    IIIyear = year == "III year"
                    IVyear = year == "IV year"

                    if Iyear:
                        if year in it_database.keys():
                            Display_Student.create_stu(self, Department.information, it_database[year])
                        else:
                            print("Not working")
                    elif IIyear:
                        if year in it_database.keys():
                            Display_Student.create_stu(self, Department.information, it_database[year])
                        else:
                            print("Not working")
                    elif IIIyear:
                        if year in it_database.keys():
                            Display_Student.create_stu(self, Department.information, it_database[year])
                        else:
                            print("Not working")
                    elif IVyear:
                        if year in it_database.keys():
                            Display_Student.create_stu(self, Department.information, it_database[year])
                        else:
                            print("Not working")
                    else:
                        print("Plese select correct year")
                elif org_stu:
                    pdf = Create_Text_PDF()
                    pdf.create_textfile(f"{Department.information}", it_database, "student")
                elif scholorship_stu:
                    Display_Student.scholarship_student(self, year_stu, it_database)
                else:
                    print("Please select the one")

            else:
                print("not working")

        else:
            print("Please select the correct department")
            self.__init__()


if __name__ == "__main__":
    dep = Department
    print(f"Welcome to Franics Xavier Engineering College\nDepartment:\n1. {dep.computer}\n2. {dep.mechanical}"
          f"\n3. {dep.electronical}\n4. {dep.electrical}\n5. {dep.information}\nThese are the service we provide?"
          "\nStudent detail\nStaff detail\nFees detail")

    service_provide = input("Please select correct one").lower()

    student_detail = service_provide == "student detail"
    staff_detail = service_provide == "staff detail"
    fees_detail = service_provide == "fees detail"

    if student_detail:
        stu = Display_Student()
    elif staff_detail:
        staff = Display_staff()
    elif fees_detail:
        fees = Display_fees()
    else:
        print("Please correct service")
