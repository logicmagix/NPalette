#!/usr/bin/env bash

INSTALL_DIR="$HOME/.local/share/npalette"
BIN_DIR="$HOME/.local/bin"
WRAPPER="$BIN_DIR/npalette"

mkdir -p "$INSTALL_DIR"
cp -r npalette "$INSTALL_DIR"

mkdir -p "$BIN_DIR"
cat << EOF > "$WRAPPER"
#!/usr/bin/env bash
PYTHONPATH="$INSTALL_DIR" python3 -m npalette.npalette
EOF

chmod u+x "$WRAPPER"

echo "npalette installed to $WRAPPER"
echo "Make sure ~/.local/bin is in your PATH."


