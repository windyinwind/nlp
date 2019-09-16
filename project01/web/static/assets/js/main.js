$(document).ready(function(){
    // fetch all speeches
    fetch('/speeches').then(function(res) {
        return res.json();
    }).then(function(data){
        console.log(data);
    }).catch(function(err){
        console.error(err);
    })
})