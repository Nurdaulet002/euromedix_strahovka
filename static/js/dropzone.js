(function($) {
  'use strict';
  $("my-awesome-dropzone").dropzone({
    url: "urbanui.com/"
  });
})(jQuery);

(function($) {
  'use strict';

  // initializing inputmask
  $(":input").inputmask();

})(jQuery);

(function($) {
  'use strict';
  if ($("#fileuploader").length) {
    $("#fileuploader").uploadFile({
      url: "YOUR_FILE_UPLOAD_URL",
      fileName: "myfile"
    });
  }
})(jQuery);