// Tiny horizontal bar chart for static PNG charts (rendered with tooling/tools/html-to-png.mjs).
// bars(el, {max, ticks, rows:[{label, value, start?, text, series}], refLine:{value,label}, series:{name:color}})
function bars(el, o) {
  const W = 760, L = 250, R = o.right || 70, rowH = 46, top = 34, plotW = W - L - R;
  const H = top + o.rows.length * rowH + 30;
  const x = v => L + (v / o.max) * plotW;
  let s = `<svg width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" xmlns="http://www.w3.org/2000/svg" font-family="inherit">`;
  for (const t of o.ticks) {
    s += `<line x1="${x(t)}" x2="${x(t)}" y1="${top - 8}" y2="${H - 26}" stroke="var(--grid)" stroke-width="1"/>`;
    s += `<text x="${x(t)}" y="${H - 8}" fill="var(--text-muted)" font-size="13" text-anchor="middle">${t}</text>`;
  }
  if (o.refLine) {
    const rx = x(o.refLine.value);
    s += `<line x1="${rx}" x2="${rx}" y1="${top - 14}" y2="${H - 26}" stroke="var(--text-secondary)" stroke-width="2" stroke-dasharray="5 4"/>`;
    s += `<text x="${rx + 6}" y="${top - 18}" fill="var(--text-secondary)" font-size="13">${o.refLine.label}</text>`;
  }
  o.rows.forEach((r, i) => {
    const y = top + i * rowH, bh = 22, x0 = x(r.start || 0), w = Math.max(x(r.value) - x0, 3);
    s += `<text x="${L - 12}" y="${y + bh / 2 + 5}" fill="var(--text-primary)" font-size="15" text-anchor="end">${r.label}</text>`;
    s += `<path d="M${x0},${y} h${w - 4} a4,4 0 0 1 4,4 v${bh - 8} a4,4 0 0 1 -4,4 h${-(w - 4)} z" fill="${o.series[r.series]}"/>`;
    s += `<text x="${x0 + w + 8}" y="${y + bh / 2 + 5}" fill="var(--text-primary)" font-size="15" font-weight="600" stroke="#1a1a19" stroke-width="10" stroke-linejoin="round" paint-order="stroke">${r.text}</text>`;
  });
  el.innerHTML = s + '</svg>';
  const legend = document.createElement('div'); legend.className = 'legend';
  legend.innerHTML = Object.entries(o.series).map(([n, c]) => `<span><i style="background:${c}"></i>${n}</span>`).join('');
  el.before(legend);
}
