$(document).ready(function () {
    function hello () {
        $('DIV#hello').empty();
        const lan = $('INPUT#language_code').val();
        $.ajax({
            type: 'GET',
            url: 'https://fourtonfish.com/hellosalut/?lang=' + lan,
            success: function (data) {
                $('DIV#hello').append(data.hello);
            }
        });
    }
    $('INPUT#btn_translate').click(function () {
        hello();
    });
    $('INPUT#language_code').key(function (e) {
        const key = e.which;
        if (key === 13) {
            hello();
        }
    });
});