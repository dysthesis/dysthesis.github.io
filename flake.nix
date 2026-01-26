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
          nativeBuildInputs = [
            inputs'.ssg.packages.default
            pkgs.imagemagick
            pkgs.woff2
          ];

          preBuild = ''
            patchShebangs tools/*
          '';
          buildPhase = ''
            runHook preBuild
            ./tools/optimise-images.sh assets/img

            # Compress the two text faces we actually use to WOFF2.
            mkdir -p fonts-woff2
            for font in \
              fonts/Literata-Regular.ttf \
              fonts/Literata-Italic.ttf \
              fonts/AtkinsonHyperlegibleNext-Regular.ttf \
              fonts/AtkinsonHyperlegibleNext-Italic.ttf
            do
              woff2_compress "$font"
              base="$(basename "$font" .ttf)"
              mv "${font}.woff2" "fonts-woff2/${base}.woff2"
            done
            rm -rf fonts
            mv fonts-woff2 fonts

            ssg
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
