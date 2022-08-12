from backend.apps.school.models import Student


def get_search(request):
    query_params = request.GET
    search_word = query_params.get('search_word')
    if search_word:
        students = Student.objects.filter(first_name__icontains=search_word) | \
                   Student.objects.filter(last_name__icontains=search_word) | \
                   Student.objects.filter(middle_name__icontains=search_word)
    else:
        students = Student.objects.all()
    return {'students': students}
