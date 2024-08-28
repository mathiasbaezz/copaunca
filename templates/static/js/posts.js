$(document).ready(function () {
            $.ajax({
                url: "/data_inicial",
                dataType: 'json',
                type: 'get',
                success: function (data) {
                    if (data.is_taken) {
                        alert(data.error_message);
                    }
                    var posts = JSON.parse(data.posts)
                    posts.forEach(function(post){
                        $("#recentPosts").append(
                            '<li>'+
                                '<p>' +  post.fields.title + '</p>'+
                                '<span><i class="fa fa-clock-o"></i>'+ post.fields.published_date + '</span>' +
                            '</li>'
                        )
                    })
                }
            })
        })