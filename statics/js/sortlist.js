$(function () {
   $('tr').on('click', 'th', function () {
       let span_ele_bottom = `<span  class="glyphicon glyphicon-triangle-bottom" aria-hidden="true" style="float:right;margin:auto 5px; top: 10px;float: left;"></span>`;
       let span_ele_top = `<span title="-qq" class="glyphicon glyphicon-triangle-top" aria-hidden="true" style="float:right;margin:auto 5px;float: left;"></span>`;
       let ele_bottom = $(this).find('.glyphicon-triangle-bottom').length;
       let ele_top = $(this).find('.glyphicon-triangle-top').length;
       if (ele_bottom == 0 && ele_top == 0) {
           ordername = '-' + $(this).text();
            $(this).append(span_ele_bottom);
            $(this).siblings().find('span').remove();
       }
       else if (ele_bottom != 0 && ele_top == 0) {
           $(this).find('span').remove();
           ordername = $(this).text();
           $(this).append(span_ele_top);
       }
       else if (ele_bottom == 0 && ele_top != 0) {
           $(this).find('span').remove();
           ordername = '-' + $(this).text();
           $(this).append(span_ele_bottom);
       }
       getdatalist(pages, admin_class_detail,  urls);
   })
});