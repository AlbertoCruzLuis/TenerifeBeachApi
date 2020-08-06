function get_url() {
    if (document.getElementById("url").value != ""){
        return "http://localhost:5000/api/" + document.getElementById("url").value
    } else {
        document.getElementById("url").value = "beachlist/";
        return "http://localhost:5000/api/beachlist/"
    }
}

url = get_url()

function get_data() {
    let jsonViewer = new JSONViewer();

    let data = fetch(get_url()).
        then(function(response) {
            return response.json();
        }).
        then(function(myJson) {
            document.querySelector(".JsonViewer").innerHTML = "";
            document.querySelector(".JsonViewer").appendChild(jsonViewer.getContainer());
            jsonViewer.showJSON(myJson,20,2);
        });
}

get_data()
