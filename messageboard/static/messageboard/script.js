/**
 * Created by housh on 2017/2/21.
 */
$(document).ready(function () {
    $("#id_submit").click(function () {
        var name = $("#id_name").val();
        var message = $("#id_message").val();
        var emergency = false;
        if($("#id_emergency").is(":checked")){
            emergency = true
        }
        var send_message_url = "leave-message/";
        var datas = $("#id_leavemessage_form").serializeArray();
        console.log(datas)
        $.ajax({
            method: "POST",
            url: send_message_url,
            data: datas,
            success: function () {
                $("textarea").val("").focus();
                var prepend_html = "<div class=\"message-item pure-g\"><div class=\"avatar pure-u-3-24\">" +
                    "<img src=\'http://random-avatar.cloudist.cc/{{ message.name }}.png?size=60\' alt=\"\">" +
                    "</div><div class=\"pure-u-3-24\"><h4 class=\"post-name\">" + name +
                    "</h4><h5 class=\"post-time\">" + "刚刚" + "</h5></div><div class=\"pure-u-18-24\"><p>"
                    + message + "</p></div></div>";
                $(".message-list").prepend(prepend_html);
            },
            statusCode: {
                400: function (xhr) {
                    if(name==""){
                        $("#id_name").addClass("invalid-input");
                    }
                    if(message==""){
                        $("#id_message").addClass("invalid-input");
                    }
                    alert(xhr.responseText);
                }
            }
        });

    });
    $("#id_name, #id_message").focus(function () {
        $(this).removeClass("invalid-input");
    })

});
