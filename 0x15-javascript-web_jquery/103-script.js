window.onload = function() {
    $('INPUT#btn_translate').click(function() {
        fetch($('INPUT#language_code').val());
    });

    $('INPUT#language_code').keypress(function(key) {
        if (key.which === 13) {
            fetch($('INPUT#language_code').val());
        }
    });
}

function fetch(lang){
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`, function(data) {
        $('DIV#hello').html(data.hello);
    });
}
