function doLike(id) {
  window.CSRF_TOKEN = csrftoken;
  $.ajax({
    method: 'POST',
    url: '/posts/like/',
    data: {
      post_id: id,
      csrfmiddlewaretoken: window.CSRF_TOKEN,
    },
  });
  window.location.reload();
}
