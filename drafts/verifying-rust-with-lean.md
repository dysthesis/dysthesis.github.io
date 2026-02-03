---
title: "Verification of Rust with Lean"
---

- Do I know Lean? Nope lmao.
- Aeneas lets you translate (a subset of) Rust into a bunch of formal languages,
  including Lean.
- We learn Lean and simultaneously how to prove Rust code with it.
- To do
  - Nix tooling to build Lean translation of Rust
  - Checks in Nix to build both your theorems and the Rust code translation,
    and combine it to verify that the theorems check out
  - ...and, probably using the combination to solve a bunch of [Project Euler]
    problems
- Reference dump:
  - https://emallson.net/blog/a-beginners-companion-to-theorem-proving-in-lean/
  - https://brandonrozek.com/blog/lean4-tutorial/
  - https://terrytao.wordpress.com/tag/lean4/

[Project Euler]: https://projecteuler.net/
