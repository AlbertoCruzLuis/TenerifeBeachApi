function get_data(url, element) {
    let jsonViewer = new JSONViewer();

    let data = fetch(url).
        then(function(response) {
            return response.json();
        }).
        then(function(myJson) {
            element.innerHTML = "";
            element.appendChild(jsonViewer.getContainer());
            jsonViewer.showJSON(myJson,20,2);
        });
}

list_viewer = document.querySelectorAll(".JsonViewer")

for (let i = 0; i < list_viewer.length; i++) {
    element = list_viewer[i]
    url = list_viewer[i].getAttribute("url")
    get_data(url, element)
}