function advanced_upload_supported() {
    return function () {
        var div = document.createElement('div');
        return (('draggable' in div) || ('ondragstart' in div && 'ondrop' in div)) && 'FormData' in window && 'FileReader' in window;
    }();
}

function get_csrf_token() {
    tokens = document.getElementsByName("csrfmiddlewaretoken")
    return tokens[0].getAttribute('value')
}

// advanced drag-n-drop should be supported by all browsers in the 2020's but who knows...
