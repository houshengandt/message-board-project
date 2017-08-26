# 留言板应用

## 演示地址

[htttp:www.zhiyuc.me/workshop/messageboard](htttp:www.zhiyuc.me/workshop/messageboard)

## 为了让发送邮件生效

在settings中设置

    EMAIL_HOST = 'smtp.ym.163.com'    // 你的邮件服务
    EMAIL_PORT = '25'
    EMAIL_HOST_USER = 'admin@admin.com'     // 你的邮件账号
    EMAIL_HOST_PASSWORD = '******'      // 密码

视图中的代码

     email = request.POST['email'] or ''
        message = request.POST['message']
        if emergency:
            if verify_code and verify_code == request.session.get('django-verify-code').lower():
                new_message = Message(name=name, email=email, message=message)
                new_message.emergency = True
                try:
                    send_mail('新的紧急留言 来自' + name,
                              message,
                              'admin@admin.com',
                              ['zhiyuc@***.com'])       # 要发送到的邮箱
                except Exception as e:
                    pass

