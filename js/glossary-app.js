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

  function paras(text) {
    var parts = Array.isArray(text) ? text : String(text || "").split(/\n\n+/);
    return parts.filter(Boolean).map(function (p) {
      return "<p>" + escapeHtml(p.trim()) + "</p>";
    }).join("");
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

    var groupN = 0;
    data.forEach(function (sec) {
      var secHtml = "";
      var secN = 0;
      (sec.groups || []).forEach(function (g, gi) {
        groupN += 1;
        var pad = groupN < 10 ? "0" + groupN : String(groupN);
        var gid = sec.id + "-g" + (gi + 1);
        var all = g.rows || [];
        var rows = all.filter(function (r) {
          return match(q, { sec: sec, group: g, row: r });
        });
        total += all.length;
        if (!rows.length) return;
        secN += rows.length;
        shown += rows.length;
        var heading = pad + " - " + g.name + " - (" + all.length + ")";
        secHtml += '<h3 id="' + escapeHtml(gid) + '">' + escapeHtml(heading) + "</h3>";
        secHtml += "<div class='table-wrap'><table class='gloss-table'><tr><th>Term</th><th>Meaning (simple)</th><th>Exam example</th></tr>";
        rows.forEach(function (r) {
          secHtml += "<tr><td><b>" + escapeHtml(r.term) + "</b></td><td class='gloss-mean'>" +
            paras(r.meaning) + "</td><td class='gloss-ex'>" + paras(r.example) + "</td></tr>";
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
