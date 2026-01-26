{
  description = "Personal site";

  outputs = inputs @ {flake-parts, ...}:
    flake-parts.lib.mkFlake {inherit inputs;} {
      systems = ["x86_64-linux" "aarch64-linux" "aarch64-darwin" "x86_64-darwin"];
      perSystem = {
        pkgs,
        inputs',
        ...
      }: {
        devShells.default = pkgs.mkShellNoCC {
          packages = with pkgs; [
            # Nix
            statix
            deadnix
            nixd
            alejandra
            python3
            inputs'.ssg.packages.default
          ];
        };
        packages.default = pkgs.stdenvNoCC.mkDerivation {
          name = "blog";
          version = "0.1.0";
          src = ./.;
          nativeBuildInputs = with pkgs; [
            inputs'.ssg.packages.default
            imagemagick
            woff2
            fontforge-fonttools
            (python3.withPackages (p:
              with p; [
                fonttools
                brotli
              ]))
          ];

          preBuild = ''
            patchShebangs tools/*
          '';
          buildPhase = ''
                        runHook preBuild
                        ./tools/optimise-images.sh assets/img

                        # Subset the serif and sans faces to Basic Latin + punctuation, then emit WOFF2.
                        mkdir -p fonts-woff2
                        subset_range="U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2013-2014,U+2018-201A,U+201C-201E,U+2022,U+2026,U+2039-203A"
                        for font in \
                          fonts/Literata-Regular.ttf \
                          fonts/Literata-Italic.ttf \
                          fonts/AtkinsonHyperlegibleNext-Regular.ttf \
                          fonts/AtkinsonHyperlegibleNext-Italic.ttf
                        do
                          base="$(basename "$font" .ttf)"
                          pyftsubset "$font" \
                            --unicodes="$subset_range" \
                            --flavor=woff2 \
                            --layout-features='*' \
                            --output-file="fonts-woff2/''${base}.woff2"
                        done
                        rm -rf fonts
                        mv fonts-woff2 fonts

                        if [ -f  assets/favicon.svg ]; then
                          convert assets/favicon.svg -define icon:auto-resize=64,32,16 assets/favicon.ico
                        fi

                        ssg

                        python - <<'PY'
            import pathlib, re
            root = pathlib.Path("public")
            woff_preloads = [
                '<link rel="preload" href="/fonts/Literata-Regular.woff2" as="font" type="font/woff2" crossorigin>',
                '<link rel="preload" href="/fonts/Literata-Italic.woff2" as="font" type="font/woff2" crossorigin>',
                '<link rel="preload" href="/fonts/AtkinsonHyperlegibleNext-Regular.woff2" as="font" type="font/woff2" crossorigin>',
                '<link rel="preload" href="/fonts/AtkinsonHyperlegibleNext-Italic.woff2" as="font" type="font/woff2" crossorigin>',
                '<link rel="icon" href="/favicon.ico" sizes="any">'
            ]
            inject_block = "".join(woff_preloads)
            meta_pattern = re.compile(r'(<meta content="width=device-width,initial-scale=1" name=viewport>)')
            for html in root.rglob("*.html"):
                text = html.read_text()
                # Drop any .ttf preload hints
                text = re.sub(r'<link[^>]+\\.(ttf)"[^>]*>', ''', text)
                # Inject our canonical preloads and icon after viewport meta if
                # not already present.
                if "fonts/Literata-Regular.woff2" not in text:
                    text = meta_pattern.sub(r'\\1' + inject_block, text, count=1)
                # Ensure KaTeX font-display stays swap (defensive)
                text = text.replace('katex.min.css', 'katex.min.css')
                html.write_text(text)
            PY
                        runHook postBuild
          '';
          installPhase = ''
            runHook preInstall
            mkdir -p $out
            cp -r public/* $out/
            cp -r fonts $out/fonts
            cp -r assets $out/assets
            runHook postInstall
          '';
        };
      };
    };

  inputs = {
    flake-parts.url = "github:hercules-ci/flake-parts";
    nixpkgs.url = "github:NixOS/nixpkgs";
    ssg = {
      url = "github:dysthesis/ssg";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };
}
