(function () {
  window.AIF = window.AIF || {};

  function $(id) { return document.getElementById(id); }

  function clone(q) {
    return JSON.parse(JSON.stringify(q));
  }

  function sameSet(a, b) {
    if (!a || !b || a.length !== b.length) return false;
    var x = a.slice().sort(), y = b.slice().sort();
    for (var i = 0; i < x.length; i++) if (x[i] !== y[i]) return false;
    return true;
  }

  function letter(i) { return String.fromCharCode(65 + i); }

  function renderStem(q, i, total) {
    var typeLabel = {
      single: "Multiple choice · one answer",
      multi: "Multiple response · select ALL that apply",
      order: "Ordering · put the steps in the correct order",
      match: "Matching · pair every item"
    };
    return (
      '<p class="muted small">Question ' + (i + 1) + " of " + total +
      " · Domain " + q.domain + " · " + (typeLabel[q.type] || q.type) + "</p>" +
      "<h3>" + escapeHtml(q.stem) + "</h3>"
    );
  }

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }

  function renderChoices(q, picked) {
    picked = picked || [];
    var html = "";
    if (q.type === "single" || q.type === "multi") {
      q.choices.forEach(function (c, i) {
        var on = picked.indexOf(i) !== -1 ? " on" : "";
        html += '<button type="button" class="choice' + on + '" data-i="' + i + '">' +
          letter(i) + ". " + escapeHtml(c) + "</button>";
      });
    } else if (q.type === "order") {
      var order = picked.length ? picked : q.items.map(function (_, i) { return i; });
      order.forEach(function (idx, pos) {
        html += '<div class="choice on" data-pos="' + pos + '">' +
          (pos + 1) + ". " + escapeHtml(q.items[idx]) +
          ' <button type="button" class="btn ghost move-up" data-pos="' + pos + '">Up</button> ' +
          ' <button type="button" class="btn ghost move-down" data-pos="' + pos + '">Down</button></div>';
      });
    } else if (q.type === "match") {
      q.left.forEach(function (L, i) {
        html += "<p><b>" + escapeHtml(L) + "</b><br><select class='match-sel' data-i='" + i + "'>";
        html += '<option value="">— choose —</option>';
        q.right.forEach(function (R, j) {
          var sel = picked[i] === j ? " selected" : "";
          html += '<option value="' + j + '"' + sel + ">" + escapeHtml(R) + "</option>";
        });
        html += "</select></p>";
      });
    }
    return html;
  }

  function userAnswer(q, picked) {
    if (q.type === "order") return picked;
    if (q.type === "match") return picked;
    return picked;
  }

  function isCorrect(q, picked) {
    if (q.type === "order" || q.type === "match") {
      if (!picked || picked.length !== q.answer.length) return false;
      for (var i = 0; i < q.answer.length; i++) if (picked[i] !== q.answer[i]) return false;
      return true;
    }
    return sameSet(picked || [], q.answer);
  }

  function explainBlock(q, picked, show) {
    if (!show) return "";
    var ok = isCorrect(q, picked);
    var key = "";
    if (q.type === "single" || q.type === "multi") {
      key = q.answer.map(function (i) { return letter(i); }).join(", ");
    } else if (q.type === "order") {
      key = q.answer.map(function (i) { return q.items[i]; }).join(" → ");
    } else {
      key = q.left.map(function (L, i) { return L + " → " + q.right[q.answer[i]]; }).join("; ");
    }
    return '<div class="' + (ok ? "ok" : "warn") + '"><h3>' +
      (ok ? "Correct" : "Incorrect") + "</h3><p><b>Key:</b> " + escapeHtml(key) +
      "</p><p>" + escapeHtml(q.explain || "") + "</p></div>";
  }

  AIF.runQuiz = function (opts) {
    var questions = opts.questions.map(clone);
    var title = opts.title;
    var timed = !!opts.timed;
    var seconds = opts.seconds || 90 * 60;
    var storeKey = opts.storeKey;
    var mockN = opts.mockN;

    if (timed && questions.length > 1) {
      for (var sh = questions.length - 1; sh > 0; sh--) {
        var sj = Math.floor(Math.random() * (sh + 1));
        var st = questions[sh];
        questions[sh] = questions[sj];
        questions[sj] = st;
      }
    }

    var i = 0;
    function shuffleOrder(q) {
      var a = q.items.map(function (_, idx) { return idx; });
      var n = a.length;
      if (n < 2) return a;
      var tries = 0;
      do {
        for (var i = n - 1; i > 0; i--) {
          var j = Math.floor(Math.random() * (i + 1));
          var t = a[i]; a[i] = a[j]; a[j] = t;
        }
        tries++;
      } while (tries < 8 && isCorrect(q, a));
      return a;
    }
    var answers = questions.map(function (q) {
      if (q.type === "order") return shuffleOrder(q);
      if (q.type === "match") return q.left.map(function () { return null; });
      return [];
    });
    var flagged = {};
    var started = Date.now();
    var left = seconds;
    var timerId = null;
    var submitted = false;

    $("exam-title").textContent = title;
    if (timed) {
      $("timer-wrap").style.display = "";
      tick();
      timerId = setInterval(tick, 1000);
    } else if ($("timer-wrap")) {
      $("timer-wrap").style.display = "none";
    }

    function tick() {
      left = Math.max(0, seconds - Math.floor((Date.now() - started) / 1000));
      var m = Math.floor(left / 60), s = left % 60;
      var el = $("timer");
      el.textContent = (m < 10 ? "0" : "") + m + ":" + (s < 10 ? "0" : "") + s;
      el.className = "timer" + (left < 300 ? " low" : "");
      if (left <= 0 && !submitted) finish();
    }

    function paintPalette() {
      var p = $("palette");
      if (!p) return;
      p.innerHTML = questions.map(function (_, idx) {
        var cls = "navq";
        if (idx === i) cls += " cur";
        var a = answers[idx];
        var filled = qFilled(questions[idx], a);
        if (filled) cls += " ans";
        if (flagged[idx]) cls += " flag";
        return '<button type="button" class="' + cls + '" data-go="' + idx + '">' + (idx + 1) + "</button>";
      }).join("");
      p.querySelectorAll("[data-go]").forEach(function (b) {
        b.onclick = function () { i = +b.getAttribute("data-go"); draw(); };
      });
    }

    function qFilled(q, a) {
      if (q.type === "match") return a.every(function (x) { return x !== null && x !== ""; });
      if (q.type === "order") return true;
      return a && a.length > 0;
    }

    function draw() {
      var q = questions[i];
      $("qbox").innerHTML = renderStem(q, i, questions.length) + renderChoices(q, answers[i]);
      bind(q);
      $("flag-btn").textContent = flagged[i] ? "Unflag" : "Flag for review";
      paintPalette();
      $("prev-btn").disabled = i === 0;
      $("next-btn").textContent = i === questions.length - 1 ? "Review & submit" : "Next";
    }

    function bind(q) {
      if (q.type === "single" || q.type === "multi") {
        $("qbox").querySelectorAll(".choice").forEach(function (btn) {
          btn.onclick = function () {
            var n = +btn.getAttribute("data-i");
            if (q.type === "single") answers[i] = [n];
            else {
              var p = answers[i].slice();
              var at = p.indexOf(n);
              if (at === -1) p.push(n); else p.splice(at, 1);
              answers[i] = p;
            }
            draw();
          };
        });
      } else if (q.type === "order") {
        $("qbox").querySelectorAll(".move-up").forEach(function (b) {
          b.onclick = function (e) {
            e.stopPropagation();
            var pos = +b.getAttribute("data-pos");
            if (pos === 0) return;
            var a = answers[i].slice();
            var t = a[pos - 1]; a[pos - 1] = a[pos]; a[pos] = t;
            answers[i] = a; draw();
          };
        });
        $("qbox").querySelectorAll(".move-down").forEach(function (b) {
          b.onclick = function (e) {
            e.stopPropagation();
            var pos = +b.getAttribute("data-pos");
            var a = answers[i].slice();
            if (pos >= a.length - 1) return;
            var t = a[pos + 1]; a[pos + 1] = a[pos]; a[pos] = t;
            answers[i] = a; draw();
          };
        });
      } else if (q.type === "match") {
        $("qbox").querySelectorAll(".match-sel").forEach(function (sel) {
          sel.onchange = function () {
            var idx = +sel.getAttribute("data-i");
            answers[i][idx] = sel.value === "" ? null : +sel.value;
          };
        });
      }
    }

    $("prev-btn").onclick = function () { if (i > 0) { i--; draw(); } };
    $("next-btn").onclick = function () {
      if (i < questions.length - 1) { i++; draw(); }
      else showSubmit();
    };
    $("flag-btn").onclick = function () {
      flagged[i] = !flagged[i];
      draw();
    };

    function showSubmit() {
      var blank = 0;
      questions.forEach(function (q, idx) { if (!qFilled(q, answers[idx])) blank++; });
      $("submit-msg").textContent = blank
        ? blank + " question(s) still blank. Unanswered count as wrong. Submit anyway?"
        : "All questions have an answer. Submit this attempt?";
      $("submit-modal").classList.add("show");
    }
    $("cancel-submit").onclick = function () { $("submit-modal").classList.remove("show"); };
    $("confirm-submit").onclick = function () { $("submit-modal").classList.remove("show"); finish(); };

    function finish() {
      if (submitted) return;
      submitted = true;
      if (timerId) clearInterval(timerId);
      var hits = 0;
      var byD = { 1: { t: 0, c: 0 }, 2: { t: 0, c: 0 }, 3: { t: 0, c: 0 }, 4: { t: 0, c: 0 }, 5: { t: 0, c: 0 } };
      questions.forEach(function (q, idx) {
        byD[q.domain].t++;
        if (isCorrect(q, answers[idx])) { hits++; byD[q.domain].c++; }
      });
      var pct = Math.round((hits / questions.length) * 100);
      var scaled = Math.round(100 + (pct / 100) * 900);
      var pass = scaled >= 700;
      var rec = {
        when: Date.now(),
        hits: hits,
        total: questions.length,
        pct: pct,
        scaled: scaled,
        pass: pass,
        domains: byD,
        seconds: Math.floor((Date.now() - started) / 1000)
      };
      if (mockN) AIF.store.saveMock(mockN, rec);
      else if (storeKey) AIF.store.saveQuiz(storeKey, rec);

      $("runner").style.display = "none";
      if ($("palette")) $("palette").style.display = "none";
      if ($("timer-wrap")) $("timer-wrap").style.display = "none";
      $("results-panel").style.display = "";
      $("res-head").textContent = pass ? "PASS — scaled " + scaled : "NOT YET — scaled " + scaled;
      $("res-sub").textContent = hits + " / " + questions.length + " correct (" + pct + "%). Passing bar is 700 scaled (~70%).";
      $("res-head").parentElement.className = pass ? "ok" : "warn";
      var rows = "";
      [1, 2, 3, 4, 5].forEach(function (d) {
        var x = byD[d];
        if (!x.t) return;
        rows += "<tr><td>Domain " + d + "</td><td>" + x.c + " / " + x.t + "</td><td>" +
          Math.round((x.c / x.t) * 100) + "%</td></tr>";
      });
      $("res-table").innerHTML = "<tr><th>Section</th><th>Score</th><th>%</th></tr>" + rows;

      var rev = "";
      questions.forEach(function (q, idx) {
        var ok = isCorrect(q, answers[idx]);
        rev += '<div class="tile" style="margin-bottom:12px"><p class="small muted">#' +
          (idx + 1) + " · Domain " + q.domain + " · " + (ok ? "Correct" : "Missed") +
          "</p><p><b>" + escapeHtml(q.stem) + "</b></p>" +
          reviewAnswers(q, answers[idx]) + explainBlock(q, answers[idx], true) + "</div>";
      });
      $("review").innerHTML = rev;
    }

    function reviewAnswers(q, picked) {
      if (q.type === "single" || q.type === "multi") {
        return q.choices.map(function (c, idx) {
          var cls = "choice";
          if (q.answer.indexOf(idx) !== -1) cls += " good";
          else if ((picked || []).indexOf(idx) !== -1) cls += " bad";
          return '<div class="' + cls + '">' + letter(idx) + ". " + escapeHtml(c) + "</div>";
        }).join("");
      }
      return "";
    }

    draw();
  };
})();
