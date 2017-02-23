from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import ListView
from django.core.exceptions import ValidationError
from django.core.mail import send_mail

from .models import Message


class IndexView(ListView):
    template_name = 'messageboard/index.html'
    context_object_name = 'messages'

    def get_queryset(self):
        messages = Message.objects.all().order_by('-pk')[:10]
        return messages


def leave_message(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST['name']
        emergency = request.POST.get('emergency')
        email = request.POST['email'] or ''
        message = request.POST['message']
        new_message = Message(name=name, email=email, message=message)
        if emergency:
            new_message.emergency = True
            try:
                send_mail('新的紧急留言 来自' + name,
                          message,
                          'admin@zhiyuc.me',
                          ['zhiyuc@outlookcom'])
            except Exception as e:
                print(e)
        try:
            new_message.save()
        except ValidationError as e:
            return HttpResponse("名字和信息不能为空", status=400)
        return HttpResponse()
    if request.method == 'GET':
        return HttpResponse(status=405)



