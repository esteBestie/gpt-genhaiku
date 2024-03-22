console.log('Script loaded successfully.');

document.getElementById('button').addEventListener('click', function() {
    console.log('Button clicked.');
    
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/generate_image', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            console.log('Response received:', xhr.status, xhr.statusText);
            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                if (response.image_url) {
                    console.log('Image URL:', response.image_url);
                    document.getElementById('image').innerHTML = '<img src="' + response.image_url + '" alt="Generated Image">';
                } else {
                    console.error('Error:', response.error);
                }
            } else {
                console.error('Error:', xhr.status, xhr.statusText);
            }
        }
    };
    xhr.send();
});
