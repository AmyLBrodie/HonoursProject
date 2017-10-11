from .models import Student, StudentInfo, ContactDetails, EmploymentInfo, EmploymentHistory, WeekendPlacement

from rest_framework import serializers

class ContactDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactDetails
        fields = ('contact')

class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = ('class_no', 'grad_or_student', 'year', 'dropout')

class EmploymentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentInfo
        fields = ('internship', 'current_employment')

class EmploymentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentHistory
        fields = ('employment')

class WeekendPlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeekendPlacement
        fields = ('placement')

class StudentSerializer(serializers.ModelSerializer):

    contact_details = ContactDetailsSerializer(many=True)
    student_info = StudentInfoSerializer(many=True)
    employment_info = EmploymentInfoSerializer(many=True)
    employment_history = EmploymentHistorySerializer(many=True)
    weekend_placement = WeekendPlacementSerializer(many=True)

    class Meta:
        model = Student
        fields = ('student_id', 'name', 'id_no', 'deceased', 'contact_details', 'student_info', 'employment_info', 'employment_history', 'weekend_placement')

    def create(self, validated_data):
        contact_details_data = validated_data.pop('contact_details')
        student_info_data = validated_data.pop('student_info')
        employment_info_data = validated_data.pop('employment_info')
        employment_history_data = validated_data.pop('employment_history')
        weekend_placement_data = validated_data.pop('weekend_placement')
        student = Student.objects.create(**validated_data)
        for contact_detail_data in contact_details_data:
            ContactDetails.objects.create(student=student, **contact_detail_data)
        for info_data in student_info_data:
            StudentInfo.objects.create(student=student, **info_data)
        for employ_info_data in employment_info_data:
            EmploymentInfo.objects.create(student=student, **employ_info_data)
        for history_data in employment_history_data:
            EmploymentHistory.objects.create(student=student, **history_data)
        for placement_data in weekend_placement_data:
            WeekendPlacement.objects.create(student=student, **placement_data)
        return student
