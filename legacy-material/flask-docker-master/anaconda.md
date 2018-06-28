## Flask without Docker

This is only a brief guide.  For a full guide that we wrote, refer to the wiki article:
https://git.generalassemb.ly/DSI-WEST-3/course-info/wiki/Web-Service-Implementation-Guide-(Flask)

### Install Flask via Conda

```bash
conda install flask
```

### Setup Environmental Variables 


#### Mac / Linux
```bash
export FLASK_APP=service.py
export FLASK_DEBUG=1
```

#### Windows
For Windows, this should work very much the same way using `Gitbash`.  There is a way to get this to work in DOS or Powershell, but for the sake of consistency, you should use a similated Bash shell type environment like Gitbash.
