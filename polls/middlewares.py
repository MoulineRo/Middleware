from datetime import datetime

from polls.models import Middlewares


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        now = datetime.now()
        tim = now.strftime("%d.%m.%Y %H:%M")
        if request.method == 'GET':
            if request.path:
                file = open("middlewares.txt", "a+")
                file.write(str(request.path) + ' ' + str(request.method) + ' ' + tim + '\n')
                file.close()
                Middlewares.objects.create(path=request.path, method=request.method, times=tim)
        if request.method == 'POST':
            if request.path:
                file = open("middlewares.txt", "a+")
                file.write(str(request.path) + ' ' + str(request.method) + ' ' + tim + '\n')
                file.close()
                Middlewares.objects.create(path=request.path, method=request.method, times=tim)
        response = self.get_response(request)

        return response
