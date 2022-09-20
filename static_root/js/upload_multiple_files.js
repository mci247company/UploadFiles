class FilesUpload {
    constructor(input) {
        this.input = input
        this.limit_size = 1024 * 1024 * 20
    }
    create_progress_bar() {
        let progress = `<div class="file-icon">
                            <i class="fa fa-file-o" aria-hidden="true"></i>
                        </div>
                        <div class="file-details">
                            <p class="filename"></p>
                            <small class="textbox"></small>
                            <div class="progress" style="margin-top: 5px;">
                                <div class="progress-bar bg-success" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%">
                                </div>
                            </div>
                        </div>`

        const DIV = document.createElement("DIV");
        DIV.innerHTML = progress;       
        document.getElementById('uploaded_files').appendChild(DIV)
    }

    upload() {
        // console.log(this);
        // console.log(this.input.files.length);
        for (let i=0; i< this.input.files.length; i++)
        {   
            this.create_progress_bar(i);         
            this.file = this.input.files[i];
            // console.log(i)
            // console.log(this.file);
            this.upload_files(this.file, i);   
        }

    }

    //upload files
    upload_files(file, i) {
        console.log(file);
        var self = this;
        var formData = new FormData();
        formData.append('file', file);
        formData.append('filename', file.name);
        $('.filename').eq(i).text(file.name)
        $('.textbox').eq(i).text("Uploading file")
        $.ajaxSetup({
            headers: {
                "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
            }
        });
        $.ajax({
            xhr: function () {
                var xhr = new XMLHttpRequest();
                xhr.upload.addEventListener('progress', function (e) {
                    // console.log(e, e.total, e.loaded);
                    if (e.lengthComputable) {
                        var percent = Math.round((e.loaded / e.total) * 100);
                        if (e.total < self.limit_size){
                            // console.log("OK1")
                            $('.progress-bar').eq(i).css('width', percent + '%')
                            $('.progress-bar').eq(i).text(percent + '%')    
                        }
                        else if (percent < 95){
                            // console.log("OK2")
                            $('.progress-bar').eq(i).css('width', percent + '%')
                            $('.progress-bar').eq(i).text(percent + '%')    
                        }
                    }
                });
                return xhr;
            },

            url: '/upload-multiple-files',
            type: 'POST',
            dataType: 'json',
            cache: false,
            processData: false,
            contentType: false,
            data: formData,
            error: function (xhr) {
                swal("Ops!", xhr.statusText, "error");
                // alert(xhr.statusText);
            },
            success: function (res) {
                // upload complete
                swal("Good job!", res.data, "success");
                $('.progress-bar').eq(i).css('width', "100%")
                $('.progress-bar').eq(i).text("100%")
                // alert(res.data)
            }
        });
    };
}

(function ($) {
    $('#submit').on('click', (event) => {
        event.preventDefault();
        var uploader = new FilesUpload(document.querySelector('#filesupload'))
        // console.log(document.querySelector('#filesupload'));
        uploader.upload();
    });
})(jQuery);

ondragenter = function(evt) {
    evt.preventDefault();
    evt.stopPropagation();
};

ondragover = function(evt) {
    evt.preventDefault();
    evt.stopPropagation();
};

ondragleave = function(evt) {
    evt.preventDefault();
    evt.stopPropagation();
};
  
ondrop = function(evt) {
    evt.preventDefault();
    evt.stopPropagation();
    const files = evt.originalEvent.dataTransfer;
    console.log(files);
    let uploader = new FilesUpload(files);
    uploader.upload();
};

$('#dropBox')
    .on('dragover', ondragover)
    .on('dragenter', ondragenter)
    .on('dragleave', ondragleave)
    .on('drop', ondrop);

