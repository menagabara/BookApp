$(function() {
        $('#FavCat').click(function(){
            var id =$('#category').val();
            if($(this).attr('name')==1){
                $('#FavCat').attr('name',"2")
             $('#FavCat').attr('src',"/static/img/RedHeart.png")
          $.post("/favCat",{id:id},
            function(data) {
              alert(data);
            });}
          else
          {
            $('#FavCat').attr('name',"1")
              $('#FavCat').attr('src',"/static/img/Empty-Heart.png")
             $.post("/delCat",{id:id},
            function(data) {
              alert(data);
            });
          }

        });
});