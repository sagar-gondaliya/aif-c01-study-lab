(function () {
  window.AIF = window.AIF || {};
  var KEY = "aif-c01-lab-v1";

  function load() {
    try { return JSON.parse(localStorage.getItem(KEY)) || {}; }
    catch (e) { return {}; }
  }
  function save(st) { localStorage.setItem(KEY, JSON.stringify(st)); }

  function state() {
    var s = load();
    s.read = s.read || {};
    s.plan = s.plan || {};
    s.quiz = s.quiz || {};
    s.mocks = s.mocks || {};
    s.cards = s.cards || { known: [] };
    return s;
  }

  AIF.store = {
    get: state,
    markRead: function (id) {
      if (!id || id === "home") return;
      var s = state();
      s.read[id] = Date.now();
      save(s);
    },
    setPlan: function (id, on) {
      var s = state();
      s.plan[id] = !!on;
      save(s);
    },
    saveQuiz: function (set, rec) {
      var s = state();
      s.quiz[set] = rec;
      save(s);
    },
    saveMock: function (n, rec) {
      var s = state();
      if (!s.mocks[n]) s.mocks[n] = [];
      s.mocks[n].push(rec);
      save(s);
    },
    setCards: function (known) {
      var s = state();
      s.cards.known = known;
      save(s);
    },
    reset: function () {
      localStorage.removeItem(KEY);
    }
  };

  AIF.markRead = function (id) { AIF.store.markRead(id); };

  AIF.pct = function (num, den) {
    if (!den) return 0;
    return Math.round((num / den) * 100);
  };
})();
