const {
  SvelteComponent: It,
  assign: Kt,
  create_slot: Zt,
  detach: Et,
  element: Tt,
  get_all_dirty_from_scope: Bt,
  get_slot_changes: Dt,
  get_spread_update: Wt,
  init: Xt,
  insert: Rt,
  safe_not_equal: Gt,
  set_dynamic_element_data: Be,
  set_style: K,
  toggle_class: Q,
  transition_in: mt,
  transition_out: ht,
  update_slot_base: Ot
} = window.__gradio__svelte__internal;
function Yt(l) {
  let e, t, n;
  const i = (
    /*#slots*/
    l[18].default
  ), f = Zt(
    i,
    l,
    /*$$scope*/
    l[17],
    null
  );
  let s = [
    { "data-testid": (
      /*test_id*/
      l[7]
    ) },
    { id: (
      /*elem_id*/
      l[2]
    ) },
    {
      class: t = "block " + /*elem_classes*/
      l[3].join(" ") + " svelte-nl1om8"
    }
  ], r = {};
  for (let a = 0; a < s.length; a += 1)
    r = Kt(r, s[a]);
  return {
    c() {
      e = Tt(
        /*tag*/
        l[14]
      ), f && f.c(), Be(
        /*tag*/
        l[14]
      )(e, r), Q(
        e,
        "hidden",
        /*visible*/
        l[10] === !1
      ), Q(
        e,
        "padded",
        /*padding*/
        l[6]
      ), Q(
        e,
        "border_focus",
        /*border_mode*/
        l[5] === "focus"
      ), Q(
        e,
        "border_contrast",
        /*border_mode*/
        l[5] === "contrast"
      ), Q(e, "hide-container", !/*explicit_call*/
      l[8] && !/*container*/
      l[9]), K(
        e,
        "height",
        /*get_dimension*/
        l[15](
          /*height*/
          l[0]
        )
      ), K(e, "width", typeof /*width*/
      l[1] == "number" ? `calc(min(${/*width*/
      l[1]}px, 100%))` : (
        /*get_dimension*/
        l[15](
          /*width*/
          l[1]
        )
      )), K(
        e,
        "border-style",
        /*variant*/
        l[4]
      ), K(
        e,
        "overflow",
        /*allow_overflow*/
        l[11] ? "visible" : "hidden"
      ), K(
        e,
        "flex-grow",
        /*scale*/
        l[12]
      ), K(e, "min-width", `calc(min(${/*min_width*/
      l[13]}px, 100%))`), K(e, "border-width", "var(--block-border-width)");
    },
    m(a, o) {
      Rt(a, e, o), f && f.m(e, null), n = !0;
    },
    p(a, o) {
      f && f.p && (!n || o & /*$$scope*/
      131072) && Ot(
        f,
        i,
        a,
        /*$$scope*/
        a[17],
        n ? Dt(
          i,
          /*$$scope*/
          a[17],
          o,
          null
        ) : Bt(
          /*$$scope*/
          a[17]
        ),
        null
      ), Be(
        /*tag*/
        a[14]
      )(e, r = Wt(s, [
        (!n || o & /*test_id*/
        128) && { "data-testid": (
          /*test_id*/
          a[7]
        ) },
        (!n || o & /*elem_id*/
        4) && { id: (
          /*elem_id*/
          a[2]
        ) },
        (!n || o & /*elem_classes*/
        8 && t !== (t = "block " + /*elem_classes*/
        a[3].join(" ") + " svelte-nl1om8")) && { class: t }
      ])), Q(
        e,
        "hidden",
        /*visible*/
        a[10] === !1
      ), Q(
        e,
        "padded",
        /*padding*/
        a[6]
      ), Q(
        e,
        "border_focus",
        /*border_mode*/
        a[5] === "focus"
      ), Q(
        e,
        "border_contrast",
        /*border_mode*/
        a[5] === "contrast"
      ), Q(e, "hide-container", !/*explicit_call*/
      a[8] && !/*container*/
      a[9]), o & /*height*/
      1 && K(
        e,
        "height",
        /*get_dimension*/
        a[15](
          /*height*/
          a[0]
        )
      ), o & /*width*/
      2 && K(e, "width", typeof /*width*/
      a[1] == "number" ? `calc(min(${/*width*/
      a[1]}px, 100%))` : (
        /*get_dimension*/
        a[15](
          /*width*/
          a[1]
        )
      )), o & /*variant*/
      16 && K(
        e,
        "border-style",
        /*variant*/
        a[4]
      ), o & /*allow_overflow*/
      2048 && K(
        e,
        "overflow",
        /*allow_overflow*/
        a[11] ? "visible" : "hidden"
      ), o & /*scale*/
      4096 && K(
        e,
        "flex-grow",
        /*scale*/
        a[12]
      ), o & /*min_width*/
      8192 && K(e, "min-width", `calc(min(${/*min_width*/
      a[13]}px, 100%))`);
    },
    i(a) {
      n || (mt(f, a), n = !0);
    },
    o(a) {
      ht(f, a), n = !1;
    },
    d(a) {
      a && Et(e), f && f.d(a);
    }
  };
}
function Ut(l) {
  let e, t = (
    /*tag*/
    l[14] && Yt(l)
  );
  return {
    c() {
      t && t.c();
    },
    m(n, i) {
      t && t.m(n, i), e = !0;
    },
    p(n, [i]) {
      /*tag*/
      n[14] && t.p(n, i);
    },
    i(n) {
      e || (mt(t, n), e = !0);
    },
    o(n) {
      ht(t, n), e = !1;
    },
    d(n) {
      t && t.d(n);
    }
  };
}
function Ht(l, e, t) {
  let { $$slots: n = {}, $$scope: i } = e, { height: f = void 0 } = e, { width: s = void 0 } = e, { elem_id: r = "" } = e, { elem_classes: a = [] } = e, { variant: o = "solid" } = e, { border_mode: c = "base" } = e, { padding: u = !0 } = e, { type: p = "normal" } = e, { test_id: m = void 0 } = e, { explicit_call: y = !1 } = e, { container: F = !0 } = e, { visible: v = !0 } = e, { allow_overflow: M = !0 } = e, { scale: _ = null } = e, { min_width: d = 0 } = e, C = p === "fieldset" ? "fieldset" : "div";
  const S = (b) => {
    if (b !== void 0) {
      if (typeof b == "number")
        return b + "px";
      if (typeof b == "string")
        return b;
    }
  };
  return l.$$set = (b) => {
    "height" in b && t(0, f = b.height), "width" in b && t(1, s = b.width), "elem_id" in b && t(2, r = b.elem_id), "elem_classes" in b && t(3, a = b.elem_classes), "variant" in b && t(4, o = b.variant), "border_mode" in b && t(5, c = b.border_mode), "padding" in b && t(6, u = b.padding), "type" in b && t(16, p = b.type), "test_id" in b && t(7, m = b.test_id), "explicit_call" in b && t(8, y = b.explicit_call), "container" in b && t(9, F = b.container), "visible" in b && t(10, v = b.visible), "allow_overflow" in b && t(11, M = b.allow_overflow), "scale" in b && t(12, _ = b.scale), "min_width" in b && t(13, d = b.min_width), "$$scope" in b && t(17, i = b.$$scope);
  }, [
    f,
    s,
    r,
    a,
    o,
    c,
    u,
    m,
    y,
    F,
    v,
    M,
    _,
    d,
    C,
    S,
    p,
    i,
    n
  ];
}
class Jt extends It {
  constructor(e) {
    super(), Xt(this, e, Ht, Ut, Gt, {
      height: 0,
      width: 1,
      elem_id: 2,
      elem_classes: 3,
      variant: 4,
      border_mode: 5,
      padding: 6,
      type: 16,
      test_id: 7,
      explicit_call: 8,
      container: 9,
      visible: 10,
      allow_overflow: 11,
      scale: 12,
      min_width: 13
    });
  }
}
const {
  SvelteComponent: Qt,
  append: je,
  attr: ne,
  bubble: xt,
  create_component: $t,
  destroy_component: el,
  detach: bt,
  element: Ie,
  init: tl,
  insert: gt,
  listen: ll,
  mount_component: nl,
  safe_not_equal: il,
  set_data: fl,
  set_style: _e,
  space: sl,
  text: ol,
  toggle_class: j,
  transition_in: al,
  transition_out: rl
} = window.__gradio__svelte__internal;
function De(l) {
  let e, t;
  return {
    c() {
      e = Ie("span"), t = ol(
        /*label*/
        l[1]
      ), ne(e, "class", "svelte-1lrphxw");
    },
    m(n, i) {
      gt(n, e, i), je(e, t);
    },
    p(n, i) {
      i & /*label*/
      2 && fl(
        t,
        /*label*/
        n[1]
      );
    },
    d(n) {
      n && bt(e);
    }
  };
}
function cl(l) {
  let e, t, n, i, f, s, r, a = (
    /*show_label*/
    l[2] && De(l)
  );
  return i = new /*Icon*/
  l[0]({}), {
    c() {
      e = Ie("button"), a && a.c(), t = sl(), n = Ie("div"), $t(i.$$.fragment), ne(n, "class", "svelte-1lrphxw"), j(
        n,
        "small",
        /*size*/
        l[4] === "small"
      ), j(
        n,
        "large",
        /*size*/
        l[4] === "large"
      ), j(
        n,
        "medium",
        /*size*/
        l[4] === "medium"
      ), e.disabled = /*disabled*/
      l[7], ne(
        e,
        "aria-label",
        /*label*/
        l[1]
      ), ne(
        e,
        "aria-haspopup",
        /*hasPopup*/
        l[8]
      ), ne(
        e,
        "title",
        /*label*/
        l[1]
      ), ne(e, "class", "svelte-1lrphxw"), j(
        e,
        "pending",
        /*pending*/
        l[3]
      ), j(
        e,
        "padded",
        /*padded*/
        l[5]
      ), j(
        e,
        "highlight",
        /*highlight*/
        l[6]
      ), j(
        e,
        "transparent",
        /*transparent*/
        l[9]
      ), _e(e, "color", !/*disabled*/
      l[7] && /*_color*/
      l[12] ? (
        /*_color*/
        l[12]
      ) : "var(--block-label-text-color)"), _e(e, "--bg-color", /*disabled*/
      l[7] ? "auto" : (
        /*background*/
        l[10]
      )), _e(
        e,
        "margin-left",
        /*offset*/
        l[11] + "px"
      );
    },
    m(o, c) {
      gt(o, e, c), a && a.m(e, null), je(e, t), je(e, n), nl(i, n, null), f = !0, s || (r = ll(
        e,
        "click",
        /*click_handler*/
        l[14]
      ), s = !0);
    },
    p(o, [c]) {
      /*show_label*/
      o[2] ? a ? a.p(o, c) : (a = De(o), a.c(), a.m(e, t)) : a && (a.d(1), a = null), (!f || c & /*size*/
      16) && j(
        n,
        "small",
        /*size*/
        o[4] === "small"
      ), (!f || c & /*size*/
      16) && j(
        n,
        "large",
        /*size*/
        o[4] === "large"
      ), (!f || c & /*size*/
      16) && j(
        n,
        "medium",
        /*size*/
        o[4] === "medium"
      ), (!f || c & /*disabled*/
      128) && (e.disabled = /*disabled*/
      o[7]), (!f || c & /*label*/
      2) && ne(
        e,
        "aria-label",
        /*label*/
        o[1]
      ), (!f || c & /*hasPopup*/
      256) && ne(
        e,
        "aria-haspopup",
        /*hasPopup*/
        o[8]
      ), (!f || c & /*label*/
      2) && ne(
        e,
        "title",
        /*label*/
        o[1]
      ), (!f || c & /*pending*/
      8) && j(
        e,
        "pending",
        /*pending*/
        o[3]
      ), (!f || c & /*padded*/
      32) && j(
        e,
        "padded",
        /*padded*/
        o[5]
      ), (!f || c & /*highlight*/
      64) && j(
        e,
        "highlight",
        /*highlight*/
        o[6]
      ), (!f || c & /*transparent*/
      512) && j(
        e,
        "transparent",
        /*transparent*/
        o[9]
      ), c & /*disabled, _color*/
      4224 && _e(e, "color", !/*disabled*/
      o[7] && /*_color*/
      o[12] ? (
        /*_color*/
        o[12]
      ) : "var(--block-label-text-color)"), c & /*disabled, background*/
      1152 && _e(e, "--bg-color", /*disabled*/
      o[7] ? "auto" : (
        /*background*/
        o[10]
      )), c & /*offset*/
      2048 && _e(
        e,
        "margin-left",
        /*offset*/
        o[11] + "px"
      );
    },
    i(o) {
      f || (al(i.$$.fragment, o), f = !0);
    },
    o(o) {
      rl(i.$$.fragment, o), f = !1;
    },
    d(o) {
      o && bt(e), a && a.d(), el(i), s = !1, r();
    }
  };
}
function ul(l, e, t) {
  let n, { Icon: i } = e, { label: f = "" } = e, { show_label: s = !1 } = e, { pending: r = !1 } = e, { size: a = "small" } = e, { padded: o = !0 } = e, { highlight: c = !1 } = e, { disabled: u = !1 } = e, { hasPopup: p = !1 } = e, { color: m = "var(--block-label-text-color)" } = e, { transparent: y = !1 } = e, { background: F = "var(--background-fill-primary)" } = e, { offset: v = 0 } = e;
  function M(_) {
    xt.call(this, l, _);
  }
  return l.$$set = (_) => {
    "Icon" in _ && t(0, i = _.Icon), "label" in _ && t(1, f = _.label), "show_label" in _ && t(2, s = _.show_label), "pending" in _ && t(3, r = _.pending), "size" in _ && t(4, a = _.size), "padded" in _ && t(5, o = _.padded), "highlight" in _ && t(6, c = _.highlight), "disabled" in _ && t(7, u = _.disabled), "hasPopup" in _ && t(8, p = _.hasPopup), "color" in _ && t(13, m = _.color), "transparent" in _ && t(9, y = _.transparent), "background" in _ && t(10, F = _.background), "offset" in _ && t(11, v = _.offset);
  }, l.$$.update = () => {
    l.$$.dirty & /*highlight, color*/
    8256 && t(12, n = c ? "var(--color-accent)" : m);
  }, [
    i,
    f,
    s,
    r,
    a,
    o,
    c,
    u,
    p,
    y,
    F,
    v,
    n,
    m,
    M
  ];
}
class _l extends Qt {
  constructor(e) {
    super(), tl(this, e, ul, cl, il, {
      Icon: 0,
      label: 1,
      show_label: 2,
      pending: 3,
      size: 4,
      padded: 5,
      highlight: 6,
      disabled: 7,
      hasPopup: 8,
      color: 13,
      transparent: 9,
      background: 10,
      offset: 11
    });
  }
}
const {
  SvelteComponent: dl,
  append: Se,
  attr: X,
  detach: ml,
  init: hl,
  insert: bl,
  noop: Ve,
  safe_not_equal: gl,
  set_style: x,
  svg_element: ye
} = window.__gradio__svelte__internal;
function wl(l) {
  let e, t, n, i;
  return {
    c() {
      e = ye("svg"), t = ye("g"), n = ye("path"), i = ye("path"), X(n, "d", "M18,6L6.087,17.913"), x(n, "fill", "none"), x(n, "fill-rule", "nonzero"), x(n, "stroke-width", "2px"), X(t, "transform", "matrix(1.14096,-0.140958,-0.140958,1.14096,-0.0559523,0.0559523)"), X(i, "d", "M4.364,4.364L19.636,19.636"), x(i, "fill", "none"), x(i, "fill-rule", "nonzero"), x(i, "stroke-width", "2px"), X(e, "width", "100%"), X(e, "height", "100%"), X(e, "viewBox", "0 0 24 24"), X(e, "version", "1.1"), X(e, "xmlns", "http://www.w3.org/2000/svg"), X(e, "xmlns:xlink", "http://www.w3.org/1999/xlink"), X(e, "xml:space", "preserve"), X(e, "stroke", "currentColor"), x(e, "fill-rule", "evenodd"), x(e, "clip-rule", "evenodd"), x(e, "stroke-linecap", "round"), x(e, "stroke-linejoin", "round");
    },
    m(f, s) {
      bl(f, e, s), Se(e, t), Se(t, n), Se(e, i);
    },
    p: Ve,
    i: Ve,
    o: Ve,
    d(f) {
      f && ml(e);
    }
  };
}
class kl extends dl {
  constructor(e) {
    super(), hl(this, e, null, wl, gl, {});
  }
}
const pl = [
  { color: "red", primary: 600, secondary: 100 },
  { color: "green", primary: 600, secondary: 100 },
  { color: "blue", primary: 600, secondary: 100 },
  { color: "yellow", primary: 500, secondary: 100 },
  { color: "purple", primary: 600, secondary: 100 },
  { color: "teal", primary: 600, secondary: 100 },
  { color: "orange", primary: 600, secondary: 100 },
  { color: "cyan", primary: 600, secondary: 100 },
  { color: "lime", primary: 500, secondary: 100 },
  { color: "pink", primary: 600, secondary: 100 }
], We = {
  inherit: "inherit",
  current: "currentColor",
  transparent: "transparent",
  black: "#000",
  white: "#fff",
  slate: {
    50: "#f8fafc",
    100: "#f1f5f9",
    200: "#e2e8f0",
    300: "#cbd5e1",
    400: "#94a3b8",
    500: "#64748b",
    600: "#475569",
    700: "#334155",
    800: "#1e293b",
    900: "#0f172a",
    950: "#020617"
  },
  gray: {
    50: "#f9fafb",
    100: "#f3f4f6",
    200: "#e5e7eb",
    300: "#d1d5db",
    400: "#9ca3af",
    500: "#6b7280",
    600: "#4b5563",
    700: "#374151",
    800: "#1f2937",
    900: "#111827",
    950: "#030712"
  },
  zinc: {
    50: "#fafafa",
    100: "#f4f4f5",
    200: "#e4e4e7",
    300: "#d4d4d8",
    400: "#a1a1aa",
    500: "#71717a",
    600: "#52525b",
    700: "#3f3f46",
    800: "#27272a",
    900: "#18181b",
    950: "#09090b"
  },
  neutral: {
    50: "#fafafa",
    100: "#f5f5f5",
    200: "#e5e5e5",
    300: "#d4d4d4",
    400: "#a3a3a3",
    500: "#737373",
    600: "#525252",
    700: "#404040",
    800: "#262626",
    900: "#171717",
    950: "#0a0a0a"
  },
  stone: {
    50: "#fafaf9",
    100: "#f5f5f4",
    200: "#e7e5e4",
    300: "#d6d3d1",
    400: "#a8a29e",
    500: "#78716c",
    600: "#57534e",
    700: "#44403c",
    800: "#292524",
    900: "#1c1917",
    950: "#0c0a09"
  },
  red: {
    50: "#fef2f2",
    100: "#fee2e2",
    200: "#fecaca",
    300: "#fca5a5",
    400: "#f87171",
    500: "#ef4444",
    600: "#dc2626",
    700: "#b91c1c",
    800: "#991b1b",
    900: "#7f1d1d",
    950: "#450a0a"
  },
  orange: {
    50: "#fff7ed",
    100: "#ffedd5",
    200: "#fed7aa",
    300: "#fdba74",
    400: "#fb923c",
    500: "#f97316",
    600: "#ea580c",
    700: "#c2410c",
    800: "#9a3412",
    900: "#7c2d12",
    950: "#431407"
  },
  amber: {
    50: "#fffbeb",
    100: "#fef3c7",
    200: "#fde68a",
    300: "#fcd34d",
    400: "#fbbf24",
    500: "#f59e0b",
    600: "#d97706",
    700: "#b45309",
    800: "#92400e",
    900: "#78350f",
    950: "#451a03"
  },
  yellow: {
    50: "#fefce8",
    100: "#fef9c3",
    200: "#fef08a",
    300: "#fde047",
    400: "#facc15",
    500: "#eab308",
    600: "#ca8a04",
    700: "#a16207",
    800: "#854d0e",
    900: "#713f12",
    950: "#422006"
  },
  lime: {
    50: "#f7fee7",
    100: "#ecfccb",
    200: "#d9f99d",
    300: "#bef264",
    400: "#a3e635",
    500: "#84cc16",
    600: "#65a30d",
    700: "#4d7c0f",
    800: "#3f6212",
    900: "#365314",
    950: "#1a2e05"
  },
  green: {
    50: "#f0fdf4",
    100: "#dcfce7",
    200: "#bbf7d0",
    300: "#86efac",
    400: "#4ade80",
    500: "#22c55e",
    600: "#16a34a",
    700: "#15803d",
    800: "#166534",
    900: "#14532d",
    950: "#052e16"
  },
  emerald: {
    50: "#ecfdf5",
    100: "#d1fae5",
    200: "#a7f3d0",
    300: "#6ee7b7",
    400: "#34d399",
    500: "#10b981",
    600: "#059669",
    700: "#047857",
    800: "#065f46",
    900: "#064e3b",
    950: "#022c22"
  },
  teal: {
    50: "#f0fdfa",
    100: "#ccfbf1",
    200: "#99f6e4",
    300: "#5eead4",
    400: "#2dd4bf",
    500: "#14b8a6",
    600: "#0d9488",
    700: "#0f766e",
    800: "#115e59",
    900: "#134e4a",
    950: "#042f2e"
  },
  cyan: {
    50: "#ecfeff",
    100: "#cffafe",
    200: "#a5f3fc",
    300: "#67e8f9",
    400: "#22d3ee",
    500: "#06b6d4",
    600: "#0891b2",
    700: "#0e7490",
    800: "#155e75",
    900: "#164e63",
    950: "#083344"
  },
  sky: {
    50: "#f0f9ff",
    100: "#e0f2fe",
    200: "#bae6fd",
    300: "#7dd3fc",
    400: "#38bdf8",
    500: "#0ea5e9",
    600: "#0284c7",
    700: "#0369a1",
    800: "#075985",
    900: "#0c4a6e",
    950: "#082f49"
  },
  blue: {
    50: "#eff6ff",
    100: "#dbeafe",
    200: "#bfdbfe",
    300: "#93c5fd",
    400: "#60a5fa",
    500: "#3b82f6",
    600: "#2563eb",
    700: "#1d4ed8",
    800: "#1e40af",
    900: "#1e3a8a",
    950: "#172554"
  },
  indigo: {
    50: "#eef2ff",
    100: "#e0e7ff",
    200: "#c7d2fe",
    300: "#a5b4fc",
    400: "#818cf8",
    500: "#6366f1",
    600: "#4f46e5",
    700: "#4338ca",
    800: "#3730a3",
    900: "#312e81",
    950: "#1e1b4b"
  },
  violet: {
    50: "#f5f3ff",
    100: "#ede9fe",
    200: "#ddd6fe",
    300: "#c4b5fd",
    400: "#a78bfa",
    500: "#8b5cf6",
    600: "#7c3aed",
    700: "#6d28d9",
    800: "#5b21b6",
    900: "#4c1d95",
    950: "#2e1065"
  },
  purple: {
    50: "#faf5ff",
    100: "#f3e8ff",
    200: "#e9d5ff",
    300: "#d8b4fe",
    400: "#c084fc",
    500: "#a855f7",
    600: "#9333ea",
    700: "#7e22ce",
    800: "#6b21a8",
    900: "#581c87",
    950: "#3b0764"
  },
  fuchsia: {
    50: "#fdf4ff",
    100: "#fae8ff",
    200: "#f5d0fe",
    300: "#f0abfc",
    400: "#e879f9",
    500: "#d946ef",
    600: "#c026d3",
    700: "#a21caf",
    800: "#86198f",
    900: "#701a75",
    950: "#4a044e"
  },
  pink: {
    50: "#fdf2f8",
    100: "#fce7f3",
    200: "#fbcfe8",
    300: "#f9a8d4",
    400: "#f472b6",
    500: "#ec4899",
    600: "#db2777",
    700: "#be185d",
    800: "#9d174d",
    900: "#831843",
    950: "#500724"
  },
  rose: {
    50: "#fff1f2",
    100: "#ffe4e6",
    200: "#fecdd3",
    300: "#fda4af",
    400: "#fb7185",
    500: "#f43f5e",
    600: "#e11d48",
    700: "#be123c",
    800: "#9f1239",
    900: "#881337",
    950: "#4c0519"
  }
};
pl.reduce(
  (l, { color: e, primary: t, secondary: n }) => ({
    ...l,
    [e]: {
      primary: We[e][t],
      secondary: We[e][n]
    }
  }),
  {}
);
function me(l) {
  let e = ["", "k", "M", "G", "T", "P", "E", "Z"], t = 0;
  for (; l > 1e3 && t < e.length - 1; )
    l /= 1e3, t++;
  let n = e[t];
  return (Number.isInteger(l) ? l : l.toFixed(1)) + n;
}
function qe() {
}
function yl(l, e) {
  return l != l ? e == e : l !== e || l && typeof l == "object" || typeof l == "function";
}
const wt = typeof window < "u";
let Xe = wt ? () => window.performance.now() : () => Date.now(), kt = wt ? (l) => requestAnimationFrame(l) : qe;
const he = /* @__PURE__ */ new Set();
function pt(l) {
  he.forEach((e) => {
    e.c(l) || (he.delete(e), e.f());
  }), he.size !== 0 && kt(pt);
}
function vl(l) {
  let e;
  return he.size === 0 && kt(pt), {
    promise: new Promise((t) => {
      he.add(e = { c: l, f: t });
    }),
    abort() {
      he.delete(e);
    }
  };
}
const de = [];
function Cl(l, e = qe) {
  let t;
  const n = /* @__PURE__ */ new Set();
  function i(r) {
    if (yl(l, r) && (l = r, t)) {
      const a = !de.length;
      for (const o of n)
        o[1](), de.push(o, l);
      if (a) {
        for (let o = 0; o < de.length; o += 2)
          de[o][0](de[o + 1]);
        de.length = 0;
      }
    }
  }
  function f(r) {
    i(r(l));
  }
  function s(r, a = qe) {
    const o = [r, a];
    return n.add(o), n.size === 1 && (t = e(i, f) || qe), r(l), () => {
      n.delete(o), n.size === 0 && t && (t(), t = null);
    };
  }
  return { set: i, update: f, subscribe: s };
}
function Re(l) {
  return Object.prototype.toString.call(l) === "[object Date]";
}
function Ke(l, e, t, n) {
  if (typeof t == "number" || Re(t)) {
    const i = n - t, f = (t - e) / (l.dt || 1 / 60), s = l.opts.stiffness * i, r = l.opts.damping * f, a = (s - r) * l.inv_mass, o = (f + a) * l.dt;
    return Math.abs(o) < l.opts.precision && Math.abs(i) < l.opts.precision ? n : (l.settled = !1, Re(t) ? new Date(t.getTime() + o) : t + o);
  } else {
    if (Array.isArray(t))
      return t.map(
        (i, f) => Ke(l, e[f], t[f], n[f])
      );
    if (typeof t == "object") {
      const i = {};
      for (const f in t)
        i[f] = Ke(l, e[f], t[f], n[f]);
      return i;
    } else
      throw new Error(`Cannot spring ${typeof t} values`);
  }
}
function Ge(l, e = {}) {
  const t = Cl(l), { stiffness: n = 0.15, damping: i = 0.8, precision: f = 0.01 } = e;
  let s, r, a, o = l, c = l, u = 1, p = 0, m = !1;
  function y(v, M = {}) {
    c = v;
    const _ = a = {};
    return l == null || M.hard || F.stiffness >= 1 && F.damping >= 1 ? (m = !0, s = Xe(), o = v, t.set(l = c), Promise.resolve()) : (M.soft && (p = 1 / ((M.soft === !0 ? 0.5 : +M.soft) * 60), u = 0), r || (s = Xe(), m = !1, r = vl((d) => {
      if (m)
        return m = !1, r = null, !1;
      u = Math.min(u + p, 1);
      const C = {
        inv_mass: u,
        opts: F,
        settled: !0,
        dt: (d - s) * 60 / 1e3
      }, S = Ke(C, o, l, c);
      return s = d, o = l, t.set(l = S), C.settled && (r = null), !C.settled;
    })), new Promise((d) => {
      r.promise.then(() => {
        _ === a && d();
      });
    }));
  }
  const F = {
    set: y,
    update: (v, M) => y(v(c, l), M),
    subscribe: t.subscribe,
    stiffness: n,
    damping: i,
    precision: f
  };
  return F;
}
const {
  SvelteComponent: ql,
  append: R,
  attr: q,
  component_subscribe: Oe,
  detach: Fl,
  element: Nl,
  init: Ml,
  insert: Ll,
  noop: Ye,
  safe_not_equal: zl,
  set_style: ve,
  svg_element: G,
  toggle_class: Ue
} = window.__gradio__svelte__internal, { onMount: Sl } = window.__gradio__svelte__internal;
function Vl(l) {
  let e, t, n, i, f, s, r, a, o, c, u, p;
  return {
    c() {
      e = Nl("div"), t = G("svg"), n = G("g"), i = G("path"), f = G("path"), s = G("path"), r = G("path"), a = G("g"), o = G("path"), c = G("path"), u = G("path"), p = G("path"), q(i, "d", "M255.926 0.754768L509.702 139.936V221.027L255.926 81.8465V0.754768Z"), q(i, "fill", "#FF7C00"), q(i, "fill-opacity", "0.4"), q(i, "class", "svelte-43sxxs"), q(f, "d", "M509.69 139.936L254.981 279.641V361.255L509.69 221.55V139.936Z"), q(f, "fill", "#FF7C00"), q(f, "class", "svelte-43sxxs"), q(s, "d", "M0.250138 139.937L254.981 279.641V361.255L0.250138 221.55V139.937Z"), q(s, "fill", "#FF7C00"), q(s, "fill-opacity", "0.4"), q(s, "class", "svelte-43sxxs"), q(r, "d", "M255.923 0.232622L0.236328 139.936V221.55L255.923 81.8469V0.232622Z"), q(r, "fill", "#FF7C00"), q(r, "class", "svelte-43sxxs"), ve(n, "transform", "translate(" + /*$top*/
      l[1][0] + "px, " + /*$top*/
      l[1][1] + "px)"), q(o, "d", "M255.926 141.5L509.702 280.681V361.773L255.926 222.592V141.5Z"), q(o, "fill", "#FF7C00"), q(o, "fill-opacity", "0.4"), q(o, "class", "svelte-43sxxs"), q(c, "d", "M509.69 280.679L254.981 420.384V501.998L509.69 362.293V280.679Z"), q(c, "fill", "#FF7C00"), q(c, "class", "svelte-43sxxs"), q(u, "d", "M0.250138 280.681L254.981 420.386V502L0.250138 362.295V280.681Z"), q(u, "fill", "#FF7C00"), q(u, "fill-opacity", "0.4"), q(u, "class", "svelte-43sxxs"), q(p, "d", "M255.923 140.977L0.236328 280.68V362.294L255.923 222.591V140.977Z"), q(p, "fill", "#FF7C00"), q(p, "class", "svelte-43sxxs"), ve(a, "transform", "translate(" + /*$bottom*/
      l[2][0] + "px, " + /*$bottom*/
      l[2][1] + "px)"), q(t, "viewBox", "-1200 -1200 3000 3000"), q(t, "fill", "none"), q(t, "xmlns", "http://www.w3.org/2000/svg"), q(t, "class", "svelte-43sxxs"), q(e, "class", "svelte-43sxxs"), Ue(
        e,
        "margin",
        /*margin*/
        l[0]
      );
    },
    m(m, y) {
      Ll(m, e, y), R(e, t), R(t, n), R(n, i), R(n, f), R(n, s), R(n, r), R(t, a), R(a, o), R(a, c), R(a, u), R(a, p);
    },
    p(m, [y]) {
      y & /*$top*/
      2 && ve(n, "transform", "translate(" + /*$top*/
      m[1][0] + "px, " + /*$top*/
      m[1][1] + "px)"), y & /*$bottom*/
      4 && ve(a, "transform", "translate(" + /*$bottom*/
      m[2][0] + "px, " + /*$bottom*/
      m[2][1] + "px)"), y & /*margin*/
      1 && Ue(
        e,
        "margin",
        /*margin*/
        m[0]
      );
    },
    i: Ye,
    o: Ye,
    d(m) {
      m && Fl(e);
    }
  };
}
function Al(l, e, t) {
  let n, i;
  var f = this && this.__awaiter || function(m, y, F, v) {
    function M(_) {
      return _ instanceof F ? _ : new F(function(d) {
        d(_);
      });
    }
    return new (F || (F = Promise))(function(_, d) {
      function C(z) {
        try {
          b(v.next(z));
        } catch (V) {
          d(V);
        }
      }
      function S(z) {
        try {
          b(v.throw(z));
        } catch (V) {
          d(V);
        }
      }
      function b(z) {
        z.done ? _(z.value) : M(z.value).then(C, S);
      }
      b((v = v.apply(m, y || [])).next());
    });
  };
  let { margin: s = !0 } = e;
  const r = Ge([0, 0]);
  Oe(l, r, (m) => t(1, n = m));
  const a = Ge([0, 0]);
  Oe(l, a, (m) => t(2, i = m));
  let o;
  function c() {
    return f(this, void 0, void 0, function* () {
      yield Promise.all([r.set([125, 140]), a.set([-125, -140])]), yield Promise.all([r.set([-125, 140]), a.set([125, -140])]), yield Promise.all([r.set([-125, 0]), a.set([125, -0])]), yield Promise.all([r.set([125, 0]), a.set([-125, 0])]);
    });
  }
  function u() {
    return f(this, void 0, void 0, function* () {
      yield c(), o || u();
    });
  }
  function p() {
    return f(this, void 0, void 0, function* () {
      yield Promise.all([r.set([125, 0]), a.set([-125, 0])]), u();
    });
  }
  return Sl(() => (p(), () => o = !0)), l.$$set = (m) => {
    "margin" in m && t(0, s = m.margin);
  }, [s, n, i, r, a];
}
class Pl extends ql {
  constructor(e) {
    super(), Ml(this, e, Al, Vl, zl, { margin: 0 });
  }
}
const {
  SvelteComponent: jl,
  append: ce,
  attr: Y,
  binding_callbacks: He,
  check_outros: Ze,
  create_component: yt,
  create_slot: vt,
  destroy_component: Ct,
  destroy_each: qt,
  detach: w,
  element: $,
  empty: be,
  ensure_array_like: Fe,
  get_all_dirty_from_scope: Ft,
  get_slot_changes: Nt,
  group_outros: Ee,
  init: Il,
  insert: k,
  mount_component: Mt,
  noop: Te,
  safe_not_equal: Kl,
  set_data: D,
  set_style: se,
  space: B,
  text: N,
  toggle_class: T,
  transition_in: O,
  transition_out: ee,
  update_slot_base: Lt
} = window.__gradio__svelte__internal, { tick: Zl } = window.__gradio__svelte__internal, { onDestroy: El } = window.__gradio__svelte__internal, { createEventDispatcher: Tl } = window.__gradio__svelte__internal, Bl = (l) => ({}), Je = (l) => ({}), Dl = (l) => ({}), Qe = (l) => ({});
function xe(l, e, t) {
  const n = l.slice();
  return n[41] = e[t], n[43] = t, n;
}
function $e(l, e, t) {
  const n = l.slice();
  return n[41] = e[t], n;
}
function Wl(l) {
  let e, t, n, i, f = (
    /*i18n*/
    l[1]("common.error") + ""
  ), s, r, a;
  t = new _l({
    props: {
      Icon: kl,
      label: (
        /*i18n*/
        l[1]("common.clear")
      ),
      disabled: !1
    }
  }), t.$on(
    "click",
    /*click_handler*/
    l[32]
  );
  const o = (
    /*#slots*/
    l[30].error
  ), c = vt(
    o,
    l,
    /*$$scope*/
    l[29],
    Je
  );
  return {
    c() {
      e = $("div"), yt(t.$$.fragment), n = B(), i = $("span"), s = N(f), r = B(), c && c.c(), Y(e, "class", "clear-status svelte-16nch4a"), Y(i, "class", "error svelte-16nch4a");
    },
    m(u, p) {
      k(u, e, p), Mt(t, e, null), k(u, n, p), k(u, i, p), ce(i, s), k(u, r, p), c && c.m(u, p), a = !0;
    },
    p(u, p) {
      const m = {};
      p[0] & /*i18n*/
      2 && (m.label = /*i18n*/
      u[1]("common.clear")), t.$set(m), (!a || p[0] & /*i18n*/
      2) && f !== (f = /*i18n*/
      u[1]("common.error") + "") && D(s, f), c && c.p && (!a || p[0] & /*$$scope*/
      536870912) && Lt(
        c,
        o,
        u,
        /*$$scope*/
        u[29],
        a ? Nt(
          o,
          /*$$scope*/
          u[29],
          p,
          Bl
        ) : Ft(
          /*$$scope*/
          u[29]
        ),
        Je
      );
    },
    i(u) {
      a || (O(t.$$.fragment, u), O(c, u), a = !0);
    },
    o(u) {
      ee(t.$$.fragment, u), ee(c, u), a = !1;
    },
    d(u) {
      u && (w(e), w(n), w(i), w(r)), Ct(t), c && c.d(u);
    }
  };
}
function Xl(l) {
  let e, t, n, i, f, s, r, a, o, c = (
    /*variant*/
    l[8] === "default" && /*show_eta_bar*/
    l[18] && /*show_progress*/
    l[6] === "full" && et(l)
  );
  function u(d, C) {
    if (
      /*progress*/
      d[7]
    ) return Ol;
    if (
      /*queue_position*/
      d[2] !== null && /*queue_size*/
      d[3] !== void 0 && /*queue_position*/
      d[2] >= 0
    ) return Gl;
    if (
      /*queue_position*/
      d[2] === 0
    ) return Rl;
  }
  let p = u(l), m = p && p(l), y = (
    /*timer*/
    l[5] && nt(l)
  );
  const F = [Jl, Hl], v = [];
  function M(d, C) {
    return (
      /*last_progress_level*/
      d[15] != null ? 0 : (
        /*show_progress*/
        d[6] === "full" ? 1 : -1
      )
    );
  }
  ~(f = M(l)) && (s = v[f] = F[f](l));
  let _ = !/*timer*/
  l[5] && ct(l);
  return {
    c() {
      c && c.c(), e = B(), t = $("div"), m && m.c(), n = B(), y && y.c(), i = B(), s && s.c(), r = B(), _ && _.c(), a = be(), Y(t, "class", "progress-text svelte-16nch4a"), T(
        t,
        "meta-text-center",
        /*variant*/
        l[8] === "center"
      ), T(
        t,
        "meta-text",
        /*variant*/
        l[8] === "default"
      );
    },
    m(d, C) {
      c && c.m(d, C), k(d, e, C), k(d, t, C), m && m.m(t, null), ce(t, n), y && y.m(t, null), k(d, i, C), ~f && v[f].m(d, C), k(d, r, C), _ && _.m(d, C), k(d, a, C), o = !0;
    },
    p(d, C) {
      /*variant*/
      d[8] === "default" && /*show_eta_bar*/
      d[18] && /*show_progress*/
      d[6] === "full" ? c ? c.p(d, C) : (c = et(d), c.c(), c.m(e.parentNode, e)) : c && (c.d(1), c = null), p === (p = u(d)) && m ? m.p(d, C) : (m && m.d(1), m = p && p(d), m && (m.c(), m.m(t, n))), /*timer*/
      d[5] ? y ? y.p(d, C) : (y = nt(d), y.c(), y.m(t, null)) : y && (y.d(1), y = null), (!o || C[0] & /*variant*/
      256) && T(
        t,
        "meta-text-center",
        /*variant*/
        d[8] === "center"
      ), (!o || C[0] & /*variant*/
      256) && T(
        t,
        "meta-text",
        /*variant*/
        d[8] === "default"
      );
      let S = f;
      f = M(d), f === S ? ~f && v[f].p(d, C) : (s && (Ee(), ee(v[S], 1, 1, () => {
        v[S] = null;
      }), Ze()), ~f ? (s = v[f], s ? s.p(d, C) : (s = v[f] = F[f](d), s.c()), O(s, 1), s.m(r.parentNode, r)) : s = null), /*timer*/
      d[5] ? _ && (Ee(), ee(_, 1, 1, () => {
        _ = null;
      }), Ze()) : _ ? (_.p(d, C), C[0] & /*timer*/
      32 && O(_, 1)) : (_ = ct(d), _.c(), O(_, 1), _.m(a.parentNode, a));
    },
    i(d) {
      o || (O(s), O(_), o = !0);
    },
    o(d) {
      ee(s), ee(_), o = !1;
    },
    d(d) {
      d && (w(e), w(t), w(i), w(r), w(a)), c && c.d(d), m && m.d(), y && y.d(), ~f && v[f].d(d), _ && _.d(d);
    }
  };
}
function et(l) {
  let e, t = `translateX(${/*eta_level*/
  (l[17] || 0) * 100 - 100}%)`;
  return {
    c() {
      e = $("div"), Y(e, "class", "eta-bar svelte-16nch4a"), se(e, "transform", t);
    },
    m(n, i) {
      k(n, e, i);
    },
    p(n, i) {
      i[0] & /*eta_level*/
      131072 && t !== (t = `translateX(${/*eta_level*/
      (n[17] || 0) * 100 - 100}%)`) && se(e, "transform", t);
    },
    d(n) {
      n && w(e);
    }
  };
}
function Rl(l) {
  let e;
  return {
    c() {
      e = N("processing |");
    },
    m(t, n) {
      k(t, e, n);
    },
    p: Te,
    d(t) {
      t && w(e);
    }
  };
}
function Gl(l) {
  let e, t = (
    /*queue_position*/
    l[2] + 1 + ""
  ), n, i, f, s;
  return {
    c() {
      e = N("queue: "), n = N(t), i = N("/"), f = N(
        /*queue_size*/
        l[3]
      ), s = N(" |");
    },
    m(r, a) {
      k(r, e, a), k(r, n, a), k(r, i, a), k(r, f, a), k(r, s, a);
    },
    p(r, a) {
      a[0] & /*queue_position*/
      4 && t !== (t = /*queue_position*/
      r[2] + 1 + "") && D(n, t), a[0] & /*queue_size*/
      8 && D(
        f,
        /*queue_size*/
        r[3]
      );
    },
    d(r) {
      r && (w(e), w(n), w(i), w(f), w(s));
    }
  };
}
function Ol(l) {
  let e, t = Fe(
    /*progress*/
    l[7]
  ), n = [];
  for (let i = 0; i < t.length; i += 1)
    n[i] = lt($e(l, t, i));
  return {
    c() {
      for (let i = 0; i < n.length; i += 1)
        n[i].c();
      e = be();
    },
    m(i, f) {
      for (let s = 0; s < n.length; s += 1)
        n[s] && n[s].m(i, f);
      k(i, e, f);
    },
    p(i, f) {
      if (f[0] & /*progress*/
      128) {
        t = Fe(
          /*progress*/
          i[7]
        );
        let s;
        for (s = 0; s < t.length; s += 1) {
          const r = $e(i, t, s);
          n[s] ? n[s].p(r, f) : (n[s] = lt(r), n[s].c(), n[s].m(e.parentNode, e));
        }
        for (; s < n.length; s += 1)
          n[s].d(1);
        n.length = t.length;
      }
    },
    d(i) {
      i && w(e), qt(n, i);
    }
  };
}
function tt(l) {
  let e, t = (
    /*p*/
    l[41].unit + ""
  ), n, i, f = " ", s;
  function r(c, u) {
    return (
      /*p*/
      c[41].length != null ? Ul : Yl
    );
  }
  let a = r(l), o = a(l);
  return {
    c() {
      o.c(), e = B(), n = N(t), i = N(" | "), s = N(f);
    },
    m(c, u) {
      o.m(c, u), k(c, e, u), k(c, n, u), k(c, i, u), k(c, s, u);
    },
    p(c, u) {
      a === (a = r(c)) && o ? o.p(c, u) : (o.d(1), o = a(c), o && (o.c(), o.m(e.parentNode, e))), u[0] & /*progress*/
      128 && t !== (t = /*p*/
      c[41].unit + "") && D(n, t);
    },
    d(c) {
      c && (w(e), w(n), w(i), w(s)), o.d(c);
    }
  };
}
function Yl(l) {
  let e = me(
    /*p*/
    l[41].index || 0
  ) + "", t;
  return {
    c() {
      t = N(e);
    },
    m(n, i) {
      k(n, t, i);
    },
    p(n, i) {
      i[0] & /*progress*/
      128 && e !== (e = me(
        /*p*/
        n[41].index || 0
      ) + "") && D(t, e);
    },
    d(n) {
      n && w(t);
    }
  };
}
function Ul(l) {
  let e = me(
    /*p*/
    l[41].index || 0
  ) + "", t, n, i = me(
    /*p*/
    l[41].length
  ) + "", f;
  return {
    c() {
      t = N(e), n = N("/"), f = N(i);
    },
    m(s, r) {
      k(s, t, r), k(s, n, r), k(s, f, r);
    },
    p(s, r) {
      r[0] & /*progress*/
      128 && e !== (e = me(
        /*p*/
        s[41].index || 0
      ) + "") && D(t, e), r[0] & /*progress*/
      128 && i !== (i = me(
        /*p*/
        s[41].length
      ) + "") && D(f, i);
    },
    d(s) {
      s && (w(t), w(n), w(f));
    }
  };
}
function lt(l) {
  let e, t = (
    /*p*/
    l[41].index != null && tt(l)
  );
  return {
    c() {
      t && t.c(), e = be();
    },
    m(n, i) {
      t && t.m(n, i), k(n, e, i);
    },
    p(n, i) {
      /*p*/
      n[41].index != null ? t ? t.p(n, i) : (t = tt(n), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(n) {
      n && w(e), t && t.d(n);
    }
  };
}
function nt(l) {
  let e, t = (
    /*eta*/
    l[0] ? `/${/*formatted_eta*/
    l[19]}` : ""
  ), n, i;
  return {
    c() {
      e = N(
        /*formatted_timer*/
        l[20]
      ), n = N(t), i = N("s");
    },
    m(f, s) {
      k(f, e, s), k(f, n, s), k(f, i, s);
    },
    p(f, s) {
      s[0] & /*formatted_timer*/
      1048576 && D(
        e,
        /*formatted_timer*/
        f[20]
      ), s[0] & /*eta, formatted_eta*/
      524289 && t !== (t = /*eta*/
      f[0] ? `/${/*formatted_eta*/
      f[19]}` : "") && D(n, t);
    },
    d(f) {
      f && (w(e), w(n), w(i));
    }
  };
}
function Hl(l) {
  let e, t;
  return e = new Pl({
    props: { margin: (
      /*variant*/
      l[8] === "default"
    ) }
  }), {
    c() {
      yt(e.$$.fragment);
    },
    m(n, i) {
      Mt(e, n, i), t = !0;
    },
    p(n, i) {
      const f = {};
      i[0] & /*variant*/
      256 && (f.margin = /*variant*/
      n[8] === "default"), e.$set(f);
    },
    i(n) {
      t || (O(e.$$.fragment, n), t = !0);
    },
    o(n) {
      ee(e.$$.fragment, n), t = !1;
    },
    d(n) {
      Ct(e, n);
    }
  };
}
function Jl(l) {
  let e, t, n, i, f, s = `${/*last_progress_level*/
  l[15] * 100}%`, r = (
    /*progress*/
    l[7] != null && it(l)
  );
  return {
    c() {
      e = $("div"), t = $("div"), r && r.c(), n = B(), i = $("div"), f = $("div"), Y(t, "class", "progress-level-inner svelte-16nch4a"), Y(f, "class", "progress-bar svelte-16nch4a"), se(f, "width", s), Y(i, "class", "progress-bar-wrap svelte-16nch4a"), Y(e, "class", "progress-level svelte-16nch4a");
    },
    m(a, o) {
      k(a, e, o), ce(e, t), r && r.m(t, null), ce(e, n), ce(e, i), ce(i, f), l[31](f);
    },
    p(a, o) {
      /*progress*/
      a[7] != null ? r ? r.p(a, o) : (r = it(a), r.c(), r.m(t, null)) : r && (r.d(1), r = null), o[0] & /*last_progress_level*/
      32768 && s !== (s = `${/*last_progress_level*/
      a[15] * 100}%`) && se(f, "width", s);
    },
    i: Te,
    o: Te,
    d(a) {
      a && w(e), r && r.d(), l[31](null);
    }
  };
}
function it(l) {
  let e, t = Fe(
    /*progress*/
    l[7]
  ), n = [];
  for (let i = 0; i < t.length; i += 1)
    n[i] = rt(xe(l, t, i));
  return {
    c() {
      for (let i = 0; i < n.length; i += 1)
        n[i].c();
      e = be();
    },
    m(i, f) {
      for (let s = 0; s < n.length; s += 1)
        n[s] && n[s].m(i, f);
      k(i, e, f);
    },
    p(i, f) {
      if (f[0] & /*progress_level, progress*/
      16512) {
        t = Fe(
          /*progress*/
          i[7]
        );
        let s;
        for (s = 0; s < t.length; s += 1) {
          const r = xe(i, t, s);
          n[s] ? n[s].p(r, f) : (n[s] = rt(r), n[s].c(), n[s].m(e.parentNode, e));
        }
        for (; s < n.length; s += 1)
          n[s].d(1);
        n.length = t.length;
      }
    },
    d(i) {
      i && w(e), qt(n, i);
    }
  };
}
function ft(l) {
  let e, t, n, i, f = (
    /*i*/
    l[43] !== 0 && Ql()
  ), s = (
    /*p*/
    l[41].desc != null && st(l)
  ), r = (
    /*p*/
    l[41].desc != null && /*progress_level*/
    l[14] && /*progress_level*/
    l[14][
      /*i*/
      l[43]
    ] != null && ot()
  ), a = (
    /*progress_level*/
    l[14] != null && at(l)
  );
  return {
    c() {
      f && f.c(), e = B(), s && s.c(), t = B(), r && r.c(), n = B(), a && a.c(), i = be();
    },
    m(o, c) {
      f && f.m(o, c), k(o, e, c), s && s.m(o, c), k(o, t, c), r && r.m(o, c), k(o, n, c), a && a.m(o, c), k(o, i, c);
    },
    p(o, c) {
      /*p*/
      o[41].desc != null ? s ? s.p(o, c) : (s = st(o), s.c(), s.m(t.parentNode, t)) : s && (s.d(1), s = null), /*p*/
      o[41].desc != null && /*progress_level*/
      o[14] && /*progress_level*/
      o[14][
        /*i*/
        o[43]
      ] != null ? r || (r = ot(), r.c(), r.m(n.parentNode, n)) : r && (r.d(1), r = null), /*progress_level*/
      o[14] != null ? a ? a.p(o, c) : (a = at(o), a.c(), a.m(i.parentNode, i)) : a && (a.d(1), a = null);
    },
    d(o) {
      o && (w(e), w(t), w(n), w(i)), f && f.d(o), s && s.d(o), r && r.d(o), a && a.d(o);
    }
  };
}
function Ql(l) {
  let e;
  return {
    c() {
      e = N(" /");
    },
    m(t, n) {
      k(t, e, n);
    },
    d(t) {
      t && w(e);
    }
  };
}
function st(l) {
  let e = (
    /*p*/
    l[41].desc + ""
  ), t;
  return {
    c() {
      t = N(e);
    },
    m(n, i) {
      k(n, t, i);
    },
    p(n, i) {
      i[0] & /*progress*/
      128 && e !== (e = /*p*/
      n[41].desc + "") && D(t, e);
    },
    d(n) {
      n && w(t);
    }
  };
}
function ot(l) {
  let e;
  return {
    c() {
      e = N("-");
    },
    m(t, n) {
      k(t, e, n);
    },
    d(t) {
      t && w(e);
    }
  };
}
function at(l) {
  let e = (100 * /*progress_level*/
  (l[14][
    /*i*/
    l[43]
  ] || 0)).toFixed(1) + "", t, n;
  return {
    c() {
      t = N(e), n = N("%");
    },
    m(i, f) {
      k(i, t, f), k(i, n, f);
    },
    p(i, f) {
      f[0] & /*progress_level*/
      16384 && e !== (e = (100 * /*progress_level*/
      (i[14][
        /*i*/
        i[43]
      ] || 0)).toFixed(1) + "") && D(t, e);
    },
    d(i) {
      i && (w(t), w(n));
    }
  };
}
function rt(l) {
  let e, t = (
    /*p*/
    (l[41].desc != null || /*progress_level*/
    l[14] && /*progress_level*/
    l[14][
      /*i*/
      l[43]
    ] != null) && ft(l)
  );
  return {
    c() {
      t && t.c(), e = be();
    },
    m(n, i) {
      t && t.m(n, i), k(n, e, i);
    },
    p(n, i) {
      /*p*/
      n[41].desc != null || /*progress_level*/
      n[14] && /*progress_level*/
      n[14][
        /*i*/
        n[43]
      ] != null ? t ? t.p(n, i) : (t = ft(n), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(n) {
      n && w(e), t && t.d(n);
    }
  };
}
function ct(l) {
  let e, t, n, i;
  const f = (
    /*#slots*/
    l[30]["additional-loading-text"]
  ), s = vt(
    f,
    l,
    /*$$scope*/
    l[29],
    Qe
  );
  return {
    c() {
      e = $("p"), t = N(
        /*loading_text*/
        l[9]
      ), n = B(), s && s.c(), Y(e, "class", "loading svelte-16nch4a");
    },
    m(r, a) {
      k(r, e, a), ce(e, t), k(r, n, a), s && s.m(r, a), i = !0;
    },
    p(r, a) {
      (!i || a[0] & /*loading_text*/
      512) && D(
        t,
        /*loading_text*/
        r[9]
      ), s && s.p && (!i || a[0] & /*$$scope*/
      536870912) && Lt(
        s,
        f,
        r,
        /*$$scope*/
        r[29],
        i ? Nt(
          f,
          /*$$scope*/
          r[29],
          a,
          Dl
        ) : Ft(
          /*$$scope*/
          r[29]
        ),
        Qe
      );
    },
    i(r) {
      i || (O(s, r), i = !0);
    },
    o(r) {
      ee(s, r), i = !1;
    },
    d(r) {
      r && (w(e), w(n)), s && s.d(r);
    }
  };
}
function xl(l) {
  let e, t, n, i, f;
  const s = [Xl, Wl], r = [];
  function a(o, c) {
    return (
      /*status*/
      o[4] === "pending" ? 0 : (
        /*status*/
        o[4] === "error" ? 1 : -1
      )
    );
  }
  return ~(t = a(l)) && (n = r[t] = s[t](l)), {
    c() {
      e = $("div"), n && n.c(), Y(e, "class", i = "wrap " + /*variant*/
      l[8] + " " + /*show_progress*/
      l[6] + " svelte-16nch4a"), T(e, "hide", !/*status*/
      l[4] || /*status*/
      l[4] === "complete" || /*show_progress*/
      l[6] === "hidden"), T(
        e,
        "translucent",
        /*variant*/
        l[8] === "center" && /*status*/
        (l[4] === "pending" || /*status*/
        l[4] === "error") || /*translucent*/
        l[11] || /*show_progress*/
        l[6] === "minimal"
      ), T(
        e,
        "generating",
        /*status*/
        l[4] === "generating"
      ), T(
        e,
        "border",
        /*border*/
        l[12]
      ), se(
        e,
        "position",
        /*absolute*/
        l[10] ? "absolute" : "static"
      ), se(
        e,
        "padding",
        /*absolute*/
        l[10] ? "0" : "var(--size-8) 0"
      );
    },
    m(o, c) {
      k(o, e, c), ~t && r[t].m(e, null), l[33](e), f = !0;
    },
    p(o, c) {
      let u = t;
      t = a(o), t === u ? ~t && r[t].p(o, c) : (n && (Ee(), ee(r[u], 1, 1, () => {
        r[u] = null;
      }), Ze()), ~t ? (n = r[t], n ? n.p(o, c) : (n = r[t] = s[t](o), n.c()), O(n, 1), n.m(e, null)) : n = null), (!f || c[0] & /*variant, show_progress*/
      320 && i !== (i = "wrap " + /*variant*/
      o[8] + " " + /*show_progress*/
      o[6] + " svelte-16nch4a")) && Y(e, "class", i), (!f || c[0] & /*variant, show_progress, status, show_progress*/
      336) && T(e, "hide", !/*status*/
      o[4] || /*status*/
      o[4] === "complete" || /*show_progress*/
      o[6] === "hidden"), (!f || c[0] & /*variant, show_progress, variant, status, translucent, show_progress*/
      2384) && T(
        e,
        "translucent",
        /*variant*/
        o[8] === "center" && /*status*/
        (o[4] === "pending" || /*status*/
        o[4] === "error") || /*translucent*/
        o[11] || /*show_progress*/
        o[6] === "minimal"
      ), (!f || c[0] & /*variant, show_progress, status*/
      336) && T(
        e,
        "generating",
        /*status*/
        o[4] === "generating"
      ), (!f || c[0] & /*variant, show_progress, border*/
      4416) && T(
        e,
        "border",
        /*border*/
        o[12]
      ), c[0] & /*absolute*/
      1024 && se(
        e,
        "position",
        /*absolute*/
        o[10] ? "absolute" : "static"
      ), c[0] & /*absolute*/
      1024 && se(
        e,
        "padding",
        /*absolute*/
        o[10] ? "0" : "var(--size-8) 0"
      );
    },
    i(o) {
      f || (O(n), f = !0);
    },
    o(o) {
      ee(n), f = !1;
    },
    d(o) {
      o && w(e), ~t && r[t].d(), l[33](null);
    }
  };
}
var $l = function(l, e, t, n) {
  function i(f) {
    return f instanceof t ? f : new t(function(s) {
      s(f);
    });
  }
  return new (t || (t = Promise))(function(f, s) {
    function r(c) {
      try {
        o(n.next(c));
      } catch (u) {
        s(u);
      }
    }
    function a(c) {
      try {
        o(n.throw(c));
      } catch (u) {
        s(u);
      }
    }
    function o(c) {
      c.done ? f(c.value) : i(c.value).then(r, a);
    }
    o((n = n.apply(l, e || [])).next());
  });
};
let Ce = [], Ae = !1;
function en(l) {
  return $l(this, arguments, void 0, function* (e, t = !0) {
    if (!(window.__gradio_mode__ === "website" || window.__gradio_mode__ !== "app" && t !== !0)) {
      if (Ce.push(e), !Ae) Ae = !0;
      else return;
      yield Zl(), requestAnimationFrame(() => {
        let n = [0, 0];
        for (let i = 0; i < Ce.length; i++) {
          const s = Ce[i].getBoundingClientRect();
          (i === 0 || s.top + window.scrollY <= n[0]) && (n[0] = s.top + window.scrollY, n[1] = i);
        }
        window.scrollTo({ top: n[0] - 20, behavior: "smooth" }), Ae = !1, Ce = [];
      });
    }
  });
}
function tn(l, e, t) {
  let n, { $$slots: i = {}, $$scope: f } = e;
  this && this.__awaiter;
  const s = Tl();
  let { i18n: r } = e, { eta: a = null } = e, { queue_position: o } = e, { queue_size: c } = e, { status: u } = e, { scroll_to_output: p = !1 } = e, { timer: m = !0 } = e, { show_progress: y = "full" } = e, { message: F = null } = e, { progress: v = null } = e, { variant: M = "default" } = e, { loading_text: _ = "Loading..." } = e, { absolute: d = !0 } = e, { translucent: C = !1 } = e, { border: S = !1 } = e, { autoscroll: b } = e, z, V = !1, U = 0, te = 0, ie = null, le = null, A = 0, W = null, oe, H = null, h = !0;
  const P = () => {
    t(0, a = t(27, ie = t(19, J = null))), t(25, U = performance.now()), t(26, te = 0), V = !0, I();
  };
  function I() {
    requestAnimationFrame(() => {
      t(26, te = (performance.now() - U) / 1e3), V && I();
    });
  }
  function Z() {
    t(26, te = 0), t(0, a = t(27, ie = t(19, J = null))), V && (V = !1);
  }
  El(() => {
    V && Z();
  });
  let J = null;
  function ae(g) {
    He[g ? "unshift" : "push"](() => {
      H = g, t(16, H), t(7, v), t(14, W), t(15, oe);
    });
  }
  const ue = () => {
    s("clear_status");
  };
  function Me(g) {
    He[g ? "unshift" : "push"](() => {
      z = g, t(13, z);
    });
  }
  return l.$$set = (g) => {
    "i18n" in g && t(1, r = g.i18n), "eta" in g && t(0, a = g.eta), "queue_position" in g && t(2, o = g.queue_position), "queue_size" in g && t(3, c = g.queue_size), "status" in g && t(4, u = g.status), "scroll_to_output" in g && t(22, p = g.scroll_to_output), "timer" in g && t(5, m = g.timer), "show_progress" in g && t(6, y = g.show_progress), "message" in g && t(23, F = g.message), "progress" in g && t(7, v = g.progress), "variant" in g && t(8, M = g.variant), "loading_text" in g && t(9, _ = g.loading_text), "absolute" in g && t(10, d = g.absolute), "translucent" in g && t(11, C = g.translucent), "border" in g && t(12, S = g.border), "autoscroll" in g && t(24, b = g.autoscroll), "$$scope" in g && t(29, f = g.$$scope);
  }, l.$$.update = () => {
    l.$$.dirty[0] & /*eta, old_eta, timer_start, eta_from_start*/
    436207617 && (a === null && t(0, a = ie), a != null && ie !== a && (t(28, le = (performance.now() - U) / 1e3 + a), t(19, J = le.toFixed(1)), t(27, ie = a))), l.$$.dirty[0] & /*eta_from_start, timer_diff*/
    335544320 && t(17, A = le === null || le <= 0 || !te ? null : Math.min(te / le, 1)), l.$$.dirty[0] & /*progress*/
    128 && v != null && t(18, h = !1), l.$$.dirty[0] & /*progress, progress_level, progress_bar, last_progress_level*/
    114816 && (v != null ? t(14, W = v.map((g) => {
      if (g.index != null && g.length != null)
        return g.index / g.length;
      if (g.progress != null)
        return g.progress;
    })) : t(14, W = null), W ? (t(15, oe = W[W.length - 1]), H && (oe === 0 ? t(16, H.style.transition = "0", H) : t(16, H.style.transition = "150ms", H))) : t(15, oe = void 0)), l.$$.dirty[0] & /*status*/
    16 && (u === "pending" ? P() : Z()), l.$$.dirty[0] & /*el, scroll_to_output, status, autoscroll*/
    20979728 && z && p && (u === "pending" || u === "complete") && en(z, b), l.$$.dirty[0] & /*status, message*/
    8388624, l.$$.dirty[0] & /*timer_diff*/
    67108864 && t(20, n = te.toFixed(1));
  }, [
    a,
    r,
    o,
    c,
    u,
    m,
    y,
    v,
    M,
    _,
    d,
    C,
    S,
    z,
    W,
    oe,
    H,
    A,
    h,
    J,
    n,
    s,
    p,
    F,
    b,
    U,
    te,
    ie,
    le,
    f,
    i,
    ae,
    ue,
    Me
  ];
}
class ln extends jl {
  constructor(e) {
    super(), Il(
      this,
      e,
      tn,
      xl,
      Kl,
      {
        i18n: 1,
        eta: 0,
        queue_position: 2,
        queue_size: 3,
        status: 4,
        scroll_to_output: 22,
        timer: 5,
        show_progress: 6,
        message: 23,
        progress: 7,
        variant: 8,
        loading_text: 9,
        absolute: 10,
        translucent: 11,
        border: 12,
        autoscroll: 24
      },
      null,
      [-1, -1]
    );
  }
}
const {
  SvelteComponent: nn,
  assign: fn,
  attr: Pe,
  binding_callbacks: sn,
  check_outros: on,
  create_component: zt,
  destroy_component: St,
  detach: ut,
  element: an,
  flush: L,
  get_spread_object: rn,
  get_spread_update: cn,
  group_outros: un,
  init: _n,
  insert: _t,
  mount_component: Vt,
  safe_not_equal: dn,
  space: mn,
  src_url_equal: hn,
  transition_in: ke,
  transition_out: Ne
} = window.__gradio__svelte__internal, { onMount: bn } = window.__gradio__svelte__internal, { tick: gn } = window.__gradio__svelte__internal;
function dt(l) {
  let e, t;
  const n = [
    { autoscroll: (
      /*gradio*/
      l[0].autoscroll
    ) },
    { i18n: (
      /*gradio*/
      l[0].i18n
    ) },
    /*loading_status*/
    l[6]
  ];
  let i = {};
  for (let f = 0; f < n.length; f += 1)
    i = fn(i, n[f]);
  return e = new ln({ props: i }), e.$on(
    "clear_status",
    /*clear_status_handler*/
    l[21]
  ), {
    c() {
      zt(e.$$.fragment);
    },
    m(f, s) {
      Vt(e, f, s), t = !0;
    },
    p(f, s) {
      const r = s[0] & /*gradio, loading_status*/
      65 ? cn(n, [
        s[0] & /*gradio*/
        1 && { autoscroll: (
          /*gradio*/
          f[0].autoscroll
        ) },
        s[0] & /*gradio*/
        1 && { i18n: (
          /*gradio*/
          f[0].i18n
        ) },
        s[0] & /*loading_status*/
        64 && rn(
          /*loading_status*/
          f[6]
        )
      ]) : {};
      e.$set(r);
    },
    i(f) {
      t || (ke(e.$$.fragment, f), t = !0);
    },
    o(f) {
      Ne(e.$$.fragment, f), t = !1;
    },
    d(f) {
      St(e, f);
    }
  };
}
function wn(l) {
  let e, t, n, i, f, s = (
    /*loading_status*/
    l[6] && dt(l)
  );
  return {
    c() {
      s && s.c(), e = mn(), t = an("iframe"), hn(t.src, n = "https://bohrium.dp.tech/app/function-panel") || Pe(t, "src", n), Pe(t, "style", i = "box-sizing: content-box;width:" + /*width*/
      l[7] + "px;height: " + /*height*/
      l[8] + "px;padding: 24px;background: #ffffff;" + /*visible*/
      (l[3] ? "" : "display: none;"));
    },
    m(r, a) {
      s && s.m(r, a), _t(r, e, a), _t(r, t, a), l[22](t), f = !0;
    },
    p(r, a) {
      /*loading_status*/
      r[6] ? s ? (s.p(r, a), a[0] & /*loading_status*/
      64 && ke(s, 1)) : (s = dt(r), s.c(), ke(s, 1), s.m(e.parentNode, e)) : s && (un(), Ne(s, 1, 1, () => {
        s = null;
      }), on()), (!f || a[0] & /*width, height, visible*/
      392 && i !== (i = "box-sizing: content-box;width:" + /*width*/
      r[7] + "px;height: " + /*height*/
      r[8] + "px;padding: 24px;background: #ffffff;" + /*visible*/
      (r[3] ? "" : "display: none;"))) && Pe(t, "style", i);
    },
    i(r) {
      f || (ke(s), f = !0);
    },
    o(r) {
      Ne(s), f = !1;
    },
    d(r) {
      r && (ut(e), ut(t)), s && s.d(r), l[22](null);
    }
  };
}
function kn(l) {
  let e, t;
  return e = new Jt({
    props: {
      visible: (
        /*visible*/
        l[3]
      ),
      elem_id: (
        /*elem_id*/
        l[1]
      ),
      elem_classes: (
        /*elem_classes*/
        l[2]
      ),
      scale: (
        /*scale*/
        l[4]
      ),
      min_width: (
        /*min_width*/
        l[5]
      ),
      allow_overflow: !1,
      padding: !0,
      $$slots: { default: [wn] },
      $$scope: { ctx: l }
    }
  }), {
    c() {
      zt(e.$$.fragment);
    },
    m(n, i) {
      Vt(e, n, i), t = !0;
    },
    p(n, i) {
      const f = {};
      i[0] & /*visible*/
      8 && (f.visible = /*visible*/
      n[3]), i[0] & /*elem_id*/
      2 && (f.elem_id = /*elem_id*/
      n[1]), i[0] & /*elem_classes*/
      4 && (f.elem_classes = /*elem_classes*/
      n[2]), i[0] & /*scale*/
      16 && (f.scale = /*scale*/
      n[4]), i[0] & /*min_width*/
      32 && (f.min_width = /*min_width*/
      n[5]), i[0] & /*width, height, visible, iframeRef, gradio, loading_status*/
      969 | i[1] & /*$$scope*/
      1 && (f.$$scope = { dirty: i, ctx: n }), e.$set(f);
    },
    i(n) {
      t || (ke(e.$$.fragment, n), t = !0);
    },
    o(n) {
      Ne(e.$$.fragment, n), t = !1;
    },
    d(n) {
      St(e, n);
    }
  };
}
function pn(l, e, t) {
  var n = this && this.__awaiter || function(h, P, I, Z) {
    function J(ae) {
      return ae instanceof I ? ae : new I(function(ue) {
        ue(ae);
      });
    }
    return new (I || (I = Promise))(function(ae, ue) {
      function Me(E) {
        try {
          ge(Z.next(E));
        } catch (fe) {
          ue(fe);
        }
      }
      function g(E) {
        try {
          ge(Z.throw(E));
        } catch (fe) {
          ue(fe);
        }
      }
      function ge(E) {
        E.done ? ae(E.value) : J(E.value).then(Me, g);
      }
      ge((Z = Z.apply(h, P || [])).next());
    });
  };
  let { gradio: i } = e, { label: f = "Textbox" } = e, { elem_id: s = "" } = e, { elem_classes: r = [] } = e, { visible: a = !0 } = e, { value: o } = e, { placeholder: c = "" } = e, { show_label: u } = e, { scale: p = null } = e, { min_width: m = void 0 } = e, { loading_status: y = void 0 } = e, { value_is_output: F = !1 } = e, { interactive: v } = e, { rtl: M = !1 } = e, { fileName: _ } = e, { fileContent: d } = e, { width: C } = e, { height: S } = e, { appAccessKey: b } = e, { clientName: z } = e, V, U;
  function te() {
    let h = /* @__PURE__ */ new Map();
    document.cookie.split(";").forEach((P) => {
      const [I, Z] = P.trim().split("=");
      h.set(I, Z);
    }), V = b ?? h.get("appAccessKey"), U = z ?? h.get("clientName");
  }
  function ie() {
    i.dispatch("change"), F || i.dispatch("input");
  }
  function le() {
    return n(this, void 0, void 0, function* () {
      yield gn(), i.dispatch("submit");
    });
  }
  let A;
  const W = () => {
    A != null && A.contentWindow && _ && A.contentWindow.postMessage(
      {
        id: "1",
        type: "selectFilePath",
        data: { fileName: _ },
        headers: { accessKey: V, "x-app-key": U }
      },
      "*"
    );
  };
  bn(() => {
    te(), t(
      9,
      A.onload = () => {
        W();
      },
      A
    ), window.addEventListener("message", function(h) {
      return n(this, void 0, void 0, function* () {
        const { data: P } = h;
        if (P.type === "selectFilePath" && P.status === "succeed") {
          const I = new URL("https://openapi.dp.tech/openapi/v1/open/file/upload/binary");
          I.searchParams.append("path", `${P.data.dirPath}${P.data.fileName}`), P.data.projectId && I.searchParams.append("projectId", P.data.projectId);
          const Z = yield fetch(I, {
            method: "GET",
            headers: { accessKey: V, "x-app-key": U }
          });
          if (Z.ok) {
            const J = yield Z.json();
            fetch(`${J.data.host}/api/upload/binary`, {
              method: "POST",
              headers: {
                Authorization: J.data.Authorization,
                "X-Storage-Param": J.data["X-Storage-Param"]
              },
              body: new File([d], _)
            }).then(() => n(this, void 0, void 0, function* () {
              t(10, o = !0), yield le(), t(10, o = void 0), A.contentWindow.postMessage(
                {
                  id: "1",
                  type: "clear",
                  data: {},
                  headers: { accessKey: V, "x-app-key": U }
                },
                "*"
              );
            }));
          }
        }
        P.type === "closeWindow" && (t(10, o = !1), yield le(), A.contentWindow.postMessage(
          {
            id: "1",
            type: "clear",
            data: {},
            headers: { accessKey: V, "x-app-key": U }
          },
          "*"
        ), t(10, o = void 0)), P.type === "ready" && W();
      });
    });
  });
  const oe = () => i.dispatch("clear_status", y);
  function H(h) {
    sn[h ? "unshift" : "push"](() => {
      A = h, t(9, A);
    });
  }
  return l.$$set = (h) => {
    "gradio" in h && t(0, i = h.gradio), "label" in h && t(11, f = h.label), "elem_id" in h && t(1, s = h.elem_id), "elem_classes" in h && t(2, r = h.elem_classes), "visible" in h && t(3, a = h.visible), "value" in h && t(10, o = h.value), "placeholder" in h && t(12, c = h.placeholder), "show_label" in h && t(13, u = h.show_label), "scale" in h && t(4, p = h.scale), "min_width" in h && t(5, m = h.min_width), "loading_status" in h && t(6, y = h.loading_status), "value_is_output" in h && t(14, F = h.value_is_output), "interactive" in h && t(15, v = h.interactive), "rtl" in h && t(16, M = h.rtl), "fileName" in h && t(17, _ = h.fileName), "fileContent" in h && t(18, d = h.fileContent), "width" in h && t(7, C = h.width), "height" in h && t(8, S = h.height), "appAccessKey" in h && t(19, b = h.appAccessKey), "clientName" in h && t(20, z = h.clientName);
  }, l.$$.update = () => {
    l.$$.dirty[0] & /*value*/
    1024 && ie(), l.$$.dirty[0] & /*fileName*/
    131072 && W();
  }, [
    i,
    s,
    r,
    a,
    p,
    m,
    y,
    C,
    S,
    A,
    o,
    f,
    c,
    u,
    F,
    v,
    M,
    _,
    d,
    b,
    z,
    oe,
    H
  ];
}
class yn extends nn {
  constructor(e) {
    super(), _n(
      this,
      e,
      pn,
      kn,
      dn,
      {
        gradio: 0,
        label: 11,
        elem_id: 1,
        elem_classes: 2,
        visible: 3,
        value: 10,
        placeholder: 12,
        show_label: 13,
        scale: 4,
        min_width: 5,
        loading_status: 6,
        value_is_output: 14,
        interactive: 15,
        rtl: 16,
        fileName: 17,
        fileContent: 18,
        width: 7,
        height: 8,
        appAccessKey: 19,
        clientName: 20
      },
      null,
      [-1, -1]
    );
  }
  get gradio() {
    return this.$$.ctx[0];
  }
  set gradio(e) {
    this.$$set({ gradio: e }), L();
  }
  get label() {
    return this.$$.ctx[11];
  }
  set label(e) {
    this.$$set({ label: e }), L();
  }
  get elem_id() {
    return this.$$.ctx[1];
  }
  set elem_id(e) {
    this.$$set({ elem_id: e }), L();
  }
  get elem_classes() {
    return this.$$.ctx[2];
  }
  set elem_classes(e) {
    this.$$set({ elem_classes: e }), L();
  }
  get visible() {
    return this.$$.ctx[3];
  }
  set visible(e) {
    this.$$set({ visible: e }), L();
  }
  get value() {
    return this.$$.ctx[10];
  }
  set value(e) {
    this.$$set({ value: e }), L();
  }
  get placeholder() {
    return this.$$.ctx[12];
  }
  set placeholder(e) {
    this.$$set({ placeholder: e }), L();
  }
  get show_label() {
    return this.$$.ctx[13];
  }
  set show_label(e) {
    this.$$set({ show_label: e }), L();
  }
  get scale() {
    return this.$$.ctx[4];
  }
  set scale(e) {
    this.$$set({ scale: e }), L();
  }
  get min_width() {
    return this.$$.ctx[5];
  }
  set min_width(e) {
    this.$$set({ min_width: e }), L();
  }
  get loading_status() {
    return this.$$.ctx[6];
  }
  set loading_status(e) {
    this.$$set({ loading_status: e }), L();
  }
  get value_is_output() {
    return this.$$.ctx[14];
  }
  set value_is_output(e) {
    this.$$set({ value_is_output: e }), L();
  }
  get interactive() {
    return this.$$.ctx[15];
  }
  set interactive(e) {
    this.$$set({ interactive: e }), L();
  }
  get rtl() {
    return this.$$.ctx[16];
  }
  set rtl(e) {
    this.$$set({ rtl: e }), L();
  }
  get fileName() {
    return this.$$.ctx[17];
  }
  set fileName(e) {
    this.$$set({ fileName: e }), L();
  }
  get fileContent() {
    return this.$$.ctx[18];
  }
  set fileContent(e) {
    this.$$set({ fileContent: e }), L();
  }
  get width() {
    return this.$$.ctx[7];
  }
  set width(e) {
    this.$$set({ width: e }), L();
  }
  get height() {
    return this.$$.ctx[8];
  }
  set height(e) {
    this.$$set({ height: e }), L();
  }
  get appAccessKey() {
    return this.$$.ctx[19];
  }
  set appAccessKey(e) {
    this.$$set({ appAccessKey: e }), L();
  }
  get clientName() {
    return this.$$.ctx[20];
  }
  set clientName(e) {
    this.$$set({ clientName: e }), L();
  }
}
export {
  yn as default
};
