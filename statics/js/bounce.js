$(function () {
    //注册新增数据库链接的事件
     $("#btn_create").click(function () {
        //取表格的选中行数据
        // var arrselections = $("#tb_departments").bootstrapTable('getSelections');
        // if (arrselections.length <= 0) {
        //     toastr.warning('请选择有效数据');
        //     return;
        // }
        var message = `<div class="input-group"><input type="text" id="name" class="form-control" placeholder="连接名称" aria-describedby="basic-addon1"></div>` +
        `<div class="input-group"><input type="text" id="host" class="form-control" placeholder="数据库地址" aria-describedby="basic-addon2"></div>` +
        `<div class="input-group"><input type="text" id= 'port' class="form-control" placeholder="数据库端口" aria-describedby="basic-addon3"></div>` +
        `<div class="input-group"><input type="text" id="user" class="form-control" placeholder="用户名" aria-describedby="basic-addon4"></div>` +
        `<div class="input-group"><input type="text" id="password" class="form-control" placeholder="密码" aria-describedby="basic-addon5"></div>` +
        `<div class="input-group"><input type="text" id='db' class="form-control" placeholder="数据库名称" aria-describedby="basic-addon6"></div>` +
        `<div class="input-group"><input type="text" class="form-control" placeholder="字符集" aria-describedby="basic-addon7" value="utf8"></div>`
        ;
        Ewin.confirm({ message: message, width: 400}).on(function (e) {
            if (!e) {
                return;
            }
            var data = {
                'name': $('#name').val(),
                'host': $('#host').val(),
                'port': $('#port').val(),
                'user': $('#user').val(),
                'password': $('#password').val(),
                'db': $('#db').val(),
                'charset': 'utf8',
            };
            toastr.options = {
                closeButton: false,
                debug: false,
                progressBar: false,
                positionClass: "toast-top-center",
                onclick: null,
                showDuration: "300",
                hideDuration: "1000",
                timeOut: "2000",
                extendedTimeOut: "1000",
                showEasing: "swing",
                hideEasing: "linear",
                showMethod: "fadeIn",
                hideMethod: "fadeOut"
            };
            if ($('#name').val() == '' || $('#host').val() == '' || $('#port').val() == '' || $('#user').val() == '' || $('#password').val() == '' || $('#db').val() == '') {
                toastr.warning('数据不能为空！');
            }
            else {
                $.ajax({
                    url: "/data_center/create_data/",
                    type: "POST",
                    data: data,
                    success: function (data,) {
                        if (data == "数据库连接创建成功！") {
                            toastr.success(data);
                            setTimeout(function (){window.location.reload()}, 2000);
                        }
                        else {
                            toastr.warning(data);
                        }
                    },
                    error: function () {
                        toastr.error('Error');
                    },
                    complete: function () {

                    }

                });
            }
        });
    });

    //注册修改数据库链接事件
    $("a#btn_update").click(function () {
        //取表格的选中行数据
        // var arrselections = $("#tb_departments").bootstrapTable('getSelections');
        // if (arrselections.length <= 0) {
        //     toastr.warning('请选择有效数据');
        //     return;
        // }
        console.log(123);
        let ele = $(this).parent().parent();
        var message = `<div class="input-group"><input type="text" id="name" class="form-control" placeholder="连接名称" aria-describedby="basic-addon1" value="${ele.find('.name').html()}"></div>` +
        `<div class="input-group"><input type="text" id="host" class="form-control" placeholder="数据库地址" aria-describedby="basic-addon2" value="${ele.find('.host').html()}"></div>` +
        `<div class="input-group"><input type="text" id= 'port' class="form-control" placeholder="数据库端口" aria-describedby="basic-addon3" value="${ele.find('.port').html()}"></div>` +
        `<div class="input-group"><input type="text" id="user" class="form-control" placeholder="用户名" aria-describedby="basic-addon4" value="${ele.find('.user').html()}"></div>` +
        `<div class="input-group"><input type="text" id="password" class="form-control" placeholder="密码" aria-describedby="basic-addon5" value="${ele.find('.password').html()}"></div>` +
        `<div class="input-group"><input type="text" id='db' class="form-control" placeholder="数据库名称" aria-describedby="basic-addon6" value="${ele.find('.db').html()}"></div>` +
        `<div class="input-group"><input type="text" class="form-control" placeholder="字符集" aria-describedby="basic-addon7" value="utf8"></div>`
        ;
        Ewin.confirm({ message: message, width: 400}).on(function (e) {
            if (!e) {
                return;
            }
            var data = {
                'name': $('#name').val(),
                'host': $('#host').val(),
                'port': $('#port').val(),
                'user': $('#user').val(),
                'password': $('#password').val(),
                'db': $('#db').val(),
                'charset': 'utf8',
            };
            toastr.options = {
                closeButton: false,
                debug: false,
                progressBar: false,
                positionClass: "toast-top-center",
                onclick: null,
                showDuration: "300",
                hideDuration: "1000",
                timeOut: "2000",
                extendedTimeOut: "1000",
                showEasing: "swing",
                hideEasing: "linear",
                showMethod: "fadeIn",
                hideMethod: "fadeOut"
            };
            if ($('#name').val() == '' || $('#host').val() == '' || $('#port').val() == '' || $('#user').val() == '' || $('#password').val() == '' || $('#db').val() == '') {
                toastr.warning('数据不能为空！');
            }
            else {
                $.ajax({
                    url: "/data_center/update_data/",
                    type: "POST",
                    data: data,
                    success: function (data,) {
                        if (data == "数据修改成功！") {
                            toastr.success(data);
                            setTimeout(function (){window.location.reload()}, 2000);
                        }
                        else {
                            toastr.warning(data);
                        }
                    },
                    error: function () {
                        toastr.error('Error');
                    },
                    complete: function () {

                    }

                });
            }
        });
    });
});