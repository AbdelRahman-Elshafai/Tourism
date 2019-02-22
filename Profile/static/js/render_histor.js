function show(id) {
  var x = document.getElementById(id);
  var h = document.getElementById('hotels-lst');
  var c = document.getElementById('cars-lst');
  var p = document.getElementById('posts-lst');
  var com = document.getElementById('comments-lst');


    h.style.display = "none";
    c.style.display = "none";
    p.style.display = "none";
    com.style.display = "none";

    x.style.display = "block";
}