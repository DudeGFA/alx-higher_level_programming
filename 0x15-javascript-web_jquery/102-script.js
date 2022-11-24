$(document).ready(function () {
    $('INPUT#btn_translate').click(function () {
        $('DIV#hello').empty();
        const lan = $('INPUT#language_code').val();
        $.ajax({
            type: 'GET',
            url: 'https://fourtonfish.com/hellosalut/?lang=' + lan,
            success: function (data) {
                $('DIV#hello').append(data.hello)
            }
        })
    })
})