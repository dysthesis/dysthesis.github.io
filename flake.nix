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
          ];
          buildPhase = ''
            runHook preBuild
            ./tools/optimise-images.sh assets/img
            ssg
            runHook postBuild
          '';
          installPhase = ''
            runHook preInstall
            mkdir -p $out
            cp -r public/* $out/
            cp -r ${./fonts} $out/fonts
            ls ${./assets} > $out/test
            cp -r ${./assets} $out/assets
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
