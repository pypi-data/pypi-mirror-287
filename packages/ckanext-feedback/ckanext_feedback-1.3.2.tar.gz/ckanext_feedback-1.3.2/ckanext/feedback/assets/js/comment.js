function checkCommentExists() {
  const comment = document.getElementById('comment_content').value;
  const rating = document.getElementById('rating').value;
  const commentErrorElement = document.getElementById('comment-error');
  const ratingErrorElement = document.getElementById('rating-error');

  // Reset display settings
  commentErrorElement.style.display = 'none';

  if (!comment) {
    commentErrorElement.style.display = '';
    return false;
  } else {
    return true;
  }
}

function checkReplyExists() {
  const errorElement = document.getElementById('reply-error');
  const reply = document.getElementById('reply_content').value;

  if (reply) {
    errorElement.style.display = 'none';
    return true;
  } else {
    errorElement.style.display = '';
    return false;
  }
}

function selectRating(selectedStar) {
  // Set rating = to clicked star's value
  document.getElementById('rating').value = selectedStar.dataset.rating;

  const stars = document.querySelectorAll('#rateable .rating-star');

  // Loop through each star and set the appropriate star icon
  stars.forEach(star => {
    if(star.dataset.rating <= selectedStar.dataset.rating) {
      star.src = '/images/rating_star.png';
    } else {
      star.src = '/images/empty_rating_star.png';
    }
  });
}

function setReplyFormContent(resourceCommentId) {
  // Set values of modal screen elements
  const category = document.getElementById('comment-category-' + resourceCommentId).textContent;
  const approved = document.getElementById('comment-created-' + resourceCommentId).textContent;
  const content = document.getElementById('comment-content-' + resourceCommentId).textContent;

  document.getElementById('selected_comment_header').innerHTML = approved + ' ' + category;
  document.getElementById('selected_comment').innerHTML = content;
  document.getElementById('selected_resource_comment_id').value = resourceCommentId;
}
