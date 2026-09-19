(function () {
  window.AIF = window.AIF || {};

  var OPEN_KEY = "aif-c01-nav-open";

  var NAV = [
    { id: "start", g: "Start", items: [
      { href: "index.html", id: "home", t: "Home" },
      { href: "exam.html", id: "exam", t: "Exam facts" },
      { href: "plan.html", id: "plan", t: "14-day plan" }
    ]},
    { id: "learn", g: "Learn · 5 domains", items: [
      { href: "glossary.html", id: "glossary", t: "All keywords" },
      { href: "d1.html", id: "d1", t: "Domain 1 · AI & ML", pct: "20%", domain: 1 },
      { href: "d2.html", id: "d2", t: "Domain 2 · GenAI", pct: "24%", domain: 2 },
      { href: "d3.html", id: "d3", t: "Domain 3 · FMs", pct: "28%", domain: 3 },
      { href: "d4.html", id: "d4", t: "Domain 4 · Responsible", pct: "14%", domain: 4 },
      { href: "d5.html", id: "d5", t: "Domain 5 · Security", pct: "14%", domain: 5 }
    ]},
    { id: "extra", g: "Extra lessons", items: [
      { href: "lesson-services.html", id: "lsvc", t: "AWS AI services" },
      { href: "lesson-bedrock.html", id: "lbed", t: "Bedrock in depth" },
      { href: "lesson-agents.html", id: "lagent", t: "Agents, MCP, AgentCore" },
      { href: "lesson-rag.html", id: "lrag", t: "RAG" },
      { href: "lesson-prompts.html", id: "lprompt", t: "Prompts & attacks" },
      { href: "lesson-guardrails.html", id: "lguard", t: "Guardrails" }
    ]},
    { id: "ref", g: "Reference", items: [
      { href: "services.html", id: "services", t: "Service cheat sheet" },
      { href: "scope.html", id: "scope", t: "Official in-scope list" },
      { href: "trees.html", id: "trees", t: "Decision trees" },
      { href: "traps.html", id: "traps", t: "Exam traps" },
      { href: "flashcards.html", id: "cards", t: "Flashcards" }
    ]},
    { id: "practice", g: "Practice quizzes", items: [
      { href: "quiz.html?set=d1", id: "qd1", t: "Domain 1 bank" },
      { href: "quiz.html?set=d2", id: "qd2", t: "Domain 2 bank" },
      { href: "quiz.html?set=d3", id: "qd3", t: "Domain 3 bank" },
      { href: "quiz.html?set=d4", id: "qd4", t: "Domain 4 bank" },
      { href: "quiz.html?set=d5", id: "qd5", t: "Domain 5 bank" },
      { href: "quiz.html?set=svc", id: "qsvc", t: "Pick the service" },
      { href: "quiz.html?set=mixed", id: "qmix", t: "Mixed rapid" }
    ]},
    { id: "mocks", g: "Timed mocks", items: [
      { href: "mock.html?n=1", id: "m1", t: "Mock 1 · Foundation" },
      { href: "mock.html?n=2", id: "m2", t: "Mock 2 · GenAI" },
      { href: "mock.html?n=3", id: "m3", t: "Mock 3 · RAG" },
      { href: "mock.html?n=4", id: "m4", t: "Mock 4 · Responsible" },
      { href: "mock.html?n=5", id: "m5", t: "Mock 5 · Final" },
      { href: "results.html", id: "results", t: "Score history" }
    ]}
  ];

  AIF.NAV = NAV;

  function pageId() {
    var b = document.body;
    return (b && b.getAttribute("data-page")) || "home";
  }

  function loadOpen() {
    try { return JSON.parse(localStorage.getItem(OPEN_KEY)) || {}; }
    catch (e) { return {}; }
  }

  function saveOpen(map) {
    try { localStorage.setItem(OPEN_KEY, JSON.stringify(map)); }
    catch (e) {}
  }

  function currentContext() {
    var cur = pageId();
    var params = new URLSearchParams(location.search);
    var topicId = cur === "topic" ? (params.get("id") || "") : "";
    var topicDomain = 0;
    if (topicId && /^d([1-5])/.test(topicId)) topicDomain = parseInt(RegExp.$1, 10);
    return { cur: cur, params: params, topicId: topicId, topicDomain: topicDomain };
  }

  function isActive(it, ctx) {
    var cur = ctx.cur;
    if (cur === "quiz") return it.href.indexOf("set=" + ctx.params.get("set")) !== -1;
    if (cur === "mock") return it.href.indexOf("n=" + ctx.params.get("n")) !== -1;
    if (cur === "topic") return it.domain && it.domain === ctx.topicDomain;
    return it.id === cur;
  }

  function defaultOpen(ctx) {
    var extraIds = { lsvc: 1, lbed: 1, lagent: 1, lrag: 1, lprompt: 1, lguard: 1 };
    var refIds = { services: 1, scope: 1, trees: 1, traps: 1, cards: 1 };
    return {
      start: true,
      learn: true,
      extra: !!extraIds[ctx.cur],
      ref: !!refIds[ctx.cur],
      practice: ctx.cur === "quiz",
      mocks: ctx.cur === "mock" || ctx.cur === "results"
    };
  }

  function topicsFor(domain) {
    return ((AIF.topics || []).filter(function (t) { return t.domain === domain; }));
  }

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  function buildSidebarHtml(ctx, openMap) {
    var html = "";
    NAV.forEach(function (group) {
      var open = openMap[group.id] !== false;
      html += '<div class="nav-block' + (open ? " open" : "") + '" data-g="' + group.id + '">';
      html += '<button type="button" class="nav-h" data-toggle="' + group.id + '">' +
        '<span>' + escapeHtml(group.g) + "</span><i></i></button>";
      html += '<div class="nav-items">';
      group.items.forEach(function (it) {
        var active = isActive(it, ctx);
        var kids = it.domain ? topicsFor(it.domain) : [];
        var showKids = !!(it.domain && (active || ctx.cur === "d" + it.domain));
        html += '<a class="nav-a' + (active ? " active" : "") + '" href="' + it.href + '">' +
          '<span class="nav-label">' + escapeHtml(it.t) + "</span>";
        if (it.pct) html += '<span class="nav-pct">' + escapeHtml(it.pct) + "</span>";
        else if (kids.length) html += '<span class="nav-pct">' + kids.length + "</span>";
        html += "</a>";
        if (showKids && kids.length) {
          html += '<div class="nav-sub">';
          kids.forEach(function (t, i) {
            var on = ctx.topicId === t.id;
            html += '<a class="nav-sub-a' + (on ? " active" : "") + '" href="topic.html?id=' +
              encodeURIComponent(t.id) + '" title="' + escapeHtml(t.title) + '">' +
              '<em>' + (i + 1) + "</em><span>" + escapeHtml(t.title) + "</span></a>";
          });
          html += "</div>";
        }
      });
      html += "</div></div>";
    });
    return html;
  }

  function ensureTopics(cb) {
    if (AIF.topics && AIF.topics.length) { cb(); return; }
    var existing = document.querySelector('script[src="js/topics.js"]');
    if (existing) {
      existing.addEventListener("load", cb);
      setTimeout(cb, 80);
      return;
    }
    var s = document.createElement("script");
    s.src = "js/topics.js";
    s.onload = cb;
    s.onerror = cb;
    document.head.appendChild(s);
  }

  function inject() {
    if (document.getElementById("topbar")) return;
    var ctx = currentContext();

    var bar = document.createElement("header");
    bar.className = "topbar";
    bar.id = "topbar";
    bar.innerHTML =
      '<button class="burger" id="burger" type="button" aria-label="Open menu">☰</button>' +
      '<a class="brand" href="index.html">AIF-C01 <span>Lab</span></a>' +
      '<span class="meta">AI Practitioner · guide v1.1</span>' +
      '<input type="search" id="qsearch" placeholder="Filter menu…" autocomplete="off" />';
    document.body.insertBefore(bar, document.body.firstChild);

    var mask = document.createElement("div");
    mask.className = "nav-mask";
    mask.id = "nav-mask";
    document.body.insertBefore(mask, bar.nextSibling);

    var side = document.createElement("nav");
    side.className = "sidebar";
    side.id = "sidebar";
    document.body.insertBefore(side, mask.nextSibling);

    var saved = loadOpen();
    var openMap = defaultOpen(ctx);
    Object.keys(saved).forEach(function (k) { openMap[k] = saved[k]; });

    function paint() {
      side.innerHTML = buildSidebarHtml(currentContext(), openMap);
      side.querySelectorAll("[data-toggle]").forEach(function (btn) {
        btn.onclick = function (e) {
          e.preventDefault();
          var id = btn.getAttribute("data-toggle");
          openMap[id] = !(openMap[id] !== false);
          saveOpen(openMap);
          paint();
          applySearch();
        };
      });
      applySearch();
    }

    function applySearch() {
      var q = (document.getElementById("qsearch").value || "").toLowerCase().trim();
      side.querySelectorAll(".nav-block").forEach(function (block) {
        var links = block.querySelectorAll("a");
        var any = false;
        links.forEach(function (a) {
          var show = !q || a.textContent.toLowerCase().indexOf(q) !== -1;
          a.style.display = show ? "" : "none";
          if (show) any = true;
        });
        if (q) {
          block.classList.add("open");
          block.style.display = any ? "" : "none";
        } else {
          block.style.display = "";
          var gid = block.getAttribute("data-g");
          block.classList.toggle("open", openMap[gid] !== false);
        }
      });
    }

    function setMenu(on) {
      side.classList.toggle("open", on);
      mask.classList.toggle("show", on);
      document.body.classList.toggle("nav-open", on);
    }

    document.getElementById("burger").onclick = function () {
      setMenu(!side.classList.contains("open"));
    };
    mask.onclick = function () { setMenu(false); };
    document.getElementById("qsearch").addEventListener("input", applySearch);

    paint();
    AIF.markRead(ctx.cur === "topic" ? "topic" : ctx.cur);
  }

  function start() {
    ensureTopics(inject);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start);
  } else {
    start();
  }
})();
