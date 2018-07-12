//渲染表格数据函数
function getdatalist(i, admin_class_detail,  urls) {
    var data = {};
    $('.col-lg-2 .form-control').each(function () {
        data[$(this).attr('name')] = $(this).find("option:selected").val();
    });
    data['page'] = i;
    data['admin_class_detail'] = admin_class_detail;
    data['ordername'] = ordername;
    $.ajax({
        url: urls,
        type: "GET",
        data: data,
        success: function (data) {
            $("tbody").html(data);
        },
        error: function (data) {
            console.log(data);
        },
    });
};