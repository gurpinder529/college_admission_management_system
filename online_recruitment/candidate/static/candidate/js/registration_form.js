$(document).ready(function (){
    $('#registration_form').on('submit', function(e){
        e.preventDeafault();
        var form={
            'name' : $('[name=name]').val(),
            'email' : $('[name=email]').val(),
            'url' : $('[name=url]').val(),
            'gender' : $('[name=gender]').val(),
            'csrfmiddlewaretoken' : $('[name=csrfmiddlewaretoken]').val(),
        }
        console.log(form)

        $.ajax({
            url: 'http://127.0.0.1:8000/registration_form',
            type: 'post',
            data: form,
            cache: false,
            success: function(response){
                if (response.success){
                    console.log('success')
                }
                else{
                    console.log('failed')
                }
            }
        })
    })
})