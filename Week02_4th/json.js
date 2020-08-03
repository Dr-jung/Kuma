


$.ajax(
    {
        url:"http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99",
        type: "GET",
        data: {},
        success: function(response){
            for(let index=0;index<response['RealtimeCityAir']['row'].length;index++) {
                console.log(response['RealtimeCityAir']['row'][index]['MSRSTE_NM']);
            }
        }
    }
);


console.log();
console.log();
console.log();
console.log();
console.log();
console.log();
