/* VIA Italian Table: the poster wall's moving parts */
(function () {
  'use strict';
  var TZ = 'America/New_York';
  var RESY = 'https://resy.com/cities/worcester-ma/venues/via-italian-table';

  /* Published hours. Minutes from midnight; null = closed. */
  var HOURS = [
    null,                                                  // Sun
    { lunch: [690, 960], dinner: [960, 1260] },            // Mon
    { lunch: [690, 960], dinner: [960, 1260] },            // Tue
    { lunch: [690, 960], dinner: [960, 1260] },            // Wed
    { lunch: [690, 960], dinner: [960, 1260] },            // Thu
    { lunch: [690, 960], dinner: [960, 1320] },            // Fri
    { lunch: null,       dinner: [960, 1320] }             // Sat
  ];
  var DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

  function nowInWorcester() {
    var parts = new Intl.DateTimeFormat('en-US', {
      timeZone: TZ, year: 'numeric', month: '2-digit', day: '2-digit',
      hour: '2-digit', minute: '2-digit', hourCycle: 'h23', weekday: 'short'
    }).formatToParts(new Date());
    var o = {};
    parts.forEach(function (p) { o[p.type] = p.value; });
    var iso = o.year + '-' + o.month + '-' + o.day;
    var dow = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'].indexOf(o.weekday);
    return { iso: iso, dow: dow, mins: parseInt(o.hour, 10) * 60 + parseInt(o.minute, 10) };
  }
  function fmt(m) {
    var h = Math.floor(m / 60), mm = m % 60, ap = h >= 12 ? 'pm' : 'am';
    h = h % 12 || 12;
    return h + (mm ? ':' + (mm < 10 ? '0' : '') + mm : '') + ap;
  }
  var NOW = nowInWorcester();

  /* Open / closed status, from the published hours */
  function statusText() {
    var d = HOURS[NOW.dow], m = NOW.mins;
    if (d) {
      if (d.lunch && m >= d.lunch[0] && m < d.lunch[1]) return { open: true, text: 'Open now · lunch until ' + fmt(d.lunch[1]) };
      if (d.dinner && m >= d.dinner[0] && m < d.dinner[1]) return { open: true, text: 'Open now · dinner until ' + fmt(d.dinner[1]) };
      var first = d.lunch || d.dinner;
      if (m < first[0]) return { open: false, text: 'Opens today at ' + fmt(first[0]) + (d.lunch ? ' for lunch' : ' for dinner') };
    }
    for (var i = 1; i <= 7; i++) {
      var k = (NOW.dow + i) % 7, n = HOURS[k];
      if (n) {
        var f = n.lunch || n.dinner;
        return { open: false, text: 'Closed now · opens ' + (i === 1 ? 'tomorrow' : DAYS[k]) + ' at ' + fmt(f[0]) };
      }
    }
    return { open: false, text: 'Closed' };
  }
  document.querySelectorAll('[data-status]').forEach(function (el) {
    var s = statusText();
    el.dataset.open = String(s.open);
    var t = el.querySelector('[data-status-text]');
    if (t) t.textContent = s.text;
  });
  document.querySelectorAll('.hours tr[data-dow]').forEach(function (tr) {
    if (tr.dataset.dow.split(',').indexOf(String(NOW.dow)) > -1) tr.classList.add('is-today');
  });
  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = NOW.iso.slice(0, 4); });

  /* Posters come down when their date passes; expired ones leave a remnant */
  document.querySelectorAll('[data-end]').forEach(function (el) {
    if (el.dataset.end < NOW.iso) {
      if (el.matches('.remnant')) return;
      el.remove();
    }
  });
  document.querySelectorAll('[data-start]').forEach(function (el) {
    if (el.dataset.start > NOW.iso) el.remove();
  });
  document.querySelectorAll('.remnant[data-end]').forEach(function (el) {
    if (el.dataset.end >= NOW.iso) el.remove(); // a remnant only shows once its poster is past
  });
  document.querySelectorAll('.wall').forEach(function (wall) {
    Array.prototype.forEach.call(wall.querySelectorAll('.poster'), function (p, i) { p.style.setProperty('--i', i); });
  });

  /* Booking strip: next 21 days, Sundays closed; hands party + date to Resy */
  document.querySelectorAll('[data-book]').forEach(function (form) {
    var dateSel = form.querySelector('[name="date"]');
    if (dateSel) {
      dateSel.innerHTML = '';
      var base = new Date(NOW.iso + 'T12:00:00');
      for (var i = 0; i < 21; i++) {
        var d = new Date(base.getTime() + i * 864e5);
        var iso = d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0');
        var label = i === 0 ? 'Today' : i === 1 ? 'Tomorrow' : d.toLocaleDateString('en-US', { weekday: 'short', month: 'short', day: 'numeric' });
        var opt = new Option(d.getDay() === 0 ? label + ' · closed' : label, iso);
        if (d.getDay() === 0) opt.disabled = true;
        dateSel.add(opt);
      }
      var firstOpen = Array.prototype.find.call(dateSel.options, function (o) { return !o.disabled; });
      if (firstOpen) firstOpen.selected = true;
    }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var seats = form.querySelector('[name="seats"]').value;
      var date = dateSel ? dateSel.value : '';
      if (seats === '9+') { location.href = 'private-dining.html'; return; }
      window.location.href = RESY + '?date=' + encodeURIComponent(date) + '&seats=' + encodeURIComponent(seats);
    });
  });

  /* Tear-off tabs: the tab tears, then the link goes */
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.addEventListener('click', function (e) {
    var tab = e.target.closest('.tab');
    if (!tab || reduce || e.metaKey || e.ctrlKey || e.shiftKey || e.button !== 0) return;
    var href = tab.getAttribute('href');
    if (!href || href.charAt(0) === '#' || /^(tel|mailto):/.test(href)) { tab.classList.add('is-torn'); setTimeout(function () { tab.classList.remove('is-torn'); }, 700); return; }
    e.preventDefault();
    tab.style.setProperty('--tear', (Math.random() * 10 - 5).toFixed(1) + 'deg');
    tab.classList.add('is-torn');
    setTimeout(function () { window.location.href = href; }, 320);
  });
  window.addEventListener('pageshow', function () {
    document.querySelectorAll('.tab.is-torn').forEach(function (t) { t.classList.remove('is-torn'); });
  });

  /* Menu tabs (a real tablist; #hash opens a menu) */
  document.querySelectorAll('[role="tablist"]').forEach(function (list) {
    var tabs = Array.prototype.slice.call(list.querySelectorAll('[role="tab"]'));
    function select(t, focus) {
      tabs.forEach(function (x) {
        var on = x === t;
        x.setAttribute('aria-selected', String(on));
        x.tabIndex = on ? 0 : -1;
        var panel = document.getElementById(x.getAttribute('aria-controls'));
        if (panel) panel.hidden = !on;
      });
      if (focus) t.focus();
    }
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { select(t); if (list.dataset.hash !== undefined) history.replaceState(null, '', '#' + t.dataset.key); });
      t.addEventListener('keydown', function (e) {
        var j = e.key === 'ArrowRight' ? i + 1 : e.key === 'ArrowLeft' ? i - 1 : e.key === 'Home' ? 0 : e.key === 'End' ? tabs.length - 1 : null;
        if (j === null) return;
        e.preventDefault();
        select(tabs[(j + tabs.length) % tabs.length], true);
      });
    });
    var h = location.hash.slice(1);
    var start = tabs.find(function (t) { return t.dataset.key === h; }) || tabs.find(function (t) { return t.getAttribute('aria-selected') === 'true'; }) || tabs[0];
    if (start) select(start);
  });

  /* Logo option switch (pitch bar) */
  function setLogo(v) {
    document.documentElement.dataset.logo = v;
    document.querySelectorAll('[data-logo-pick]').forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.logoPick === v)); });
    try { localStorage.setItem('via-logo', v); } catch (e) {}
  }
  document.querySelectorAll('[data-logo-pick]').forEach(function (b) {
    b.addEventListener('click', function () { setLogo(b.dataset.logoPick); });
  });
  setLogo(document.documentElement.dataset.logo || 'b');

  /* Copy buttons (phone numbers, address) */
  document.querySelectorAll('[data-copy]').forEach(function (b) {
    b.addEventListener('click', function () {
      var text = b.dataset.copy, done = function () { var o = b.textContent; b.textContent = 'Copied'; setTimeout(function () { b.textContent = o; }, 1400); };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, function () { selectText(b); });
      } else selectText(b);
    });
  });
  function selectText(b) {
    var target = b.previousElementSibling;
    if (!target) return;
    var r = document.createRange(); r.selectNodeContents(target);
    var s = getSelection(); s.removeAllRanges(); s.addRange(r);
  }

  /* Event request form: validates here; on the live site it posts to VIA's Tripleseat lead form */
  document.querySelectorAll('[data-event-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = true, firstBad = null;
      form.querySelectorAll('[required]').forEach(function (f) {
        var err = form.querySelector('[data-err-for="' + f.id + '"]');
        var bad = !f.value.trim() || (f.type === 'email' && !/^\S+@\S+\.\S+$/.test(f.value)) || (f.type === 'number' && (+f.value < 1));
        f.setAttribute('aria-invalid', String(bad));
        if (err) err.textContent = bad ? f.dataset.msg : '';
        if (bad) { ok = false; firstBad = firstBad || f; }
      });
      if (!ok) { firstBad.focus(); return; }
      var size = +form.querySelector('#ev-guests').value;
      var room = size <= 16 ? 'the semi-private room (up to 16)' : size <= 36 ? 'the private dining room or the patio (up to 36 each)' : 'a full buyout conversation with Maria';
      var done = form.parentElement.querySelector('.form-done');
      done.querySelector('[data-room]').textContent = room;
      done.classList.add('is-shown');
      form.hidden = true;
      done.focus();
    });
  });
})();
