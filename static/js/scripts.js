function search() {
    keyword = $('#keyword').val()

    $('#modal-thead').empty()
    $('#modal-tbody').empty()

    $.ajax({
        type: "GET",
        url: "/oembed?url=" + keyword,
        timeout: 10000,
        contentType: "application/json",
        success: function (response, status, request) {
            let keys = Object.keys(response)
            let temp_html = ""

            title = response["title"]
            temp_html =
                            `
                            <tr>
                                <th scope="col">title</th>
                                <th scope="col">"${title}"</th>
                            </tr>
                            `
            $('#modal-thead').append(temp_html)     

            for (let i = 0; i < keys.length; i++){
                target_key = keys[i]
                target_value = response[target_key]
                
                if (target_key == "thumbnail_url"){
                    temp_html =
                        `<tr>
                        <th scope="row">"${target_key}"<br> "${response["thumbnail_height"]}"/"${response["thumbnail_width"]}" </th>
                        <td><img id="youtubeimg" src="${target_value}"/></td>
                        </tr>`
                }else {
                    temp_html =
                        `<tr>
                        <th scope="row">"${target_key}"</th>
                        <td>"${target_value}"</td>
                        </tr>`
                }
                $('#modal-tbody').append(temp_html)       
            }
        },
        error: function (response, status, error) {
            alert(response["responseJSON"]["msg"])
        },
    })
}