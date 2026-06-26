/* Self-assembly signature: particles drift from disorder into a lattice.
   Embodies the group's "designing self-assembling kinetics" work.
   Static, settled lattice rendered when reduced motion is preferred. */
(function () {
  var canvas = document.getElementById("lattice");
  if (!canvas) return;
  var ctx = canvas.getContext("2d");
  var DPR = Math.min(window.devicePixelRatio || 1, 2);

  var COLS = 7, ROWS = 7;
  var INK = "#3A2A6E", TEAL = "#0E9C8E", SOFT = "#9A95A8";
  var pts = [];

  function size() {
    var r = canvas.getBoundingClientRect();
    canvas.width = r.width * DPR;
    canvas.height = r.height * DPR;
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
    return r;
  }

  function build() {
    var r = size();
    var W = r.width, H = r.height;
    var pad = W * 0.12;
    var gx = (W - pad * 2) / (COLS - 1);
    var gy = (H - pad * 2) / (ROWS - 1);
    pts = [];
    for (var i = 0; i < COLS; i++) {
      for (var j = 0; j < ROWS; j++) {
        // hexagonal offset on alternate rows -> colloidal-crystal feel
        var off = (j % 2) * gx * 0.5;
        var tx = pad + i * gx + off - (j % 2 ? gx * 0.25 : 0);
        var ty = pad + j * gy;
        if (tx < pad * 0.5 || tx > W - pad * 0.5) continue;
        var accent = ((i + j) % 6 === 0);
        var corr = (i === 3 && j === 3); // the "corrected" defect, in teal
        pts.push({
          tx: tx, ty: ty,
          x: W / 2 + (Math.random() - 0.5) * W * 0.9,
          y: H / 2 + (Math.random() - 0.5) * H * 0.9,
          r: corr ? 7 : accent ? 5.5 : 4.5,
          c: corr ? TEAL : accent ? INK : SOFT,
          ph: Math.random() * Math.PI * 2
        });
      }
    }
  }

  function bonds() {
    var r = canvas.getBoundingClientRect();
    var thr = (r.width / (COLS - 1)) * 1.15;
    ctx.lineWidth = 1;
    for (var a = 0; a < pts.length; a++) {
      for (var b = a + 1; b < pts.length; b++) {
        var dx = pts[a].x - pts[b].x, dy = pts[a].y - pts[b].y;
        var d = Math.hypot(dx, dy);
        if (d < thr) {
          var al = (1 - d / thr) * 0.5;
          ctx.strokeStyle = "rgba(58,42,110," + (al * 0.55).toFixed(3) + ")";
          ctx.beginPath();
          ctx.moveTo(pts[a].x, pts[a].y);
          ctx.lineTo(pts[b].x, pts[b].y);
          ctx.stroke();
        }
      }
    }
  }

  function draw(settleAmt) {
    var r = canvas.getBoundingClientRect();
    ctx.clearRect(0, 0, r.width, r.height);
    if (settleAmt > 0.55) bonds();
    for (var k = 0; k < pts.length; k++) {
      var p = pts[k];
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = p.c;
      ctx.globalAlpha = p.c === SOFT ? 0.85 : 1;
      ctx.fill();
      ctx.globalAlpha = 1;
    }
  }

  function settled() {
    for (var k = 0; k < pts.length; k++) { pts[k].x = pts[k].tx; pts[k].y = pts[k].ty; }
    draw(1);
  }

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  build();

  if (reduce) { settled(); }
  else {
    var t0 = null, DUR = 2200;
    function frame(ts) {
      if (!t0) t0 = ts;
      var e = Math.min((ts - t0) / DUR, 1);
      var ease = 1 - Math.pow(1 - e, 3);
      for (var k = 0; k < pts.length; k++) {
        var p = pts[k];
        var wob = (1 - ease) * Math.sin(ts / 320 + p.ph) * 6;
        p.x = p.x + (p.tx - p.x) * (0.04 + ease * 0.18) + wob * 0.04;
        p.y = p.y + (p.ty - p.y) * (0.04 + ease * 0.18) + wob * 0.04;
      }
      draw(ease);
      if (e < 1) requestAnimationFrame(frame);
      else settled();
    }
    requestAnimationFrame(frame);
  }

  var rt;
  window.addEventListener("resize", function () {
    clearTimeout(rt);
    rt = setTimeout(function () { build(); settled(); }, 150);
  });
})();

/* Mobile nav */
(function () {
  var btn = document.querySelector(".nav-toggle");
  var links = document.querySelector(".nav-links");
  if (!btn || !links) return;
  btn.addEventListener("click", function () {
    var open = links.classList.toggle("open");
    btn.setAttribute("aria-expanded", open ? "true" : "false");
    btn.textContent = open ? "close" : "menu";
  });
  links.addEventListener("click", function (e) {
    if (e.target.tagName === "A") {
      links.classList.remove("open");
      btn.setAttribute("aria-expanded", "false");
      btn.textContent = "menu";
    }
  });
})();
