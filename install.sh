#!/usr/system/bin/sh
#!/sys/bin/bash

# webX installer

if command -v curl -q
then
    if command -v wget -q
    then
        echo "wget packages installed"
    else
        sudo apt install wget || pkg install wget
    fi
    echo "curl packages installed"
else
     sudo apt install curl || pkg install curl
fi
