console.log("Hello")


function handleCredentialResponse(response){
    let csrftoken =  $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        type:'POST',
        url: '/onboarding/',
        headers: {'X-CSRFToken': csrftoken},
        data:response,
        success:function(response){
            if(response.status === true){
                iziToast.success({
                        position: 'topRight',
                        message: response.message,

                });
                location.reload();
            }else{
                iziToast.error({
                        position: 'topRight',
                        message: "Please Use Your @juitsolan.in Email!!",
                });
            }

        },
        error: function(response){
            iziToast.error({
                        position: 'topRight',
                        message: "Please Use Your @juitsolan.in Email!!",
            });
        }
    });
}
