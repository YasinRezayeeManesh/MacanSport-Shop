function sendArticleComment(article_Id) {
    var comment = $('#commentText').val();
    var parentId = $('#parent_id').val();
    $.get('/articles/article-comment/', {
        articleComment: comment,
        articleId: article_Id,
        parentId: parentId,
    }).then(res => {
        console.log(res);
        location.reload()
    });
}


function fillParentId(parentId) {
    $('#parent_id').val(parentId);
    document.getElementById('comment_form').scrollIntoView({behavior: "smooth"})
}


function sendProductComment(product_Id) {
    var comment = $('#product_comment_text').val();
    var parentId = $('#product_parent_id').val();
    $.get('/products/product-comment/', {
        productComment: comment,
        productId: product_Id,
        parentId: parentId,
    }).then(res => {
        console.log(res);
        location.reload();
    });
}


function fillParentProductId(parent_Id) {
    $('#product_parent_id').val(parent_Id);
    document.getElementById('product_comment_form').scrollIntoView({behavior: "smooth"})
}


function addProductToOrder(productId) {
    const productCount = $('#product_count').val();
    $.get('/orders/add-to-order?product_id=' + productId + '&count=' + productCount).then(res => {
        Swal.fire({
            title: res.title,
            text: res.text,
            icon: res.icon,
            showCancelButton: false,
            confirmButtonColor: "#3085d6",
            confirmButtonText: res.confirm_button_text,
        }).then((result) => {
            if (result.isConfirmed && res.status === "user is not authenticated") {
                window.location.href = "/account/login";
            }
        });
    });
}


function removeOrderDetail(detailId){
    $.get('/panel/remove-order-detail?detail_id=' + detailId).then(res => {
        if (res.status === 'success') {
            $("#order-detail-content").html(res.body);
        }
    })
}

function changeOrderDetailCount(detailId, state){
    $.get("/panel/change-order-detail-count?detail_id=" + detailId + "&state=" + state).then(res => {
        if (res.status === 'success') {
            $("#order-detail-content").html(res.body);
        }
    })
}
