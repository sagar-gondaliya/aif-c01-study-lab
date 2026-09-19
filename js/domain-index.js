(function () {
  var d = parseInt(document.body.getAttribute("data-domain") || "1", 10);
  var list = ((window.AIF && AIF.topics) || []).filter(function (t) { return t.domain === d; });
  var titles = {
    1: ["Domain 1 — AI and ML", "20% of the exam · official tasks 1.1 terms · 1.2 use cases · 1.3 lifecycle"],
    2: ["Domain 2 — Generative AI", "24% of the exam · official tasks 2.1 concepts · 2.2 limits · 2.3 AWS stack"],
    3: ["Domain 3 — Foundation models", "28% of the exam · official tasks 3.1 design · 3.2 prompts · 3.3 train · 3.4 eval"],
    4: ["Domain 4 — Responsible AI", "14% of the exam · official tasks 4.1 responsible systems · 4.2 explainability"],
    5: ["Domain 5 — Security and governance", "14% of the exam · official tasks 5.1 secure · 5.2 govern"]
  };
  var box = document.getElementById("dbox");
  var meta = titles[d];
  var html = "<h1>" + meta[0] + "</h1><p class='lead'>" + meta[1] +
    ". Read the <a href='glossary.html#d" + d + "'>keyword table</a> first. Each topic page is a quiz only.</p>";
  html += '<div class="topic-list">';
  list.forEach(function (t, i) {
    html += '<a class="topic-row" href="topic.html?id=' + t.id + '">' +
      '<span class="topic-n">' + (i + 1) + "</span>" +
      "<span><b>" + t.title + "</b><small>" + t.lead + " · task " + t.task +
      " · " + (t.quiz ? t.quiz.length : 0) + " questions</small></span></a>";
  });
  html += "</div>";
  var first = list[0];
  if (first) {
    html += "<p class='btn-row'><a class='btn' href='topic.html?id=" + first.id + "'>Start topic 1 ›</a></p>";
  }
  box.innerHTML = html;
})();
