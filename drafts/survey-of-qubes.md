---
title: A Survey of QubesOS
tags:
  - linux
  - virtualisation
  - security
  - qubes
---

# Personal issues with understanding Qubes

- Linux can be broadly partitioned into two categories
  - DIY distributions gives you almost nothing, leaving you to build your own
    system
    - Requires steep prerequisite knowledge
    - Lets you understand your whole system since you literally built it
      yourself -- perfect for hackers
  - Pre-build distributions that comes with everything ready
    - No prerequisite knowledge required, trivial to use for the layperson
    - Monolithic, takes time to fully wrap your head around, generally not made
      with the hacker in mind
      - Complex systems aside, you also need to understand someone else's way of
        thinking: for any given component of the system, you need to understand
        the developers' thought process to understand _why_ it's built that way.
  - Historically, I've always used the former
    - Started Linux as a learning journey rather than to meet any specific
      requirement
      - Previously used macOS, strictly speaking, it did pretty much everything
        I _needed_ to do (but not necessarily everything I _wanted_; learning is
        a want).
    - Ended up liking it that way as I generally like to intimately understand
      the thing I spend most of my day on so that I can easily mold it ad-hoc to
      fit a new use case of mine.
- Qubes falls into the latter
  - Makes sense for the target demographic -- journalists, activists, _etc._ who
    needs high security without having a CS degree or being that knowledgeable
    about tech in general.
  - Not great for me as it is arguably bigger than most systems
    - It has to deal with not _just_ the average desktop system, but also
    - has to deal with virtualisation, qube management and orchestration, etc.
    - minor nitpick: I think GUIs are a first class citizen in Qubes, while CLI
      is a second class citizen
      - Makes sense given the target demographic
      - I personally don't like to use GUIs.
- I want to have my cake and eat it to
  - Can use it to mess with dodgy stuff in peace
  - Simplify project management, conflicting dependency and toolchain version,
    etc. though to a certain extent it's less of a problem with Nix.
- Post will explore Qubes in an _inductive_ manner
  - I will iterate through actual concrete things I want to set up and do with
    the system, _e.g._ setting up a window manager like dwm, Nix qube for
    development, `sys-gui` to isolate X11, etc.
  - From the concrete we will do induction to the more abstract, _i.e._ the the
    actual constructions and mechanisms provided by Qubes (mainly in the CLI).
- Things to get working
  - [LUKS over yubikey]
  - Running Xorg in `sys-gui` instead of `dom0`
  - [DWM] instead of XFCE
    - a dedicated qube to edit and build (perhaps separately) the window manager
      and deploy it to `sys-gui`
  - [Microcode updating]
  - [sys-net on OpenBSD] for a smaller attack surface on such an exposed
    component
  - Attempt to create a [minimal service template] for network, firewall, etc.,
    extrapolating from the above.
  - [dom0 auth for root] instead of passwordless
  - [MAC anonymisation]
  - [Nix qube] for development (either pure NixOS or some distro + Nix on it)
  - [Command line + rofi keyboard-driven qube management]
  - [Audio qube] to isolate audio drivers
  - Ephemeral dispvm, either by making them [RAM-based] or [LUKS-based]
  - [Salt] for declarative and reproducible Qube management
  - [GPU HVM] for GPU-intensive activities like games or local LLMs
  - [auth splitting] for GPG, SSH, _etc._
  - [Qube to manage and update uBlock and Tor Browser]
  - [Signal messenger]
  - [Video playback performance]
  - [redshift] for blue-light reduction
  - offline dvm
  - qubes policies
- More dumps
  - [Browser stuff]
  - [Qube types]
  - [Privacy enhancement]

[DWM]: https://forum.qubes-os.org/t/guide-how-to-install-suckless-dwm-in-qubesos/8822
[Audio qube]: https://forum.qubes-os.org/t/audio-qube/20685
[RAM-based]: https://forum.qubes-os.org/t/really-disposable-ram-based-qubes/21532/3
[LUKS-based]: https://forum.qubes-os.org/t/fully-ephemeral-dispvms/12030
[Salt]: https://forum.qubes-os.org/t/qubes-salt-beginners-guide/20126
[GPU HVM]: https://forum.qubes-os.org/t/create-a-gaming-hvm/19000
[sys-net on OpenBSD]: https://forum.qubes-os.org/t/fortifying-sys-net-a-shift-to-openbsd/31973
[auth splitting]: https://forum.qubes-os.org/t/split-everything-collection-of-how-to-guides-for-split-configurations/11480
[minimal service template]: https://forum.qubes-os.org/t/guide-to-build-a-sys-mini-template-for-all-service-qubes/38764
[Qube to manage and update uBlock and Tor Browser]: https://forum.qubes-os.org/t/qubo-manage-ublock-origin-and-tor-browser-the-qubes-way/24616
[Microcode updating]: https://forum.qubes-os.org/t/updating-amd-microcode-from-qubes-os/34485
[Command line + rofi keyboard-driven qube management]: https://forum.qubes-os.org/t/how-to-create-qubes-os-vms-on-the-command-line/26550
[Signal messenger]: https://forum.qubes-os.org/t/signal-messenger/19073
[Browser stuff]: https://forum.qubes-os.org/t/the-grand-unified-browser/15284
[Qube types]: https://forum.qubes-os.org/t/qube-types-for-beginners/28942
[Privacy enhancement]: https://forum.qubes-os.org/t/qubes-os-privacy-enhancement-guide/24338/4
[dom0 auth for root]: https://forum.qubes-os.org/t/replacing-passwordless-root-with-a-dom0-prompt/19074
[MAC anonymisation]: https://forum.qubes-os.org/t/anonymizing-your-mac-address/19072
[LUKS over yubikey]: https://forum.qubes-os.org/t/luks-with-yubikey-2fa-chal-resp-on-qubes-4-2-0/23119
[Nix qube]: https://forum.qubes-os.org/t/how-to-install-nix-in-a-qubes-os-appvm/18698
[Video playback performance]: https://forum.qubes-os.org/t/improve-video-playback-performance-including-youtube-ytfzf/21946
[redshift]: https://forum.qubes-os.org/t/blue-light-filter-in-xfce-redshift/540
