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

if (window.location.href.includes('my_post')) {
  document.getElementById('my-post-nav').classList.add('active');
} else if (window.location.href === 'http://127.0.0.1:8000/') {
  document.getElementById('home-nav').classList.add('active');
}
