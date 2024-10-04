//1. ajax를 사용한 데이터 가져오기
var count = 1;
var total = 0;
var avg = 0;
var id_num;
let temp = 0; //수정버튼 클릭확인
$(function(){ //제이쿼리 선언

  $("#dataBtn").click(function(){ //dataBtn 선언
    $.ajax({ //ajax선언
      url:"js/stuData.json",
      type:"get",
      data:"",
      dataType:"json",
      success:function(data){
        console.log(data);
        var s_data = "";
        for(var i=0;i<data.length;i++){
          count++;
          console.log("count :"+count);
          var total = `${data[i].kor+data[i].eng+data[i].math}`;
          var avg = `${(total/3).toFixed(2)}`;
          s_data +=
            `<tr id="${data[i].no}">
              <td>${data[i].no}</td>
              <td>${data[i].name}</td>
              <td>${data[i].kor}</td>
              <td>${data[i].eng}</td>
              <td>${data[i].math}</td>
              <td>${total}</td>
              <td>${avg}</td>
              <td><button class="updateBtn">수정</button><button class="delBtn">삭제</button></td>
            </tr>`;
        }
        $("#tbody").html(s_data);
  
      },
      error:function(){
        alert("실패")
      }
    });//ajax선언
  });//dataBtn 선언
  
  //dleBtn 버튼
  $(document).on("click",".delBtn", function(){
    id_num = $(this).closest("tr").attr("id");
    if(confirm("진짜 삭제하실?")){
    $("#"+id_num).remove()};
  });


  //create 입력버튼 이벤트
  $(document).on("click","#create",function(){
    //입력된 데이터 가져오기
    //번호 : count
    //이름, 국어, 영어, 수학, 합계, 평균을 가져와야함
    let name = $("#name").val();
    let kor = Number($("#kor").val());
    let eng = Number($("#eng").val());
    let math = Number($("#math").val());
    total = kor+eng+math;
    avg = (total/3).toFixed(2);
    
    //입력란에 데이터가 없을때
    if($("#name").val().length<1 || $("#kor").val().length<1 || $("#eng").val().length<1 || $("#math").val().length<1){
      alert("값 느라");
      return false;
    };

    alert("성적을 추가함");

    //가져온 데이터 표에 추가하기
    let s_data = 
            `<tr id="${count}">
              <td>${count}</td>
              <td>${name}</td>
              <td>${kor}</td>
              <td>${eng}</td>
              <td>${math}</td>
              <td>${total}</td>
              <td>${avg}</td>
              <td><button class="updateBtn">수정</button><button class="delBtn">삭제</button></td>
            </tr>`;
            $("tbody").prepend(s_data)
        
  });//create 입력버튼 이벤트


  //수정버튼
  $(document).on("click",".updateBtn",function(){
    $(this).css({"font-weight":"600","color":"red"});
    if(temp==1){
      alert("수정완료 또는 취소해라");
      return false;
    }
    id_num = $(this).closest("tr").attr("id");
    let u_data = $(this).closest("tr");
    $("#name").val(u_data.children("td:eq(1)").text());
    $("#kor").val(u_data.children("td:eq(2)").text());
    $("#eng").val(u_data.children("td:eq(3)").text());
    $("#math").val(u_data.children("td:eq(4)").text());

    $("#create,#update,#updateCancel").toggle();
    temp=1;
  
  });
  
  //수정취소
  $(document).on("click","#updateCancel",function(){
    $("#create,#update,#updateCancel").toggle();
    //인풋란 데이터 지우기
    $("#name").val("");
    $("#kor").val("");
    $("#eng").val("");
    $("#math").val("");
    $(".updateBtn").css({"font-weight":"400","color":"black"});
    temp=0;
  })

  //수정완료
  $(document).on("click","#update",function(){
    //입력된 데이터 가져오기
    let name = $("#name").val();
    let kor = Number($("#kor").val());
    let eng = Number($("#eng").val());
    let math = Number($("#math").val());
    total = kor+eng+math;
    avg = (total/3).toFixed(2);

    //입력란에 데이터가 없을때
    if($("#name").val().length<1 || $("#kor").val().length<1 || $("#eng").val().length<1 || $("#math").val().length<1){
      alert("값 느라");
      return false;
    };

    //데이터 수정해서 넣기
    console.log("수정완료버튼 클릭 id_num :"+id_num);
    let s_data = 
             `<td>${id_num}</td>
              <td>${name}</td>
              <td>${kor}</td>
              <td>${eng}</td>
              <td>${math}</td>
              <td>${total}</td>
              <td>${avg}</td>
              <td><button class="updateBtn">수정</button><button class="delBtn">삭제</button></td>`;
            $("#"+id_num).html(s_data);

        //입력란 데이터 지우기
        $("#name").val(""); 
        $("#kor").val("");
        $("#eng").val("");
        $("#math").val("");

        alert("수정완료");
        $("#create,#update,#updateCancel").toggle();
        $(".updateBtn").css({"font-weight":"400","color":"black"});
        temp=0;

  });



});//제이쿼리 선언