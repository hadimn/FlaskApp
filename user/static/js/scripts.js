

$("form[name=signup_form").submit(function (e) {
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/signup",
        type: "POST",
        data: data,
        dataType: "json",
        success: function (resp) {
            window.location.href = "/dashboard/";
        },
        error: function (resp) {
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    })
    e.preventDefault();
})

$("form[name=login_form").submit(function (e) {
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/login",
        type: "POST",
        data: data,
        dataType: "json",
        success: function (resp) {
            window.location.href = "/";
        },
        error: function (resp) {
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    })

    e.preventDefault();
})

$("form[name=scrape-form").submit(function (e) {
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/scrape",
        type: "POST",
        data: data,
        dataType: "json",
        success: function (resp) {
            window.location.href = "/tweets";
        },
        error: function (resp) {
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    })
    e.preventDefault();
})

$("form[name=filter-form").submit(function (e) {
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/myTweets",
        type: "POST",
        data: data,
        dataType: "json",
        success: function (resp) {
            window.location.href = "/tweets/filter";
        },
        error: function (resp) {
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    })
    e.preventDefault();
})


function showMe(box1=undefined,box2=undefined,name) {
    var chboxs = document.querySelectorAll(name)
    var vis = "none";
    if(box1!=undefined){
        for (var i = 0; i < chboxs.length; i++) {
            if (chboxs[i].checked) {
                vis = "block";
                break;
            }
        }
        document.getElementById(box1).style.display = vis;
    }
    if(box2!=undefined){
        for (var i = 0; i < chboxs.length; i++) {
            if (chboxs[i].checked) {
                vis = "card d-inline-block";
                break;
            }
        }
        document.getElementById(box2).className = vis;
    }
}