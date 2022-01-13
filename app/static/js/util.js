function del_movie(movie_name){
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("POST", "/del_movie", true);
    xmlhttp.setRequestHeader("Content-Type", "application/json");
    var data = JSON.stringify({"name": movie_name})
    xmlhttp.send(data)
    document.location.reload();
}


function del_hall(hall_name){
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("POST", "/del_hall", true);
    xmlhttp.setRequestHeader("Content-Type", "application/json");
    var data = JSON.stringify({"name": hall_name})
    xmlhttp.send(data)
    document.location.reload();
}


function gen_session(){
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("POST", "/gen_session", true);
    xmlhttp.setRequestHeader("Content-Type", "application/json");
    var data = JSON.stringify({"act":"gen"})
    xmlhttp.send(data)

}