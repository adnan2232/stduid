
async function dataEntry(url,csrf_token, data){

    const dataArray = data.split(".");
    
    // if(dataArray.length < 4){
    //     alert("Length of new password should greater than 7");
    //     return
    // }

    await fetch(url,{
        method:"POST",
        headers: {
            'Accept':"application/json",
            'Content-Type':"application/json",
            'X-CSRFTOKEN':csrf_token,
        },
        body: JSON.stringify({
            "stateId": dataArray[0],
            "uniId": dataArray[1],
            "collegeId" : dataArray[2], 
            "grNo" : dataArray[3]
        })
    }).then((res) =>{
            return res.json()
            }).then((res)=>{

                // const studentId = res["studentUid"];
                // const studentName = res["studentName"];
                // const collegeName = res["collegeName"];
                // const universityName = res["uniName"];
                // const state = res["state"];

                console.log(res["state"])
                console.log("success")

        }).catch((fail) =>{
            alert(fail);
        })
};