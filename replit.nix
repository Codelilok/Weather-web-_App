{pkgs}: {
  deps = [
    pkgs.python312Packages.gunicorn
    pkgs.cacert
    pkgs.yakut
    pkgs.nmh
  ];
}
