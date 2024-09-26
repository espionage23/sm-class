var count = 1;
$(function(){ //제이쿼리

  $("#searchBtn").click(function(){ //searchBtn
    
    alert("검색버튼")
    let surl = "https://apis.data.go.kr/B551011/PhotoGalleryService1/gallerySearchList1?serviceKey=eEMWUqlUDcFvHmN6L0%2BV1lKUXC1YpGLuAkhU%2Fmkb%2FwZI4sFmQakEjx21opj117BCIJjBXIpd%2BCq6dpkkT%2B6exA%3D%3D&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json&keyword=";
    let searchWord = $("#search_txt").val();
    surl += searchWord
    $.ajax({ //ajax
      url:surl,
      type:"get",
      data:"",
      dataType:"json",
      success:function(data){
        alert("성공")
        // console.log(data);

        var items = data.response.body.items.item;
          for (var i = 0; i < 10; i++) {
            
            console.log("item " + (i + 1) + ": ", items[i]); // 각 아이템 콘솔에 출력
          }
          items +=
          data += `<tr id='${i}' >`;
          data += `<td class='num'>${items[i].galContentId}</td>`;
          data += `<td><a href='#'>${items[i].galTitle}</a></td>`;
          data += `<td>${items[i].galPhotographer}</td>`;
          data += `<td>${items[i].galModifiedtime}</td>`;
          data += `<td><img src=${items[i].galWebImageUrl}></td>`;
          data += `</tr>`;
        
          document.getElementById("tbody").innerHTML = data;


      },
      error:function(){
        alert("실패")
      }
      
    })//ajax
    
  });//searchBtn
});//제이쿼리
