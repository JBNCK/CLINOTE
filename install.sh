#!/usr/bin/env sh

if [ $(id -u) -ne 0 ]; then
    echo 'Please run as root'
    exit 1
fi

echo "Installing CLINOTE..."
sleep 1
cp src/notes.py /usr/bin/notes && chmod 755 /usr/bin/notes
echo "Done."