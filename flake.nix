{
  description = "Notes Environment";

  inputs = {
    flake-compat = {
      url = "https://git.lix.systems/lix-project/flake-compat/archive/main.tar.gz";
    };

    flake-parts = {
      url = "github:hercules-ci/flake-parts/main";
      inputs.nixpkgs-lib.follows = "nixpkgs";
    };

    nixpkgs = {
      url = "github:NixOS/nixpkgs/nixos-unstable";
    };
  };

  outputs =
    { flake-parts, ... }@inputs:
    flake-parts.lib.mkFlake { inherit inputs; } {
      systems = [
        "x86_64-linux"
        "aarch64-linux"
        "x86_64-darwin"
        "aarch64-darwin"
      ];

      perSystem =
        { pkgs, ... }:
        {
          devShells.default = pkgs.mkShellNoCC {
            packages = [
              pkgs.hugo
              pkgs.just
              pkgs.nixfmt
              pkgs.nixfmt-tree
              pkgs.pandoc
              pkgs.poppler-utils
              (pkgs.python3.withPackages (pypkgs: [
                pypkgs.pymupdf
                pypkgs.pytesseract
                pypkgs.pdf2image
              ]))
              pkgs.tesseract
            ];
          };
        };
    };
}
