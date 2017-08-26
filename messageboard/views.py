from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import ListView
from django.core.exceptions import ValidationError
from django.core.mail import send_mail

from .models import Message
from .verify_code import VerifyCode


class IndexView(ListView):
    template_name = 'messageboard/message_board.html'
    context_object_name = 'messages'

    def get_queryset(self):
        messages = Message.objects.all().order_by('-pk')[:10]
        return messages


def leave_message(request):
    if request.method == 'POST':
        # print(request.POST)
        # print(request.session.get('django-verify-code'))
        name = request.POST['name']
        emergency = request.POST.get('emergency')
        verify_code = request.POST.get('verify-code')
        email = request.POST['email'] or ''
        message = request.POST['message']
        if emergency:
            if verify_code and verify_code == request.session.get('django-verify-code').lower():
                new_message = Message(name=name, email=email, message=message)
                new_message.emergency = True
                try:
                    send_mail('新的紧急留言 来自' + name,
                              message,
                              'admin@zhiyuc.me',
                              ['zhiyuc@outlook.com'])
                except Exception as e:
                    # print(e)
                    pass
                try:
                    new_message.save()
                except ValidationError as e:
                    return HttpResponse("名字和信息不能为空", status=400)
                return HttpResponse()
            else:
                return HttpResponse("验证码错误", status=400)
        else:
            new_message = Message(name=name, email=email, message=message)
            try:
                new_message.save()
            except ValidationError as e:
                return HttpResponse("名字和信息不能为空", status=400)
            return HttpResponse()
    if request.method == 'GET':
        return HttpResponse(status=405)


def get_verify_code(request):
    verify_code = VerifyCode()
    request.session['django-verify-code'] = verify_code.code
    image = verify_code.verify_code_image.getvalue()
    verify_code.verify_code_image.close()
    return HttpResponse(image, 'image/gif')


