const addAlertDismissListener = () => {
    let dismissButton = $('.form-alert-dismiss-button')
    dismissButton.click(
        function () {$('.form-alert-container').hide()}
    )
}

if ($('.form-alert-dismiss-button')) {
    addAlertDismissListener()
}

window.onload = () => {
    $('.basket-container').on('click', 'input[type="number"]', function () {
        let t_href = event.target;
        console.log(t_href.name); // basket id
        console.log(t_href.value); // basket quantity

        $.ajax({
            url: "/baskets/edit/" + t_href.name + "/" + t_href.value + "/",
            success: function (data) {
                $('.basket-container').html(data.result);
            }
        });
        event.preventDefault();
    });
}
