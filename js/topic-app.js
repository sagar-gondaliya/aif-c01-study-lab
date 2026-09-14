(function () {
  var id = new URLSearchParams(location.search).get("id") || "d1-stack";
  var list = (window.AIF && AIF.topics) || [];
  var idx = -1;
  var t = null;
  for (var i = 0; i < list.length; i++) {
    if (list[i].id === id) { t = list[i]; idx = i; break; }
  }
  if (!t) {
    document.getElementById("title").textContent = "Topic not found";
    return;
  }

  document.title = t.title + " — AIF-C01";
  document.getElementById("crumb").textContent = "Domain " + t.domain + " · Official task " + t.task;
  document.getElementById("title").textContent = t.title;
  document.getElementById("lead").textContent = t.lead;
  document.getElementById("lesson").innerHTML = t.body;
  document.getElementById("exam-title").textContent = t.title + " quiz";

  var prev = list[idx - 1];
  var next = list[idx + 1];
  var hub = "d" + t.domain + ".html";
  document.getElementById("pager").innerHTML =
    '<a class="btn ghost" href="' + (prev ? "topic.html?id=" + prev.id : hub) + '" title="' +
    (prev ? prev.title : "Domain " + t.domain + " index") + '">‹ Previous</a>' +
    '<a class="btn" href="' + (next ? "topic.html?id=" + next.id : hub) + '" title="' +
    (next ? next.title : "Back to domain") + '">Next ›</a>';

  AIF.markRead("topic-" + t.id);

  if (t.quiz && t.quiz.length) {
    AIF.runQuiz({
      title: t.title,
      questions: t.quiz,
      storeKey: "topic-" + t.id,
      timed: false
    });
    document.getElementById("after").innerHTML =
      '<a class="btn" href="topic.html?id=' + t.id + '">Retry topic quiz</a>' +
      (next ? '<a class="btn dark" href="topic.html?id=' + next.id + '">Next topic</a>' : "") +
      '<a class="btn ghost" href="' + hub + '">Domain index</a>';
  }
})();
