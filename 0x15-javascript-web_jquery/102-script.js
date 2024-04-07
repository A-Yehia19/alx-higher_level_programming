window.onload = function() {
    $('INPUT#btn_translate').click(function() {
        fetch($('INPUT#language_code').val());
    });
}

function fetch(lang){
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`, function(data) {
        $('DIV#hello').html(data.hello);
    });
}
