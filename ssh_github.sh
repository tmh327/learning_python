#!/bin/bash

ssh-keygen -t rsa -b 4096 -C "taiducnguyen.drexel@gmail.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
sudo apt-get install xclip
xclip -sel clip < ~/.ssh/id_rsa.pub
echo "key copied to clipboard"
