#!/usr/bin/env bash

# Get location of install file
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

{ 
# Create file in /usr/bin and make excecutable
touch /usr/bin/ydl
chmod +x /usr/bin/ydl
} ||
{
# Else, error
echo "Error, could not write to /usr/bin!" && exit
}
{
# Echo lines to file
echo "#!/usr/bin/env python3" > /usr/bin/ydl
cat $(SCRIPT_DIR)/ydl.py >> /usr/bin/ydl
} ||
{
# Else, error
echo "Error, could not write file contents!" && exit
}
echo "Script moved to '/usr/bin/ydl'!"
exit
