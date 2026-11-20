# main_module

Demo app that consumes **math_lib** and **log_lib** as git submodules.

```text
main_module/          ← this git repo
  app.py
  calculator.py
  math_lib/           ← submodule → https://github.com/gern121/math_lib.git
  log_lib/            ← submodule → https://github.com/gern121/log_lib.git
```

## Clone with submodules

```powershell
git clone --recurse-submodules https://github.com/gern121/main_module.git
```

## Run

```powershell
python app.py
```
