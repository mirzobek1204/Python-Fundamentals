def build_class_roster(enrollment_data):
    class_roster={}
    for student in enrollment_data:
        class_roster[student['student_id']]=student['full_name']
    return class_roster
def verify_attendance(roster_dict, sign_in_ids):
    roster_ids=set(roster_dict.keys())
    signed_ids=set(sign_in_ids)
    absent_students=roster_ids - signed_ids
    unregistered_students=signed_ids - roster_ids
    return absent_students, unregistered_students

def generate_absence_report(roster_dict, absent_ids):
    report = []
    for student_id in absent_ids:
       report.append(f"ABSENT: {roster_dict[student_id]} (ID: {student_id})")
    report.sort(key=lambda x: x.split(": ")[1])
    return report
enrollment = [
    {'student_id': 501, 'full_name': "Sam Porter"},
    {'student_id': 502, 'full_name': "Fragile Express"},
    {'student_id': 503, 'full_name': "Die Hardman"}
]

signed_in=[501, 503, 999]
roster=build_class_roster(enrollment)
attendance_result = verify_attendance(roster, signed_in)
absent_ids = attendance_result[0]
unregistered_ids = attendance_result[1]
report=generate_absence_report(roster, absent_ids)
print(f"Absent IDs: {absent_ids}")
print(f"Unregistered IDs: {unregistered_ids}")
print(f"Report: {report}")
