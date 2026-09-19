(function () {
  var data = (window.AIF && AIF.glossary) || [];
  var box = document.getElementById("gloss");
  var search = document.getElementById("gloss-q");
  var jumps = document.getElementById("gloss-jumps");
  var countEl = document.getElementById("gloss-count");

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }

  function allRows() {
    var out = [];
    data.forEach(function (sec) {
      (sec.groups || []).forEach(function (g) {
        (g.rows || []).forEach(function (r) {
          out.push({ sec: sec, group: g, row: r });
        });
      });
    });
    return out;
  }

  function match(q, item) {
    if (!q) return true;
    var blob = (item.row.term + " " + item.row.meaning + " " + item.row.example + " " +
      item.group.name + " " + item.sec.title).toLowerCase();
    return blob.indexOf(q) !== -1;
  }

  function paint() {
    var q = ((search && search.value) || "").toLowerCase().trim();
    var total = 0;
    var shown = 0;
    var html = "";

    data.forEach(function (sec) {
      var secHtml = "";
      var secN = 0;
      (sec.groups || []).forEach(function (g) {
        var rows = (g.rows || []).filter(function (r) {
          return match(q, { sec: sec, group: g, row: r });
        });
        total += (g.rows || []).length;
        if (!rows.length) return;
        secN += rows.length;
        shown += rows.length;
        secHtml += "<h3>" + escapeHtml(g.name) + "</h3>";
        secHtml += "<div class='table-wrap'><table class='gloss-table'><tr><th>Term</th><th>Meaning (simple)</th><th>Exam example</th></tr>";
        rows.forEach(function (r) {
          secHtml += "<tr><td><b>" + escapeHtml(r.term) + "</b></td><td>" +
            escapeHtml(r.meaning) + "</td><td>" + escapeHtml(r.example) + "</td></tr>";
        });
        secHtml += "</table></div>";
      });
      if (!secHtml && q) return;
      html += '<section class="gloss-sec" id="' + escapeHtml(sec.id) + '">';
      html += "<h2>" + escapeHtml(sec.title) + "</h2>";
      if (sec.lead) html += "<p class='lead'>" + escapeHtml(sec.lead) + "</p>";
      html += secHtml || "<p class='muted'>No matches in this domain.</p>";
      html += "</section>";
    });

    box.innerHTML = html;
    if (countEl) {
      countEl.textContent = q
        ? shown + " matching keywords (of " + total + ")"
        : total + " keywords across all 5 domains";
    }
  }

  if (jumps) {
    jumps.innerHTML = data.map(function (sec) {
      return '<a class="btn ghost" href="#' + sec.id + '">' + escapeHtml(sec.short || sec.title) + "</a>";
    }).join("");
  }

  if (search) search.addEventListener("input", paint);
  paint();
  AIF.markRead && AIF.markRead("glossary");
})();
