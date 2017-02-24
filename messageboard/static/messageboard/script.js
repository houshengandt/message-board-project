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
