"""
Advanced Student Management System using Linked List
A comprehensive implementation of linked list operations for student records
"""

class StudentNode:
    """
    A node class representing a student in the linked list
    Each node contains student information and a reference to the next student
    """
    def __init__(self, name, father_name, roll_no, marks, grade):
        self.name = name
        self.father_name = father_name
        self.roll_no = roll_no
        self.marks = marks
        self.grade = grade
        self.next = None

    def __str__(self):
        """String representation of a student node"""
        return (f"Student: {self.name} | Roll No: {self.roll_no} | "
                f"Marks: {self.marks} | Grade: {self.grade} | "
                f"Father: {self.father_name}")

class StudentLinkedList:
    """
    A comprehensive linked list implementation for student management
    Supports CRUD operations, analytics, and various search functionalities
    """
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_student(self, name, father_name, roll_no, marks, grade):
        """Insert a new student at the end of the list"""
        new_student = StudentNode(name, father_name, roll_no, marks, grade)
        
        if self.head is None:
            self.head = new_student
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_student
        
        self.size += 1
        print(f"✅ Student {name} added successfully!")

    def display_all_students(self):
        """Display all students in the list"""
        if self.head is None:
            print("📭 No students in the database")
            return
        
        print("\n" + "="*80)
        print("🎓 STUDENT DATABASE".center(80))
        print("="*80)
        
        current = self.head
        index = 1
        while current is not None:
            print(f"{index}. {current}")
            current = current.next
            index += 1
        print("="*80)

    def search_by_partial_name(self, search_term):
        """Search students by partial name match (case-insensitive)"""
        if self.head is None:
            print("📭 No students to search")
            return
        
        found = False
        current = self.head
        search_term = search_term.lower()
        
        print(f"\n🔍 Searching for '{search_term}':")
        print("-" * 50)
        
        while current is not None:
            if search_term in current.name.lower():
                print(f"✅ Found: {current.name} (Roll No: {current.roll_no}, Marks: {current.marks})")
                found = True
            current = current.next
        
        if not found:
            print("❌ No matching students found")

    def search_by_exact_name(self, name):
        """Search for student by exact name match (case-insensitive)"""
        if self.head is None:
            print("📭 No students to search")
            return
        
        found = False
        current = self.head
        name = name.lower()
        
        while current is not None:
            if current.name.lower() == name:
                print(f"\n🎯 Exact match found:")
                print(f"   Name: {current.name}")
                print(f"   Roll No: {current.roll_no}")
                print(f"   Marks: {current.marks}")
                print(f"   Grade: {current.grade}")
                print(f"   Father's Name: {current.father_name}")
                found = True
                break
            current = current.next
        
        if not found:
            print(f"❌ Student '{name}' not found")

    def search_by_roll_no(self, roll_no):
        """Search for student by roll number"""
        if self.head is None:
            print("📭 No students to search")
            return
        
        current = self.head
        while current is not None:
            if current.roll_no == roll_no:
                print(f"\n🎯 Student found with Roll No {roll_no}:")
                print(f"   Name: {current.name}")
                print(f"   Marks: {current.marks}")
                print(f"   Grade: {current.grade}")
                return current
            current = current.next
        
        print(f"❌ No student found with Roll No {roll_no}")
        return None

    def calculate_average_marks(self):
        """Calculate and return the average marks of all students"""
        if self.head is None:
            return 0
        
        total = 0
        current = self.head
        while current is not None:
            total += current.marks
            current = current.next
        
        return total / self.size

    def find_highest_marks(self):
        """Find and return the highest marks"""
        if self.head is None:
            return 0
        
        highest = 0
        current = self.head
        while current is not None:
            if current.marks > highest:
                highest = current.marks
            current = current.next
        
        return highest

    def count_students(self):
        """Return the total number of students"""
        return self.size

    def get_students_by_grade(self, grade):
        """Get all students with a specific grade"""
        if self.head is None:
            print("📭 No students in the database")
            return
        
        found = False
        current = self.head
        print(f"\n📊 Students with grade '{grade}':")
        print("-" * 40)
        
        while current is not None:
            if current.grade.upper() == grade.upper():
                print(f"✅ {current.name} - Marks: {current.marks}")
                found = True
            current = current.next
        
        if not found:
            print(f"❌ No students found with grade '{grade}'")

    def delete_student(self, roll_no):
        """Delete a student by roll number"""
        if self.head is None:
            print("📭 No students to delete")
            return
        
        # If head node needs to be deleted
        if self.head.roll_no == roll_no:
            deleted_student = self.head
            self.head = self.head.next
            self.size -= 1
            print(f"🗑️ Student {deleted_student.name} deleted successfully!")
            return
        
        # Search for the student to delete
        current = self.head
        while current.next is not None:
            if current.next.roll_no == roll_no:
                deleted_student = current.next
                current.next = current.next.next
                self.size -= 1
                print(f"🗑️ Student {deleted_student.name} deleted successfully!")
                return
            current = current.next
        
        print(f"❌ No student found with Roll No {roll_no}")

    def get_class_statistics(self):
        """Display comprehensive class statistics"""
        if self.head is None:
            print("📭 No students for statistics")
            return
        
        total = 0
        highest = 0
        lowest = float('inf')
        grade_distribution = {}
        
        current = self.head
        while current is not None:
            total += current.marks
            highest = max(highest, current.marks)
            lowest = min(lowest, current.marks)
            
            # Grade distribution
            grade = current.grade.upper()
            grade_distribution[grade] = grade_distribution.get(grade, 0) + 1
            
            current = current.next
        
        average = total / self.size
        
        print("\n📈 CLASS STATISTICS:")
        print("=" * 40)
        print(f"Total Students: {self.size}")
        print(f"Average Marks: {average:.2f}")
        print(f"Highest Marks: {highest}")
        print(f"Lowest Marks: {lowest}")
        print(f"\n📊 Grade Distribution:")
        for grade, count in grade_distribution.items():
            print(f"   {grade}: {count} student(s)")

# Example usage and demonstration
def main():
    """Main function to demonstrate the Student Management System"""
    print("🎓 STUDENT MANAGEMENT SYSTEM USING LINKED LIST")
    print("=" * 60)
    
    # Create student database
    database = StudentLinkedList()
    
    # Add sample students
    database.insert_student("Fatir", "M.Kausar", 40208, 900, "A")
    database.insert_student("Shoaib", "M.Ali", 40209, 950, "A+")
    database.insert_student("Mirza", "M.Alyan", 40210, 1000, "A+")
    database.insert_student("M.Faraz", "Jimmy", 40211, 1100, "B")
    database.insert_student("Fahad Ali", "Mr.Random", 40212, 1000, "A+")
    
    # Display all students
    database.display_all_students()
    
    # Demonstrate search functionalities
    database.search_by_partial_name("fa")
    database.search_by_exact_name("fatir")
    database.search_by_roll_no(40210)
    
    # Demonstrate analytics
    database.get_class_statistics()
    database.get_students_by_grade("A+")
    
    # Demonstrate deletion
    database.delete_student(40208)
    database.display_all_students()
    
# if file runs directly(i.e, without importing), this will be true
if __name__ == "__main__":
    main()