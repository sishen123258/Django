from django.http import HttpResponse

from TestModel.models import Test
from TestModel.models import Test2

def testdb(request):
	test1 = Test(name='w3cschool.cc')
	test1.save()
	test2 = Test2(name='Tong')
	test2.save()
	return HttpResponse("<p>Success</p>")