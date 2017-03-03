/**
 * Created by housh on 2017/2/21.
 */
$(document).ready(function () {
    $("#id_emergency").on("click", function () {
        if($("#id_emergency").is(":checked")){
                $("#id_emergency_wrap").after("<div id='id_verify_wrap' class='pure-control-group'><label for='verify-code/'></label><input type='text'" +
                    " name='verify-code'><img src='get-verify-code/" + $.now() + "/' alt=''></div>");
        }else {
            $("#id_verify_wrap").remove();
        }
    });
    $("#id_submit").click(function () {
        var name = $("#id_name").val();
        var message = $("#id_message").val();
        var emergency = false;
        if($("#id_emergency").is(":checked")){
            emergency = true
        }
        var send_message_url = "leave-message/";
        var datas = $("#id_leavemessage_form").serializeArray();
        $.ajax({
            method: "POST",
            url: send_message_url,
            data: datas,
            success: function () {
                $("textarea").val("").focus();
                $("#id_emergency").click();
                var prepend_html = "<header class=\"post-header\"><img class=\"post-avatar\" src=\"http://random-avat" +
                    "ar.cloudist.cc/{{ message.name }}.png?size=60\" alt=\"\"> <h2 class=\"post-title\">" +
                    name + "</h2> <p class=\"post-meta\">刚刚</p> </header> <div class=\"post-description\"> <p>" +
                     message + "</p></div>";
                $(".post").prepend(prepend_html);
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
